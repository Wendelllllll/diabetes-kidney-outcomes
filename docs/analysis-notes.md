# Analysis notes

The final Google document titled *Research Report* was reviewed on September 22, 2026. Its full title is *Sodium-Glucose Cotransporter-2 Inhibitors versus Glucagon-Like Peptide 1 Receptor Agonists Effects on Kidney in Patients with Type 2 Diabetes from the All of Us Research Program*.

The report establishes the final study scope. The local notebooks establish what code is currently available. Neither has been treated as proof that the repository reproduces the final results.

## Report and code comparison

| Item | Final report | Available notebooks |
| --- | --- | --- |
| Endpoint follow-up | Two years / 24 months | Target restored to 104 weeks; nearest measurement selected without a strict window |
| Cohort size | 1,197 overall; 1,141 in the Event20 survival section | Historical outputs showed 1,471 in exploratory regression and 1,198 in the mixed model |
| Survival analysis | Cox models, Kaplan–Meier curves, cumulative hazards | `survival.ipynb` is missing from the local files |
| Longitudinal model | Random intercept plus treatment-by-time interactions | Earlier random-intercept model with a common time slope |
| Longitudinal follow-up | Median approximately six months, range 0–2.4 years | Includes pre-treatment records; not restricted to a two-year window |

The report's Code Availability section identifies `survival.ipynb` and `Hao's mix-effect mode.ipynb` in its All of Us workspace. The workspace requires a separate sign-in. The final source files have not been retrieved; no substitute survival code has been written.

## Corrections to repository preparation

The initial repository preparation changed `52*2` to `52*3` based on the older proposal's three-year plan. That was an incorrect interpretation of the final study design. Both notebooks now use `follow_up_weeks = 52 * 2`, and the misleading three-year variable name and comments have been replaced.

Other preparation edits remain:

- Removed saved outputs, execution counts, original metadata, directory listings, and ad hoc data exports.
- Added early pandas/NumPy imports and an explicit Workbench environment check.
- Fixed use of `clean_dataset` before initialization.
- Fixed the mismatch between `heart failure` and `heart_failure` in the comorbidity comparison.
- Replaced execution-day age calculation with a fixed reference date of 2024-11-20. This is a repository convention, not confirmation of the final study's age definition. Age at initiation still needs review.

The original local files are unchanged. No participant-data analysis has been rerun after these edits, so historical estimates should not be attributed to the edited notebooks.

## Questions to resolve with the final source

1. **Cohort accounting.** Explain the transition from 1,197 to 1,141 and reconcile both with the older notebook counts. The report does not provide enough detail to assign a reason to each exclusion.
2. **Event times and censoring.** The available code compares baseline and endpoint values. It does not locate the first threshold crossing, and medication-gap filtering is inactive. Recover the Cox code to verify event-time construction, censoring, covariates, and proportional-hazards diagnostics.
3. **Longitudinal specification.** Recover the interaction model and its time-standardization definition. Pre-treatment observations belong to eventual treatment users, not a separate untreated cohort. A formal contrast is needed to test the difference between treatment-specific slopes; separate significant coefficients do not establish that contrast.
4. **Sparse models.** The report's Event40 table includes zero/infinite estimates and unbounded confidence intervals for some covariates. Inspect convergence warnings and sparse-event behavior before relying on those estimates.
5. **Report consistency.** The abstract repeats the SGLT2i interaction confidence interval for GLP-1RA; Table 4 instead gives -7.907 to -6.814 for GLP-1RA. A discussion sentence compares GLP-1RA with itself. The software section lists two R versions. These should be checked against original output, not silently resolved by guessing.
6. **Measurement and covariate definitions.** Baseline timing, diagnosis timing, medication exposure, demographic coding, and age definition need reconciliation. The available code uses the measurement nearest initiation, whereas the report describes the first available baseline measurement.

## Sharing and reproducibility

Only selected aggregate treatment results are summarized in the README. The report contains small subgroup counts and an individual-trajectory figure; the document and those figures have not been copied into the repository.

Keep participant-level processing inside the authorized All of Us environment. Clear outputs and inspect metadata before adding recovered notebooks. Run `python scripts/check_notebooks.py` before committing, but treat it as a source check rather than a full disclosure audit.

The synthetic demo is a separate illustration with invented data and parameters. It is not evidence that the study can be reproduced from the files currently in this repository.
