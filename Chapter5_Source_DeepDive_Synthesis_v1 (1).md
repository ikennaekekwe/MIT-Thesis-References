# CHAPTER 5 — SOURCE DEEP-DIVE SYNTHESIS (v1)
## Primary-source reading pass behind the architecture and Table 5.2 / Appendix H
## Compiled: June 14, 2026

Scope: the repo and comparative sources read to primary-source depth for Chapter 5. This document records what each source establishes, how it is used, the analytical decisions it forces (especially the Table 5.2 backbone), and the corrections it requires to the v2 architecture and the worksheet.

---

## 1. DECISION: the Table 5.2 backbone (your six categories, advised)

**Advice: reject the six inductive categories as the backbone; adopt Risk-Based Process Safety (RBPS, CCPS 2007/2016) as the authoritative backbone for the operational-integrity dimension, bridged to Ferreira by a published mapping.**

Why the six categories should not be the backbone, despite being a sound first sketch:
- **Provenance.** The six were inductive (mine, refined from your suggestions). A reviewer would ask where they come from. RBPS is the recognized CCPS standard, and is the framework used by the very paper that grounds Chapter 5's safety mechanism.
- **They are largely a reworded subset of RBPS**, so nothing is lost by switching, and coverage improves.
- **The bridge.** The process-safety paper already maps Ferreira's 22 IKT elements onto RBPS elements (its Tables 4-5). Anchoring Axis 1 on RBPS lets the framework's two axes connect through *published* evidence rather than a cross-walk I invent.

**RBPS, 20 elements across four pillars (CCPS 2007), authoritative source for Table 5.2:**
1. **Commit to process safety:** process safety culture; compliance with standards; process safety competency; workforce involvement; stakeholder outreach.
2. **Understand hazard and risk:** process knowledge management; hazard identification and risk analysis.
3. **Manage risk:** operating procedures; safe work practices; **asset integrity and reliability**; contractor management; training and performance assurance; management of change; operational readiness; conduct of operations; **emergency management**.
4. **Learn from experience:** incident investigation; measurement and metrics; auditing; management review and continuous improvement.

**Resulting structure (replaces the worksheet's Axis 1):**
- **Table 5.2 (visible, Chapter 5)** = the **four RBPS pillars** (four groups, Kosslyn-clean), each mapped to a Chapter 4 finding, a legal hook, and the role split (seller discloses / buyer absorbs / regulator verifies). The Aiteo failure sits in pillar 3 (asset integrity and reliability; emergency management; operational readiness), the keystone.
- **Appendix H** = the 20 RBPS elements x Ferreira's 22 IKT elements mapping (the published IKT-to-RBPS bridge), element-level, with the Chapter 4 finding and legal hook per row. This is the auditable detail behind both Table 5.2 (content) and the 5.4 transfer-design obligations (process).
- **5.2 mechanism** uses the bridge directly: a transfer-process failure (Ferreira element) degrades a specific RBPS capability element, which surfaces as a safety event. This is the framework's causal spine, and it is published, not inferred.

**Two findings from the paper that shape the framework beyond Table 5.2:**
- **Criticality (Table 3).** Experts judged the IKT failures that are *hard for the buyer to fix alone* as most safety-critical: contractual specification of transfer content, decision-making characteristics, transfer period, seller-personnel availability, proactivity, provision of resources, responsibility for the transfer, and **access to legacy databases**. Buyer-manageable items (training-need identification, transfer objectives/scope, routines, mechanisms) were less critical. → This tells the framework **which transfer-process obligations to make mandatory** (the seller/contractual/data ones) versus **proportionate** (buyer-manageable), and it is empirical, not assumed. Direct input to 5.4 and 5.6.
- **The transaction agreement is the highest-leverage instrument.** Contractual characteristics alone touched three RBPS pillars (e.g., unspecified transfer content → missing emergency-response procedures → Emergency Management; unspecified staff numbers → Compliance with Standards). → The framework should specify **what the assignment/transfer agreement must contain**, which is also where NUPRC consent and Alberta both attach requirements.

**Open call for you (production dimension).** RBPS is an operational-integrity (safety) taxonomy. The thesis's dependent construct spans **production performance (DV1)** and **operational integrity (DV2)**. RBPS covers DV2 authoritatively, and DV2 is where the catastrophic, externality-bearing failures and the mandatory-intervention justification live. Options: (A) keep Table 5.2 RBPS-pure (four pillars, DV2) and address production/subsurface operating capability in 5.2 prose as a parallel domain grounded in Chapter 4 + KBV; or (B) add a fifth domain ("production and subsurface operating capability") to Table 5.2. My recommendation is **(A)**: it keeps Table 5.2 fully sourced and Kosslyn-clean, ties the table to the externality argument, and avoids one domain breaking the RBPS provenance. Confirm A or B.

---

## 2. Source précis (rhetorical précis where load-bearing; key findings + use)

### A. Theory and mechanism

**Ferreira et al. (2024), "Challenges in IKT for the Life Extension of Oil and Gas Facilities," IEEE TEM.** Ferreira et al. argue, from a qualitative case study of an ageing offshore platform transferred between two companies, that 22 key IKT elements (across eight themes: structural governance, absorptive capacity, motivation, prior experience, training, management capacity, interorganizational routines, coordination tools) and 27/39 challenges must be managed for a successful handover, because most failures originate in planning. They evidence this with coded interviews and a pretransition/transition/post-transition guideline. Their purpose is to give managers and future frameworks a basis for designing IKT in asset acquisition. Audience: engineering-management scholars and operating-company managers. **Use:** Axis 2 (transfer-process), Appendix H; the pre/during/post structure maps to the framework's lifecycle; the 22 elements are transfer determinants, not capability content (the worksheet's headline).

