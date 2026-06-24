# Full-Thesis Comment Tracker — v1
**Source:** Full_Thesis_Comments_v1.txt (647 lines) | **Built:** 2026-06-20 | **Thesis state:** 207 pp proof, clean build

**How to use:** veto or override any row by its ID (e.g., "veto C4-06, AP-G1"). I execute only rows marked **ADOPT / ADOPT-MOD / DECIDED** that you have not vetoed. Verdict legend below.

**Verdict legend**
- **ADOPT** — clear win, no conflict; will apply as written.
- **ADOPT-MOD** — adopt the intent, modified for our locked constraints/calibration (modification stated).
- **DECIDED** — your Tier-4 / 10-point decision recorded here.
- **HOLD** — blocked on a verification (PIA text, COUHES record) before I touch it.
- **VERIFY-DONE** — likely already handled this session; confirm against live text before re-cutting.
- **DECLINE** — stale, factually wrong, or would weaken the thesis; not actioned.

**Status:** Queued / Blocked-(reason) / Closed.

---

## 1. General / global (comments lines 1–93)

| ID | Comment | Cmt¶ | Target | Verdict | Status / note |
|----|---------|------|--------|---------|---------------|
| G-01 | Vary repetitive verdict phrasing ("most consistent with the evidence", "the evidence shows") | 3–22, 53 | all ch. | ADOPT-MOD | Queued. Vary *connective* prose only; the five verdict labels are locked vocabulary and stay verbatim. |
| G-02 | Split/active-voice key sentences (e.g., the abstract "transfer at completion…does not") | 23–31 | abstract, var. | ADOPT | Queued. Burstiness split, not substance; first example sits in the conceptual abstract lead we keep. |
| G-03 | Add a Tier-A/Tier-B transparency note where only Tier-B sources exist | 33 | §3.3 | ADOPT | Queued. One sentence; see C3-01. |
| G-04 | "Cut 15–20 pages of repetition" | 35 | global | ADOPT-MOD | Queued. Executed via the targeted compressions below, not a literal page quota. Net-page tracked (your point 8). |
| G-05 | Check all table headers + pagination | 37 | front matter | VERIFY-DONE | LoT self-contained titles done; reconfirm pagination on final build. |
| G-06 | Allow rare "spoken" phrases ("In plain terms", "Put differently") | 39–43 | Ch5–6 only | ADOPT-MOD | Queued. Permitted in 5–6 only; declined in 1–3 (figurative-language constraint). |
| G-07 | Modest first person in methods/limitations | 45–49 | §3, §6 | DECIDED | **Reject** except personal motivation (§1.8). Closed. |
| G-08 | Flatten fronted-participle "AI tells" in Ch4 + Ch6 | 51–53 | Ch4, Ch6 | ADOPT | Queued; specific instances at C4-13/14, C6-09. |
| G-09 | domestic → indigenous **global find-and-replace** | 55 | global | DECIDED | **Decline the global F&R** (your point 10). Context-sensitive: "indigenous operator" where Nigerian legal/industry terminology matters; "domestic operator/company" for a non-IOC acquirer in plain analytical prose; never touch "domestic regime/law/foundation". |
| G-10 | Standardize "uncontrolled blowout" | 57 | global | ADOPT | Queued. Ch1 already uses it; sweep for "uncontrolled well blowout" / variants. |
| G-11 | Reduce "significant" (where = "important") and "serves as" | 58–59 | global | ADOPT | Queued; word-level humanizer pass. |
| G-12 | Keep exact title "…(Assignment of Interest) Regulations 2024" | 60 | global | ADOPT | Queued. **Check:** Appendix G currently reads "Assignment of Interests" (plural) — reconcile. |
| G-13 | Shorten long sentences (<25 w) | 62 | global | VERIFY-DONE | Burstiness pass cut the 50–80w tier; reconfirm, do not re-trim. |
| G-14 | Forward-looking sentence at each chapter end | 64–77 | Ch2–4 | ADOPT-MOD | Queued. One sentence each, only where it advances the argument; watch bloat (point 8). |
| G-15 | SDM-manual governing standard | 79–92 | n/a | DECIDED | **Standard = proposition + argument maintained through question/method/evidence/logic** (your point 7), not "story". Guides all edits; no standalone edit. |

---

## 2. Acronym list (comments lines 95–104) — **Tier 1, must-fix (verified present)**

| ID | Comment | Cmt¶ | Target | Verdict | Status / note |
|----|---------|------|--------|---------|---------------|
| AC-01 | AER "Alberta" → "Alberta Energy Regulator" | 100 | list_of_acronyms.tex L6 | ADOPT | Queued. Placeholder, not an expansion. |
| AC-02 | NSTA "United Kingdom" → "North Sea Transition Authority" | 101 | …L20 | ADOPT | Queued. Placeholder. |
| AC-03 | NNPC: use "Corporation" for historic usage, or distinguish NNPC/NNPCL | 102 | …L16 | ADOPT-MOD | Queued. Confirm body usage, then set one convention. |
| AC-04 | DOC: "domestic operating company" vs "domestic oil company" — define once | 103 | …L8 | ADOPT | Queued. Keep "domestic operating company (DOC)"; ties to G-09. |
| AC-05 | SPDC → "Shell Petroleum Development Company of Nigeria" | 104 | …L25 | ADOPT | Queued. |

