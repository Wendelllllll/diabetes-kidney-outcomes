# Kidney Outcomes in Type 2 Diabetes

I worked on this project for MED264 at UC San Diego to compare kidney-function changes in adults with type 2 diabetes receiving SGLT2 inhibitors or GLP-1 receptor agonists. The study used electronic health records from the All of Us Research Program.

The analysis covered two questions: how long patients took to reach a decline in estimated glomerular filtration rate (eGFR), and how eGFR changed across repeated measurements.

## Study and methods

The final research report describes a cohort of **1,197 patients**: 803 in the GLP-1RA group and 394 in the SGLT2i group. Patients recorded as receiving both drug classes were excluded.

- **Cohort preparation:** SQL queries and Python processing linked demographic, medication, laboratory, and diagnosis records.
- **Survival analysis:** Cox proportional hazards models assessed time to a 20% decline in eGFR, with a 40% decline as an additional endpoint, within two years of treatment initiation. The report also includes Kaplan–Meier curves and cumulative hazard plots.
- **Longitudinal analysis:** A linear mixed-effects model used patient-level random intercepts and treatment-by-time interactions, with adjustment for demographic and comorbidity variables. Pre-treatment observations served as the reference treatment status.

The survival-results section reports **1,141 patients** for the 20% endpoint. The report does not fully explain the reduction from the overall cohort, so these counts are kept separate here.

## Reported results

The final report gives the following treatment comparisons, with GLP-1RA as the reference:

| Endpoint | Hazard ratio for SGLT2i | 95% confidence interval | p-value |
| --- | --- | --- | --- |
| 20% decline in eGFR | 1.44 | 0.98–2.11 | 0.0612 |
| 40% decline in eGFR | 1.92 | 0.89–4.13 | 0.0976 |

Neither comparison met the study's 0.05 significance threshold. This does not establish equivalence between treatments.

The longitudinal model reported a more negative treatment-by-time coefficient for SGLT2i. A direct statistical comparison between the two slopes is not provided in the report. Time was standardized, so these coefficients should not be described as annual rates of decline.

These are results recorded in the final report, not results regenerated from this repository. The study is observational; treatment selection, missing prescription records, and uneven follow-up limit causal interpretation.

## What is in this repository

The available notebooks are earlier local versions. They cover data preparation and exploratory regression, but do not reproduce every analysis in the final report.

| File | Contents |
| --- | --- |
| [Cohort and regression notebook](notebooks/01_cohort_and_regression.ipynb) | SQL extraction, cohort preparation, linear and logistic regressions |
| [Mixed-effects notebook](notebooks/02_longitudinal_mixed_effects.ipynb) | Earlier random-intercept model with a shared time slope |
| [Analysis notes](docs/analysis-notes.md) | Differences between the report and available code, corrections, and open checks |
| [Synthetic demo](scripts/synthetic_demo.py) | Small example using entirely artificial data |
| [Notebook checker](scripts/check_notebooks.py) | Source syntax and saved-output checks |

The final report names `survival.ipynb` in the All of Us workspace as the survival-analysis source. That file and the final mixed-effects implementation have not yet been recovered. The model in the current mixed-effects notebook has no treatment-by-time interaction.

**Tools used in the study:** SQL/BigQuery, Python, pandas, NumPy, statsmodels, and R's survival and survminer packages. The R survival code is not included here.

## Running the code

The research notebooks require an authorized All of Us Researcher Workbench with access to Registered Tier v7. Queries read the `WORKSPACE_CDR` environment variable. Review [requirements.txt](requirements.txt) against that environment before running either notebook from the beginning. Dependency ranges are not a verified lockfile.

For a local demonstration without participant data:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "numpy>=1.24,<3" "pandas>=2.0,<3" "statsmodels>=0.14,<0.15"
python scripts/synthetic_demo.py
```

The demo generates artificial repeated measurements and fits a random-intercept model with a treatment-by-time interaction. It illustrates the model structure; it does not reproduce the study's data, estimates, or full adjustment set.

## Data and validation

Participant data, individual trajectories, and saved research outputs are excluded. The full report is not reproduced here because its tables and figures need a separate disclosure review.

Notebook source checks run through GitHub Actions and can also be run with `python scripts/check_notebooks.py`. The synthetic demo has run successfully. The research notebooks have not been rerun after repository edits, and source checks do not validate the clinical analysis.

Clear outputs before sharing executed notebooks and follow the All of Us [Data and Statistics Dissemination Policy](https://www.researchallofus.org/faq/data-and-statistics-dissemination-policy/).
