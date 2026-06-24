#!/usr/bin/env python3
"""
Committed build script for the MIT thesis LaTeX project.

WHY THIS FILE EXISTS
--------------------
Two failure modes were hit during development and are now structurally prevented here,
rather than relying on per-session discipline:

  1. DATA-LOSS BUG. The pattern  open(f, "w").write(transform(open(f).read()))  evaluates
     open(f, "w") FIRST, which truncates the file to empty BEFORE the inner read runs, so
     transform("") = "" is written back. This wiped all six canonical chapters once.
     PREVENTION: read() and safe_write() are separate calls. Never nest a read inside an
     open-for-write. There is no code path in this file that opens a file for writing while
     simultaneously reading it.

  2. TOC-INJECTION OMISSION. The "Appendix X:" prefix and the bold "Appendices" divider in
     the table of contents are produced by \appendixtocsetup, which must be written into the
     .toc BEFORE Appendix A ships. The only reliable position is the END of chapter6.tex.
     Regenerating chapter6.tex from the canonical .md drops that line. PREVENTION:
     regen_chapters() re-appends it every time, idempotently.

USAGE:  cd mitthesis_build && python3 build.py
"""
import re, os, glob, subprocess, shutil

OUT   = "/mnt/user-data/outputs"
BUILD = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- safe I/O
def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()

def safe_write(path, text):
    """text MUST be fully computed already. Never pass an expression that reads `path`."""
    assert isinstance(text, str)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)

# ---------------------------------------------------------------- source maps
def _latest_md(prefix):
    """Resolve the highest _vN.md for a canonical stem so a version bump is picked up
    automatically; the build can never silently read a stale version, and this single
    rule is shared with build_all.py so the two maps cannot diverge."""
    cands = glob.glob(os.path.join(OUT, prefix + "_v*.md"))
    if not cands:
        raise RuntimeError("no source matching %s_v*.md in %s" % (prefix, OUT))
    return os.path.basename(max(cands, key=lambda p: int(re.search(r"_v(\d+)\.md$", p).group(1))))

CHAPTERS = {("chapter%d" % n): _latest_md("Chapter%d_Full" % n) for n in range(1, 7)}
APPENDICES = {
    "appendixa": "Appendix_A_Case_Study_Protocol.md",
    "appendixb": "Appendix_B_Discrimination_Matrix.md",
    "appendixc": "Appendix_C_Interview_Guides.md",
    "appendixd": "Appendix_D_Case_by_Case_Evidence_Table.md",
    "appendixe": "Appendix_E_Verdict_Traceability_Matrix.md",
    "appendixf": "Appendix_F_Survey_Response_Data.md",
    "appendixg": "Appendix_G_Capability_Element_Traceability_Matrix.md",
}
FIGURES = [
    "Figure_2_1_divestment_failure_equilibrium.png",
    "Figure_4_1_production_trajectories.png",
    "Figure_5_1_capability_assurance_loop.png",
    "Figure_5_2_breaking_the_failure_equilibrium.png",
]
APPENDIX_TOC_LINE = "\\addtocontents{toc}{\\protect\\appendixtocsetup}"

# ---------------------------------------------------------------- latexify
def _strip_section_numbers(s):
    # remove baked-in section numbers so LaTeX numbers them; {1,2} bound protects 4-digit years
    return re.sub(r'(?m)^(#{2,6})\s+(?:[A-Z]\.)?\d{1,2}(?:\.\d{1,2})*\.?\s+(?=\S)', r'\1 ', s)

def latexify_chapter(s):
    s = _strip_section_numbers(s)
    s = re.sub(r'(?m)^# Chapter \d+\s*\n\n# (.+)$', r'# \1', s)
    s = re.sub(r'(?m)^# Chapter \d+[:.]\s*(.+)$', r'# \1', s)
    return s.replace('.svg', '.png')

def _single_h1(s):
    seen = False; out = []
    for line in s.split("\n"):
        if line.startswith("# "):
            out.append(("#" + line) if seen else line); seen = True
        else:
            out.append(line)
    return "\n".join(out)

def latexify_appendix(s):
    s = _strip_section_numbers(s)
    s = re.sub(r'(?m)^# Appendix [A-Z][.:]\s*(.+)$', r'# \1', s)
    return _single_h1(s.replace('.svg', '.png'))