---

## 3. Abstract (comments lines 108–134)

| ID | Comment | Cmt¶ | Target | Verdict | Status / note |
|----|---------|------|--------|---------|---------------|
| AB-01 | "Overly abstract?" / lead with empirical puzzle | 110, 116–123 | abstract.tex | DECIDED | **Reject** case-led rewrite; keep conceptual lead (matches title). Closed. |
| AB-02 | Proof opens with an older abstract — replace | 112 | abstract.tex | DECLINE | Stale: proof abstract = canonical v6. |
| AB-03 | "best accounted for" → calibrated verdict language | 114, 133 | abstract.tex | ADOPT | **Tier 1.** "best accounted for" → "most consistently explained by capability-related factors"; also "uncontrolled well blowout" → "uncontrolled blowout". |
| AB-04 | "This thesis argues" → "The argument is that" | 125–131 | abstract.tex | ADOPT-MOD | Queued; only if it reads naturally in the kept lead. |

---

## 4. Chapter 1 (comments lines 136–194)

| ID | Comment | Cmt¶ | Target | Verdict | Status / note |
|----|---------|------|--------|---------|---------------|
| C1-01 | Add "The Story of This Thesis" section | 138 | §1 | DECIDED | **Reject** (bloat/artificial). Instead sharpen 1.x opening + one bridge sentence (C1-08). Closed. |
| C1-02 | Add Thesis Roadmap figure | 140 | §1 | DECIDED | **Reject** for body. Closed. |
| C1-03 | Move systematic explanation development to Ch2 | 142 | §1.3 | ADOPT | Queued; see C1-09. |
| C1-04 | "(OPEC, 2022. NUPRC, 2024)" → semicolon; fix "(SDN. Environmental Defense Fund)" | 146–150 | Ch1 L41 | ADOPT | **Tier 1, verified present.** |
| C1-05 | Trim Aiteo mechanics / Eroton / Shebah FPSO / marginal-field counts / population proxies | 152–160 | §1.2 | ADOPT-MOD | Queued. Defer detail to Ch4; keep stakes (see C1-08). |
| C1-06 | "This thesis employs" → "The study uses" | 162–168 | Ch1 | ADOPT-MOD | Queued; minor, where natural. |
| C1-07 | Rexer years "2000 to 2018" error | 170–176 | §1.2 | DECLINE | Stale: text already reads "2006 to 2016" (verified L63). |
| C1-08 | Strip adjudicative trajectory numbers from §1.2 | 174–178 | §1.2 | DECIDED | **Strip** Aiteo 23k→90k/41k, Eroton 6k→50k, Seplat 85,200, OML 30 80k/67k. **Keep** 26 OMLs, ~$21B, 41 communities, 33 days, national decline/recovery. Add bridge sentence: *"The pattern is not simply that some operators failed and others succeeded. It is that the failures appeared where operating capability had to be exercised, not merely where assets had to be owned."* |
| C1-09 | Reduce 5-explanation walk-through across 1.3/2.3/3.1 | 180–188 | §1.3, §3.1 | ADOPT | Queued. Full version stays in §2.3; 1.3 → overview + gap sentence; 3.1 → point to Ch2. |
| C1-10 | "hardware vs embedded knowledge" restated in 1.1–1.2/2.2/3.1/5.2 | 190–192 | §1.1–1.2, §3.1 | ADOPT | Queued. Full in §2.2, brief link in §5.2; trim elsewhere. |
| C1-11 | Shorten problem statement 1.2 | 194 | §1.2 | ADOPT | Queued; overlaps C1-05/08. |

---

## 5. Chapter 2 (comments lines 196–329)

