# THESIS — MIT COMPLIANCE VALIDATION (v1)
## Validated against the MIT Specifications for Thesis Preparation (OCR of the 22-page source) and Field & de Neufville, *Thesis Definition and Preparation* (2021)
## Compiled: June 14, 2026

This audit checks the thesis against the two authoritative sources, not memory. Status uses: **OK** (compliant / handled by standing constraints), **VERIFY** (likely fine, confirm in the file), **ACTION** (work needed), **BUILD** (final-build step before submission).

---

## 1. Formatting compliance (MIT Specifications)

| # | Requirement (source) | Our status | Note / action |
|---|---|---|---|
| 1 | **Pagination:** title page = page 1; one consecutive sequence across title, prefatory, illustrations, text, appendices | BUILD | The pandoc build must produce a single continuous page sequence; no separate roman-numeral front matter. Set at final assembly. |
| 2 | **Title:** search-engine-meaningful; word substitutes for formulas/symbols/Greek | OK | "A Capability Assurance Framework for IOC Divestments" (recommended) is descriptive and symbol-free. |
| 3 | **Font:** sans serif suggested (not required) | VERIFY | Confirm the reference docx (`Chapter1_Ekekwe_v9.docx`) uses a sans-serif body; switch if serif. |
| 4 | **Spacing:** body single/1.5/double; **abstract, biography, notes, bibliography, acknowledgment single-spaced** | ACTION | Ensure abstract + bibliography + any notes/acknowledgments are single-spaced in the build, even if body is 1.5/double. |
| 5 | **Title page fields, in order, centered:** title; "by" + author (preferred name); previous degrees; "Submitted to the [Department] in partial fulfillment of the requirements for the degree of [degree]"; month + year (May/June, Sept, or Feb only); copyright statement; the MIT nonexclusive-license legend; "Authored by"; department; "Certified by" (supervisor name + title); "Accepted by" (program officer) | VERIFY/ACTION | **Verify the title page in the reference docx carries the *current* MIT copyright-and-license legend** (author retains copyright; grants MIT a worldwide, irrevocable, royalty-free nonexclusive license). This legend changed in recent MIT policy; older templates omit it. If absent, add. Department = IDSS / System Design and Management; supervisor = Dr. George Lordos; confirm the "Accepted by" officer. |
| 6 | **Abstract page (Required):** ≤ **500 words**, single-spaced, immediately after title page; fields: title / "by" / author / submitting statement / "ABSTRACT" / body / supervisor name + title | ACTION | Abstract not yet written. **Target 300 words (Field & de Neufville cap: 200-300 maximum), well within the MIT 500 cap.** Written last; apply the lead-sentence test. |
| 7 | **Table of contents** | VERIFY | Generate at build from heading styles. |
| 8 | **List of figures (required if figures present)** and **List of tables (required if tables present)** | ACTION | We have multiple figures (4.1, 5.1, 5.2) and tables (4.x, 5.1-5.4) → **both lists are required** and must be generated at build. Currently not assembled. |
| 9 | **Notes and bibliographic references:** department-prescribed style; may sit at chapter end or thesis end; respect margins | VERIFY | Confirm a single consistent citation style across all chapters (Zotero). Field & de Neufville use Harvard with an APA-style bibliography; confirm the thesis style and apply uniformly. |
| 10 | **Appendices:** permitted; **"appendices and references are not considered supplementary information"** (part of the paginated document) | ACTION | Appendices B, F, G, and the planned H are part of the main document and must be paginated in sequence. **Each must be referenced from the body** (see deliverable 2). |
| 11 | **Copyright:** © and/or "copyright"; year; author; "All rights reserved" or a chosen Creative Commons license | VERIFY | On the title page; choose "All rights reserved" or a CC license consciously. |
| 12 | **Use of others' copyrighted material:** permission/attribution for figures/excerpts created or published by others | ACTION | The RBPS framework is CCPS's and the IKT elements are Ferreira's. **Do not reproduce CCPS or IEEE figures directly; build original representations and cite the source** (CCPS 2007 for RBPS; Ferreira et al. for IKT). Same for any adapted Wood Mackenzie/NEITI exhibit. |
| 13 | **Accessibility:** heading styles, alt-text on figures/images (and formulas), embedded metadata (author, title, year, department, keywords) | BUILD | Use Word heading styles (already implied by the docx pipeline); add alt-text to every figure (4.1, 5.1, 5.2); set document metadata before PDF/A conversion. |
| 14 | **PDF/A-1 (a or b) required for submission**; submit source (.docx) alongside; convert from source, not from a flat PDF; no embedded multimedia/scripts | BUILD | Final step: convert the assembled docx to PDF/A-1. Validate. |
| 15 | **Degree month:** May/June, September, or February only | OK | Submission July 31 → September degree conferral; ensure the title/abstract pages say September [year]. |

