# Mining Geospatial Analytics

Applied geospatial data science, spatial machine learning, geochemical compositional analysis, and reproducible analytics for mineral exploration and mining.

This repository presents reproducible technical walkthroughs that connect geospatial reasoning, scientific validation, reusable Python code, automated testing, and clear technical communication.

The portfolio is developed incrementally. Each public laboratory is intended to demonstrate not only that code runs, but that the underlying analysis is scientifically meaningful, reproducible, and testable.

## Featured work

### LAB 01A - Coordinate Systems for Mineral Exploration

[Open the recruiter-facing notebook](labs/lab01_geospatial_foundations/01a_coordinate_foundations.ipynb)

**Problem:** geographic coordinates can produce numerically valid calculations that are scientifically incorrect when degrees are interpreted as metric distances.

The walkthrough demonstrates:

- WGS84 / EPSG:4326 interpretation
- geographic versus projected coordinates
- automatic UTM zone selection
- projected distance calculation
- independent geodesic validation
- GeoPandas CRS cross-checking
- reusable CRS utilities
- automated tests

**Core lesson:**

```text
degrees are not metres
```

---

### LAB 01B - Crossing UTM Zones in Spatial Analysis

[Open the recruiter-facing notebook](labs/lab01_geospatial_foundations/01b_cross_zone_crs.ipynb)

**Problem:** projected coordinates expressed in metres are still not directly comparable when they belong to different Coordinate Reference Systems.

The walkthrough compares:

1. an independent WGS84 geodesic reference
2. a valid calculation using one common projected CRS
3. an intentionally invalid calculation mixing UTM Zones 18S and 19S

Key numerical evidence:

| Method | Distance | Difference vs geodesic | Spatially valid |
| --- | ---: | ---: | --- |
| WGS84 geodesic reference | ~38.594 km | 0.0000% | Yes |
| Common CRS - EPSG:32719 | ~38.619 km | ~0.0635% | Yes |
| Mixed UTM 18S / 19S | ~540.215 km | ~1299.72% | No |

**Core lesson:**

```text
metres are not automatically comparable
```

A spatial operation requires geometries to use a compatible spatial reference system.

---

### LAB 02 - Spatial Exploratory Data Analysis

[Open the recruiter-facing notebook](labs/lab02_spatial_eda/02_spatial_eda.ipynb)

**Problem:** an apparent spatial hotspot can reflect uneven sampling intensity rather than a strong underlying spatial signal.

The walkthrough demonstrates:

- synthetic spatial sampling with regional and campaign components
- projected analysis in WGS 84 / UTM Zone 19S (`EPSG:32719`)
- nearest-neighbour sampling-density diagnostics
- regular-grid aggregation
- separation of sampling density from underlying synthetic signal
- grid-resolution sensitivity using persisted Monte Carlo results
- geographic context with documented Natural Earth provenance
- reusable spatial utilities
- automated tests

Key numerical evidence:

| Metric | Result |
| --- | ---: |
| Observations | 800 |
| Regional mean NN distance | 1807.35 m |
| Campaign mean NN distance | 502.73 m |
| Campaign / regional NN ratio | 0.278 |
| Primary descriptive grid | 10 km |
| Densest cell | `c2_r3` |
| Highest observed-signal cell | `c6_r6` |
| Highest true-signal cell | `c6_r6` |

The densest cell differs from both signal hotspots, while the highest observed-signal cell agrees with the highest true-signal cell in this synthetic realization.

The 10 km grid is used only as the primary descriptive resolution for this experiment. It is not presented as a universal optimum.

**Core lesson:**

```text
sampling density is not underlying spatial signal
```

---

### LAB 03 - Spatial Cross-Validation

[Open the recruiter-facing notebook](labs/lab03_spatial_cross_validation/03_spatial_cross_validation.ipynb)

**Problem:** conventional random cross-validation can produce optimistic performance estimates when spatially close observations are distributed between training and validation sets.