| ID | Comment | Cmt¶ | Target | Verdict | Status / note |
|----|---------|------|--------|---------|---------------|
| C2-01 | Define "operating capability" operationally, early | 198–204 | §2.2 / §2.3.5 | ADOPT | **Tier 2, top content win.** Concrete: people, routines, integrity systems, decision rights, data, contractor relationships. Pairs with the missing IKT paragraph. |
| C2-02 | Introduce "selective failure" signature earlier | 206–211 | §2.3.5 | ADOPT-MOD | Render as a **table**, not a box (your point 6). |
| C2-03 | Recast coordination failure: symptom, not tested cause | 213–220, 273 | §2.4 | ADOPT-MOD | Queued. Keep the test (it demonstrates symptom-status); sharpen prose + add "because" pivots so it never reads as a competing cause. |
| C2-04 | Engage enterprise-architecture (Nightingale & Rhodes) + CCPS-RBPS + decommissioning lit | 222–235 | §2 | ADOPT | **Tier 2.** Add a paragraph on enterprise architecture ("plant without the organizational architecture") + decommissioning tie for the externality. |
| C2-05 | Figure 2.1 self-contained caption | 237–242 | Fig 2.1 | ADOPT | Queued; matches our illustration standard. |
| C2-06 | Long sentence (§2.3.1 example) | 244–251 | §2.3.1 | VERIFY-DONE | Check against burstiness pass; split if still >50w. |
| C2-07 | "Key Concepts" box (selective failure, absorptive capacity, five explanations) | 253–264 | §2 | ADOPT-MOD | Render as a **table** (point 6); watch net page add (point 8). |
| C2-08 | "Discrimination Logic" table | 265 | §2 | VERIFY-DONE | Discrimination matrix already exists (Appendix B / Table B.1); add a compact in-chapter pointer rather than duplicate. |
| C2-09 | Address organizational-quality confound directly | 267 | §2 | ADOPT-MOD | Queued. Acknowledge capability may proxy general quality, then answer it (better argument, not concession). |
| C2-10 | Add "How This Advances the Literature" section | 271 | §2 | ADOPT-MOD | Queued. A short paragraph, not a new section (point 8). |
| C2-11 | Vary repeated "The observable evidence patterns include…" | 283–297 | §2.3 | ADOPT | Queued. Keep analytical symmetry, vary prose; reviewer's per-explanation fixes are usable. |
| C2-12 | Clarify "insufficient on its own" (operator- vs system-level) | 299 | §2.6 | ADOPT | Queued. Add the "enabling but non-differentiating" clarifier. |
| C2-13 | Vary recurring four-criteria frame in §2.6 | 315–329 | §2.6 | ADOPT | **Tier 2 burstiness**; reviewer's humanized version is a good model. |

---

## 6. Chapter 3 (comments lines 332–365)

| ID | Comment | Cmt¶ | Target | Verdict | Status / note |
|----|---------|------|--------|---------|---------------|
| C3-01 | Tier-B transparency note | 334–339 | §3.3 | ADOPT | Queued; one statement (= G-03). |
| C3-02 | "core verdicts rest on Tier 1" stated repeatedly | 341 | §3.3 | ADOPT | Queued; state once. |
| C3-03 | §3.5 may still say "Shell, Total, Eni" vs §3.2 SPDC emphasis | 343 | §3.5 | HOLD | Blocked-verify: read §3.5 against the SPDC-seller framing before editing. |
| C3-04 | Triads in 3.1–3.4 | 359–365 | §3.1–3.4 | ADOPT-MOD | Queued; vary where formulaic, check against burstiness pass. |

---

## 7. Chapter 4 (comments lines 368–461)

| ID | Comment | Cmt¶ | Target | Verdict | Status / note |
|----|---------|------|--------|---------|---------------|
| C4-01 | Capital-constraints rejection "overstated" — acknowledge marginal-cohort confound | 370–377 | §4.7.1 | ADOPT-MOD | Queued. Clarify "necessary, not sufficient; cannot explain differentiation among the funded" WITHOUT softening the rejection. Verify §4.7.1 already does this. |
| C4-02 | Substitutability table (political economy vs capability) | 379–392 | §4.7.2 | ADOPT | **Tier 2.** Substitutable (theft/community/survival) vs non-substitutable (well control/crisis/equipment). High clarity value. |
| C4-03 | Marginal-field evidence limit | 394–399 | §4.x | ADOPT-MOD | Queued. State "corroboration at cohort level, not decisive"; verify already present. |
| C4-04 | §4.2 repeats Ch1 narrative | 401 | §4.2 | ADOPT | Queued; keep tables, cut re-summary. |
| C4-05 | §4.7.1 repeats Table 4.5 | 403 | §4.7.1 | VERIFY-DONE | Compressed 27% this session; confirm. |
| C4-06 | Ch4→Ch5 bridge paragraph | 405–414 | end §4.8 | ADOPT-MOD | Queued. **Short** bridge only; do not pre-state the whole framework (point 8). |
| C4-07 | Quantitative summary in §4.2 ("correlated perfectly") | 416–421 | §4.2 | DECIDED | **Decline "correlated perfectly."** Use your sentence: *"Across the formal cases, sustained production and integrity outcomes align more closely with demonstrated upstream operating capability than with capital, fiscal regime, or regulatory exposure alone."* |
| C4-08 | Survey overweighted — cut to paragraph | 423–428 | §4.8 | DECIDED | De-weight hard; one mention in §4.8: *"The survey is retained for transparency, but not used as inferential evidence. Its small, seller-side sample limits it to contextual corroboration."* No "supports the finding" language. |
| C4-09 | Modeled-vs-audited "data note box" | 430–447 | §4.2 | ADOPT-MOD | Render as a **table** (point 6). Aligns with production-basis discipline (never splice bases). |
| C4-10 | Substitutability section in Ch6/4.7 | 451 | §4.7 / §6 | ADOPT | Queued; = C4-02 + a Ch6 pointer. |
| C4-11 | Connect externality to decommissioning lit | 453 | §4.7.3 | ADOPT | Queued; = C2-04. |
| C4-12 | Calibration language repeated | 455 | §4.x | ADOPT | Queued; keep 4.1/4.8, thin middle. |
| C4-13 | §4.3.6 "Read across the two outcome dimensions…" → "The diagnostic split across…" | 457 | §4.3.6 | ADOPT | **Tier 2** fronted-participle fix. |
| C4-14 | §4.7.1 "Aggregated across the cases…" → "When aggregated across the cases…" | 459 | §4.7.1 | ADOPT | **Tier 2** fronted-participle fix. |
| C4-15 | "because" pivots in 4.3/4.4 (coordination failed → deeper why) | 461 | §4.3–4.4 | ADOPT | Queued; = C2-03 application. |