**Ferreira et al. (2026), "How failures in IKT impact process safety," J. Loss Prevention.** The authors show, via the same platform's incident data plus expert interviews mapping IKT challenges to RBPS, that unsuccessful IKT during an ageing-asset handover with **no personnel transferred** raised incident frequency and severity (one severe accident in eleven years under the seller versus one within a year under the buyer), because governance-related IKT failures (seller availability; access to legacy databases) degrade RBPS elements, especially process knowledge management. Their purpose is to support improved IKT frameworks for managers and regulators. Audience: process-safety researchers and regulators. **Use:** the safety-outcome warrant for 5.2; the RBPS backbone for Table 5.2; the IKT-to-RBPS bridge; the criticality and contract-leverage findings for 5.4/5.6.

### B. Legal backbone (Nigeria)

**NOGICD 2010.** §7-9: a Nigerian Content Plan and Certificate of Authorization are required *before* acquiring a licence, permit, or interest (Board review ≤30 days). §29-30: Employment and Training Plan. §31: succession plan, Nigerians understudy expatriate incumbents ≤4 years, then Nigerianized (**within one operator**, the analogy caveat). §43-47: technology-transfer and JV/partnering plans; "regulations for further growth of indigenous capacity." **Use:** capability-building and transfer-design hooks (C1/C6/transition); §31 cited as a clearly-labeled analogy with Ferreira/process-safety as the primary warrant.

**PIA 2021.** §117: Minister's consent for assignment/transfer of a licence or lease. §232-233: decommissioning and abandonment plan and fund. Chapter 3 (§§234-257): Host Communities Development Trusts (needs assessment, development plan). Transfer-of-employees provisions; fit-and-proper/disqualification. **Use:** the consent gate (5.4 enforcement), the externality hooks (Gap 4), employee-transfer (team retention), and fitness.

**NUPRC Assignment of Interests Regulations 2024.** Reg. 7(2) due diligence covers technical capacity, financial capacity, legal requirements, decommissioning and abandonment, host-community-trust and environmental-remediation-fund arrangements, industrial relations and labour, and **data repatriation**. Reg. 7(4): due diligence **may include site visits for competency evaluation**. Reg. 7(5): the acquirer must have sufficient technical knowledge and experience, good standing, **directors not previously convicted of any crime**, and FGN acceptability. **Use:** the load-bearing existing hook; the framework re-specifies "technical capacity" as asset-specific operating capability, makes the competency visit mandatory and asset-specific for higher-risk transfers, extends data repatriation into structured asset-history disclosure, and adds the missing seller-disclosure duty, structured transfer, and post-transfer verification.

**Minister's Consent Guidelines 2021 (DPR).** Establish the pre-PIA consent procedure for assignment of OPL/OML/MF/OGPL and a broad assignment definition (shares, merger, acquisition, divestment, intra-group). **Use:** the predecessor regime; shows the evolution to the 2024 Regulations, where capability due-diligence specificity and the competency-visit power were added.

