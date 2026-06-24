# Claims-and-Citations Inventory — Chapter 5, Chapter 6, Appendix D

Scope: a full inventory of the three previously-unverified units, capturing **all citation forms** (parenthetical author-year, narrative "Author (year)", and instrument-name), with every claim line classified into one of four buckets and the first three deep-checked. Companion to the Verification_Decision_Impact_Ledger.

**Bucket taxonomy.** (1) **restated-fact** = repeats a Ch4/Ch2 finding, must be consistent with the corrected version; (2) **new-citation** = a source/case not vetted in Ch1-4, needs existence/accuracy check; (3) **overclaim** = a generalizability/strength claim, needs calibration check; (4) **structure** = framework logic, prose, instrument design with no external factual claim, no check needed.

---

## 1. NEW-CITATION bucket — ALL VERIFIED

Citation extraction (parenthetical + narrative) across the three units surfaced six author-year sources new to the thesis prose plus one new court case and two regulatory comparators. Verification status:

| Citation | Where | Status | Note |
|---|---|---|---|
| **Oriaku et al. (2016)** | Ch5 (44% figure), AppD line 198 | **VERIFIED (exact)** | "Technical Assessment of In-Country Capabilities in the Oil and Gas Operations in Nigeria." Abstract: "for the Tubing Inspection Services, 44% out of the 18 companies sampled scored the mandatory 60% minimum required to qualify technically." Matches verbatim. Already in bib. |
| **Akinwale et al. (2022)** | AppD line 198 | **VERIFIED (exact)** | "Nigerian Marginal Oil and Gas Field Development: A collaborative perspective," African Journal of Science Policy and Innovation Management. Finds collaboration with Financial Institutions (2.50), Government Agencies (2.43), Universities (2.31) was low. Matches. Already in bib. (Distinct from the 2018 Akinwale paper on innovation capability.) |
| **Aiteo v. Shell (FHC/ABJ/C8/738/2021)** | AppD line 40 | **VERIFIED** | Filed 27 July 2021, FHC Abuja, counsel Kemi Pinheiro (SAN), $2.5B claim. Alleged Shell sold Kugbo West and Okiori wells already transferred to the FGN and did not disclose full asset condition. Matches AppD exactly. The "C8" code is what every public source reports (possibly a widespread transcription of "CS"); thesis matches all sources. Already covered by existing bib key aiteoVshell2021. On-point support for the disclosure gap (Gap 1). |
| **NSTA (capability pack)** | Ch5 lines 183, 196; comparator table | **VERIFIED; date-precision flag** | The NSTA Capability Pack is real: buyer and seller prepare a pack setting out the buyer's financial and technical capability for the consenting parties' assessment. **Date nuance:** the FINAL guidance was published 8 October 2024 (after the March-May 2023 consultation); the statutory change-of-control consent basis is the Energy Act 2023. The thesis cites "NSTA 2023." Bib entry nsta2024 ADDED; the in-text "(NSTA, 2023)" should be reconciled to 2024 (final guidance) or clarified as the 2023 consultation in the prose pass. |
| **Norway prequalification** | Ch5 line 185 | **ACCEPTED (well-established)** | The Norwegian Continental Shelf prequalification regime is a well-documented comparator. Optional spot-check; low risk. |
| **Coase (1960); Pigou (1920)** | Ch5 lines 78, 89 (Gap 4 externality) | **VERIFIED; usage correct** | Canonical externality references. Coase invoked as the bargaining objection, Pigou for intervention. Both already in bib. |
| **Leveson (2011)** | Ch5 line 109; Ch6 line 97 | **VERIFIED; usage correct** | "Engineering a Safer World" (STAMP). Used to frame the three-actor design as a systems-theoretic control structure (control actions + feedback holding a hazardous process within safe bounds). Correct usage. Already in bib. |
| **Nightingale and Rhodes (2015); Trist and Bamforth (1951)** | Ch6 line 97 | **VERIFIED (already vetted)** | Both confirmed present in Ch2 and in the bib. Enterprise-architecting and the sociotechnical-systems origin, respectively. |

**Net new bib entry required from the entire sweep: one (`nsta2024`).** Everything else was already in the bibliography.

