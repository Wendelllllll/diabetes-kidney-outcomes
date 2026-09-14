"""Entirely artificial data; not fitted to or derived from All of Us records."""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf


def main():
    rng = np.random.default_rng(264)
    rows = []
    for participant in range(160):
        treatment = "SGLT2i" if participant % 2 else "GLP1RA"
        intercept = rng.normal(0, 5)
        # Arbitrary demonstration parameters, not estimates of drug effects.
        slope = -1.0 if treatment == "SGLT2i" else -1.5
        for year in np.linspace(0, 3, 7):
            rows.append({
                "synthetic_id": participant,
                "treatment": treatment,
                "year": year,
                "gfr": 80 + intercept + slope * year + rng.normal(0, 2),
            })
    data = pd.DataFrame(rows)
    result = smf.mixedlm(
        "gfr ~ year * C(treatment)", data, groups="synthetic_id"
    ).fit()
    if not result.converged:
        raise RuntimeError("Synthetic demonstration model did not converge")
    print("SYNTHETIC DEMONSTRATION ONLY - no real participant data or clinical findings")
    print(result.summary())


if __name__ == "__main__":
    main()