**NUPRC Annual Report 2024.** NUPRC concluded **twenty assignment due-diligence exercises** in 2024 (active assignment screening under the 2024 Regs). D&A guided by PIA §232-233. **Corrections this forces (see §3):** the "functional capability before allocating" line is about the Domestic Crude Supply Obligation, not divestment screening; and no "seven-pillar divestment framework" is evidenced in the report itself.

### C. Nigerian capability and externality evidence

**Oriaku, Udo & Ifeduba (2016, NPDC), "Technical Assessment of In-Country Capabilities," SPE-184346-MS.** The authors show, via NPDC's table-top plus facility-inspection evaluation of 33 indigenous service companies, that **paper evaluations overstated demonstrated capability** (only 44% of tubing-inspection firms met the 60% benchmark; facility inspection exposed deficiencies in personnel, tools, and equipment that table-top scores hid), and that firms can win work on a multinational's backing **without the expertise themselves**. Their purpose is to argue for periodic technical evaluation of indigenous capability under the local-content mandate. Audience: SPE Nigeria practitioners and regulators. **Use:** a Nigerian, NPDC-authored, quantified anchor for the framework's core, paper capability ≠ demonstrated capability, and **site verification is what reveals the gap** (supporting mandatory competency visits); also the borrowed-capability risk relevant to the technical-operator lever (5.5.1, 5.3, 5.6).

**National Principles for Responsible Petroleum Industry Divestment (civil society, Steiner et al.).** Proposes 90-day public notice + community FPIC; FGN confirmation that the seller disclosed all pollution/liabilities as a consent-checklist item; buyers demonstrating to an **independent auditing body** their technical and financial capacity, a robust **integrity-management program and spill prevention/response capability**, and transparent disclosure of company history/staff/directors; full EER/ESHIA/ESDD; and a third-party **Asset Integrity Review** with deficiencies remedied before approval. **Use and positioning:** a precursor reform proposal that independently converges on disclosure + demonstrated capability + verification, which the thesis *improves on* by grounding these in a capability theory (RBPS, IKT, KBV) and the Chapter 4 critical-experiment evidence, adding absorptive capacity, the Ferreira transfer-process, and post-transfer verification, and re-specifying existing statutory hooks rather than proposing a new treaty/voluntary-signature mechanism. Engage as complement, not competitor; do not argue it more convincingly than the thesis.

**Pre-divestment hollowing evidence (SDN, "Selling Out Nigeria," Just Transition/Steiner, Renaissance NGO letter).** Documented: aged infrastructure and under-investment causing "integrity failures"; pipelines a decade overdue for replacement, past 15-year technical life; a 2009 Shell employee email warning of corporate exposure; Shell's decision not to proceed with clean-up (Wood Mackenzie and NGO sources). **No direct Shell admission of cutting HSE spending before divestment exists in the corpus.** **Use:** Gap 1's primary warrant is the Aiteo undecommissioned well plus this third-party-documented under-investment/integrity-failure pattern; the single survey response (R5) is secondary.

**Chapter 2 (project file) economics cross-check.** Chapter 2 cites Akerlof, adverse selection, and information asymmetry, and mentions externality, but contains **no Pigou or Coase citation** (and no Spence/signaling). **Use:** Gap 2 is grounded; for Gap 4, add one canonical externality reference (Pigou 1920 / Coase 1960, or a polluter-pays formulation) when drafting 5.3.

### D. Comparative regulators and voluntary standards

**NSTA (UK), Norway (NOD/Havtil/PSA), Alberta (AER)** — as recorded in the v2 architecture (consent + Capability Pack + fitness; prequalification + HSE-management-system + site visits + in-country organisation; holistic multifactor LCA + both-party assessment + security tied to D&A). Drawn selectively; none verifies asset-specific operating/crisis capability, tacit-knowledge/team retention, or post-transfer operation, which Nigerian conditions require. Per your guard: each is fit for its own context; the claim is only that none supplies the verification Nigeria's conditions need.