# ---------------------------------------------------------------- caption / float / landscape
# The .md stays clean markdown (Word path). This pass converts markdown captions into proper
# LaTeX floats with \caption[short]{full} so caption and table/figure stay together, wide
# tables go landscape, and the lists of tables/figures populate. Auto-numbering (per chapter)
# is used, so table/figure numbers must be sequential in the source.
LANDSCAPE_MIN_COLS = 5

def _short_title(cap):
    s = re.split(r'[.,:;]', cap, maxsplit=1)[0].strip()
    if len(s) > 62:
        s = s[:60].rsplit(' ', 1)[0].rstrip(',;:') + '...'
    return s

def _fig_float(fpath, cap):
    cap = ' '.join(cap.split()); short = _short_title(cap)
    return ('\\begin{figure}[H]\n\\centering\n'
            f'\\includegraphics[width=\\textwidth,height=0.45\\textheight,keepaspectratio]{{{fpath}}}\n'
            f'\\caption[{short}]{{{cap}}}\n\\end{{figure}}')

def _caption_figures(tex):
    # Case C: pandoc figure float (stub \caption) then the real \textbf{Figure N.} caption paragraph (Ch5)
    tex = re.sub(
        r'\\begin\{figure\}\s*\n\\centering\s*\n\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}\s*\n'
        r'\\caption\{[^}]*\}\s*\n\\end\{figure\}\s*\n\s*\\textbf\{Figure\s+[\d.]+\.\}\s*(.*?)(?=\n\s*\n)',
        lambda m: _fig_float(m.group(1), m.group(2)), tex, flags=re.DOTALL)
    # Case B: bare \includegraphics + \emph{Figure N. ...} (Ch4, all-italic caption)
    tex = re.sub(
        r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}\s*\n\s*\\emph\{(?:Figure\s+[\d.]+\.\s*)([^}]*)\}',
        lambda m: _fig_float(m.group(1), m.group(2)), tex, flags=re.DOTALL)
    # Case A: bare \includegraphics + \textbf{Figure N.} text (Ch2, bold-label caption)
    tex = re.sub(
        r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}\s*\n\s*\\textbf\{Figure\s+[\d.]+\.\}\s*(.*?)(?=\n\s*\n)',
        lambda m: _fig_float(m.group(1), m.group(2)), tex, flags=re.DOTALL)
    return tex

_LT_HEAD = (r'(\\begin\{longtable\}\[\]\{@\{\}.*?@\{\}\})\s*\n'
            r'(\\toprule\\noalign\{\}.*?\\midrule\\noalign\{\})\s*\n\\endhead')

# Hand-written, self-contained titles for the List of Tables (override the 60-char truncation).
TABLE_TITLES = {
    '2.1': 'Key concepts used in the discrimination analysis',
    '2.2': 'The binding constraint and key prediction of each competing explanation',
    '3.1': 'The decisive falsification condition and discriminating test for each explanation',
    '3.2': 'Design-quality tests applied to the study, after Yin (2009)',
    '4.1': 'Post-divestment outcomes across the six formal cases',
    '4.2': 'Structural precedent and design contrasts beyond the formal cases',
    '4.3': 'Verdicts for the Aiteo critical experiment on OML 29',
    '4.4': 'Two transfer mechanisms sharing one capability-assessment gap',
    '4.5': 'Consolidated verdicts on the five explanations across the cases',
    '4.6': 'Buyer background against the two outcome dimensions',
    '4.7': 'Where political access or capital can substitute for operating capability',
    '5.1': 'The value dimensions an operating-capability gap puts at risk',
    '5.2': 'The four structural gaps behind an unassisted-divestment capability gap',
    '5.3': 'The capability bundle by domain: what is disclosed, absorbed, and verified',
    '5.4': 'Capability as a condition of transfer across four petroleum regimes',
    '5.5': 'Risk-tiered divestment assurance scaled to demonstrated capability',
    'B.1': 'The discrimination matrix: evidence patterns and their strength-coded implications',
    'B.2': 'The five-step decision protocol for applying the discrimination matrix',
    'D.1': 'Case-by-case evidence summary across the discrimination logic',
    'E.1': 'Verdict matrix for the Aiteo case (OML 29)',
    'E.2': 'Verdict matrix for the Eroton case (OML 18)',
    'E.3': 'Verdict matrix for the First Hydrocarbon case (OML 26)',
    'E.4': 'Verdict matrix for the Seplat case (OMLs 4, 38, 41)',
    'E.5': 'Verdict matrix for the OML 30 within-asset operator change',
    'E.6': 'Verdict matrix for the NPDC case',
    'E.7': 'Verdict matrix for the Marginal Field Program',
    'F.1': 'Profile of the three completed survey respondents',
    'F.2': 'Driver rankings by the three completed respondents',
    'F.3': 'Counterfactual, policy, and overall-adequacy survey responses',
    'G.1': 'Criticality tiers for the transfer-process elements',
    'G.2': 'RBPS Pillar 1 (Commit to Process Safety): elements and transfer factors',
    'G.3': 'RBPS Pillar 2 (Understand Hazards and Risks): elements and transfer factors',
    'G.4': 'RBPS Pillar 3 (Manage Risk): elements and transfer factors',
    'G.5': 'RBPS Pillar 4 (Learn from Experience): elements and transfer factors',
}