---

## 8. Chapter 5 (comments lines 464–516)

| ID | Comment | Cmt¶ | Target | Verdict | Status / note |
|----|---------|------|--------|---------|---------------|
| C5-01 | "Wrong-variable diagnosis" too sharp / dismissive of NUPRC | 466–474 | §5.3.5 | ADOPT-MOD | Queued. Soften the dismissiveness; **but** "moves in the right direction" already changed to "narrows the gap without closing it" — do not revert. Verify v5 softening. |
| C5-02 | Repetition 5.2/5.3/5.4 (+ from Ch2) | 475–479 | §5.2–5.4 | VERIFY-DONE | §5.3 de-duplicated this session; confirm before more cutting. |
| C5-03 | Value-Dimensions table (5.1): warrant for V3–V8 not established | 481 | §5.1 / Table 5.1 | HOLD | Blocked-verify: read Table 5.1 + warrants; establish or trim V3–V8. |
| C5-04 | "Warranted not proven" repeated — keep 3 spots | 483, 501 | §5 | ADOPT | Queued; aligns with refrain-thinning. |
| C5-05 | Figures 5.1 / 5.2 visual + grammar | 485–499 | Fig 5.1, 5.2 | ADOPT | **Tier 1.** Fix "triggers installs" → "triggers install the requirement and restore the corrective signal"; Fig 5.1 center label → "Transferred asset and operating requirements"; regen for clarity (5.2 overlap already pending). |
| C5-06 | "this is the necessary remedy" overclaim → "warranted as design response, not proven effective" | 503 | §5 | ADOPT | **Tier 2** calibration; our locked discipline. |
| C5-07 | Triads in 5.4–5.6 | 509–516 | §5.4–5.6 | ADOPT-MOD | Queued; vary where formulaic. |

---

## 9. Chapter 6 (comments lines 518–558)

| ID | Comment | Cmt¶ | Target | Verdict | Status / note |
|----|---------|------|--------|---------|---------------|
| C6-01 | Frame contribution as a reframing more boldly | 520–525, 541 | §6.6 | VERIFY-DONE | §6.6 already recast affirmatively; keep strong, not sensational (point 9). |
| C6-02 | Lead §6.1 with a one-sentence answer per RQ | 527, 537 | §6.1 | ADOPT-MOD | Queued; verify §6.1 structure (compressed this session). |
| C6-03 | Substitutability section in Ch6 | 529 | §6 | ADOPT | Queued; = C4-02/10 pointer. |
| C6-04 | Propose future tests (Renaissance natural experiment) | 531 | §6.x | ADOPT | **Tier 2**; aligns with Renaissance future-test role (never present evidence). |
| C6-05 | "Boundaries of Generalizability" (6.5) defensive | 533 | §6.5 | ADOPT-MOD | Queued. Tighten over-hedging; better argument, not disclaimer. Verify §6.5 (sharpened this session). |
| C6-06 | Condense recommendations to a table | 539 | §6.x | ADOPT-MOD | Queued; table (point 6), watch bloat (point 8). |
| C6-07 | Sharper closing sentence | 543 | §6 end | ADOPT-MOD | Queued; sharpen, not sensational (point 9). |
| C6-08 | Conclusion opening "the asset becomes a hazard" | 545–554 | §6.1 open | DECIDED | **Decline the sensational opener** (point 9). Craft strong-but-calibrated alternative grounded in capability *risk* / open control loop, not "becomes a hazard". |
| C6-09 | §6.6 "Read this way…" → "Under this sociotechnical framework…"; §6.1 "Adjudicated against…" → "When evaluated against…" | 550, 556 | §6.1, §6.6 | ADOPT | **Tier 2** fronted-participle fixes. |
| C6-10 | Clarify contribution = institutional-design argument, not tested prescription | 558 | §6.6 | ADOPT | **Tier 2** calibration. |

---

## 10. Appendices (comments lines 561–642)