**Dismissed regex artifacts (not citations):** "2012 to 2017" / "2012-2017" (NPDC-era date range), "Asset Management Team (2016)" (NNPC team-formation event), "November 2012" (OML 30 completion date), "March 2023" (Eroton removal date). Verified as date/event references, not sources.

---

## 2. RESTATED-FACT bucket — Appendix D carries real consistency issues; Ch5/Ch6 largely clean

### 2a. Appendix D (Case-by-Case Evidence Table) — flags to fix in the prose pass

Appendix D contains the detailed per-case figures, and several do not reconcile with the audited Ch4 / Appendix E basis. Citations in AppD are clean (Oriaku, Akinwale, Adekunle, Aiteo v. Shell all verified; Idigbe 2013 and Danmadami 2021 already in bib); **no A1/A2 statute language appears in AppD**, so the Section 29 / mandate reframe has no locus here.

**HIGH-priority reconciliations:**
- **H2 man-hours (LOCAL).** AppD says Seplat "**two million** man-hours" (Table D.1 line 14) and "2 million man-hours" (line 100). The locked figure is **11 million** (Seplat 2024 AR; Ch4 and matrix already at 11M). Fix both AppD loci. (Aware of a separate "2 million incident-free offshore man-hours" NNPC/Seplat-JV figure; the locked company-wide figure is 11M.)
- **Seplat-MPNU price (LOCAL, reconcile).** AppD says the 2024 ExxonMobil/MPNU acquisition was "**$1.28 billion**" (lines 14, 96); Ch4 line 52 says "$800M." A ~$480M discrepancy across the thesis. Verify against the Seplat/MPNU completion disclosure and reconcile (base vs revised vs net).
- **OML 30 production basis (reconcile).** AppD shows "25,000-45,000 bopd under NPDC; grew to 80,000 under HEOSL" (lines 15, 116, 120). The matrix shows audited "trough near 3,800 bpd" under NPDC and "~24,000-30,000 (2021-22), operator-reported peak ~67,000 (2025)." Reconcile the gross/operator-reported vs audited basis and the NPDC trough, per the Production Data Integrity Protocol.
- **Aiteo production basis (label).** AppD "tripled from 23,000 to 90,000 bpd by 2017" (lines 11, 28) vs Ch4 audited metered 38.2 kb/d / modeled ~41 kb/d. Reconcilable as gross (90k x 45% WI ≈ 40.5k net), but AppD must label 90,000 as gross to avoid an apparent contradiction.
- **Renaissance price presentation (reconcile).** AppD summary line 19 "$1.3 billion"; line 158 "$1.3 billion ($2.4 billion total)"; Ch1 "$2.4 billion." Reconcilable (base vs total) but must be presented consistently and labeled.