## 2. Content and argument compliance (Field & de Neufville)

| Requirement | Our status | Note |
|---|---|---|
| A thesis is a **proposition + an argument, maintained throughout** (not a topic/report/essay) | OK | The fixed thesis statement and the critical-experiment design satisfy this. |
| **Question / Method / Evidence / Logic** as the four structural pillars | OK | Ch1 (question), Ch3 (method), Ch4 (evidence), throughout (logic). |
| **Abstract length ≤ 200-300 words maximum** (manual), descriptive | ACTION | Reinforces the 300-word target in item 6. |
| **Descriptive title** ("titles that do not describe the subject should be left to literary efforts") | OK | Supports the direct title "A Capability Assurance Framework for IOC Divestments" with the subtitle "Re-specifying Transfer Approval Around Sociotechnical Operating Capability," over "Closing the Loop" as a chapter title. |
| **Figure/table quality** (Tufte standard); every exhibit organized around one point; **captions above tables, below figures; self-contained** | OK | Already a standing constraint; carry into Ch5 (Figure 5.1, Tables 5.1-5.4) and Appendix H. |
| **Citation discipline; no patchwriting** | OK | Standing constraint; every idea in Ikenna's words with attribution. |
| Argument-construction sequence per section; Principle of Least Astonishment | OK | Standing constraint. |
| Claim calibration (demonstrated vs proven; "in the cases examined") | OK | Standing constraint; especially load-bearing for Ch5/Ch6 and the new value dimensions (deliverable 2). |

---

## 3. Prioritized action list

**Now (affects drafting):**
1. Lock the **citation style** (one style, applied uniformly via Zotero) and confirm references placement (chapter-end vs thesis-end).
2. Keep building original (not reproduced) figures and cite sources (CCPS for RBPS, Ferreira for IKT) to satisfy item 12.
3. Reference every appendix (B, F, G, H) from the body (deliverable 2).

**Verify in the reference docx (`Chapter1_Ekekwe_v9.docx`):**
4. Title-page **copyright-and-license legend** present and current (item 5). If absent, add the MIT nonexclusive-license legend.
5. Sans-serif body font (item 3).

**Final build (before submission):**
6. Assemble single continuous pagination from the title page (item 1).
7. Generate **List of Figures** and **List of Tables** (item 8) and Table of Contents (item 7).
8. Single-space abstract + bibliography (item 4).
9. Alt-text on all figures + document metadata (item 13).
10. Convert to **PDF/A-1** and validate; submit .docx source alongside (item 14).
11. Confirm September conferral wording on title + abstract pages (item 15).

**Offer:** I can extract the title page from the reference docx now and check items 4-5 directly, rather than leaving them as VERIFY.

---

## 4. One structural note this validation surfaces
The MIT Specifications treat appendices as part of the paginated document and require lists of figures and tables. Our growing appendix set (B Discrimination Matrix; F Verdict Traceability; G Survey Data; H Capability/Ferreira Traceability) and exhibit set are compliant in principle but **not yet assembled into a single front-to-back document with the required prefatory lists and continuous pagination**. That assembly is a discrete late-stage task; flagging it now so it is not discovered at submission.