| ID | Comment | Cmt¶ | Target | Verdict | Status / note |
|----|---------|------|--------|---------|---------------|
| AP-A1 | Appendix A: cut 20% (condense A.5 coding) | 563–565 | App A | ADOPT-MOD | Queued; only genuine redundancy (point 8); verify. |
| AP-B1 | Appendix B: add worked example (Aiteo) | 571–573 | App B | ADOPT-MOD | Queued; compact worked example; net-page tracked (point 8). |
| AP-B2 | Appendix B: reduce cell prose + coded notation/legend | 575–576 | App B | ADOPT-MOD | Queued; formatting, preserve readability. |
| AP-C1 | Consolidate three interview guides → one + role probes | 581–589 | App C | HOLD | **Blocked (point 4):** confirm whether COUHES protocol E-7658 record benefits from preserving role-specific instruments before condensing. |
| AP-D1 | Appendix D: cut 20% (redundant with Ch4) | 594–596 | App D | ADOPT-MOD | Queued; verify redundancy (point 8). |
| AP-D2 | Appendix D heading "Seplat, OMLs 4,38,41 + ExxonMobil" — split | 598–607 | App D | ADOPT | **Tier 1.** Separate formal case from MPNU seller-independence check. |
| AP-E1 | Appendix E: reduce cell prose + coded notation/legend | 611–614 | App E | ADOPT-MOD | Queued; formatting. |
| AP-F1 | Appendix F: cut/eliminate | 618–624 | App F | DECIDED | **Do not delete.** Compact to ≤2 pp: one profile table + one response-summary table; not used for inference (= C4-08). |
| AP-G1 | Appendix G: cut 20% (repetitive with Table 5.3) | 628–638 | App G | ADOPT-MOD | Queued; verify overlap (point 8). |
| AP-G2 | "Reading the Bridge Backward" → integrate into Ch5 | 636 | App G/§5 | ADOPT-MOD | Queued; verify; watch bloat. |
| AP-G3 | PIA Section 104 (environmental remediation) → 103 | 640 | App G L74 (+L89) | ADOPT | **Tier 1.** Confirm 103 against gazetted PIA, then fix both 104 instances. |
| AP-G4 | PIA Section 117 (upstream condition-setting) → 95 / Reg. 7 | 642 | App G L92 (+ Ch5 L?) | HOLD | **Blocked-verify:** memory lists 117 as a valid hook; reviewer says midstream/downstream. Read gazetted PIA Section 117 scope before changing. |

---

## 11. References (comments line 645–647)

| ID | Comment | Cmt¶ | Target | Verdict | Status / note |
|----|---------|------|--------|---------|---------------|
| R-01 | 19 `[VERIFY]` placeholders block submission | 647 | references.bib | ADOPT | **Tier 1.** Web-verify real titles (NEITI/SDN/SOMO/manual). Never fabricate; unverifiable ones flagged to you. |
| R-02 | Ferreira 2024a/2024b duplicated vs body's 2026 | 647 | references.bib | DECLINE | Stale: bib correctly has ferreira2024 (IKT) + ferreira2026 (RBPS), two distinct papers. |

---

## Summary counts
- **Tier-1 must-fix (verified):** AC-01..05, C1-04, AB-03, AP-D2, AP-G3, C5-05, R-01 (+ AP-G4 pending PIA).
- **ADOPT / ADOPT-MOD (queued):** ~48 rows.
- **DECIDED (your calls, recorded):** G-07, G-09, G-15, AB-01, C1-01, C1-02, C1-08, C4-07, C4-08, C6-08, AP-F1.
- **HOLD (blocked on verification):** C3-03, C5-03, AP-C1, AP-G4 (PIA / COUHES / live-text).
- **VERIFY-DONE (confirm before re-cutting):** G-05, G-13, C2-06, C2-08, C4-05, C5-02, C6-01.
- **DECLINE (stale/wrong/weakening):** AB-02, C1-07, R-02 (+ "correlated perfectly", the case-led abstract, the "becomes a hazard" opener — recorded under their rows).

**Proposed execution order:** (1) Tier-1 errors; (2) resolve the four HOLDs (PIA read, COUHES check, §3.5 and Table 5.1 reads); (3) Tier-2 content additions; (4) one verified compression pass for the repetition rows so we don't double-trim.

---

# VERIFICATION LOG — 2026-06-20 (pre-execution, grounded in live files)
Backup taken: `_BACKUP_pre-review_2026-06-20_2240/` (sha256 anchors + BEFORE_review_proof_207pp.pdf).

## HOLDs — all resolved
- **AP-G3 — CONFIRMED, fix.** PIA verified against the official text/TOC: **Section 104 = "Gas flaring penalties"; Section 103 = "Financial contribution for remediation of environmental damage."** Appendix G "Section 104 environmental remediation" (line 74) and the line-89 instance → **Section 103**. Memory was wrong.
- **AP-G4 — CONFIRMED, fix (Appendix G only).** **Section 117 = "Assignment or transfer of licence or permit," Part III (midstream/downstream administration); Section 95 = "Assignments, mergers, transfers and acquisitions" (upstream), with Ministerial consent on the Commission's recommendation, s.95(5).** Appendix G line 92 "condition-setting under Section 117" → **Section 95 + NUPRC Reg. 7**. The Chapter 5 line-270 instance is CORRECT (it states midstream/downstream proceed under 117 and the Authority vs 95 and the Commission) and STAYS. Memory's listing of 117 as a valid upstream hook was wrong.
- **C3-03 — RESOLVED, no change.** §3.5 already reads "divested through the Shell-operated SPDC joint venture, in which Total and Eni were the other international partners" — consistent with §3.2.
- **AP-C1 — RESOLVED, preserve.** The three guides (Group A IOC-seller, Group B DOC-buyer, Group C regulator) are substantively different role-specific instruments with role-tagged probes, forming part of the COUHES E-7658 record. Decline the consolidation; at most factor out the shared preamble.

