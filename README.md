# Thesis Deliverables -- Inheriting Hardware Without the System
**Ikenna Ekekwe | MIT SDM | regenerated 2026-06-21 (tables rebuilt from scratch)**

202-page proof, clean biber build. Reflects the full canonical chain and references.bib (87 entries).

## TABLES: rebuilt from scratch in python-docx (NOT pandoc)
Pandoc's docx tables are structurally unrenderable (7-col tables collapse to a stacked single
column in Word/LibreOffice even though the XML is well-formed). Every table is now rebuilt as a
clean python-docx table: fixed layout, header-fitting proportional column widths, booktabs rules
(top rule, header rule, bottom rule; no verticals), bold header, 8-9 pt. Render-verified via
LibreOffice against the LaTeX PDF. 32 tables rebuilt across chapters and appendices.

## What changed this session
- NEITI 2020/2021/2022/2023(new)/2024 wired to eiti.org + Vanguard URLs; [VERIFY] cleared on those.
- Appendix G: 7 centered '---' dividers removed (saved 2 pp; near-empty pp 188/190/194 gone).
- build.py now syncs references.bib AND abstract.tex from canonical on every run.
- (Prior) §1.3 compression, Figure 4.1 caption, Energy Voice 2022a/b, Iwuoha/Mohamed titles.

## docx/ (16 components) -- Thesis_Full.docx (combined) -- Thesis_Full_Proof.pdf (202 pp) -- md/ -- figures/ -- tex/

## Build provenance (answer to "is everything canonical?")
PDF: build.py regenerates chapters + appendices from canonical .md, and now syncs figures, bib,
and abstract. Cover/title (main.tex) and acronyms are static metadata, verified correct
(title/author/Supervisor Lordos/Acceptor Rubin right; degree date September 2026 is a placeholder).
TOC/LoF/LoT auto-generate. docx: all 16 components regenerated from canonical. NUPRC 2024 IS used
(cited 46x) -- kept.

## Residuals: NUPRC 2022 (Marginal Field Status Report) title unverified; Energy Voice 2022a/b article URLs.