**Same-as-Ch1 corrections that also land in AppD:**
- **H3 spill volume.** AppD "200,000+ barrels" (lines 11, 32) is a contested estimate (Nigerian Senate ~2M; never officially determined). Apply the same caveat as Ch1.
- **Trinity Spirit precision.** AppD "nearly 50-year-old" (lines 20, 178) -> 46 years; "10 crew dead or missing" (lines 20, 178) -> contested toll (Lloyd's List: 3 dead + 3 rescued + 4 missing). Same softening as Ch1.

**Tier-B spot-checks (AppD claims not yet independently verified):**
Nembe "buyer beware" decree 2015 (line 48); Eroton "EFCC investigation ongoing" vs the matrix's "NNPC forensic audit" (line 68); "October 2023 abandoned well explosion in OML 66 under NPDC" (line 136); NPDC "332,000 bpd by late 2018" (line 128); Afren "14-year director ban" and "N36.63 billion" (lines 80, 84); Neconde consortium members (line 144, Aries Energy/VP Global vs the Yinka Folawiyo seen elsewhere); "41 communities" at Santa Barbara (line 11, also Ch5 line 89); marginal-field denominators (24 vs 30 awarded fields, lines 190). None is verdict-bearing; verify opportunistically.

### 2b. Chapter 5 — restated facts are qualitative and consistent
Ch5 does NOT restate the contested production figures or the man-hours (grep for 90,000/85,200/38.2/42.3/tripled/two million/11 million returns nothing). Its case references are qualitative: the suspended, undecommissioned Santa Barbara well; Seplat's founding team and Maurel et Prom; the OML 30 operator change; 41 communities; the absent blowout contingency plan (the G5 anchor). The regulator-pillar is **A2-consistent**: "NUPRC's 2024 reforms moved in the right direction, and the design here extends them," and a "corporate screen can pass an operator that has not demonstrated the asset-specific crisis readiness." No restated-fact conflict. (The "41 communities" figure is the one Tier-B item, shared with AppD.)

### 2c. Chapter 6 — one statutory-citation check
Ch6 restates verdicts (all consistent and calibrated, see Section 3) and cites specific PIA provisions for the "instruments funded out of failing operations" argument: **Host Communities Development Trust at 3% of operating expenditure (PIA Section 240)**, the **Decommissioning and Abandonment Fund (Sections 232 and 233)**, and the **environmental remediation contribution (Section 103)**. These are load-bearing and must be exact. **Spot-check against the gazetted PIA** (in the repo) in the prose pass. No A1 "Section 29" language appears in Ch6.

---

## 3. OVERCLAIM bucket — Ch6 is well-calibrated; Ch5 framework claims are bounded

**Chapter 6 — CLEAN.** The conclusion uses the locked Section 2.6 verdict vocabulary verbatim ("most consistent with the evidence," "rejected as sufficient," "an enabling condition insufficient on its own"), runs the two-inference discipline explicitly ("an operator able to raise and deploy capital for production cannot have its later integrity failure explained by capital scarcity alone. A separate body of evidence points to capability... The two readings rest on different evidence"), and bounds generalizability ("a design of this kind can corroborate... not prove universally"; the population and marginal-field evidence is "consistent corroborating context that does not, by itself, carry the verdicts"; "no implementation data yet show that it improves performance"). The regulatory framing is already A2-consistent (the 2024 reforms "created a technical-capacity route, but it is assessed at the corporate level"). The label "capability-related factors" and "two outcome dimensions" are used throughout. No overclaim detected across 6.1, 6.2, 6.4, 6.5. Confidence ~92% (close read of 6.3 recommendations and 6.6 conclusion in the prose pass would settle the remainder).

**Chapter 5 — bounded.** The framework is presented as "a re-specification of an existing rule, not a new regime," with the central claim explicitly hedged ("The empirical regularities and the design logic warrant the framework, short of proof from a tested intervention"). The misfire analysis (Section 5, "substitution of paper for practice") is itself a calibration. No "guarantees / will prevent / universal" claims. Bucket: largely structure with sound calibration.

---

## 4. STRUCTURE bucket — no check needed
The bulk of Ch5 (the loop dynamics, the role allocation across seller/buyer/regulator, the four-pillar mapping in Tables 5.x, the tiered apparatus) and Ch6 (the prose of 6.3 recommendations, 6.5 future research) is framework logic and design with no external factual claim. No verification required beyond internal consistency with the corrected Ch4 verdicts (confirmed in Sections 2-3 above).

---

## 5. Remaining bounded items (for the prose pass)
1. **PIA statutory sections** in Ch6 6.2 (Sections 240, 232/233, 103) — verify against the gazetted PIA. HIGH priority (statutory exactness).
2. **Seplat-MPNU $1.28B vs $800M** (AppD vs Ch4) — verify and reconcile.
3. **NSTA in-text date** — reconcile "(NSTA, 2023)" to 2024 final guidance or clarify as the consultation.
4. **AppD production-basis labels** — Aiteo 90k, OML 30 25-45k/80k, Seplat 85.2k: label gross vs audited per the Production Data Integrity Protocol.
5. **Tier-B AppD spot-checks** (Section 2a) — verify opportunistically; none verdict-bearing.

## Bib change-log (this sweep)
- ADDED `nsta2024` (North Sea Transition Authority, Guidance on the conduct of licence assignments, 8 October 2024; Capability Pack; Energy Act 2023 basis).
- Confirmed already present: coase1960, pigou1920, leveson2011, oriaku2016, akinwale2022, nightingale/rhodes 2015, trist/bamforth 1951, idigbe 2013, danmadami 2021, aiteoVshell2021.
