# Mining Geospatial Analytics

Applied geospatial data science, spatial machine learning, and reproducible analytics for mineral exploration and mining.

This repository presents reproducible technical walkthroughs that connect geospatial reasoning, scientific validation, reusable Python code, automated testing, and clear technical communication.

The portfolio is developed incrementally. Each public laboratory is intended to demonstrate not only that code runs, but that the underlying spatial analysis is scientifically meaningful, reproducible, and testable.

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

## Why this matters for GeoAI

Spatial errors can silently propagate into features such as:

```text
distance_to_fault_m
distance_to_intrusive_m
distance_to_contact_m
distance_to_occurrence_m
nearest_anomaly_distance_m
neighbourhood_density
```

A machine-learning model may train successfully even when these input features are spatially incorrect.

For this reason, the portfolio treats spatial validation as a prerequisite for predictive modelling.

The current workflow follows:

```text
problem
 ->
spatial reasoning
 ->
reproducible analysis
 ->
independent validation
 ->
reusable implementation
 ->
automated testing
 ->
technical interpretation
```

## Current evidence

The current public portfolio includes:

- 3 recruiter-facing geospatial notebooks
- reusable CRS and spatial-analysis utilities under `src/geoai/`
- automated pytest validation
- 24 passing automated tests
- persisted synthetic Monte Carlo result artifacts for LAB 02
- documented provenance for the LAB 02 geographic context layer
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
|   `-- lab02_spatial_eda/
|       |-- 02_spatial_eda.ipynb
|       |-- 02_spatial_eda.py
|       |-- README.md
|       |-- data/
|       |   `-- context/
|       |       |-- chile_context.geojson
|       |       `-- SOURCE.md
|       `-- results/
|           |-- experiment_metadata.json
|           |-- monte_carlo_by_realization.csv
|           `-- resolution_summary.csv
|
|-- src/
|   `-- geoai/
|       |-- __init__.py
|       |-- crs.py
|       `-- spatial.py
|
|-- tests/
|   |-- test_crs.py
|   |-- test_cross_zone_crs.py
|   `-- test_spatial.py
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
   executable notebooks and results

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

The current geospatial stack includes:

- NumPy
- Pandas
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
24 passed
```

Reusable CRS and spatial-analysis logic is tested independently from the explanatory notebooks.

## Data strategy

The current walkthroughs use synthetic spatial examples.

This approach keeps the experiments:

- reproducible
- redistribution-safe
- independent of proprietary exploration datasets
- focused on the spatial concept being demonstrated

LAB 02 additionally uses a Natural Earth country boundary only for geographic context. Its source, version, license status, and integrity hashes are documented alongside the local context file. The analytical experiment itself remains entirely synthetic.

Future external datasets will require explicit review of source, license, attribution, CRS, resolution, redistribution rights, and known limitations.

## Current roadmap

| Lab | Topic | Status |
| --- | --- | --- |
| LAB 01 | Geospatial Python Foundations | Complete |
| LAB 02 | Spatial Exploratory Data Analysis | Complete |
| LAB 03 | Spatial Cross-Validation | Planned |
| LAB 04 | Geochemical CoDA | Planned |
| LAB 05 | Mineral Prospectivity Mapping | Planned |
| LAB 06 | Explainable GeoAI | Planned |
| LAB 07 | Uncertainty Quantification | Planned |
| LAB 08 | Remote Sensing | Planned |
| LAB 09 | Deep Learning for GeoAI | Planned |
| LAB 10 | Graph & Multimodal GeoAI | Planned |

LAB 01 and LAB 02 are completed and validated.

LAB 03 will extend the portfolio from exploratory spatial reasoning into spatial cross-validation, with explicit attention to spatial leakage and the limitations of conventional random train/test splits.

## Technical principles

- Reproducibility before complexity
- Spatially correct feature engineering
- Explicit CRS and units
- Independent validation where appropriate
- Simple evidence before advanced modelling
- Automated tests for reusable code
- Clear assumptions and limitations
- No credentials or proprietary datasets committed to Git

## Portfolio direction

This repository is intended as a curated technical portfolio rather than a production mineral exploration platform.

Later releases will progressively demonstrate capabilities in spatial EDA, spatial validation, geochemistry, mineral prospectivity modelling, explainability, uncertainty, remote sensing, deep learning, and advanced GeoAI.

The emphasis throughout the portfolio is:

> **Build evidence of analytical capability, not just code execution.**