The walkthrough demonstrates:

- Random K-Fold versus Spatial Block Cross-Validation
- a fixed local KNN baseline so that validation design, rather than model selection, is the experimental variable
- 5 km spatial blocks as the primary validation scenario
- 10 km sensitivity analysis
- 20 km stress testing
- train-validation spatial-separation diagnostics
- spatial-group overlap diagnostics
- RMSE and MAE as primary performance metrics
- limitations of R² when validation folds contain very low target variance

For the primary 5 km scenario:

- Random pooled RMSE: **3.9676**
- Spatial Block CV pooled RMSE: **4.2610**
- relative RMSE optimism: **6.89%**
- Random median test-to-train separation: **1.11 km**
- Spatial median test-to-train separation: **2.39 km**
- mean 5 km spatial-group overlap: **73.6** for Random K-Fold versus **0.0** for Spatial Block CV

The result is experiment-specific and is not presented as a universal correction factor or as evidence that one spatial block size is optimal for other datasets.

**Core lesson:**

```text
validation geometry changes the prediction problem being evaluated
```

---

### LAB 04 - Geochemical Compositional Data Analysis

[Open the recruiter-facing notebook](labs/lab04_geochemical_coda/04_geochemical_coda.ipynb)

**Problem:** multivariate geochemical concentrations can be misinterpreted when relative compositional structure is ignored and conventional Euclidean analysis is applied without considering closure and log-ratio geometry.

The walkthrough demonstrates:

- deterministic synthetic geochemical data generation
- ten-element geochemical subcomposition
- explicit detection-limit and missing-value semantics
- constant-sum closure
- centered log-ratio transformation
- isometric log-ratio transformation
- Aitchison distance
- raw, closed, CLR, and ILR PCA comparison
- numerical equivalence of non-zero CLR and ILR PCA eigenvalues
- detection-limit replacement sensitivity
- explicit geochemical data contracts
- automated notebook and analytical validation

The controlled dataset contains:

- **1,200** synthetic samples
- **10** selected elements
- WGS 84 / UTM Zone 19S (`EPSG:32719`)
- **1,169** synthetically censored cells
- **111** missing elemental observations
- **1,092** complete samples used in the primary multivariate analysis

For `D = 10` compositional variables:

```text
CLR dimension = 10
CLR rank = 9
ILR dimension = 9
```

The non-zero eigenvalues from CLR and ILR PCA agree numerically, providing an internal validation of the compositional geometry implementation.

Detection-limit sensitivity between `LOD / 2` and `LOD / sqrt(2)` produced:

| Component | Score correlation |
| --- | ---: |
| PC1 | 0.983686 |
| PC2 | 0.981298 |
| PC3 | 0.954433 |

The absolute change in PC1 explained variance was approximately `0.020898`.

This indicates substantial structural agreement without implying complete invariance to the censoring treatment.

The selected ten elements are explicitly treated as a **subcomposition**. Closure to 100 is a relative normalization step and must not be interpreted as complete whole-rock mass balance.

**Core lesson:**

```text
geochemical composition requires relative, not purely absolute, geometry
```

## Why this matters for GeoAI

Spatial and geochemical errors can silently propagate into downstream predictive features such as:

```text
distance_to_fault_m
distance_to_intrusive_m
distance_to_contact_m
nearest_anomaly_distance_m
neighbourhood_density
clr_Cu
clr_Mo
clr_Au
ilr_1
ilr_2
```

A machine-learning model may train successfully even when its spatial validation is optimistic or its geochemical representation is methodologically inappropriate.

For this reason, the portfolio builds predictive modelling only after establishing:

```text
problem
 ->
spatial reasoning
 ->
data semantics
 ->
reproducible analysis
 ->
independent validation
 ->
compositional reasoning
 ->
reusable implementation
 ->
automated testing
 ->
technical interpretation
```

## Current evidence