## VERIFY-DONE — re-checked against live text
- **C2-06 — NOT done → ADOPT.** Reviewer's §2.3.1 sentence still present verbatim in v29; apply the split.
- **C4-05 — NOT confirmed → re-tighten in execution.** §4.7.1 ≈1055 w in v9 (claimed 779). Re-examine.
- **C5-02 — done** (wrong-variable framing appears once). **G-13 — reflected** (burstiness: Ch4 36→23, Ch5 30→20 over-50w). **C6-01 — done** (§6.6 recast). **C2-08 — done** (Table B.1 exists). **G-05 — clean**.
- **C2-09 — already handled** (org-quality confound at §2.3.5 L113; not a new addition).

## Corrected verdicts (your three flags)
- **C2-02 — selective failure: anchor earlier/crisper in PROSE, not a table.** Already developed in §2.3.5 (named L117); make it a clearer/earlier reader anchor.
- **C5-03 — V3–V8: make the warrant explicit in prose; do NOT trim.** Table 5.1 tags V3–V8 "Warranted"; the table-intro prose (L9–11) does not develop why each warranted dimension counts.
- **C2-03 — coordination failure: see approach in chat.** Logic already correct (symptom, persistence test); fix is presentational consistency in the verdict matrices (the Aiteo matrix L116 lacks the "observable feature" tag the consolidated matrix L284 carries) plus "because" pivots; use the locked label, NOT the reviewer's "capability deficit."

## Fronted-participle inventory (canonical files; ~8 genuine, after filtering 11 false positives)
- Comment-cited already fixed in canonical: §4.3.6 "Read across", §4.7.1 "Aggregated across", §6.1 "Adjudicated against".
- Remaining to vary (frequency is the issue, not any single one): Ch1 "Evaluated individually" ×1; Ch4 "Read together" ×2; Ch5 "Taken together" ×1, "Left to itself" ×1; Ch6 "Read this way" ×1, "Seen this way" ×1, "Taken with the evidence" ×1. Keep ≤1 synthesis "Taken together"; vary the rest, context-reviewed. (False positives left alone: gerund/noun-phrase subjects such as "Operating an asset… requires", "Flaring, …, ran", "Lagging/Leading indicators, …".)

---
# TIER-1 EXECUTED & REBUILT — 2026-06-20 (207pp clean, verified in rendered PDF)
Backups: `_BACKUP_pre-review_2026-06-20_2240/tier1/*.bak_tier1`. All single-match assertions passed.
- Acronyms: AER→Alberta Energy Regulator; NNPC→Corporation; NSTA→North Sea Transition Authority; SPDC→…of Nigeria. (DOC kept.)
- Abstract (both .md + abstract.tex): "best accounted for"→"most consistently explained"; "uncontrolled well blowout"→"uncontrolled blowout".
- Ch1 citations: "(OPEC, 2022. NUPRC, 2024)"→semicolon; "(SDN. Environmental Defense Fund)"→"(Stakeholder Democracy Network, 2022)" [EDF flagged for R-01 if flaring stat is theirs].
- Appendix D: heading + table label "Seplat … + ExxonMobil"→"Seplat (OMLs 4, 38, 41)" (ExxonMobil/MPNU 2024 stays prose-distinguished).
- Appendix G legal hooks: Section 104→103 (×2, environmental remediation); "condition-setting under Section 117"→"condition-setting at consent under PIA Section 95 and NUPRC Reg. 7". Ch5 L270 (117=midstream/downstream) correct, untouched.
- Figure 5.1: center label → "Transferred asset / and its operating / requirements" (fits 156px box). Figure 5.2: grammar "install … and restore …"; removed stray "feedback/restored" overlap labels; widened intervention-3 box. Both re-rendered (cairosvg) + visually verified + copied to build/deliverables.

---
# HOLD-CLEARED CONTENT BATCH EXECUTED — 2026-06-20 (207pp clean)
Backups: `_BACKUP_pre-review_2026-06-20_2240/holds/*.bak_holds`. Single-match verified.
- **C2-03 coordination failure recast (diagnostic indicator):** §2.4 now states the persistence test is diagnostic and that a "rejected" verdict reports a structural finding (an observable feature common to the unsuccessful cases, which the deeper conditions explain). Aiteo verdict matrix (Ch4 L116) tagged "an observable feature of the unsuccessful cases," consistent with the consolidated matrix (L284). Logic unchanged; presentation now unambiguous that coordination failure is a diagnostic symptom, not a sixth competing explanation. Locked label preserved (no "capability deficit"). §4.4 Eroton because-pivot already present (colon-explained), no change.
- **C5-03 V3-V8 warrant made explicit:** added one paragraph after the hinge paragraph (~149 words, ~0.3pp) giving each warranted dimension its distinct warrant — V3/V4 catastrophic-failure externalities; V5 local-content workforce capacity; V6 royalty/tax base; V7 production resilience (theft/price confounds); V8 abandonment liability — tied to the "distance from the sale" ordering. Dimensions NOT trimmed.
- **AP-C1:** no edit (role-specific guides preserved per verification).