def _inject_tcap(num, cap, ltbegin, head):
    cap = ' '.join(cap.split())
    short = TABLE_TITLES.get(num, _short_title(cap))
    return (ltbegin + '\n\\caption[' + short + ']{' + cap + '}\\\\\n'
            + head + '\n\\endfirsthead\n' + head + '\n\\endhead')

def _caption_tables(tex):
    # ONE canonical caption format, enforced for all current and future tables:
    #   a fully-bold paragraph  **Table N. CAPTION**  immediately before the table,
    # which pandoc renders as \textbf{Table N. CAPTION} with the whole caption inside the
    # bold. Any other format will NOT promote here, and assert_floats_captioned then fails
    # the build -- so the single-format rule is enforced, not merely documented.
    tex = re.sub(r'\\textbf\{Table\s+([\dA-Z.]+)\.\s+([^}]*)\}\s*\n\s*' + _LT_HEAD,
                 lambda m: _inject_tcap(m.group(1), m.group(2), m.group(3), m.group(4)), tex, flags=re.DOTALL)
    return tex

def _landscape_wide(tex):
    pat = re.compile(r'\\begin\{longtable\}\[\]\{@\{\}.*?\\end\{longtable\}', re.DOTALL)
    def repl(m):
        block = m.group(0)
        ncol = block.split('\\toprule')[0].count('\\real{')
        if ncol < LANDSCAPE_MIN_COLS:
            return block
        # Make letter/letter slashes breakable so a token like "Documentary/regulatory"
        # can never overrun its cell into the neighbouring column (the overlay bug).
        block = re.sub(r'(?<=[A-Za-z])/(?=[A-Za-z])', r'/\\allowbreak{}', block)
        extra = '\\footnotesize\n'   # every wide landscaped table uses the smaller font
        # Verdict tables (Appendix E and the Chapter 4 verdict summary) share one 7-column
        # structure; give them proportionate widths (Evidence widest; section/confidence
        # narrow). Detected by the verdict-table header, NOT by column count, so other
        # 7-column tables (e.g. the Chapter 4 outcomes table) keep pandoc's widths.
        if ncol == 7 and 'What would change this verdict' in block:
            widths = ['0.10', '0.15', '0.17', '0.25', '0.13', '0.08', '0.12']
            head, sep, rest = block.partition('\\toprule')
            parts = re.split(r'(\\real\{[0-9.]+\})', head)
            wi = 0
            for i in range(len(parts)):
                if re.fullmatch(r'\\real\{[0-9.]+\}', parts[i]) and wi < len(widths):
                    parts[i] = '\\real{' + widths[wi] + '}'; wi += 1
            block = ''.join(parts) + sep + rest
        return '\\begin{landscape}\n' + extra + block + '\n\\end{landscape}'
    return pat.sub(repl, tex)

def _table_hyphenation(tex):
    # pandoc's \raggedright in p{} columns suppresses hyphenation, so a long word
    # (e.g. "Rehabilitation") in a narrow column overruns its cell. ragged2e's
    # \RaggedRight keeps ragged-right but allows hyphenation, eliminating that overflow.
    tex = tex.replace('\\raggedright\\arraybackslash', '\\RaggedRight\\arraybackslash')
    tex = tex.replace('{\\linewidth}\\raggedright', '{\\linewidth}\\RaggedRight')
    return tex