The current public portfolio includes:

- 5 recruiter-facing analytical notebooks
- reusable CRS, spatial-analysis, spatial-validation, and compositional-analysis utilities under `src/geoai/`
- automated pytest validation
- 58 passing automated tests
- persisted synthetic Monte Carlo result artifacts for LAB 02
- persisted spatial-validation results for LAB 03
- persisted geochemical CoDA summaries and PCA artifacts for LAB 04
- documented provenance for the LAB 02 geographic context layer
- explicit geochemical data contracts for LAB 04
- reproducible Conda environment definition
- pre-commit quality controls
- Gitleaks secret scanning
- synthetic and redistribution-safe analytical examples

## Repository structure

```text
mining-geospatial-analytics/
|
|-- labs/
|   |-- lab01_geospatial_foundations/
|   |   |-- 01a_coordinate_foundations.ipynb
|   |   |-- 01b_cross_zone_crs.ipynb
|   |   `-- README.md
|   |
|   |-- lab02_spatial_eda/
|   |   |-- 02_spatial_eda.ipynb
|   |   |-- 02_spatial_eda.py
|   |   |-- README.md
|   |   |-- data/
|   |   |   `-- context/
|   |   |       |-- chile_context.geojson
|   |   |       `-- SOURCE.md
|   |   `-- results/
|   |       |-- experiment_metadata.json
|   |       |-- monte_carlo_by_realization.csv
|   |       `-- resolution_summary.csv
|   |
|   |-- lab03_spatial_cross_validation/
|   |   |-- 03_spatial_cross_validation.ipynb
|   |   |-- 03a_run_spatial_cv_experiment.py
|   |   |-- 03b_summarize_cv_results.py
|   |   |-- README.md
|   |   `-- results/
|   |       |-- aggregate_comparison.csv
|   |       |-- aggregate_metrics.csv
|   |       |-- experiment_metadata.json
|   |       |-- fold_results.csv
|   |       |-- scenario_diagnostics.csv
|   |       |-- strategy_summary.csv
|   |       `-- validation_comparison.csv
|   |
|   `-- lab04_geochemical_coda/
|       |-- 04_geochemical_coda.ipynb
|       |-- 04a_generate_synthetic_geochemistry.py
|       |-- 04b_run_coda_analysis.py
|       |-- 04c_lod_sensitivity.py
|       |-- 04d_audit_data_contract.py
|       |-- geochemistry_config.py
|       |-- geochemistry_contract.json
|       |-- README.md
|       |-- data/
|       |   `-- synthetic_geochemistry.csv
|       `-- results/
|           |-- analysis_summary.json
|           |-- correlation_closed.csv
|           |-- correlation_clr.csv
|           |-- correlation_raw.csv
|           |-- data_contract_audit.json
|           |-- lod_sensitivity_summary.json
|           |-- lod_sensitivity_variance.csv
|           |-- pca_explained_variance.csv
|           |-- pca_loadings_closed.csv
|           |-- pca_loadings_clr.csv
|           |-- pca_loadings_ilr.csv
|           `-- pca_loadings_raw.csv
|
|-- src/
|   `-- geoai/
|       |-- __init__.py
|       |-- composition.py
|       |-- crs.py
|       |-- spatial.py
|       `-- validation.py
|
|-- tests/
|   |-- test_composition.py
|   |-- test_cross_zone_crs.py
|   |-- test_crs.py
|   |-- test_lab04_contract.py
|   |-- test_lab04_notebook.py
|   |-- test_spatial.py
|   `-- test_validation.py
|
|-- environment.yml
|-- pyproject.toml
`-- README.md
```

## Engineering approach

The portfolio separates four complementary layers:

```text
1. COMMUNICATE
   Markdown + visual evidence

2. DEMONSTRATE
   executable notebooks and persisted results

3. ENGINEER
   reusable Python components

4. VALIDATE
   automated tests + quality controls