---
# TIER-2 BATCH EXECUTED & REBUILT — 2026-06-20 (207pp clean)
Backups: `_BACKUP_pre-review_2026-06-20_2240/tier2/*.bak_*`. All single-match verified.
- **C2-01 operating-capability operational definition:** §2.2 now names and defines operating capability (six embedded components, forward-ref to §5.2); §5.2 six-families paragraph linked back ("That capability, defined in Section 2.2…"). One definition, cross-referenced.
- **C4-07 calibrated cross-case sentence:** Ikenna's sentence inserted at start of §4.7.2 ("sustained production and integrity outcomes align more closely with demonstrated upstream operating capability than with capital, fiscal regime, or regulatory exposure alone"). No "correlated perfectly" existed.
- **C2-02 selective-failure signature named at first appearance:** §2.3.5 L99 now reads "a selective failure signature: routine success…"; L107/L117 reinforce; distinguishing logic (uniform-degradation vs self-correction) already present.
- **Fronted participles — 9 varied, 1 kept (Ch5 'Taken together', six-families synthesis).** Original scan missed 2 paragraph-initial openers (Ch4 "Classified…"→"Before any explanation is applied…"; Ch6 L75 "Taken together…"→"These limits together…"); corrected scan + canonical verification caught both. Final canonical count = exactly 1 fronted participle.
- **C6-08 — VERIFIED NO EDIT.** Ch6 opening already strong-not-sensational (argues capability + open control loop; no "becomes a hazard"/"every asset"). Later "hazard" uses conditional + technical (Leveson).
- **C5-06/C6-10 calibration sweep — VERIFIED SATISFIED.** All "guarantee" usages are calibrated negations; "warranted by/not proven by" refrain 5x Ch5, 4x Ch6; Ch6 L71 explicit "does not prove a universal law… most consistent with the observed pattern, not a demonstrated universal regularity." 19 calibration anchors in Ch6.

---
# C1-08 EXECUTED — 2026-06-20 (207pp clean). Backup: tier2/Chapter1_Full_v30.md.bak_c108
- Number-stripping VERIFIED ALREADY DONE: Ch1 already uses qualitative trajectory language ("grew production substantially," "sustained production growth," "production recovered"); no adjudicative bpd figures present. Stakes figures retained.
- Bridge sentence added at §1.2 synthesis (L45), verbatim: "The pattern is not simply that some operators failed and others succeeded. It is that the failures appeared where operating capability had to be exercised, not merely where assets had to be owned." Placed as the sharpened pattern observation leading into the central question; neutral open-question framing preserved. [PLACEMENT NOTE for Ikenna: positioned at §1.2 capstone; can relocate to §1.6 if a later preview point is preferred.]

---
# COMPRESSION PASS — STARTED 2026-06-20 (207pp clean). Backup: tier2/Chapter4_Full_v9.md.bak_compress1
- §4.7.1 (C4-05): surgical duplicate removal — cut "a contribution confined to the small, underfunded operators" (repeats preceding clause); tightened the Aiteo capital-deployment sentence. 1026→1006 words. Note: §4.7.1 is the consolidated-verdicts synthesis; aggressive compression to the once-claimed 779w would cost verdict nuance, so duplicate-removal only.
- PENDING compression rows: C1-09, C1-10 (Ch1), C4-04, C4-12 (Ch4 cross-section repetition), C5-04 (Ch5) — require genuine cross-section duplicate identification, next pass.
- PENDING: R-01 bibliography (19 [VERIFY] placeholders, web-verify); AP-F1/C4-08 survey de-weight (Appendix F ≤2pp + §4.8 "retained for transparency, not inferential evidence"); deliverable DOCX/MD regeneration (stale vs canonical).

---
# R-01 BIBLIOGRAPHY — PARTIAL (2026-06-20). Backup: references.bib.bak_R01
DONE (web-verified / fixed):
- fielddeneufville2021: title corrected to "Thesis Definition and Preparation: Some General Guidelines"; URL fixed to ardent.mit.edu/.../thesis_manual_2021-FINAL-2.pdf; [VERIFY] cleared.
- Auwalu year inconsistency: 2 canonical Ch1 instances "Auwalu, 2021" -> "Auwalu, 2020" (now matches bib + body majority; same marginal-field source).
BLOCKED ON IKENNA (genuinely unfindable via web; cited in body; MUST supply author/title/outlet):
- mohamed2024 "Comparative fiscal analysis of the Nigerian PIA" (cited Ch2 §2.3.2) — SOURCE NEEDED.
- iwuoha2021 "IOC divestment and indigenous operators in the Niger Delta" (cited Ch1 §1.6) — SOURCE NEEDED; web search returned only unrelated IOC-divestment articles.
NEEDS IKENNA'S SOURCE COPIES (exact titles/headlines; citations usable as-is meanwhile, [VERIFY] is polish):
- NEITI audit reports 2020/2021/2022/2024 exact report titles; nuprc2022 Marginal Field Status Report title.
- News headlines: vanguard2015 (Afren collapse), businessday2025 (Renaissance staff retention), africaoilgas2024.
- Corporate: seplat2024 Annual Report title, sanleon2019, heritage2020, somo2024, sdn2020 exact doc titles.
- Legal: courtofappeal2019 (R v Shahenshah & Ullah) neutral citation; brookings2022 (Ovadia) author confirm.

