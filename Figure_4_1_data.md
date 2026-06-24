# Figure 4.1 data series (RECOVERED, provenance-tracked)

Production trajectories of the formal-case OMLs, thousand barrels per day (kb/d).
Recovered from the figure built in the 2026-06-14 sessions (uploads `Figure_4_1_production_trajectories__1_.png` / `__2_.png`) and cross-verified against `NEITI_OML26_extraction_log.md` and `Section_4_5_Figure_Traceability_Table__1_.md`. The OML 26 modeled row matches the extraction log's Wood Mackenzie column digit for digit, which validates the read.

Two measurement bases, never spliced into a single series:
- **Modeled** = Wood Mackenzie 2026, license-level field liquids, sales basis after estimated theft (drawn as lines with markers).
- **Audited** = NEITI fiscalized / NUPRC annual, the regulator-signed basis that governs in disrupted years (drawn as stars).

The Aiteo and Eroton modeled lines end at 2023; Wood Mackenzie's 2024-2025 segment shows a recovery that runs above the audited record and is omitted as a modeling artifact.

## Modeled (Wood Mackenzie 2026), kb/d

| Year | Aiteo (OML 29) | Eroton (OML 18) | Seplat (OMLs 4/38/41) | Heritage/HEOSL (OML 30) | First Hydrocarbon (OML 26) |
|---|---|---|---|---|---|
| 2016 | 29.5 | 28.5 | 16.5 | 3.8 | 2.1 |
| 2017 | 36.0 | 27.0 | 35.0 | 13.0 | 3.1 |
| 2018 | 40.3 | 30.0 | 52.5 | 22.5 | 6.4 |
| 2019 | 36.0 | 32.0 | 46.5 | 29.0 | 7.9 |
| 2020 | 41.0 | 21.0 | 47.0 | 29.5 | 8.6 |
| 2021 | 34.0 | 4.4 | 40.3 | 35.0 | 9.2 |
| 2022 | 10.0 | 4.4 | 34.3 | 33.3 | 9.9 |
| 2023 | 11.7 | 5.5 | 33.0 | 33.0 | 10.3 |
| 2024 | (ends) | (ends) | 33.3 | 33.3 | 10.8 |
| 2025 | (ends) | (ends) | 38.7 | 35.0 | 14.8 |

Anchor cross-checks (audited governs where it diverges): Seplat peak 52.6 = OML 4 (14.0) + OML 38 (33.4) + OML 41 (5.2), 2018; Seplat 2021 modeled 40.4 vs audited 42.3; OML 30 modeled 3.8 (2016) rising to 35 (2021), holding 33-35; OML 26 modeled 9.2/9.9/10.3 for 2021-2023 against audited 8.8/3.7/6.2 (audited governs, divergence noted).

## Audited / regulatory actuals (stars), kb/d

| OML | Year | Value | Basis |
|---|---|---|---|
| Aiteo (OML 29) | 2022 | 0.7 | NEITI fiscalized (4.9 metered, 74% metering-error deduction) |
| Aiteo (OML 29) | 2024 | 7.4 | NUPRC annual |
| Eroton (OML 18) | 2024 | 13.6 | NUPRC annual |

Aiteo 2021 modeled equals the audited fiscalized figure (34.0 = 34.0). Eroton's 2022 fiscalized trough was 0.21 (3.29 million metered, 0.205 million fiscalized) under the fourth-quarter trunk-line force majeure; the dotted vertical at 2022 marks the Aiteo blowout shut-in (modeled 10.0 down to audited 0.7).

## Source files
- `NEITI_OML26_extraction_log.md` (full OML 26 NEITI series 2012-2023 + cohort)
- `Section_4_5_Figure_Traceability_Table__1_.md` (Seplat, OML 30, NPDC, OML 26, marginal-field provenance)
- `build_fig41.py` (the matplotlib build, with this data inlined)