def _heading_into_landscape(tex):
    # A section heading immediately followed by a landscaped table (no prose between) would
    # otherwise strand the heading alone on a portrait page while the table starts on the
    # next landscape page. Move the heading inside the landscape environment so the heading
    # and its table share one landscape page. The heading rotates with the page, which is
    # acceptable for these prose-free verdict sections. Only fires when nothing but
    # whitespace separates the heading from the table, so prose-bearing sections are left
    # alone.
    pat = re.compile(
        r'(\\hypertarget\{[^}]*\}\{%\n'
        r'\\(?:sub)?section\{(?:[^{}]|\{[^{}]*\})*\}'
        r'\\label\{[^}]*\}\})\s*'
        r'(\\begin\{landscape\})')
    return pat.sub(r'\2\n\1\n', tex)

def postprocess_tex(tex):
    return _heading_into_landscape(_landscape_wide(_table_hyphenation(_caption_tables(_caption_figures(tex)))))

def _pandoc(md_text, out_tex):
    tmp = "/tmp/_thesis_build_src.md"
    safe_write(tmp, md_text)
    subprocess.run(["pandoc", tmp, "-o", out_tex, "--top-level-division=chapter"], check=True)
    processed = postprocess_tex(read(out_tex))      # read first, then write (no truncate-before-read)
    safe_write(out_tex, processed)

# ---------------------------------------------------------------- build steps
def regen_chapters():
    for stem, md in CHAPTERS.items():
        _pandoc(latexify_chapter(read(os.path.join(OUT, md))), os.path.join(BUILD, stem + ".tex"))
    # re-arm the appendix TOC setup (prefix + divider) at the end of chapter6.tex
    c6 = os.path.join(BUILD, "chapter6.tex")
    txt = read(c6)                                   # read first
    if "appendixtocsetup" not in txt:
        safe_write(c6, txt.rstrip() + "\n\n" + APPENDIX_TOC_LINE + "\n")
    print("  chapters regenerated; appendix TOC setup armed in chapter6.tex")

def regen_appendices():
    for stem, md in APPENDICES.items():
        _pandoc(latexify_appendix(read(os.path.join(OUT, md))), os.path.join(BUILD, stem + ".tex"))
    print("  appendices a-g regenerated (one \\chapter each)")

def copy_figures():
    for png in FIGURES:
        src = os.path.join(OUT, png)
        if os.path.exists(src):
            shutil.copy(src, BUILD)
    print("  figures copied")

def copy_abstract():
    src = os.path.join(OUT, "Abstract_Ekekwe_v6.md")
    if os.path.exists(src):
        shutil.copy(src, os.path.join(BUILD, "abstract.tex"))
        print("  abstract.tex synced from canonical")

def copy_bib():
    src = os.path.join(OUT, "references.bib")
    if os.path.exists(src):
        shutil.copy(src, BUILD)
        print("  references.bib synced from canonical")
    else:
        print("  WARNING: canonical references.bib not found")

def compile_pdf():
    os.chdir(BUILD)
    for f in ["main.aux", "main.toc", "main.bcf", "main.lof", "main.lot"]:
        if os.path.exists(f):
            os.remove(f)
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], stdout=subprocess.DEVNULL)
    subprocess.run(["biber", "main"], stdout=subprocess.DEVNULL)
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], stdout=subprocess.DEVNULL)
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], stdout=subprocess.DEVNULL)
    shutil.copy("main.pdf", "MIT_format_proof.pdf")
    n = subprocess.run(["pdfinfo", "main.pdf"], capture_output=True, text=True).stdout
    pages = next((l.split()[1] for l in n.splitlines() if l.startswith("Pages")), "?")
    print(f"  compiled: {pages} pages -> MIT_format_proof.pdf")

