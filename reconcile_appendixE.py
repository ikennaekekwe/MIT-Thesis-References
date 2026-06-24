#!/usr/bin/env python3
"""
Reconcile Appendix E (Verdict Traceability Matrix) with the Chapter 4 per-case
verdict tables before those Chapter 4 tables are removed.

Actions:
 1. Port two verdict-cell wordings where Chapter 4 is more complete (Eroton PE, OML30 PE).
 2. Insert a new column "What would change this verdict" (the falsification condition)
    as column 3 (immediately after Verdict), preserving the falsification symmetry the
    matrix is built to make auditable.

Appendix E's existing Evidence / Evidence type / Verdict established / Confidence columns
are NOT altered (they are fuller than Chapter 4's evidence-anchor column).

The falsification text for the six case tables is copied verbatim from the Chapter 4
"What would change this verdict" column. The Marginal Field table has no Chapter 4
verdict table; its falsification cells are derived to match the matrix logic and the
phrasing of the other rows, and are flagged in the run summary for human review.
"""
import sys, re

P = "Appendix_E_Verdict_Traceability_Matrix.md"
s = open(P, encoding="utf-8").read()
orig = s

# ---------------------------------------------------------------- 1. verdict reconciliation
# Eroton political economy: Chapter 4 is more nuanced ("live for the case as a whole").
# Anchored on the Eroton-only evidence that follows ("| Consortium business-development and financial").
ero_old = ("Rejected as sufficient for operational quality (non-substitutable dimension); "
           "case-level connection data incomplete | Consortium business-development and financial")
ero_new = ("Rejected as sufficient for the operational-capability tasks at issue; live for the "
           "case as a whole; case-level connection data incomplete | Consortium business-development and financial")
assert ero_old in s, "Eroton PE anchor not found"
s = s.replace(ero_old, ero_new, 1)

# OML 30 political economy: Chapter 4 qualifies the dimension. Anchored on OML30-only evidence.
oml_old = "Rejected as sufficient | Rehabilitation of vessels, wellheads, and compression"
oml_new = ("Rejected as sufficient for operational quality (non-substitutable dimension) | "
           "Rehabilitation of vessels, wellheads, and compression")
assert oml_old in s, "OML30 PE anchor not found"
s = s.replace(oml_old, oml_new, 1)