```

This structure is intended to make the work reviewable by different audiences, including recruiters, data scientists, geoscientists, and software-oriented technical reviewers.

## Reproducible environment

The project currently targets:

```text
Python 3.12
```

The validated environment is defined in:

```text
environment.yml
```

Create it with:

```bash
conda env create -f environment.yml
conda activate mining-geospatial-analytics
```

The analytical stack currently includes:

- NumPy
- Pandas
- SciPy
- scikit-learn
- GeoPandas
- Shapely
- PyProj
- Pyogrio
- Rasterio
- Matplotlib
- pytest

Dependencies are introduced incrementally as the portfolio develops rather than installing an entire future GeoAI stack in advance.

## Validation

Run the automated tests with:

```bash
python -m pytest -q
```

Current validated result:

```text
58 passed
```

Reusable CRS, spatial-analysis, spatial-validation, and compositional-analysis logic is tested independently from the explanatory notebooks.

The public LAB04 notebook additionally retains:

```text
24 code cells
24 executed code cells
24 outputs
0 notebook error outputs
```

## Data strategy

The current analytical experiments use synthetic data.

This approach keeps the experiments:

- reproducible
- redistribution-safe
- independent of proprietary exploration datasets
- focused on the methodological concept being demonstrated

LAB 02 additionally uses a Natural Earth country boundary only for geographic context. Its source, version, license status, and integrity hashes are documented alongside the local context file. The analytical experiment itself remains synthetic.

LAB 04 uses a synthetic ten-element geochemical subcomposition with explicit units, detection-limit semantics, missing-value semantics, and compositional assumptions documented in a machine-readable data contract.

Synthetic detection limits and concentration values are methodological assumptions and must not be interpreted as certified assay values or as empirical properties of a real mineral deposit.

Future external datasets will require explicit review of source, license, attribution, CRS, measurement units, analytical methods, detection limits, resolution, redistribution rights, and known limitations.

## Current roadmap

| Lab | Topic | Status |
| --- | --- | --- |
| LAB 01 | Geospatial Python Foundations | Complete |
| LAB 02 | Spatial Exploratory Data Analysis | Complete |
| LAB 03 | Spatial Cross-Validation | Complete |
| LAB 04 | Geochemical CoDA | Complete |
| LAB 05 | Mineral Prospectivity Mapping | Planned |
| LAB 06 | Explainable GeoAI | Planned |
| LAB 07 | Uncertainty Quantification | Planned |
| LAB 08 | Remote Sensing | Planned |
| LAB 09 | Deep Learning for GeoAI | Planned |
| LAB 10 | Graph & Multimodal GeoAI | Planned |

LAB 01 through LAB 04 are completed and validated.

LAB 03 establishes that validation geometry can materially change estimated predictive performance when observations are spatially structured.

LAB 04 adds the compositional-data foundation needed to represent multivariate geochemistry without treating a constrained subcomposition as ordinary unconstrained Euclidean data.

LAB 05 will combine these foundations in a controlled mineral prospectivity mapping experiment, with particular attention to spatial validation, leakage control, baseline comparison, and interpretable geoscientific features.

## Technical principles

- Reproducibility before complexity
- Spatially correct feature engineering
- Explicit CRS and units
- Explicit data contracts and analytical assumptions
- Appropriate treatment of compositional information
- Independent validation where appropriate
- Leakage-aware predictive modelling
- Simple evidence before advanced modelling
- Automated tests for reusable code
- Clear assumptions and limitations
- No credentials or proprietary datasets committed to Git

## Portfolio direction

This repository is intended as a curated technical portfolio rather than a production mineral exploration platform.

Later releases will progressively demonstrate capabilities in mineral prospectivity modelling, explainability, uncertainty quantification, remote sensing, deep learning, graph methods, and multimodal GeoAI.

The emphasis throughout the portfolio is:

> **Build evidence of analytical capability, not just code execution.**
