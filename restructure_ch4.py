#!/usr/bin/env python3
"""
Chapter 4 declutter (Option A) + renumber, executed as one verified pass.
Reconciliation into Appendix E is already complete, so the five per-case verdict
tables can be removed without losing content.

Order matters (each step keeps every match-string unique):
 1. Remove the five per-case verdict tables (matched by distinctive caption text;
    the trailing blank line is consumed so no double blank is left behind).
 2. Fix in-text references (removed tables -> Appendix E; surviving tables -> new number).
 3. Renumber surviving captions (.md number must be right for the Word path; PDF auto-numbers).
 4. Caption the Aiteo verdict table (now the only remaining verdict table) as 4.3.
 5. Add the 4.1->4.2 bridge sentence and the Appendix E pointer.
References stay plain text (correct in both PDF and Word); \\ref/\\label is a separate decision.
"""
import re

P = "Chapter4_Full_v9.md"
s = open(P, encoding="utf-8").read()
orig = s

def sub1(old, new, label):
    global s
    n = s.count(old)
    assert n == 1, f"[{label}] expected 1 occurrence, found {n}"
    s = s.replace(old, new, 1)

def remove_table(caption_start, label):
    global s
    pat = re.escape(caption_start) + r"[^\n]*\*\*\n\n(?:\|[^\n]*\n)+\n"
    n = len(re.findall(pat, s))
    assert n == 1, f"[{label}] block match count = {n}"
    s = re.sub(pat, "", s, count=1)

# 1) Remove the five per-case verdict tables
remove_table("**Table 4.2. Verdicts for the Eroton case on OML 18,", "Eroton")
remove_table("**Table 4.3. Verdicts for the First Hydrocarbon case on OML 26,", "FHN")
remove_table("**Table 4.4. Verdicts for the Seplat case on OMLs 4, 38, and 41,", "Seplat")
remove_table("**Table 4.5. Verdicts for OML 30, the within-asset operator change,", "OML30")
remove_table("**Table 4.6. Verdicts for the NPDC case across its operated licenses,", "NPDC")

# 2) In-text reference fixes (do before renumbering so numbers stay unambiguous)
sub1("Table 4.4 sets out the verdicts. The question for the alternatives",
     "Appendix E sets out the verdicts for this case. The question for the alternatives",
     "Seplat ref -> Appendix E")
sub1("The verdicts follow in Table 4.6. The case carries two findings on different dimensions, and the table records them separately.",
     "The verdicts for this case are recorded in Appendix E. The case carries two findings on different dimensions, which the matrix records separately.",
     "NPDC ref -> Appendix E")
sub1("the two mechanisms converge, as Table 4.7 sets out.",
     "the two mechanisms converge, as Table 4.4 sets out.",
     "mechanisms ref 4.7 -> 4.4")
sub1("The pattern holds across the two dimensions, as Table 4.9 sets out.",
     "The pattern holds across the two dimensions, as Table 4.6 sets out.",
     "buyer ref 4.9 -> 4.6")

# 3) Renumber surviving captions
sub1("**Table 4.1A. Post-divestment outcomes", "**Table 4.1. Post-divestment outcomes", "4.1A -> 4.1")
sub1("**Table 4.7. Two transfer mechanisms", "**Table 4.4. Two transfer mechanisms", "4.7 -> 4.4 caption")
sub1("**Table 4.8. ", "**Table 4.5. ", "4.8 -> 4.5 caption")
sub1("**Table 4.9. Buyer background", "**Table 4.6. Buyer background", "4.9 -> 4.6 caption")

# 4) Caption the Aiteo verdict table (4.3)
AITEO_CAP = ("**Table 4.3. Verdicts for the Aiteo case on OML 29, the critical experiment, where "
             "funded production growth alongside an uncontained well-control crisis rejects the "
             "capital, fiscal, and political-economy explanations as sufficient for the integrity "
             "failure and leaves capability-related factors most consistent with the evidence.**")
sub1("with the elimination of rivals set aside.\n\n| Explanation | Verdict | Evidence anchor | What would change this verdict |",
     "with the elimination of rivals set aside.\n\n" + AITEO_CAP + "\n\n| Explanation | Verdict | Evidence anchor | What would change this verdict |",
     "Aiteo caption insert")

# 5a) Bridge between Table 4.1 (formal cases) and Table 4.2 (precedent); also renumber 4.1B -> 4.2
BRIDGE = ("Three further transactions inform the analysis at a lower evidentiary weight, their data "
          "limited or non-comparable: an earlier transfer mechanism that serves as a structural "
          "precedent, and two recent acquisitions whose deliberate structure offers a design "
          "contrast. Table 4.2 records them.")
sub1("corporate filings.*\n\n**Table 4.1B. Structural precedent",
     "corporate filings.*\n\n" + BRIDGE + "\n\n**Table 4.2. Structural precedent",
     "bridge + 4.1B -> 4.2")

# 5b) Appendix E pointer at the end of Section 4.3.6
POINTER = ("Appendix E reproduces this verdict matrix for every case, recording the evidence, "
           "confidence level, and falsification condition behind each verdict; the analyses that "
           "follow state their verdicts in prose and refer to that appendix for the full matrices.")
sub1("what the replications test next (Sections 4.4 and 4.5).\n\n\n## 4.4 Cross-Case",
     "what the replications test next (Sections 4.4 and 4.5).\n\n" + POINTER + "\n\n\n## 4.4 Cross-Case",
     "Appendix E pointer")

# safety: collapse any stray triple-blank before prose (not before headers)
s = re.sub(r"\n{3,}(?=[A-Z])", "\n\n", s)

open(P, "w", encoding="utf-8").write(s)

# integrity: no per-case verdict captions remain; exactly six table captions remain (4.1-4.6)
remaining = re.findall(r"\*\*Table 4\.\d", s)
print(f"Ch4: {len(orig)} -> {len(s)} bytes; surviving '**Table 4.x' captions: {len(remaining)}")
for bad in ["Verdicts for the Eroton", "Verdicts for the First Hydrocarbon",
            "Verdicts for the Seplat", "Verdicts for OML 30", "Verdicts for the NPDC"]:
    assert bad not in s, f"removed-case text still present: {bad}"
assert "Verdicts for the Aiteo case on OML 29" in s, "Aiteo caption missing"
print("Ch4 integrity OK: 5 per-case tables gone, Aiteo captioned")

# ---------- Chapter 5 ----------
P5 = "Chapter5_Full_v8.md"
s5 = open(P5, encoding="utf-8").read()
assert s5.count("4.5.2; Table 4.9)") == 1, "Ch5 ref not found uniquely"
s5 = s5.replace("4.5.2; Table 4.9)", "4.5.2; Table 4.6)", 1)
open(P5, "w", encoding="utf-8").write(s5)
print("Ch5: Table 4.9 -> Table 4.6")