def assert_floats_captioned():
    """Every longtable AND every figure float must carry a \\caption, or it is silently
    missing from the List of Tables / List of Figures (the Table 4.7 / Table 2.2 failure).
    Covers chapters and appendices. Turn that silent drop into a loud build error."""
    problems = []
    for stem in list(CHAPTERS) + list(APPENDICES):
        tex = os.path.join(BUILD, stem + ".tex")
        if not os.path.exists(tex):
            continue
        t = read(tex)
        for m in re.finditer(r"\\begin\{longtable\}.*?\\end\{longtable\}", t, re.DOTALL):
            if "\\caption" not in m.group(0):
                pre = t[max(0, m.start() - 400):m.start()]
                lbl = re.findall(r"Table\s+([\dA-Z.]+)", pre)
                problems.append("%s: longtable WITHOUT caption (near 'Table %s')"
                                % (stem, lbl[-1] if lbl else "??"))
        for m in re.finditer(r"\\textbf\{Table\s+([\dA-Z.]+)\.[^}]*\}", t):
            if "\\begin{longtable}" in t[m.end():m.end() + 600]:
                problems.append("%s: un-promoted bold caption before a table (Table %s)"
                                % (stem, m.group(1)))
        # figures: every includegraphics must sit in a figure float carrying a caption
        fig_spans = []
        for fb in re.finditer(r"\\begin\{figure\}.*?\\end\{figure\}", t, re.DOTALL):
            fig_spans.append((fb.start(), fb.end()))
            if "\\includegraphics" in fb.group(0) and "\\caption" not in fb.group(0):
                problems.append("%s: figure float WITHOUT a caption" % stem)
        for m in re.finditer(r"\\includegraphics", t):
            if not any(a <= m.start() < b for a, b in fig_spans):
                problems.append("%s: includegraphics outside any captioned figure float" % stem)
        for m in re.finditer(r"\\(?:textbf|emph)\{Figure\s+([\dA-Z.]+)\.", t):
            if "\\includegraphics" in t[max(0, m.start() - 500):m.start() + 500]:
                problems.append("%s: un-promoted figure caption (Figure %s)" % (stem, m.group(1)))
    if problems:
        raise RuntimeError("FLOAT CAPTION PROMOTION FAILED -- these would be missing from the "
                           "List of Tables / Figures:\n  " + "\n  ".join(problems))
    print("  caption check: every table and figure float is captioned (no silent drops)")

def assert_lot_sane():
    """After compile, table numbers must be contiguous 1..n within each numbered chapter.
    A gap (e.g. Chapter 2 starting at 2.2) means an uncaptioned float consumed a number --
    the phantom-counter bug behind the broken 'Table 2.1' references."""
    lot_path = os.path.join(BUILD, "main.lot")
    if not os.path.exists(lot_path):
        return
    nums = re.findall(r"numberline \{([\dA-Z]+)\.(\d+)\}", read(lot_path))
    bygrp = {}
    for grp, tb in nums:
        bygrp.setdefault(grp, []).append(int(tb))
    problems = []
    for grp, tbs in sorted(bygrp.items()):
        if sorted(tbs) != list(range(1, len(tbs) + 1)):
            label = ("Chapter " + grp) if grp.isdigit() else ("Appendix " + grp)
            problems.append("%s table numbers %s are not contiguous 1..%d"
                            % (label, sorted(tbs), len(tbs)))
    if problems:
        raise RuntimeError("LIST-OF-TABLES NUMBERING ANOMALY:\n  " + "\n  ".join(problems))
    print("  LoT check: table numbers contiguous per chapter")

def assert_references_resolve():
    """Every 'Table X.Y' / 'Figure X.Y' citation in the prose must resolve to a float the
    compile actually produced (present in main.lot / main.lof). Catches a reference left
    pointing at a number no float carries -- the broken-cross-reference failure mode the
    caption and numbering guards do not police."""
    lot_path = os.path.join(BUILD, "main.lot")
    lof_path = os.path.join(BUILD, "main.lof")
    if not (os.path.exists(lot_path) and os.path.exists(lof_path)):
        return
    tables = set(re.findall(r"numberline \{([\dA-Z]+\.\d+)\}", read(lot_path)))
    figures = set(re.findall(r"numberline \{([\dA-Z]+\.\d+)\}", read(lof_path)))
    srcs = list({**CHAPTERS, **APPENDICES}.values()) + [_latest_md("Abstract_Ekekwe")]
    problems = set()
    for md in srcs:
        path = os.path.join(OUT, md)
        if not os.path.exists(path):
            continue
        t = read(path)
        for num in re.findall(r"Table[~ ]+(\d+\.\d+|[A-Z]\.\d+)", t):
            if num not in tables:
                problems.add("%s cites 'Table %s' but no such table float exists" % (md, num))
        for num in re.findall(r"Figure[~ ]+(\d+\.\d+|[A-Z]\.\d+)", t):
            if num not in figures:
                problems.add("%s cites 'Figure %s' but no such figure float exists" % (md, num))
    if problems:
        raise RuntimeError("UNRESOLVED FLOAT REFERENCES:\n  " + "\n  ".join(sorted(problems)))
    print("  reference check: every Table/Figure X.Y citation resolves to a real float")

if __name__ == "__main__":
    print("Building thesis ...")
    regen_chapters()
    regen_appendices()
    assert_floats_captioned()
    copy_figures()
    copy_bib()
    copy_abstract()
    compile_pdf()
    assert_lot_sane()
    assert_references_resolve()
    print("Done.")
