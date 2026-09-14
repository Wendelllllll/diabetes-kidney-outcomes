# Kidney Outcomes in Type 2 Diabetes

Exploring kidney-function changes among patients exposed to **SGLT2 inhibitors** or **GLP-1 receptor agonists**, using electronic health records from the **All of Us Research Program**.

Developed independently as a MED264 course project at UC San Diego, this analysis connects cohort construction, medication and laboratory data processing, and statistical modeling of repeated kidney-function measurements.

**Project status:** The repository contains cleaned analysis code and a runnable synthetic demonstration. The restricted-data notebooks have received preprocessing corrections but have not been rerun on the original data. No updated clinical findings are reported here.

## Research question

How do changes in estimated glomerular filtration rate (eGFR), a measure of kidney function, differ between adults with type 2 diabetes exposed to SGLT2 inhibitors and those exposed to GLP-1 receptor agonists?

The analyses examine changes from baseline and indicators of at least a 20% or 40% decline in eGFR. A longitudinal model also examines repeated measurements within patients.

## Analysis workflow

1. **Extract records:** Query person, drug exposure, measurement, and condition tables from the All of Us Registered Tier Dataset v7 using SQL.
2. **Build the cohort:** Classify medications into the two drug classes and select patients observed with only one of those classes in the extracted records.
3. **Align measurements:** Calculate time relative to each patient's first observed drug exposure and identify baseline and follow-up eGFR measurements.
4. **Prepare covariates:** Merge demographic characteristics and comorbidity indicators with the kidney-function data.
5. **Explore outcomes:** Fit linear regressions for eGFR change and logistic regressions for decline indicators; examine baseline-function subgroups and follow-up timing.
6. **Model repeated measurements:** Fit a patient-level random-intercept model with time, treatment status, demographics, and comorbidities as fixed effects.

The endpoint analysis targets a measurement near 156 weeks. The longitudinal notebook includes measurements before and after first observed exposure; it does not enforce the same three-year follow-up window.

## Repository contents

| File | Purpose |
| --- | --- |
| [01_cohort_and_regression.ipynb](notebooks/01_cohort_and_regression.ipynb) | Data extraction, cohort preparation, exploratory summaries, linear and logistic regressions |
| [02_longitudinal_mixed_effects.ipynb](notebooks/02_longitudinal_mixed_effects.ipynb) | Data preparation and mixed-effects modeling of repeated eGFR measurements |
| [synthetic_demo.py](scripts/synthetic_demo.py) | Local modeling example using entirely artificial data |
| [check_notebooks.py](scripts/check_notebooks.py) | Checks notebook syntax and absence of saved outputs, execution state, and attachments |
| [analysis-notes.md](docs/analysis-notes.md) | Preparation changes, execution guidance, and detailed methodological limitations |
| [requirements.txt](requirements.txt) | Candidate dependencies for the notebooks and demo |

**Tools:** Python, SQL/BigQuery, pandas, NumPy, statsmodels, Matplotlib, Seaborn, and Jupyter.

## Run the synthetic demonstration

No All of Us account or participant data is needed for this example. From the repository directory, using Python 3.11 or newer:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "numpy>=1.24,<3" "pandas>=2.0,<3" "statsmodels>=0.14,<0.15"
python scripts/synthetic_demo.py
```

On Windows, activate the environment with `.venv\Scripts\activate` in Command Prompt instead.

The script generates 160 artificial participants with seven measurements each, fits a random-intercept model, and prints a model summary. A fixed random seed makes the generated data repeatable. All data and treatment-effect parameters are invented for demonstration; they are not derived from participant records.

The demo includes a treatment-by-time interaction to illustrate different slopes. The original longitudinal notebook uses a common time slope, so the demo is a separate modeling illustration rather than a reproduction of that analysis.

## Run the research notebooks

The notebooks require an authorized **All of Us Researcher Workbench** environment with access to the referenced Registered Tier v7 data. Their generated queries use the `WORKSPACE_CDR` environment variable.

Within that authorized environment, review [requirements.txt](requirements.txt) against the installed packages and run each notebook from top to bottom. Each notebook includes its own extraction and preparation steps. The dependency ranges are not a verified lockfile, and full notebook execution has not been validated following the corrections.

Participant data and saved research outputs are not included. Keep participant-level processing inside the authorized Workbench; use the synthetic example for local exploration.

## Interpretation and limitations

This is an exploratory observational project. Treatment selection, baseline differences, and irregular follow-up can confound comparisons, so model coefficients should not be interpreted as causal treatment effects.

- **Measurement timing:** The nearest baseline and endpoint measurements have no maximum distance requirement. Baseline can occur after initiation, and endpoint timing can vary substantially.
- **Outcome definition:** Decline indicators compare two measurements rather than identifying the first threshold crossing. Medication-gap censoring is not active, and Cox survival analysis is not implemented.
- **Longitudinal design:** The notebook labels pre-exposure records as `Untreated` and sets negative relative times to zero. Those records come from eventual treatment users, not an independent untreated cohort. The model does not estimate separate treatment-specific time slopes.
- **Covariates and diagnostics:** Comorbidity definitions, diagnosis timing, demographic coding, and model stability require further review. Age currently uses a fixed historical reference date rather than age at initiation.

During repository preparation, the intended three-year endpoint was corrected from 104 to 156 weeks, a heart-failure label mismatch was fixed, and execution-order problems were addressed. These changes can affect results. Historical figures and estimates are therefore not presented as findings of the corrected code. See the [analysis notes](docs/analysis-notes.md) for details.

## Validation and data handling

The synthetic example has been run successfully, and the notebook source checks run automatically through GitHub Actions. These checks do not execute the restricted-data analysis or validate its statistical conclusions.

To run the source checks locally:

```sh
python scripts/check_notebooks.py
```

Executing the research notebooks can recreate participant-level tables, small subgroup summaries, and individual trajectories. Clear notebook outputs before committing and review any figures or aggregate results before sharing. The source checker is not a comprehensive privacy audit.

Data access and dissemination are governed by the All of Us Research Program. Consult its [Data and Statistics Dissemination Policy](https://www.researchallofus.org/faq/data-and-statistics-dissemination-policy/) and [Publication and Presentation Policy](https://www.researchallofus.org/faq/publication-and-presentation-policy/).