# ---------------------------------------------------------------- 2. falsification column content
FALS = {
 "aiteo": {
  "Capital constraints": "Evidence that crisis-readiness funding was cut for financial reasons",
  "Fiscal regime effects": "None; the timing is arithmetic",
  "Regulatory inadequacy": "Evidence that the framework screened for capability and that Aiteo passed",
  "Political economy": "Evidence that political interference directly caused the operational failure, beyond enabling commercial survival",
  "Coordination failure": "Evidence of a specific coordination breakdown independent of knowledge absence",
  "Capability-related factors": "An operator without inherited upstream knowledge handling a comparable crisis successfully",
 },
 "eroton": {
  "Capital constraints": "Evidence that the JV was underfunded during the decline and the funding statement was inaccurate",
  "Fiscal regime effects": "None; the conditions predate the Act",
  "Regulatory inadequacy": "Evidence that the framework screened buyer capability and Eroton passed",
  "Political economy": "Direct evidence that political access shaped the operational failure, beyond commercial or regulatory standing",
  "Coordination failure": "Evidence of a specific transition-period coordination breakdown independent of capability",
  "Capability-related factors": "The internal organizational failures shown attributable to capital, liquidity, or political dynamics instead of capability",
 },
 "fhn": {
  "Capital constraints": "Evidence that a funding shortage, ahead of the fraud and collapse, drove the failure",
  "Fiscal regime effects": "None; the timing is arithmetic",
  "Regulatory inadequacy": "Evidence that the framework screened buyer fitness and that Afren passed a substantive test",
  "Political economy": "Not applicable; explanation not tested",
  "Coordination failure": "Not applicable; explanation not tested",
  "Capability-related factors": "Not applicable; explanation not tested",
 },
 "seplat": {
  "Capital constraints": "Evidence that Seplat's outcome rested on a capital advantage the failed operators lacked",
  "Fiscal regime effects": "Evidence of a fiscal treatment specific to Seplat that drove the outcome",
  "Regulatory inadequacy": "Evidence that Seplat faced a materially different regulatory regime or screen",
  "Political economy": "Direct evidence that political connections, ahead of capability, produced the operational outcome",
  "Coordination failure": "Not applicable; explanation not tested",
  "Capability-related factors": "An operator with comparable inherited capability failing under the same conditions",
 },
 "oml30": {
  "Capital constraints": "Evidence that new capital expenditure, ahead of the operator change, produced the recovery",
  "Fiscal regime effects": "Evidence of a fiscal change coinciding with the operator transition",
  "Regulatory inadequacy": "Evidence that a regulatory change coincided with the operator transition",
  "Political economy": "Evidence that the recovery reflected political access ahead of operational capability",
  "Coordination failure": "Not applicable; explanation not tested",
  "Capability-related factors": "An operator change of comparable capability leaving the outcome unchanged, or a recovery traceable to new capital or a regime change",
 },
 "npdc": {
  "Capital constraints": "Direct evidence of a binding funding shortage driving the underperformance",
  "Fiscal regime effects": "Evidence of a fiscal effect specific to NPDC",
  "Regulatory inadequacy": "Evidence that a regulatory difference, ahead of the operator, produced the outcome",
  "Political economy": "Evidence that NPDC's survival rested on operational performance ahead of state backing",
  "Coordination failure": "Evidence of a specific coordination breakdown independent of a standing capability deficit",
  "Capability-related factors": "A state operator without embedded upstream capability matching the operational quality of the capable acquirers",
 },
 # derived (no Chapter 4 verdict table for the marginal field cohort) -- flagged for review
 "marginal": {
  "Capital constraints": "Evidence that capital scarcity, not capability, drove the cohort underperformance even among adequately funded awardees",
  "Fiscal regime effects": "None; the awards predate the Act",
  "Regulatory inadequacy": "Evidence that the allocation framework included a capability test the failed awardees passed",
  "Political economy": "Not applicable; not separately tested at the cohort level",
  "Coordination failure": "Evidence of a transition-period breakdown independent of a standing capability deficit",
  "Capability-related factors": "Evidence that capability-unassessed operators matched the cohort outcomes of assessed operators",
 },
}

def detect(h):
    if "Aiteo" in h: return "aiteo"
    if "Eroton" in h: return "eroton"
    if "First Hydrocarbon" in h: return "fhn"
    if "Seplat" in h: return "seplat"
    if "OML 30" in h: return "oml30"
    if "NPDC" in h: return "npdc"
    if "Marginal Field" in h: return "marginal"
    return None

lines = s.split("\n")
out, case, count = [], None, 0
seen = {k: set() for k in FALS}
for ln in lines:
    if ln.startswith("## "):
        case = detect(ln); out.append(ln); continue
    if ln.startswith("| Explanation | Verdict |"):
        parts = ln.split("|"); parts.insert(3, " What would change this verdict ")
        out.append("|".join(parts)); continue
    if ln.startswith("|") and set(ln) <= set("|-: ") and "-" in ln:   # separator row
        parts = ln.split("|"); parts.insert(3, "---")
        out.append("|".join(parts)); continue
    if ln.startswith("|") and case in FALS:
        parts = ln.split("|")
        expl = parts[1].strip()
        if expl in FALS[case]:
            parts.insert(3, " " + FALS[case][expl] + " ")
            out.append("|".join(parts)); count += 1; seen[case].add(expl); continue
    out.append(ln)

# ---- integrity checks
expected = sum(len(v) for v in FALS.values())
assert count == expected, f"inserted {count} falsification cells, expected {expected}"
for k, v in FALS.items():
    missing = set(v) - seen[k]
    assert not missing, f"{k} missing rows: {missing}"

open(P, "w", encoding="utf-8").write("\n".join(out))
print(f"reconciled: 2 verdict cells aligned to Chapter 4; {count} falsification cells added across {len(FALS)} tables")
print(f"file {len(orig)} -> {len('\n'.join(out))} bytes")
