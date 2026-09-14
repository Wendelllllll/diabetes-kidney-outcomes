# Analysis preparation notes

The repository contains two cleaned versions of the original MED264 notebooks.
See the repository README for a project overview and synthetic demo instructions.
No license has been selected yet. This is exploratory observational analysis,
not a clinical claim.

## Preparation changes

- Cleared all saved outputs, execution counts, attachments, and original metadata.
- Removed workspace directory listings and ad hoc bucket transfers/CSV exports.
- Added early pandas/NumPy imports and an explicit Researcher Workbench check.
- Fixed use of `clean_dataset` before its initialization in the regression notebook.
- Changed the intended three-year endpoint from 104 to 156 weeks.
- Fixed the heart-failure label comparison: `heart failure` was compared with
  `heart_failure`, producing an all-false indicator.
- Fixed the age reference date at 2024-11-20 instead of the day of execution.
  This preserves a historical reference date; age at treatment initiation remains
  a future methodological correction.

These changes can alter results. Original statistics and figures have not been
carried forward as results of the corrected code. The original folder is intact.
The proposal and workflow PDF are also omitted: their scope, authorship labels,
and sample counts require reconciliation before reuse.

## Remaining limitations

- Endpoint measurements are selected nearest 156 weeks without a maximum allowed
  distance. Baseline is nearest initiation and can be after initiation. Neither
  selection guarantees an appropriate baseline or follow-up window.
- Medication-gap censoring is commented out. Event flags compare baseline and
  endpoint values, rather than finding the first threshold crossing. Cox survival
  analysis described in the original proposal is not implemented here.
- The mixed-effects notebook includes pre-treatment records, calls those records
  `Untreated`, and sets negative times to zero. This is not a separate untreated
  cohort. The model uses a shared time slope, with no treatment-by-time interaction.
- Comorbidity extraction uses name matching and does not restrict diagnoses to
  baseline. Concept-set validation and temporal restrictions need review.
- Models use gender while labeling some derived variables as sex; category
  exclusions and simplified race coding need explicit justification.
- Historical regressions showed numerical warnings and sparse predictors. Model
  fitting and diagnostics must be revisited after preprocessing corrections.
- Remaining exploratory branches remove predictors based on historical behavior;
  those choices must be reconsidered after the heart-failure fix.
- Confounding, treatment selection, and irregular follow-up limit interpretation.

## Execution

For the two notebooks, use an authorized All of Us Researcher Workbench and
Registered Tier v7 data. The generated SQL reads `WORKSPACE_CDR`. The dependency
file is a candidate environment, not a verified lockfile. Run notebooks from top
to bottom inside the authorized environment. Do not move participant data into
this repository to make them runnable locally.

For a local, entirely artificial modeling illustration:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/synthetic_demo.py
```

The demo illustrates a random-intercept model and treatment-by-time interaction.
It does not reproduce the cohort pipeline or results, and is not a replacement
for validation on the original data.

## Distribution

Run `python scripts/check_notebooks.py` before committing. It checks notebook
syntax, saved outputs, execution state, and attachments; it is not a comprehensive
privacy audit. Executing the original notebooks can recreate participant-level
outputs, small subgroup summaries, and individual trajectories. Clear outputs
before sharing and review any exported figures separately.

All of Us policies:
- https://www.researchallofus.org/faq/data-and-statistics-dissemination-policy/
- https://www.researchallofus.org/faq/publication-and-presentation-policy/