**IOGP / IPIECA voluntary standards.** Report 510/511 (Operating Management System Framework + OMS in Practice): an integrated lifecycle risk-management approach (OH&S, environment/social, process safety, quality, security), explicitly **excluding financial risk** and explicitly **not a mandatory commitment**. Report 415 (asset integrity, barrier-based, leading/lagging KPIs). Report 456 (process-safety KPIs; Tier 1/2 PSE, aligned to API RP 754). ISO/TC 67 is developing ISO 29010 from 510/511. **Use (5.5.3):** the right capability *content* but the wrong *delivery* for divestment, voluntary, single-operator-internal, transfer-blind, adoption-dependent. The framework mandates via existing hooks what these recommend, and adds the transfer-process and verification they omit. **Bonus:** reference IOGP 415/OMS as the buyer's required integrity-management standard, and IOGP Tier 1/2 PSE rates as ready-made **post-transfer verification metrics**.

### E. Deal
**Renaissance / SPDC** — as recorded (capability-preservation design per PwC; staff retention; ex-Shell leadership; NUPRC blocked then approved Dec 2024; completed 13 March 2025; 133k→~330k bpd). Framed per your instruction: **evidence that capability-preservation design is feasible and already emerging in practice; not yet outcome evidence.**

---

## 3. Corrections this pass forces (for architecture v3 and the worksheet)

1. **Table 5.2 backbone:** RBPS four pillars (CCPS), not the six inductive categories. The 20 RBPS elements x Ferreira's 22 elements → Appendix H. (Supersedes worksheet §1 and the six-category framing.)
2. **NUPRC "functional capability before allocating"** is the **Domestic Crude Supply Obligation** mechanism, not divestment screening. Do not cite it as an assignment-capability hook.
3. **"Seven-pillar NUPRC divestment framework"** is **not** evidenced in the 2024 Annual Report; source it to the separate NUPRC Regulatory Divestment Framework document (web/Task-2) before asserting it, or drop the "seven-pillar" label. The defensible datum is the twenty 2024 assignment due-diligences and the Reg. 7 areas.
4. **FHN/Afren** is a **pre-2024 historical** illustration of a fitness gap the 2024 Regulations (Reg. 7(5)(a)(iv) director-conviction screen) have **partly closed**, not a current gap.
5. **Gap 1 warrant:** Aiteo undecommissioned well + third-party-documented under-investment/integrity-failure pattern; **no direct Shell HSE-spend admission**; survey R5 secondary.
6. **National Principles** positioned as a precursor the thesis improves on (theory + critical-experiment evidence + absorptive capacity + transfer-process + post-transfer verification + statutory re-specification), not a competitor.
7. **Gap 4:** add a Pigou/Coase externality citation when drafting 5.3 (absent in Chapter 2).
8. **5.4/5.6 proportionality** now has an empirical basis: make the seller/contractual/data transfer-process obligations mandatory (most safety-critical, buyer cannot fix alone); buyer-manageable items proportionate. Specify what the **transfer agreement** must contain (highest leverage).
9. **5.5.3** IOGP/IPIECA: right content, wrong delivery; also used as buyer integrity standard + post-transfer PSE verification metrics.

---

## 4. Remaining items (small)
- Pin Ferreira's canonical 22 element names against Table V when building Appendix H (deferred, confirmed).
- Pull the **NUPRC Regulatory Divestment Framework + Due Diligence Reference List** exact text (web/Task-2) and resolve the seven-pillar sourcing.
- Add a Pigou/Coase citation in 5.3 (confirm Chapter 2 will not be retro-edited; if it should be, that is a separate Chapter 2 task).
- Verify the faithful use of the Chapter 2 theory anchors (Cohen & Levinthal; Kogut & Zander; Nonaka; Grant; Baxter & Sommerville) when drafting 5.2; no full re-read needed (Chapter 2 resident).

---

## 5. Open decisions for Ikenna
1. **Adopt RBPS as the Table 5.2 backbone** (four pillars), with the six categories retired and the RBPS x Ferreira mapping in Appendix H. (The central decision this pass produced.)
2. **Production dimension:** option A (RBPS-pure Table 5.2 + production handled in 5.2 prose) vs option B (add a fifth production/subsurface domain). Recommendation: A.
3. **National Principles positioning** as precursor-improved-upon (confirm).
4. Proceed to issue **architecture v3** folding in your eleven v2 comments plus the nine corrections above, then build **Appendix H** (RBPS x Ferreira) and draft **5.2**.