---
# AP-F1/C4-08 SURVEY DE-WEIGHT — 2026-06-20 (207pp clean). Backup: tier2/Chapter4_Full_v9.md.bak_apf1
- VERIFIED already de-weighted: §4.7.1 L271 frames survey as design-implication support "departing from the documentary ranking"; §4.8 L334 "small, seller-only, perception-tier sample… qualifies the documentary reading while leaving it standing."
- ADDED §4.8 explicit non-inferential sentence: "The survey is reported for transparency and treated as contextual corroboration, with the case-level verdicts resting on the documentary record."
- Appendix F ≤2pp reduction FLAGGED (not done): conflicts with the appendix's stated "reproduced here in full so that the summaries can be read against the underlying evidence" transparency rationale. Needs Ikenna's decision (cut data vs preserve transparency).

---
# DELIVERABLE PACKAGE REGENERATED — 2026-06-20 (reflects all session edits)
- _reference.docx created (Times New Roman 12pt); 14 content components (abstract + Ch1-6 + Appendices A-G) regenerated from canonical via pandoc; cover + references retained.
- Continuous MD reassembled (16 components); figures refreshed (5.1/5.2 fixes); proof PDF refreshed (207pp); README updated (5.2 overlap RESOLVED); thesis_deliverables.zip rebuilt (~4.95 MB).

---
# R-01 BIBLIOGRAPHY BATCH 2 — 2026-06-20 (user-verified sources; 207pp clean). Backup: refbatch_*/
14 entries updated + 7 added + 5 body edits, all asserted:
- First Hydrocarbon Nigeria 2021 (does not exist) -> Acha et al. 2019, SPE-198801-MS (OML 26 HSE paper); in-text + bib.
- Auwalu 2020 -> Sweet Crude Reports 2020 (news report quoting DPR; 5 in-text + bib swap).
- Ovadia 2022 -> Nwuke 2021 (Brookings PIA article; 1 in-text "Brookings,2022"->"Nwuke,2021" in Ch2 + bib). [Nwuke first name "Kasirim" to confirm.]
- Afren body fix: "shell companies they controlled" -> "a Caribbean or Bermudan shell company they controlled" (SFO wording).
- Africa Oil & Gas Report: 1 entry -> 5 dated (2012/2013/2014/2024/2025) with exact slugs.
- San Leon 2019 (annual report) + added 2017/2022/2023; Energy Voice 2019 (pipeline) + 2020/2022.
- Updated URLs/titles: SOMO 2024, SDN 2020, BusinessDay 2025, Vanguard 2015, Heritage 2020, Seplat 2024, Court of Appeal 2019 (Red Lion Chambers).
- Mohamed 2024 + Iwuoha 2021: URLs wired in (JSTOR/ScienceDirect); exact titles to confirm.
STILL [VERIFY] (user did not supply): NEITI 2020/2021/2022/2024 report titles; nuprc2022; Energy Voice 2020/2022 exact headlines.

---
# COMPRESSION ROWS — 2026-06-20 (evidence-driven; most already satisfied by prior revisions)
- C1-09a (Ch1 §1.2 figure redlines): ALREADY DONE in v30 — Aiteo "grew production substantially in its first two years", Seplat "sustained production growth across its portfolio", HEOSL "Gross production recovered under the new operator". Specific figures already gone.
- C1-09b §3.1: ALREADY DONE — §3.1 defers to Ch2 ("apparatus constructed in the preceding chapter", "defined in Section 2.6", "Section 2.2"); covers only method/apparatus, not explanation substance.
- C1-09b §1.3: OPEN — still one full paragraph per explanation (lines 51-59); §2.3 carries the full backbone (subsections 2.3.1-2.3.5). PRESENTED TO IKENNA for level decision (golden rule: paragraphs carry distinct analytical hooks — funded-failure puzzle, design-vs-execution sub-question).
- C1-10 (hardware/knowledge motif): ALREADY DONE — distribution Ch1=1, Ch2=11 (backbone), Ch3=0 (pointer only), Ch5=2 (brief). Matches reviewer target exactly.
- C4-04 (§4.2 repeats Ch1): APPLIED — only genuine overlap was the national-decline backdrop; trimmed para 21 to a Chapter 1 pointer + the 2M-target point. Operator figures/integrity events/Tables 4.1-4.2 retained (DV measurement, not re-summary).
- C4-12 grammar (§4.3.6, §4.7.1 dangling modifiers): ALREADY DONE in v9.
- C4-12 middle calibration: APPLIED one trim — removed §4.3.6 redundant forward-pointer ("Whether the pattern holds is what the replications test next") since §4.4 opening supplies it. Verdict-vocabulary statements at 90/146/251/261 retained (binding Ch2 §2.6 terms, distinct case verdicts — not refrain).
- C5-04 (warranted-not-proven): ALREADY DONE — only 1 instance in Ch5 (line 262, risk section); no "necessary remedy" over-claiming (line 109 conditionally framed).
