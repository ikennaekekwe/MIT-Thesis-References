# Verification Decision & Impact Ledger
**Living document.** references.bib is updated live as citations are found/corrected. **All other prose (chapters, appendices, tables, figures) is deferred to ONE comprehensive update pass**, read end-to-end so the argument's logic is confirmed before anything commits.

**Workflow rule (agreed).** Decide each finding's corrected claim and trace its impact *continuously*; write prose *once*. Argument-altering findings become the **working premise** for all subsequent verification, so later chapters are checked against corrected logic, never stale logic.

**Standing policy (2026-06-23).** Identified enhancements (current and future) are **auto-approved** for incorporation everywhere applicable. Lock the decision and trace impact now, add supporting citations to references.bib live, and defer the prose to the one comprehensive pass.

**Legend**
- **Class:** `LOCAL` = a fact is wrong but no inference changes (citation, section number, date, figure, broken ref) — compile, applies cleanly in the pass. `ARG` = a claim, verdict, or the *direction of an inference* changes — lock direction now, map impact now, defer prose.
- **Status:** `APPLIED` (already in v30/bib) · `PENDING` (compiled, awaiting the pass) · `DEFERRED` (awaiting a later chapter's verification before it can be finalized).
- **Locus tags:** `[confirmed]` = I have read the exact text · `[predicted]` = expected location, verify when that chapter is reached.

---

## SECTION A — Chapter 2 findings

### A1 · "Section 29 of the Petroleum Act" → Paragraph 14 / 16, First Schedule
- **Class:** LOCAL (but **coupled to A2** — Para 16(b) is where the capability criterion lives, which is A2's evidence; apply together).
- **Status:** PENDING.
- **Finding.** §2.3.3 line 79 cites "Section 29" for assignment-consent capability criteria. The Act itself places assignment consent at **Para 14** and the consent *criteria* (incl. technical knowledge) at **Para 16**; Para 29 is the revocation notice. The 2021 Guidelines cite "paragraphs 14 to 16 of the First Schedule."
- **Corrected claim.** Consent power = Para 14; criteria = Para 16; the question becomes "does **Paragraph 16** include an operational-capability criterion?" — and per A2 the answer is "a general technical-knowledge criterion, yes."
- **Confidence:** ~99% (verified against Petroleum Act 1969 in repo).
- **Impact.** Upstream: §2.3.3 line 79 `[confirmed]`. Downstream: **Ch4 line 153 `[CONFIRMED]`** (direct "Section 29 of the Petroleum Act required ministerial consent to assign the lease" assertion), §4.3.3, §4.4.2, Appendix E (E.1, E.4) wherever "Section 29" recurs `[predicted]`.

### A2 · "The mandate did not exist" (design failure) → "existed but lacked operational specificity" (specification/execution gap)
- **Class:** ARG. **The only direction-changer found so far.**
- **Status:** PENDING (decision to apply made; held for coordinated pass with Chapter 4).
- **Finding.** §2.3.3 line 73 asserts no operational-capability criterion existed. Contradicted by three primary sources: Petroleum Act 1969 First Schedule **Para 16(b)** ("sufficient technical knowledge and experience … in respect of operations under the licence or lease"); 2021 Minister's Consent Guidelines **5.4.1 + 7.1.3**; 2024 Assignment Regulation **pillar (a) technical capacity**.
- **Locked corrected claim (working premise going forward).** A technical-capability mandate has existed continuously since 1969 and was reaffirmed in 2014/2021; what was missing is **operational specificity** for assessing *embedded* operational capability. The 2024 framework operationalized it. The regulatory gap is specification/execution, **not** absence. This is the stronger position: the framework's contribution becomes *operationalizing existing law*, not *asking for new law*.
- **Confidence:** ~98%. Only a 1969–2021 provision repealing Para 16(b) would overturn it; none seen; 2021 Guidelines re-state it.
- **Impact map (per requirement — full upstream/downstream):**
  - **Upstream (sets up the claim):**
    - §2.3.3 lines 73 / 75 / 79 / 81 `[confirmed]` — line 73 is the direct error; line 75 (execution failure) becomes the *supported* branch; line 79's question is now answered ("operationalize existing"); **line 81's NUPRC "first in 68 years" quote** must be reframed as a claim about the *comprehensive/operationalized* framework, not the first criterion.
    - Chapter 1 regulatory-gap preview `[predicted]`.
  - **Downstream (depends on the claim):**
    - §4.3.3 and §4.4.2 — regulatory-inadequacy verdict; re-derive from "criterion existed, not operationalized/enforced for embedded capability." **Confirmed Ch4 loci: line 153** ("leaving the acquirer's fitness, capability, and governance untested" — the exact claim Para 16(b) contradicts), **line 84** (NUPRC seven-pillar "first" framing), **line 86** (regulatory-gap discussion) `[CONFIRMED]`. **Open question the pass must answer: does the verdict ("enabling condition insufficient on its own") survive, or only its basis?** `[predicted]`
    - Table 4.5 (≈ line 276) — "no criterion" cell(s) `[memory-flagged]`.
    - Appendix E — regulatory-inadequacy row: Evidence + "what-would-change-the-verdict" columns `[confirmed structure]`.
    - Appendix F — verdict traceability, regulatory row `[predicted]`.
    - Chapter 5 — regulator-verification pillar + justification; possibly framework-diagram caption (contribution shifts "create criterion" → "operationalize existing") `[predicted, high importance]`.
    - Chapter 6 — any conclusion that the framework "lacked capability criteria"; policy recommendation shifts "create criteria" → "operationalize existing criteria." **Overclaiming risk lives here.** `[predicted]`
    - Abstract — if it states the regulatory finding or framework's regulatory contribution `[predicted]`.
    - **Chapter 3 line 39** — marginal-field "without mandatory capability assessment" is the same overstatement in the marginal-field context (verified against 2020 DPR Guidelines; see F1) `[confirmed]`.
  - **Resolves pending integration item:** "Ministers Consent: criterion lacked operational specificity, not 'no capability criterion existed'" is this same issue, now grounded in three primary sources.

### A3 · "(Andersen, 2022)" was a broken citation (no bib entry)
- **Class:** LOCAL. **Status:** APPLIED (bib).
- **Resolution.** `andersen2022` added to references.bib (source confirmed: ng.andersen.com marginal-fields PIA piece, Oct 2022, carries the 85%→45% / 15% HCT / 30% CIT figures). In-text citation now resolves.

### A4 · PIA transfer provision: "Sections 232-233" → "Section 95"
- **Class:** LOCAL. **Status:** APPLIED (Chapter2_Full_v30.md line 79, PIA clause only).
- Note: §232-233 (decommissioning) are correctly cited elsewhere; only the *transfer*-assessment question was mis-pointed.

### A5 · Trist & Bamforth 1951 "technology unchanged" → split 1951 (founding) + Trist et al. 1963 (constant-technology)
- **Class:** LOCAL. **Status:** APPLIED (v30 line 23; `tristetal1963` added to bib).
- Verified: 1963 *Organizational Choice* studied conventional-vs-composite longwall (same technology, different social organization) — the correct home for the claim.

### A6 · HCT 15% (marginal-field rate) misapplied to large divested OMLs
- **Class:** LOCAL. **Status:** APPLIED (v30 line 59) · **one DEFERRED sub-check.**
- **Applied.** Scoped 85%→45% / 15% HCT to marginal fields (per Andersen 2022); added that converted OMLs become PMLs at 30% HCT (~60% combined) for the large leases this study examines.
- **DEFERRED → Chapter 4 fiscal sub-section.** Confirm per lease (Aiteo OML 29, Eroton OML 18, Seplat OMLs 4/38/41, FHN OML 26, Shoreline OML 30) whether each actually converted OML→PML, against NEITI/NUPRC data (likely "Nigerian Upstream Concession Situation Report - 1 Feb 2026" in repo). If a lease stayed on legacy OML/PPT terms, line 59 needs a third clause.

### A7 · Williamson 1975 triad → "Williamson, 1975, 1985"
- **Class:** LOCAL. **Status:** APPLIED (v30 line 151; `williamson1985` added to bib).
- Note: williamson1985 entry added from canonical knowledge; not independently re-confirmed by search this session (low risk — among the most-cited economics books).

---

## SECTION B — Appendix E / verdict-matrix (from the earlier circularity audit)

### B1 · Political-economy rejection at Seplat (E.4) and OML 30 (E.5) rests on non-discriminating production evidence
- **Class:** ARG (changes the *evidence basis* of a verdict, not the verdict itself). **Status:** PENDING.
- **Finding.** The PE cells for Seplat and OML 30 cite production / production-growth, which is **non-discriminating**: the thesis's own Rexer reliance holds that political connections *raise* production (+33%), so high production is *consistent with* PE, not evidence against it. Aiteo/Eroton/NPDC PE cells are clean (crisis-response failure / barge-plan / low-efficiency-plus-survival).
- **Corrected claim.** Re-derive the Seplat and OML 30 PE rejections from **operational-integrity / non-substitutable-domain** evidence (LTI-free safety record; rehabilitation) and **excise production** from those cells.
- **Confidence:** ~90% (the non-discrimination is entailed by the thesis's own Rexer premise).
- **Impact.** Appendix E rows E.4, E.5 (PE Evidence cells) `[confirmed]`; Chapter 4 wherever the Seplat/OML 30 PE verdict is argued in prose `[predicted]`; Chapter 5 if the PE distinction feeds the framework's political-economy handling `[predicted]`. Verdict vocabulary (§2.6 five terms) unaffected.

---

## SECTION C — Verified clean (no action)
**Theory (repo source-verified):** Cohen & Levinthal 1990 · Kogut & Zander 1992 · Kogut & Zander 1993 · Zander & Kogut 1995 · Nonaka 1994 · Grant 1996 · Baxter & Sommerville 2011 · Ferreira et al. 2024.
**Theory (full bib entry + characterization verified):** Akerlof 1970 · North 1990 · Stigler 1971 · Myers & Majluf 1984 · Pfeffer & Salancik 1978 · Zahra & George 2002 · Nelson & Winter 1982 · Nightingale & Rhodes 2015 · CCPS 2007. *(Verbatim OCR not possible — files absent; bib metadata + canonical characterization confirmed.)*
**Empirical (verified):** Rexer 2025 · Rui et al. 2018 · SPE 184346 · Spiff et al. 2022 · Okonkwo 2019 · Akpomera 2015 · Mohamed et al. 2024 · Iwuoha 2021 · Nwuke 2021.
**Primary sources/statutes:** PIA fiscal terms · NUPRC 2024 framework · Petroleum Act 1969 · 2021 Minister's Consent Guidelines · 2024 Assignment Regulation · Santa Barbara blowout · seller-independence deals (Oando/ConocoPhillips 2014, Seplat/MPNU 2024, Oando/NAOC 2024).

---

## SECTION D — Previously-identified items to fold into the same pass (not verification-driven)
- **George review comments** (analysis done, decisions pending): Q1 (PE naming + prose-vs-matrix gap + production excision — overlaps B1); Q2 (conform §2.3.5 "strongest control" to Ch4 within-asset OML 30); Q3 (Tier-2 corroborative role + seller-weighting limitation).
- **Pending integration items:** Ch2 missing IKT paragraph (Ferreira 2024 + Sumbal 2018 currently in Ch1); Ch1 line 119 proximate-mechanism fix; RQ1/RQ2 overlap (Option A); CLD placement (Ch2 + Ch5); case-selection table as Ch3 complement; Ch4 §4.1 P6 redundancy with §3.4; §2.4 overhaul-cycle softening ("well beyond a short transition period" — no citation for the three-year cycle).

---

## SECTION E — references.bib change log (LIVE)
- **2026-06-23 added:** `andersen2022` (Andersen, Marginal Fields & PIA 2021, 2022) · `tristetal1963` (Trist/Higgin/Murray/Pollock, Organizational Choice, Tavistock 1963) · `williamson1985` (Williamson, Economic Institutions of Capitalism, Free Press 1985).
- **2026-06-23 added (G5 enhancement, auto-approved):** `businessday2021nembe` (NOSDRA: lacks capacity; Aiteo did not subscribe to spill-response service; Bonga contrast), `vanguard2021nembe` (NOSDRA: beyond the capacity of a single company; Tier 2), `thisday2021baptism` (editorial: absence of effective blowout contingency plan). Updated `nosdra2021` note (statement IS archived after all).
- Backups: `references.bib.bak_flagfixes`, `references.bib.bak_premerge`, `references.bib.bak_item1additions`, `references.bib.bak_g5enhancement`.

---

## SECTION F — Chapter 3 findings (verification COMPLETE except case facts deferred to Ch4)

**Citation load fully verified (only three works):**
- **Yin (2009)** — text, bib (4th ed., 2009), and repo source all agree on 2009; replication terms (literal/theoretical replication, analytic/statistical generalization) confirmed verbatim in the repo source. *(My earlier "Yin 2003" note was wrong; no thesis error.)*
- **Field & de Neufville (2021)** — MIT thesis manual, in bib; case-selection-logic use is correct.
- **Beach & Pedersen (2013)** — in bib; process-tracing test types (hoop, smoking-gun, straw-in-the-wind) correctly attributed at lines 15, 19.

**COUHES E-7658 — CORRECT.** Line 96 reads "received exemption from the MIT Committee on the Use of Humans as Experimental Subjects (COUHES Protocol E-7658)." Described as an *exemption*, not an approval. ✓

**F1 · Marginal-field "without mandatory capability assessment" (line 39) — imprecise; PARALLEL TO A2.**
- **Class:** ARG (coupled to A2). **Status:** PENDING.
- **Finding.** Line 39 states the marginal-field program (2003–2020) allocated assets "without mandatory capability assessment." The 2020 DPR Marginal-Field Guidelines in fact carried a prequalification with explicit criteria: "background and experience with exploration and production at sufficiently high level" (5.4.6a); "Company Management Systems (Business and HSE principles, Recruitment and training policy, Business controls)" (5.4.1.iii); "Evidence of Financial Capability" (5.4.1.v); and disqualification of sponsors whose existing assets "are not being operated in a business-like manner" (5.4.8).
- **Corrected claim.** Reframe to "without mandatory assessment of *embedded operational* capability." A general technical/financial prequalification existed; what was absent — exactly as in the divestment regime (A2) — is assessment of embedded tacit operational capability. This *strengthens* the structural-precedent argument: both mechanisms shared the identical gap.
- **Confidence:** ~95% (2020 Guidelines verified in repo). Note: more defensible for the 2003 round (largely discretionary) than 2020; the reframe covers both.
- **Impact.** Ch3 line 39 `[confirmed]`; must stay consistent with A2's reframe; check Ch4/Ch6 if the marginal-field "no assessment" framing recurs `[predicted]`.

**Deferred to Chapter 4 (case acquisition facts — verify once, shared with Ch4):**
- Aiteo OML 29 acquired from Shell in 2015 (line 29).
- All six cases acquired from Shell (line 37) — seller-uniformity claim.
- Per-lease deal values/dates to verify at Ch4 and cross-check Ch3↔Ch4 consistency.


---

## SECTION G — Chapter 4 findings

### Cluster 1 · Aiteo OML 29 / Santa Barbara blowout (the critical experiment) — VERIFIED SOLID

**Sources.** Repo blowout special report (NGO/HOMEF field report, community-impact focused) + independent news (Vanguard, THISDAY, Businessday, Mongabay, Energy Voice, TheCable, THEWILL, allAfrica, Daily Trust) + biography (Wikipedia, Crunchbase, Grokipedia, Nairametrics, Peters.ng). The special report does NOT carry the regulatory statements; the news record supplies them.

**All load-bearing claims CONFIRMED:**

| Ch4 claim | Locus | Status | Anchor |
|---|---|---|---|
| Blowout November 2021 | L96 | OK (unspecified day is correct) | Leak ~Nov 1; Aiteo *reported* Nov 5. Both real; Ch4's vagueness sidesteps the dispute. |
| Santa Barbara Well 1, OML 29, Nembe, Bayelsa | L68 | OK | Special report + all news |
| Well dormant / non-producing since 2015, undecommissioned | L68 | OK | Vanguard, THISDAY ("dormant and non producing since its acquisition in 2015") |
| From Shell (+Total+Eni, 45%) in 2015; $1.7B stake / $2.562B with NCTL | L35 | OK | Special report ($1.7B stake); Grokipedia + Peters.ng ($2.56B w/ NCTL). Agreed 2014, completed Sept 2015. |
| JIT (NOSDRA+NUPRC) attributed cause to third-party interference | L133 | OK | Daily Trust, Mongabay |
| After-the-fact engagement of well-control specialists (Boots & Coots) | L113, L316 | OK | THEWILL, THISDAY, Energy Frontier, Mongabay |
| NOSDRA attributed containment difficulty to a capacity deficit | L113 | OK | Businessday Nov 25 ("Nigeria lacks the capacity"); Vanguard Dec 7 ("beyond the capacity of a single company like Aiteo to handle") |
| Containment ~33 days / "over a month" | L314 | OK (caveat) | Control date Dec 8 2021 firm (Energy Voice, THISDAY). 33 days = Nov 5 to Dec 8; ~37 from Nov 1. |
| Peters: geography & regional planning degree; downstream (fuel storage + trading) | L74, L297 | OK | Wikipedia, Crunchbase, Grokipedia, Nairametrics |

**Findings:**

- **G1 [RETRACTED] — false alarm on the keystone.** My in-session preliminary flag (that the NOSDRA capacity attribution at L113 was a misattribution, because the special report lacks it) is WITHDRAWN. A confirmatory search showed NOSDRA DG Idris Musa explicitly said the spill was "beyond the capacity of a single company like Aiteo to handle" (Vanguard, Dec 7 2021) and that "Nigeria lacks the capacity" (Businessday, Nov 25 2021). The claim stands. *Lesson: absence in one primary source is not fabrication; a real search was required before flagging.* SOURCING NOTE for the pass: cite Businessday/Vanguard for L113, not the special report.

- **G2 [SOURCING NOTE].** Boots & Coots engagement is real for the Nov 2021 blowout, but the repo special report's Boots & Coots mention (its line 404) belongs to a DIFFERENT, earlier OML 29 incident (DPR May 2020 promise; fire "still burning August 2021"). Cite news, not the special report's line 404.

- **G3 [PRECISION, minor].** "33 days" (L314) is defensible (Nov 5 reported to Dec 8 controlled) but the disputed start date makes the true count 33-37 days. Control date Dec 8 2021 is firm. Options: keep "33 days" with a source, or soften to "about five weeks." Ikenna's call.

- **G4 [RESOLVED].** Deal values ($1.7B stake; $2.562B ~= $2.56B with NCTL) CONFIRMED. No change.

- **G5 [ENHANCEMENT — AUTO-APPROVED 2026-06-23; incorporate in pass].** Bib added: `businessday2021nembe`, `vanguard2021nembe`, `thisday2021baptism`. Two documented facts strengthen the capability/preparedness reading while respecting the two-inference discipline (these are operational evidence, kept separate from the funded-growth/capital inference):
  (a) NOSDRA DG: Aiteo "did not subscribe" to the international oil-spill response service (OSRL-type) that let Shell contain the 2011 Bonga spill quickly, so foreign well-control had to be contracted reactively ("negotiate terms and that will take some time") — Businessday, Nov 25 2021. A precise *no-standing-contract* anchor plus a clean Shell-vs-Aiteo preparedness contrast.
  (b) THISDAY editorial (Nov 29 2021): Aiteo/NNPC "displayed a shocking absence of an effective blowout contingency plan" and "lacks the technical know-how to manage and monitor its oil assets." Corroborates the absent-contingency-plan / undecommissioned-well anchors.

- **G6 [NOTE].** NOSDRA officially classified the spill **Tier 2** (Vanguard, Dec 7 2021); the NGO report/environmentalists said "Tier 3." If any tier label appears in Ch4 or appendices, use NOSDRA's Tier 2.

**Confirmed A1/A2 loci in Chapter 4 (feed the impact maps):**
- **L153** "Section 29 of the Petroleum Act required ministerial consent to assign the lease while leaving the acquirer's fitness, capability, and governance untested" — direct instance of BOTH A1 (Section 29 -> Para 14/16) AND A2 (the "untested" claim is exactly what Para 16(b) contradicts).
- **L84** NUPRC "seven-pillar ... first" framing — A2 locus (reframe to operationalized-comprehensive-framework claim).
- **L86** regulatory-gap discussion — A2 locus.

**Deferred within cluster 1 -> cluster 2:** the production figures in the L35 table (modeled ~41k peak / NEITI 38.2k 2021 / 4.9k metered + 0.7k fiscalized 2022 / 7.4k NUPRC 2024) verified next against Wood Mackenzie (project knowledge) + NEITI extraction logs (this chat) + repo NEITI audits, honoring measurement-basis discipline.


### Cluster 2 · Production figures (Tables 4.1/4.2) — Ch4 figures VERIFIED; consistency flags in Ch1

**Sources.** Project knowledge: Task2_Evidence_Mining_Results.md (NEITI audited series 2014-2023 + WoodMac modeled series 2016-2025), Section_4_5_Figure_Traceability_Table (basis-tier mapping), NEITI_OML26_extraction_log.md, Figure 4.1. Cross-checked against repo NEITI audits.

**Ch4 production figures — ALL CONFIRMED against the audited + modeled series:**

| Operator | Ch4 claim | Verified against extraction |
|---|---|---|
| Aiteo OML 29 | modeled peak ~41k (2020); NEITI 38.2k (2021); 4.9k metered/0.7k fiscalized (2022); 7.4k NUPRC (2024) | WoodMac 41.1 (2020); NEITI 38,195 (2021); 4,925 / 0.7 (2022); 7.4 (2024) OK |
| Eroton OML 18 | modeled 32k peak | WoodMac 32.0 (2019) OK |
| Seplat 4/38/41 | ~53k combined peak (2018); NEITI 42.3k (2021), 43.1k (2020) | WoodMac 52.6 (2018); NEITI 42,296 (2021), 43,140 (2020) OK |
| Shoreline OML 30 | NEITI 24k (2021), 30k (2022) | NEITI 23,936 (2021), 29,560 (2022) OK |

Measurement-basis discipline correctly applied: cells labeled modeled vs audited; Figure 4.1 uses WoodMac modeled with audited-actual stars for disrupted years (2022 = 0.7; 2024 = 7.4); OML 30 operator-reported 67k labeled and the inflated 80k claim explicitly set aside (line 191).

**Cross-chapter consistency findings (Ch1 v30 carries operator-PR figures Ch4 avoids):**

- **H2 [LOCAL — RESOLVED].** Ch1 line 31 "accumulated two million man-hours without a recordable safety incident" is WRONG. Seplat's 2024 full-year figure is **11 million** man-hours LTI-free (Seplat 2024 Annual Report; Chairman AGM statement; AfriSAFE 2024). Ch1's "two million" likely came from Q1 2024 (2.3 million). Ch4 line 175 already uses "more than 11 million." FIX: Ch1 -> "more than 11 million man-hours." Strengthens the thesis. Confidence ~99%. Resolved within H1 family (no bib change; Seplat 2024 already cited).

- **H3 [consistency/accuracy — flag].** Ch1 line 25 states the blowout "spilled an estimated 200,000 barrels (SDN, 2022)." Cluster 1 found the federal government denied the 200,000 figure and the volume was never officially determined (claims ranged 2 million / 200,000 / unknown). Ch4 avoids any volume. RESOLUTION (recommended): caveat as "an SDN estimate the federal government disputed," or align with Ch4 and drop the number. Ikenna's call on which; either restores consistency. ("41 communities" recurs Ch1 line 43; SDN 2022; special report says "no fewer than 40" -- minor, leave SDN-attributed.)

- **H7 [verify].** Seplat acquisition "$340M (45%, from a $610M valuation)" (Ch4 L38) -- Section 4.5 table flags it "not re-verified this pass." Verify in cluster 4 / web.

- **H8 [citation accuracy — verify].** Ch1 line 28 cites "(Wood Mackenzie, 2026)" for Eroton "recognized by NNPC as one of two operators with the lowest technical cost per barrel." Originates with San Leon Energy / NNPC, not WoodMac. Verify WoodMac 2026 supports it; else revert to the San Leon/NNPC source.

**Pre-existing extraction-log flags to fold into the pass:**
- NEITI_OML26 log: the clause "recovering to around ten thousand by the early 2020s" (OML 26/FHN, Section 4.4.2) holds on WoodMac and on NEITI only for 2020-2021; NEITI shows a 2022-2023 relapse to 3.7-6.2 kb/d. Decide which source the thesis privileges. -> cluster 3.
- Section 4.5 table: Seplat flaring 11.4% "not re-extractable from the report dump this pass; stated qualitatively" -- confirm against NEITI 2021 in the pass.

**Confirmed via Ch1<->Ch4 consistency (no action):** marginal-field 2003 round = 24 fields to 31 companies, 11 revoked, ~2% of reserves; deal values (Aiteo $1.7B/$2.562B); NOSDRA capacity attribution; well non-producing since 2015 + prior 2018/2019 spills.

**Deferred to later clusters (surfaced here):** FHN/Afren (FTSE 250, $2.6B, 45% OML 26 in 2011, CEO/COO SFO conviction 2017, administration July 2015 -- cluster 3); Shebah/Trinity Spirit FPSO 2022 ~10 deaths (context); Renaissance/SPDC $2.4B, ex-Shell staff, >200k bpd Apr 2025, "first in 15 years" (seller-independence); NPDC 23% efficiency (Adekunle 2019), target 180k->500k, Benin River Valve Station OML 40 July 2020 seven deaths (cluster 5); Salvic team 27 yrs Shell + 39 yrs NNPC (cluster 4); national production 2.5M(2005)/1M(2022)/1.5M(2024)/2M target (context); Rexer spill figure +10% operational-failure vs +18% (consistency note).


### Cluster 2 — RE-EXTRACTION from NEITI 2021/2022 audits (both contested quantities RESOLVED)

- **H9 [ENHANCEMENT — AUTO-APPROVED; flaring is AUDITED and exact].** NEITI 2021 Table 33 (2021 Gas Utilisation, mmscf; columns Flared / Re-injection / Fuel / Sales / Unaccounted / Total) gives flare intensity = Flared / Total:
  - **NPDC/SEPLAT JV: 11,323 / 99,617 = 11.4%** (line 7332).
  - Cross-checks (exact): **Aiteo 7,105 / 14,350 = 49.5%** (line 7260); **Eroton 6,285 / 17,840 = 35.2%** (line 7292).
  All three match Ch4 line 25 to one decimal. The Section 4.5 table's "11.4% not re-extractable this pass; stated qualitatively" caveat is REMOVED: state the flaring as NEITI 2021 audited figures with the explicit flared/total basis. No bib change (NEITI 2021 already cited).

- **H10 [LOCAL/accuracy — CONFIRMED via re-extraction; clause needs fix].** OML 26 crude (NEITI metered), verified to file/line:
  - **2021 = 3,198,427 bbls = 8.8 kb/d** (NEITI 2021, per-operator metered table, line 4960).
  - **2022 = 1,338,742 bbls = 3.7 kb/d** (NEITI 2022, row "NEPL/FHN | FB | 26", line 3381).
  - (2023 = 2,260,970 bbls = 6.2 kb/d per the extraction log; same basis.)
  The audited relapse (8.8 -> 3.7 kb/d) is real. The earlier markdown reading of ~10k for 2022-2023 was GAS (mmscf) misread as oil. FIX (audited governs over WoodMac's modeled smooth ~10k): revise the Section 4.4.2 clause "recovering to around ten thousand by the early 2020s" to state that OML 26 reached ~9 kb/d (audited) only in 2020-2021 and relapsed to 3.7 (2022) / 6.2 (2023) kb/d. Confidence ~99%. (Note: per the 4.4.2 framing, OML 26 production does not measure FHN capability anyway -- NPDC operates, FHN never operated -- so this is an accuracy fix, not a verdict change.)


### Cluster 3 · Afren / First Hydrocarbon on OML 26 (Section 4.4.2) — VERIFIED

**Sources.** UK SFO press release (2018-10-29); Royal Gazette, Willkie Farr, Offshore Energy (Oct/Nov 2018); NEITI re-extraction (H10); Ch4 vs Ch1 cross-check.

**Confirmed (Ch4 4.4.2):**
- FHN acquired 45% OML 26 (Shell 30% + Total 10% + Eni 5%) from the Shell JV in 2011 (agreement Oct 2010); NPDC 55%. OK
- FHN = SPV created by London-listed Afren plc; Afren held 45% of FHN at completion. OK
- FHN never operated; NPDC ran the asset under a first-refusal clause (consistent with the NEITI "NEPL/FHN" rows + NPDC operatorship). OK
- Afren FTSE 250, peaked ~$2.6B market value (FTSE 250 certain; $2.6B widely reported). OK
- CEO Osman Shahenshah + COO Shahid Ullah convicted **2018** of fraud + money laundering. OK (SFO 2018-10-29)
- Diverted ~$45M (15%) from a $300M transaction with Oriental Energy (Nigerian partner) into a BVI/Caribbean + Bermudian shell. OK (exact)
- Afren collapsed into administration July 2015. OK
- Nigerian banks lost ~$185M (Vanguard 2015; N31.45bn ~= $185M at ~2015 FX). OK
- Capital constraints rejected (well-funded FTSE 250 failed via governance fraud, not funding scarcity). OK

**Finding:**
- **H11 [LOCAL — cross-chapter consistency].** Ch1 v30 cites the SFO conviction as "(UK Serious Fraud Office, 2017)"; the conviction/sentencing was **29 October 2018** (charges were Sept 2017). Ch4 correctly says 2018. FIX: Ch1 -> 2018. Confidence ~99%.

**Good-practice note (do NOT reintroduce):** the SFO "30 years" headline is the sum of concurrent counts across both men (~6 years actual each); both Ch1 v30 and Ch4 correctly avoid stating "30 years." Keep it that way.

**H10 status:** Ch4 v9 line 159 already states OML 26 "reached roughly eight to ten thousand around 2020 to 2021. The audited record then shows output slipping back" -- which matches the re-extraction (8.8k 2021 -> 3.7k 2022). The flagged "recovering to ten thousand by the early 2020s" was an older-draft phrasing; Ch4 v9 is accurate. H10 is RESOLVED in Ch4 (verify the same in Appendix E/F during the pass).

**Secondary (accept; low-priority):** Court of Appeal refused appeal 2019 + £5.45M confiscation 2020 (Ch4; consistent with timeline, not independently re-verified); Afren 45%->70% of FHN, $280M facilities, ~$98M acquisition (Shell portion) -- minor financing details, accept as cited.


### Cluster 4 · Salvic / Shoreline / HEOSL — OML 30 (Section 4.5.x) — VERIFIED

**Sources.** Wood Mackenzie report title; Vanguard (2013-02-04), allAfrica (2013-02-11), Heritage Oil Wikipedia/company profile, Shoreline Natural Resources site/LinkedIn (acquisition); TheCable / Premium Times / Punch / Guardian / businessamlive / Orient Energy Review HEOSL interview (operatorship + turnaround); Salvic Executive Team + Board pages (team credentials).

**Confirmed:**
- OML 30 acquisition: Shoreline Natural Resources (JV of Nigerian Shoreline Power + Heritage Oil, via Heritage Oil Shoreline Natural Resources (Nigeria) B.V., a subsidiary of Heritage Oil Limited, UK) acquired 45% (Shell 30% + Total 10% + Eni 5%) for **US$850 million**; announced June 2012, SPA signed 29 June 2012, completed effective Nov 2012; NNPC/NPDC held 55% and pre-empted operatorship. OK -- resolves the OML 30 deal value.
- HEOSL = indigenous, 100% Nigerian, non-equity-holding third-party operator; took over OML 30 + Trans Forcados Pipeline from NPDC in **March 2017**. Heritage Oil Limited (UK) is the parent of the Shoreline equity side; HEOSL itself is indigenous. (HEOSL-indigenous classification HOLDS.) OK
- Salvic Petroleum Resources = HEOSL's technical operator under a Technical Services Agreement, **March 2017 to April 2018**, with a **$25M penalty** if production targets were missed. OK
- Turnaround: from zero (15 months shut-in, TFP down) to **75,000 bpd by end-Dec 2017 without drilling new wells**; TFP restored in under 3 months at 86% uptime; 1.1M+ LTI-free man-hours by Feb 2018; no major HSSE incident. OK (operator-reported; Ch4 correctly labels operator-reported figures and sets aside the inflated 80k claim; WoodMac ~35k / NEITI ~24-30k govern the production-basis series).
- Salvic team credentials:
  - 39-year NNPC engineer who managed the Shell-to-NPDC takeovers of OMLs 26/42/30/34/40 = **Simon M. Ukpaka**. CONFIRMED exactly (Salvic site).
  - 27-year engineer = **Boma Brown** (27+ years O&G; joined Shell/SPDC as an O&G Engineer after an initial SSL seismologist stint; Shell leadership in Engineering, Production, Planning, Project Management, Technical Auditing, Asset Management). CONFIRMED as a real Salvic team member.

**Finding:**
- **H12 [LOCAL/precision -- minor].** Ch4 ~line 191 "an engineer with twenty-seven years at Shell's Nigerian operating company" = Boma Brown, whose bio gives "over 27 years" of TOTAL industry experience (SSL first, then Shell), not 27 years at Shell specifically. Optional refinement: "twenty-seven years in the industry, with engineering and asset-management leadership at Shell's Nigerian operating company." The analytical point (deep Shell + NNPC operating depth on the Salvic team) stands either way. Confidence ~98% Boma Brown is the referent (unique 27yr+Shell combo). Ikenna's call (GOLDEN RULE).

**Note (CEO):** Salvic CEO Ikemefuna Okafor is an oilfield-services veteran (Schlumberger/ORION/Shebah E&P), NOT the 27-year Shell person -- do not attribute the Shell tenure to him.


### Cluster 5 · NPDC (Section 4.5.3) — VERIFIED (no errors; one minor bib note)

**Sources.** Consensus (Adekunle paper); references.bib abstract; Africa Oil+Gas Report / ThisDay / Punch / Upstream / Energy Voice / Orient Energy Review / The Nation / Blueprint / AIT (Benin River); Vanguard 2017 + Reuters/Rigzone + Leadership + Guardian + Businessday (500k target).

**Confirmed:**
- **Adekunle et al. (2019) technical efficiency.** Paper is REAL (Consensus top hit; Cogent Engineering 6(1); DOI 10.1080/23311916.2019.1575638; 6 citations). Abstract gives the grades verbatim: national oil company (NPDC) = **23%**, joint venture = **75%**, marginal field = **67%** (also sole risk 65%, PSC 64%, service 42%). Matches Ch4 exactly (NPDC 23%, JV ~75%, marginal-field 67%). OK
- **Benin River Valve Station explosion (the "valve-station fatalities" table cell).** Incident **7 July 2020** (NNPC press release 8 July 2020), Gbetiokun field, **OML 40**, operated by **NPDC** on behalf of the NPDC/Elcrest JV; **seven fatalities** during installation of a ladder on the BRVS platform; the dead were contractors (Weld Affairs and Flow Impact). Confirmed by ~10 independent outlets. OK (the bib's "8 July" = release date; incident = 7 July; both correct).
- **NPDC 500k-by-2020 target from ~180,000 bpd in 2017** (Vanguard 2017; MD Yusuf Matashi, Sept 2017). Confirmed exactly across Vanguard + Reuters/Rigzone + Leadership + Guardian + ThisDay. The "fell short" is also confirmed: the NNPC Dec 2017 monthly report put NPDC actual equity production at ~90,548 bpd, far below both the 180k stated baseline and the 500k target. OK
- OML 26 cross-ref in 4.5.3 (8.8k 2021, 3.7k 2022, 2022 fiscalized ~3.2k) is consistent with the cluster-2 re-extraction (H10). OML 30 cross-ref (3,800 trough, HEOSL recovery) is consistent with cluster 4. OK

**Finding (minor):**
- **H13 [bib cleanup -- minor].** Adekunle 2019 second author is Wumi Iledare (Omowumi O. Iledare), but references.bib stores him as "Omowumi, Iledare O." -- surname/given reversed; should be "Iledare, Omowumi O." Invisible in the "Adekunle et al." in-text cite; would mis-render in the references list. Low-priority.

**Note:** The 180k-2017 baseline was NPDC's own stated figure; audited production was lower (~90.5k, Dec 2017 NNPC report). The thesis cites the stated 180k->500k framing (accurate to the Vanguard source); the lower audited actual only strengthens the "fell short / lowest efficiency" reading. No change required.


### Cluster 6 · Opu Nembe Kingdom v Aiteo (Ch4 line 133, Section 4.4.1) — VERIFIED; conflation flag CLOSED

**Sources.** Niger Delta Herald, New National Star, Lawyard, Newsonline, Daily News Nigeria, Southern Examiner, Bayelsa State Oil + Environment Commission report, TheCable (2025 fresh spill).

**Resolution of the earlier "conflation" flag:** In the CURRENT references.bib, opunembe2024 (the court case) and homef2021 (the HOMEF ecological-horror-tale blog) are SEPARATE entries. opunembe2024 has a clean court-case citation with no URL. The earlier note that opunembe2024 "conflates the court-case title with a HOMEF URL" is OUTDATED -- already resolved. CLOSED.

**Confirmed:**
- **Suit No. FHC/YN/CS/284/2024 is REAL** (cited verbatim by multiple independent outlets). Not fabricated. OK
- Case: Opu Nembe Kingdom (King Iyerite Chiefson Awululu Atubu et al.) v Aiteo Eastern E&P Company Ltd, Federal High Court, Yenagoa, Bayelsa; filed 15 August 2024; lead counsel Iniruo Wills (Ntephe Smith and Wills); claim ~N122bn. OK
- Allegations match Ch4 exactly: spills resulted from "operational failure and negligence" and "failure to replace corroded pipelines." OK
- Suit PENDING (no merits finding): as of early 2026 the court struck out Aiteo's preliminary objection (10 March 2026) and granted amendment of the defendant's name; substantive hearing ahead. Ch4's "the suit is pending, with a finding yet to be made" is ACCURATE, and the conditional framing ("if established, would reopen that reading") is well-calibrated. OK
- Underlying spills: the suit covers three incidents (Sept 2019 NCTL Botokiri axis; Oct 2019 Santa Barbara Well 1; May 2020 Odeama Creek Well 9). Ch4's "trunk-line spills" captures the NCTL + corroded-pipeline component. OK

**Side-findings (optional / awareness):**
- The OML 29 operating entity changed its name from **Aiteo Eastern E&P to Nembe Exploration and Production Company Ltd (NEPCo) on 4 March 2025**. The thesis cites the case by its original filing name, which is correct for the proceedings; optionally note the name change. No bib edit required (the suit number is the key identifier and is confirmed). 
- **Cross-reference to H3:** the Nigerian Senate estimated the Nov 2021 spill at "over two million barrels" (Aiteo disputed it); SDN's figure was ~200,000 (Ch1). The volume was never officially determined (JIV inconclusive; Bayelsa govt rejected it). Reinforces H3: Ch1's "200,000 barrels (SDN, 2022)" should be caveated as a contested estimate. (No new action; folds into the existing H3 decision.)

**CLUSTERS 1-6 COMPLETE.** Remaining: deferred carry-ins (H7 Seplat $340M; H8 Eroton "lowest cost" citation; A6 per-lease PML conversion; Shebah/Trinity Spirit FPSO; Renaissance/SPDC; national production figures), then George Q1-Q3 + integration items, folded into the single prose pass.


### CARRY-INS — completed

- **H7 [LOCAL — Seplat $340M / $610M].** $340M CONFIRMED for the 45% interest in OMLs 4/38/41 (2010): M&P paid $153M + guaranteed the $187M BNP bridge loan to Shebah/Platform = $340M total cash to Shell/Total/Eni (Africa Oil + Gas Report; Seplat history). Avuru (Platform Petroleum, wellsite geologist, ~30 yrs) and Maurel et Prom partnership confirmed. BUT the **"$610M valuation" parenthetical does not reconcile** (45% of $610M = $274M; $340M/0.45 implies a $755M whole), is not corroborated, and should be verified against the Seplat 2014 prospectus or dropped. FLAG.
- **H8 [LOCAL/citation — Eroton "lowest cost"].** Claim is REAL but MISCITED. Ch1 line 25 attributes "recognized by the NNPC as one of two operators with the lowest technical cost per barrel" to "(Wood Mackenzie, 2026)." The claim actually originates from **Eroton's press release of 13 March 2023** (MD Emeka Onyeka), noted by **San Leon Energy** (RNS, 14 March 2023) and reported across Nigerian media; it is a self-report made during Eroton's operatorship dispute with NNPC. FIX (prose pass): change the citation to sanleon2023 (added to bib); optionally frame as Eroton's claim. Confidence ~99%.
- **A6 [RESOLVED].** Ch4's fiscal verdict (4.3.2 + Table 4.3) rejects fiscal effects on TIMING (transaction closed 2015; PIA enacted Aug 2021), not on Hydrocarbon-Tax rates or PML conversion. The per-lease OML->PML detail belongs only in the Ch2 framework (already fixed at Ch2 line 59). No Ch4 change. CLOSED.
- **Renaissance / SPDC — CONFIRMED.** $2.4B for 100% of SPDC (Shell's onshore subsidiary, which held 30% of the JV); Shell completed the sale **13 March 2025**; production surpassed **200,000 bpd by April 2025** (all pipelines working 12 April 2025). Staff-retention framing consistent (BusinessDay 2025; "first in 15 years" per Africa Oil + Gas Report 2024). Ch1 line 35 accurate. OK
- **Trinity Spirit FPSO — CONFIRMED with TWO precision flags.** Event 2 Feb 2022; Shebah/SEPCOL (in receivership); 1976-built FPSO at the Ukpokiti field. Flags: **(a) age** -- the vessel was **46 years old**, so Ch1's "nearly 50-year-old" is loose; use "46-year-old." **(b) death toll** -- Ch1's "killing at least 10 crew members" OVERSTATES: ten were aboard; the most detailed account (Lloyd's List) reports 3 confirmed dead + 3 rescued + 4 unaccounted (so up to 7 died), and the operator/NUPRC downplayed fatalities. Soften to e.g. "with ten crew aboard, several confirmed dead and others never found." (Aside: SEPCOL's CEO Ikemefuna Okafor is the same person who later led Salvic on OML 30.) FLAG both.
- **National production (2.5M 2005 / ~1M 2022 / ~1.5M 2024 / 2M target) — ACCEPTED.** Corroborated across searches (BRS ~1.25M crude 2022; ~1.63M 2025) and widely established; cited OPEC 2022 + NUPRC 2024. No change.

bib: ADDED sanleon2023 (backup references.bib.bak_carryins).


## APPENDIX E/F CONSISTENCY SWEEP (against every corrected claim)

**Canonical files.** Appendix E = Verdict Traceability Matrix (Appendix_E_Verdict_Traceability_Matrix.md, mtime 2026-06-21, current). Appendix F = Survey Response Data (Appendix_F_Survey_Response_Data.md). The Appendix_F_Verdict_Traceability_Matrix_v2..v17 series is the SUPERSEDED F-lettered history of the matrix (now re-lettered E); do not edit it. Matrix structure: one row per case x explanation (Tables E.1-E.7), columns Explanation / Verdict / What would change this verdict / Evidence / Evidence type / Verdict established / Confidence.

### Appendix E — rows that MUST move with the chapter (apply in the single prose pass):

- **[A1 — Section 29] 2 rows.** E.1 Aiteo regulatory-inadequacy ("Section 29 specifies no capability criterion") and E.3 FHN regulatory-inadequacy ("Section 29 required ministerial consent but no fitness, capability, or governance test"). Fix the statute reference to Petroleum Act First Schedule Para 14 (assignment consent) / Para 16 (criteria), matching the chapter A1 decision.
- **[A2 — mandate reframe; THE DIRECTION-CHANGER] ~6 rows.** Every regulatory-inadequacy row plus the marginal-field row carries the "no capability criterion / screened no capability / no capability test / none before" framing: E.1 ("none before"), E.2 ("screened no operational or organizational capability at transfer"), E.3 ("no fitness, capability, or governance test"), E.6 ("screened no capability"), E.7 ("no capability test"); E.4/E.5 echo "same pre-2024 framework." Reframe from "no mandate existed" to "the mandate existed (Petroleum Act 1969 Para 16(b): sufficient technical knowledge and experience) but lacked operational specificity for embedded capability." **RESOLVES THE OPEN QUESTION: the VERDICT ("an enabling condition insufficient on its own") SURVIVES; only the BASIS reframes.** The discriminating logic ("same pre-2024 framework, different outcomes across operators") is untouched and still supports "insufficient on its own"; the reframe makes the gap a specification/execution failure rather than an absence, which strengthens the thesis. Chapter and matrix must reframe in lockstep.
- **[B1 — excise non-discriminating production from the PE rejection] 2 rows.** E.4 Seplat PE row cites "sustained production and 11M+ man-hours" -> rest the PE rejection on the LTI-free man-hours alone (excise "sustained production"). E.5 OML30 PE row cites "rehabilitation... and the production growth" -> rest on the rehabilitation/technical achievements (excise "production growth"). Production is non-discriminating under the thesis's own Rexer premise (connections RAISE production), so it cannot carry a PE rejection. Matches the standing B1 finding.
- **[H12 — Boma Brown] 1 row.** E.5 capability row says "Brown, 27 yrs SPDC." Couple to the chapter H12 decision: if "twenty-seven years at Shell" is refined to "twenty-seven years in the industry, with leadership at Shell's Nigerian operating company," match here (Brown's 27 yrs is total industry experience, not 27 yrs at SPDC).
- **[G5 — Aiteo anchors; enhancement, optional] 1 row.** E.1 capability row may ADD the no-standing-well-control-contract (OSRL-type) and THISDAY contingency-plan-absence anchors if the chapter adds them.

### Appendix E — ALREADY consistent (NO fix needed):
- **H10 (OML 26):** E.6 already states "~3,700 bpd metered and ~3,200 fiscalized in 2022" -- matches the re-extraction. OK
- **H7 ($340M):** E.4 uses "~$340M"; no "$610M valuation" appears in the matrix. OK (the $610M issue is confined to the Ch4 table line 38.)
- **H2 (11M man-hours):** E.4 uses "11M+ man-hours." OK
- **H9 (flaring) and H3 (spill volume):** neither the 49.5/35.2/11.4 flaring figures nor the 200,000/2M spill volume appears in the matrix. OK (N/A.)
- **Verdict vocabulary:** all verdicts use the five locked Section 2.6 terms (with dimensional qualifiers) plus the matrix-defined "not tested / not applicable" test-status. No out-of-set terms. OK

### Appendix F (Survey Response Data):
Practitioner-perception data from Group A/IOC sellers; independent of the case-fact corrections. Quick scan finds none of the corrected figures. NO changes from the sweep.

### Downstream note:
The matrix header points to **Appendix D** ("supporting evidence, with full citations") for the detailed evidence behind these rows. Appendix D is the same-direction downstream locus for A1, A2, B1, H12 -- check it in the prose pass so D, E, and the chapter all move together.

**SWEEP COMPLETE.** Net Appendix E edits required: A1 (2 rows), A2 (~6 rows, verdict-preserving), B1 (2 rows), H12 (1 row), G5 (1 row optional). All deferred to the single prose pass, coupled to their chapter loci.


## CH5 / CH6 / APPENDIX D — CLAIMS-AND-CITATIONS INVENTORY + DEEP-CHECK (COMPLETE)

Full inventory in Ch5_Ch6_AppD_Claims_Citations_Inventory.md. All citation forms captured (parenthetical, narrative, instrument-name). Four-bucket classification; first three buckets deep-checked.

**New-citation bucket — ALL VERIFIED.**
- Oriaku et al. (2016) VERIFIED EXACT (44% of 18 firms, 60% min, tubing inspection). Already in bib.
- Akinwale et al. (2022) VERIFIED EXACT (collaboration low: FI 2.50, Govt 2.43, Univ 2.31). Already in bib. Distinct from Akinwale 2018.
- Aiteo v. Shell (FHC/ABJ/C8/738/2021) VERIFIED (27 Jul 2021, FHC Abuja, Pinheiro SAN, $2.5B; Kugbo West + Okiori wells pre-transferred to FGN; non-disclosure of asset condition). Already covered by aiteoVshell2021. On-point Gap-1 (disclosure) support. "C8" is the universally-reported code.
- NSTA Capability Pack VERIFIED; DATE FLAG: final guidance 8 Oct 2024 (after Mar-May 2023 consultation); statutory basis Energy Act 2023. Thesis cites "NSTA 2023." Bib nsta2024 ADDED; reconcile in-text date in the pass.
- Coase 1960, Pigou 1920, Leveson 2011 VERIFIED + usage correct; ALL already in bib.
- Nightingale & Rhodes 2015, Trist & Bamforth 1951 confirmed in Ch2 + bib.
- NET NEW BIB ENTRY FROM ENTIRE SWEEP: one (nsta2024).

**Restated-fact bucket — AppD has real consistency issues; Ch5/Ch6 largely clean.**
AppD citations clean; NO A1/A2 statute language in AppD. AppD fixes for the prose pass:
- H2: "two million" man-hours -> 11 million (lines 14, 100).
- Seplat-MPNU price: "$1.28 billion" (lines 14, 96) vs Ch4 "$800M" -- ~$480M discrepancy, verify + reconcile.
- OML 30 basis: "25-45k NPDC / 80k HEOSL" vs matrix audited "trough ~3,800 / ~67,000" -- reconcile gross-vs-audited.
- Aiteo basis: "90,000 bpd" (gross) vs audited 38.2k -- label gross.
- Renaissance price: "$1.3B" (line 19) vs "$1.3B ($2.4B total)" (line 158) vs Ch1 "$2.4B" -- present consistently.
- H3 spill volume "200,000+ barrels" (lines 11, 32) -- contested caveat (same as Ch1).
- Trinity Spirit "nearly 50-year-old"->46; "10 dead or missing"->contested toll (lines 20, 178).
- Tier-B spot-checks: Nembe buyer-beware decree; Eroton EFCC vs NNPC-audit; OML 66 Oct-2023 explosion; NPDC 332k late-2018; Afren 14-yr ban / N36.63bn; Neconde consortium; 41 communities; marginal-field 24-vs-30 denominators. None verdict-bearing.
Ch5: restated facts QUALITATIVE and consistent; regulator-pillar A2-consistent ("2024 reforms... the design extends them"; "corporate screen" insufficient for asset-specific readiness). No contested figures.
Ch6: cites PIA Sections 240 (HCDT 3% opex), 232/233 (Decommissioning Fund), 103 (environmental remediation) -- VERIFY against gazetted PIA in the pass (load-bearing statutory citations).

**Overclaim bucket — Ch6 CLEAN.** Locked Section 2.6 verdict vocabulary verbatim; two-inference discipline explicit; generalizability bounded ("corroborate... not prove universally"; "corroborating context that does not, by itself, carry the verdicts"; "no implementation data yet"); regulatory framing ALREADY A2-consistent (2024 reforms created a corporate-level technical-capacity route). "Capability-related factors" + "two outcome dimensions" throughout. No overclaim across 6.1/6.2/6.4/6.5. Ch5 framework claims bounded ("warrant the framework, short of proof from a tested intervention"). Confidence ~92%; close read of 6.3/6.6 in the pass settles the remainder.

**Structure bucket — no check needed** (loop dynamics, role allocation, pillar mapping, tiered apparatus, recommendation prose).

**Remaining bounded items for the prose pass:** (1) PIA Sections 240/232/233/103 vs gazette [HIGH]; (2) Seplat-MPNU $1.28B vs $800M; (3) NSTA in-text date 2023->2024; (4) AppD production-basis labels (gross vs audited); (5) Tier-B AppD spot-checks.

bib: ADDED nsta2024 (backup references.bib.bak_ch56appd).

**VERIFICATION SCOPE NOW COMPLETE across Ch1-Ch6 + Appendices D, E, F.** Remaining appendices A (Protocol), B (Discrimination Matrix), C (Interview Guides), G (Capability Element Traceability) are Tier-3 instrument/structural artifacts (light triage only). The single prose pass can now proceed against the consolidated ledger.


## HIGH-VALUE FLAG RESOLUTIONS + TIER-B CHECKS (this session)

### PIA statutory citations (Ch6 6.2 + 6.3) — ALL VERIFIED against the gazetted PIA in the repo
- **Section 240** = Host Communities Development Trust settlor contribution/funding. Attribution CONFIRMED via internal cross-references (line 6695 "the Board of Trustees shall... under section 240... allocate from the host communities development trust fund"; line 6894 "payment made by the settlor under section 240(2)"). The 3% figure is OCR-obscured in the gazette but is the established PIA rate. VERIFIED (attribution solid; 3% external-confirmed).
- **Section 232** = "Abandonment, decommissioning and disposal" (TOC line 423-424); the decommissioning-and-abandonment fund "complies with sections 232 [and 233]" (lines 2742, 3858). VERIFIED.
- **Section 233** = companion decommissioning/abandonment fund provision. VERIFIED.
- **Section 103** = "As a condition for the grant of a licence or lease," a "financial contribution to an environmental remediation fund established by the Commission or Authority" (lines 3664, 3670, 3681). Confirms Ch6's "a financial contribution the Commission can reach, fixed at the point of operation." VERIFIED.
- **BONUS (from 6.3 close-read) — also verified:** Section 95 = "Assignments, mergers, transfers and acquisitions" (line 199) -- this is the A4-correct assignment-consent reference, confirming Ch6 does NOT carry the A1 "Section 29" error. Section 231 = "Power to issue administrative penalties" (line 422). Section 7 (Commission functions) present; 7(d)/7(g) are standard enumerated powers. Assignment Regulation 2024 Reg. 7 = "Due diligence by the Commission," 7(2)(a) "technical capacity" (lines 64, 291, 298) -- the A2-relevant route. **NOGICDA (not in repo, web-verified):** Section 31 = succession plan + 4-year understudy of incumbent expatriate (NCDMB official text); Sections 43-47 = technology transfer + JV/partnering support. All VERIFIED. Ch6's statutory spine is fully accurate.

### Seplat-MPNU price ($1.28B vs $800M) — RESOLVED (both correct; presentation fix)
Deal originally valued at **$1.283 billion** (Feb 2022, incl. up to $300M contingent), **adjusted to a final consideration of $800 million** at completion **12 December 2024** ($128M deposit 2022 + $672M at closing; THISDAY: "No explanation was given for the difference"). So AppD's "$1.28 billion" = original 2022 headline; Ch4's "$800M" = final completion consideration (the accurate acquisition price). NOT a factual error -- a presentation-consistency issue. PROSE-PASS FIX: state consistently, e.g., "originally $1.28 billion (2022), completed at $800 million (December 2024)"; AppD line 96 + Table D.1 line 14 should adopt this. MPNU = 40% operated OMLs 67/68/70/104 + Qua Iboe + Bonny River (Ch4 "40% operated" confirmed).

### Ch6 6.3 + 6.6 — READ IN FULL; calibration CLEAN (overclaim bucket confirmed clean)
- 6.3 (Recommendations): six instrument-specific recommendations, each re-specifying an existing Nigerian instrument; risk-tiered; correctly cites PIA Section 95, Reg. 7, NOGICDA 31 + 43-47, PIA 7(d)/7(g)/231/240/232-233/103. Explicitly bounded: "warranted by the conditions the cases document, not by evidence of their effect... the claim is that they make capability assurable, not that they will prevent the next incident or raise national production." A2-consistent ("That route assesses capacity at the corporate level; the recommendations re-specify the same consent gate... to the asset-specific operating capability").
- 6.6 (Contribution/Conclusion): "The scope of this contribution is bounded by what the evidence supports... warranted by the documented regularities and the design logic, not by implementation results... The claim that holds is narrower and, within the cases examined, secure." Exemplary calibration. Citations Trist & Bamforth 1951, Nightingale & Rhodes 2015, Leveson 2011, Cohen & Levinthal 1990 -- all vetted.
- Ch6 close-read now COMPLETE (6.1-6.6). No overclaim anywhere. Confidence ~97%.

### Tier-B Appendix D checks
- **Nembe "buyer beware" decree 2015 (AppD line 48) — CONFIRMED EXACT.** allAfrica + EnviroNews: "in 2015 the Nembe community (Bayelsa State) placed a caveat emptor ('buyer beware') decree on a proposed sale from Shell to Aiteo," described as "prophetic" given the 2019/2021 blowouts. STRONG corroborating source for the community-foresight / pre-sale-capability-concern point. No change.
- **OML 66 "abandoned well explosion" Oct 2023 under NPDC (AppD line 136) — NEEDS CORRECTION.** The OML 66/NPDC incident was a GAS LEAK/blowout from non-producing well Kurogbagba 1 (TheCable, 27 Oct 2023), NOT an explosion (residents only feared fire). The Oct 2023 "explosion" was a SEPARATE incident at an abandoned wellhead in Okpoama Kingdom, Bayelsa. AppD conflates the two and mischaracterizes the OML 66 one. PROSE-PASS FIX: "October 2023 gas leak/blowout from a non-producing well (Kurogbagba 1) in OML 66 under NPDC" (drop "explosion"); optionally note the separate Okpoama wellhead explosion. (Underlying NPDC integrity-failure point holds.)
- **Still-unverified Tier-B (bounded, not verdict-bearing):** NPDC "332,000 bpd by late 2018"; Afren "14-year director ban" / "N36.63 billion"; Neconde consortium members (Aries Energy/VP Global vs Yinka Folawiyo); "41 communities" (Ch5/Ch6/AppD); marginal-field 24-vs-30 denominators; Eroton "EFCC investigation" vs the matrix's "NNPC forensic audit." Verify opportunistically.

## DEFERRED PROSE-PASS TASK (locked) — REBUILD TABLE 3.1 AS A LANDSCAPE TABLE
When the prose pass runs, rebuild the current Table 3.1 as a LANDSCAPE table with exactly these seven columns:
1. Explanation
2. Key prediction
3. Decisive falsification / discriminating condition
4. Test type
5. Operationalization / principal carrier case
6. Principal evidence sources
7. RQ link
Source content already exists (Ch3 discrimination logic + Appendix B Discrimination Matrix + Appendix E verdict matrix). The rebuild consolidates the five explanations (capital constraints, fiscal regime effects, regulatory inadequacy, political economy, capability-related factors) into the seven-column landscape format. Verdict vocabulary and the A2 reframe (verdict-preserving) must be carried in consistently; landscape orientation per MIT formatting for wide tables.

**STATUS:** All four explicitly-requested high-value items resolved (PIA sections verified; MPNU reconciled; 6.3/6.6 read; named Tier-B checked). Statutory spine fully verified. Remaining: a handful of non-verdict-bearing Tier-B spot-checks + the prose pass (now including the Table 3.1 landscape rebuild).


## RESIDUAL TIER-B CLEARED + 3% CONFIRMED (this session)
- **3% HCDT (PIA Section 240) — CONFIRMED EXACT (online).** Multiple legal sources quote the gazette: "section 240 of the PIA provides that three per cent (3%) of the actual annual operating expenditure of the preceding financial year in upstream petroleum operations shall be contributed to the host communities development fund" (Mondaq; ao2law "Section 240(2)"; piaandyou verbatim; African Journal). Political backstory confirms: communities sought 10%, House debated 2.5-5%, Senate pegged 3%. Ch6 6.2/6.3 wording exact. CLOSES the one OCR-obscured item.
- **Afren 14-year director ban — CONFIRMED EXACT.** SFO press release: "In March 2018, following an investigation by the Insolvency Service, both Shahenshah and Ullah were banned by the courts from being company directors for 14 years." Separate from custodial terms.
- **Afren N36.63bn / $185M Nigerian bank loss — CONFIRMED EXACT.** Guardian Nigeria: "Nigerian banks... lost a whopping N36.630 billion ($185 million) following Afren's liquidation." (Also confirms thesis's 6/5-yr concurrent custodial framing is correct vs the misleading "30 years" headline = sum of concurrent counts.)
- **Neconde consortium — RESOLVED, no conflict.** Nestoil (30%), Aries E&P = part of the Yinka Folawiyo group (25%), VP Global = local communities (5%), Kulczyk Investments + Kulczyk Oil Ventures (20% each); $390M for 45% of OML 42 (April 2011). AppD's "Aries Energy/VP Global" and the "Yinka Folawiyo" seen elsewhere are the SAME interest (two names for one shareholder). AppD accurate.
- **"41 communities" — CORROBORATED (minor precision).** EnviroNews: community leader cites "41 fishing settlements in the Nembe speaking area"; other outlets say "45 communities" or "about forty fishing settlements." 41 defensible; best stated as "41 fishing settlements/communities" or "more than 40." Non-verdict-bearing.
- **NPDC "332,000 bpd by late 2018" — UNVERIFIED / basis-ambiguous (FLAG).** Guardian Sept-2017 puts NPDC EQUITY production ~180k (target 400k 2019 / 500k 2020, never met); NUPRC 2023 shows ~153,592 bopd. 332k plausibly OPERATED/gross (NPDC operates many JV OMLs) but no direct source found for the number/date. PROSE-PASS: source it + label basis (operated vs equity) per Production Data Integrity Protocol. Not verdict-bearing (NPDC verdict rests on 23% efficiency + OML 30 within-asset comparison).
- **INCIDENTAL FINDING (new) — Boots & Coots vs Kenyon International West Africa.** TheCable's detailed account attributes the OML 29 well-kill to Kenyon International West Africa (CEO Victor Ekpenyong: "our company killed the well"), which may differ from/complement the thesis's Boots & Coots attribution in Counterargument 2. Argument holds either way (external contractor, after the fact; NOSDRA capacity-deficit anchor unaffected), but the SPECIFIC contractor name needs a quick reconciliation before the pass.

**ALL ASSIGNED TIER-B CLEARED. Verification scope fully closed across Ch1-Ch6 + Appendices D/E/F + statutory spine. Remaining open: Boots&Coots/Kenyon reconciliation (quick), the two held sign-offs (A1, A2 wording), and the single prose pass (incl. Table 3.1 landscape rebuild).**


## TRAJECTORY RE-DERIVATION + BOOTS&COOTS/KENYON + A1/A2 SIGN-OFF (this session)

### (a) Trajectory groups re-derived against audited figures — NO RECLASSIFICATION (Tier-1 clean)
Metric: later production / post-acquisition peak; >=70% sustained, <=30% deterioration, 30-70% claimed empty. Tested each case at its audited 2024 figure (Table 4.1):
- Aiteo: 7.4k / 41k = 18% -> deterioration (unchanged; not just the 2022 trough of 12%).
- Eroton: 13.6k / 32k = 42.5% -> still "growth then deterioration" (established by 2022 collapse; 2024 = partial recovery).
- Seplat: 39k / 53k = 74% -> sustained (just above 70%; also backed by 11M LTI-free man-hours, no integrity failure).
- HEOSL/OML30: ~35k / 35k = 100% -> sustained.
- FHN low-level survival; NPDC underperformance; marginal fields non-development (separate categories, no peak-share boundary).
RESULT: no case crosses a boundary. "Zero fundamental changes" now ~98%.
PRECISION FLAG (Tier-3, prose pass): Eroton's 2024 audited recovery (42.5%) falls INSIDE the 30-70% band, so the Ch4 line 27 claim "every one falls below 30% or above 70%" and "insensitive to the choice among them" is OVERSTATED. Fix: tie the empty-band claim explicitly to the 2022-trough basis (where Eroton is 2% fiscalized / 28% metered); note Eroton's 2024 recovery reflects easing of the external NCTL evacuation shock and is CONSISTENT with the confounded partial-replication treatment (Section 4.4); does not reclassify. Does NOT change any verdict.

### (b) Boots & Coots vs Kenyon — RESOLVED, NO CHANGE (thesis already correct)
Ch4 line 66 already distinguishes the roles precisely: "Halliburton's Boots and Coots working with a local resource. NOSDRA separately engaged Kenyon International for spill response" (cites Upstream Online 2021; Vanguard 2021). Boots & Coots = well control (Aiteo); Kenyon = spill response (NOSDRA). The accurate division. TheCable's "Kenyon killed the well" (CEO Ekpenyong) is reconcilable (Kenyon may be the "local resource"); argument holds regardless (external specialists after the fact + NOSDRA capacity-deficit anchor). My earlier flag came from reading TheCable in isolation. OPTIONAL: name Kenyon as the local executing partner to preempt readers who saw TheCable. NO required change.

### (c) A1/A2 sign-off language — DRAFTED (Sign_off_A1_A2.md), AWAITING IKENNA APPROVAL
A1 VERIFIED vs 1969 Act repo: assignment consent = First Schedule paragraph 14; criteria = paragraph 16 (16(b) "sufficient technical knowledge and experience"); revocation = paragraphs 26-30. "Section 29" wrong on both counts. Four A1 loci: Ch2 L79, Ch4 L153, Appendix E.1 (L18), E.3 (L44).
A2 reframe (verdict-preserving): mandate existed since 1969 (para 16(b)) but lacked OPERATIONAL SPECIFICITY for asset-specific operating capability/crisis readiness; 2024 NUPRC pillar made it explicit. Verdict "enabling condition insufficient on its own" PRESERVED via the differentiation logic (Ch2 L83 preserved verbatim). PRIMARY loci: Ch2 L73 ("the mandate did not exist"), Ch4 L84 ("the Petroleum Act... silent on it before"); plus Ch2 L81, Appendix E.1/E.6/E.7 (minor). E.2/E.4/E.5 already consistent. CAVEAT: wording must not tip regulatory inadequacy toward "primary driver."
Full current/proposed/rationale per locus in Sign_off_A1_A2.md. Three approvals requested: (1) A1 citation + 4 loci, (2) A2 reframe wording (esp. 2 PRIMARY loci + verdict-preservation read), (3) paragraph vs Paragraph capitalization.

**STATUS: verification fully closed; "zero fundamental changes" ~98% (one Eroton empty-band wording flag added to prose-pass list). Awaiting A1/A2 sign-off + capitalization preference to start the prose pass.**
