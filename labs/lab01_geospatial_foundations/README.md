# LAB 01 - Geospatial Python Foundations

## Overview

LAB 01 establishes the geospatial foundations required for reliable GeoAI workflows in mineral exploration.

The objective is to develop a correct, reproducible, and testable understanding of vector and raster spatial data before introducing spatial machine learning, mineral prospectivity modelling, remote sensing, or advanced GeoAI techniques.

This laboratory prioritizes **spatial correctness, interpretability, validation, and reproducibility before model complexity**.

---

## Current status

**Status: In progress - LAB 01A and LAB 01B completed and validated**

The LAB 01 geospatial environment has been qualified on Python 3.12.

Two applied portfolio walkthroughs are currently available:

- LAB 01A - Coordinate Systems for Mineral Exploration
- LAB 01B - Crossing UTM Zones in Spatial Analysis

Together they demonstrate:

- Coordinate Reference System (CRS) inspection and reprojection
- geographic versus projected coordinates
- WGS84 / EPSG:4326 interpretation
- automatic WGS84 UTM zone selection
- projected versus geodesic distance validation
- cross-zone UTM failure analysis
- use of a common projected CRS for joint spatial operations
- reusable CRS utilities
- automated validation with pytest
- geospatial visualization
- recruiter-facing technical communication

Current automated CRS validation:

```text
15 tests passing
```

Remaining LAB 01 topics include geometry validation, spatial joins, buffering, overlays, raster foundations, raster sampling, and raster/vector integration.

---

## Portfolio walkthroughs

### LAB 01A - Coordinate Systems for Mineral Exploration

[Open the recruiter-facing notebook](01a_coordinate_foundations.ipynb)

**Problem:** distance-based spatial features are common in mineral exploration, but they can become scientifically unreliable when the Coordinate Reference System and measurement units are misunderstood.

The walkthrough demonstrates:

- geographic versus projected coordinates
- WGS84 / EPSG:4326 interpretation
- why longitude and latitude cannot be treated directly as metric coordinates
- automatic UTM zone selection
- validation against GeoPandas `estimate_utm_crs()`
- projected versus geodesic distance
- implications for mineral-exploration feature engineering
- reusable CRS utilities
- automated validation with pytest

**Key finding:** a spatial calculation can be computationally correct while still being geoscientifically invalid if the CRS and measurement units are misunderstood.

### LAB 01A evidence

| Evidence | Status |
| --- | --- |
| Recruiter-facing notebook | Complete |
| CRS-aware distance experiment | Complete |
| Automatic UTM selection | Complete |
| GeoPandas CRS cross-check | Complete |
| UTM vs geodesic validation | Complete |
| Visual spatial evidence | Complete |
| Reusable CRS utilities | Complete |
| LAB 01A automated CRS tests | 13 passing |

---

### LAB 01B - Crossing UTM Zones in Spatial Analysis

[Open the recruiter-facing notebook](01b_cross_zone_crs.ipynb)

**Problem:** projected coordinates expressed in metres are not automatically comparable when they belong to different Coordinate Reference Systems.

The walkthrough demonstrates:

- UTM Zone 18S / EPSG:32718 identification
- UTM Zone 19S / EPSG:32719 identification
- independent WGS84 geodesic distance
- use of one common projected CRS for joint spatial analysis
- an intentionally invalid mixed-CRS calculation
- numerical comparison of valid and invalid approaches
- implications for mineral-exploration feature engineering
- automated regression testing

**Key finding:** using metres does not guarantee spatial comparability. Joint projected operations require geometries to share a compatible spatial reference system.

### LAB 01B evidence

| Evidence | Result |
| --- | ---: |
| WGS84 geodesic reference | ~38.594 km |
| Common CRS - EPSG:32719 | ~38.619 km |
| Common CRS relative difference | ~0.0635% |
| Invalid mixed UTM 18S / 19S result | ~540.215 km |
| Invalid mixed-CRS relative difference | ~1299.72% |
| Cross-zone automated tests | 2 passing |
| Total CRS-related automated tests | 15 passing |

---

## Combined GeoAI lesson

LAB 01A and LAB 01B demonstrate two progressively stronger spatial controls:

```text
LAB 01A
degrees are not metres
        ->
CRS and units must be interpreted correctly
        ->
LAB 01B
metres are not automatically comparable
        ->
joint spatial operations require a compatible common CRS
```

The central lesson is that **successful code execution does not guarantee scientifically valid spatial analysis**.

Spatial meaning, units, coordinate systems, and analytical context must be validated before derived spatial features are used in later machine-learning workflows.

---

## Technical artifacts

The public LAB 01 portfolio currently includes:

- [LAB 01A recruiter-facing notebook](01a_coordinate_foundations.ipynb)
- [LAB 01B recruiter-facing notebook](01b_cross_zone_crs.ipynb)
- [Reusable CRS utilities](../../src/geoai/crs.py)
- [Core CRS automated tests](../../tests/test_crs.py)
- [Cross-zone CRS automated tests](../../tests/test_cross_zone_crs.py)
- [Reproducible environment definition](../../environment.yml)

The separation between communication, reusable implementation, and validation is intentional:

```text
communication
     ->
notebooks
     ->
reusable implementation
     ->
src/geoai/
     ->
automated validation
     ->
tests/
```

This allows the work to be reviewed at different levels by recruiters, geoscientists, data scientists, and software-oriented technical reviewers.

---

## Objectives

LAB 01 aims to develop and validate the ability to:

- understand fundamental spatial data structures
- work with vector and raster geospatial data
- identify and manage Coordinate Reference Systems
- reproject spatial datasets correctly
- perform geometric and spatial operations
- calculate spatial distances using appropriate projected coordinate systems
- perform spatial joins and overlays
- inspect and validate geometry quality
- sample raster information using vector geometries
- create reproducible geospatial visualizations
- build reusable Python components for later GeoAI laboratories

---

## Scientific principles

### Spatial location matters

Geospatial observations are not independent in the same way as ordinary tabular observations.

Spatial relationships, proximity, scale, projection, spatial dependence, and autocorrelation must be considered explicitly.

### CRS is part of the data

A coordinate pair without its Coordinate Reference System is incomplete.

CRS validation must therefore occur before:

- distance calculations
- buffering
- overlay
- area calculations
- raster/vector alignment
- spatial feature engineering
- model feature extraction

### Units must be explicit

A numerical spatial result has limited analytical value if its physical units are unknown or incorrectly interpreted.

For example:

```text
0.014142
```

may be mathematically valid as an angular separation in degrees while being inappropriate if interpreted as metres or kilometres.

Spatial variables should therefore communicate their units explicitly where practical, for example:

```text
distance_to_fault_m
distance_to_intrusive_m
distance_to_contact_m
```

### Visualization is not validation

A map that looks correct may still contain:

- incorrect CRS definitions
- invalid geometries
- spatial misalignment
- unit inconsistencies
- duplicated features
- incorrect raster transforms
- inconsistent spatial extents

Geospatial workflows therefore require programmatic validation in addition to visual inspection.

### Computational correctness is not enough

Code can execute successfully while producing a scientifically invalid spatial result.

GeoAI workflows must therefore consider:

```text
CRS
 ->
units
 ->
spatial operation
 ->
validation
 ->
interpretation
```

before spatial variables are used in machine-learning pipelines.

---

## Scope

LAB 01 covers the following foundations.

### Vector data

Topics include:

- points
- lines
- polygons
- GeoDataFrames
- geometry columns
- geometry validation
- spatial relationships
- spatial indexing

### Coordinate Reference Systems

Topics include:

- geographic CRS
- projected CRS
- EPSG identifiers
- coordinate transformations
- coordinate units
- WGS84
- UTM zones
- appropriate CRS selection for spatial measurements
- limitations of local projections

### Core spatial operations

The laboratory introduces:

- spatial joins
- clipping
- buffering
- intersections
- overlays
- centroid operations
- bounding boxes
- distance calculations

### Raster foundations

Topics include:

- raster dimensions
- bands
- cells
- resolution
- transform
- extent
- CRS
- NoData
- raster sampling
- raster/vector relationships

### Visualization

The laboratory produces geospatial visualizations suitable for:

- exploratory inspection
- spatial quality assurance
- technical communication
- interpretation
- portfolio demonstrations

---

## Geospatial dependency stack

The LAB 01 scientific stack was assessed incrementally and validated in the dedicated project environment.

Current direct scientific, geospatial, interactive, and testing dependencies include:

```text
NumPy
Pandas
GeoPandas
Shapely
PyProj
Pyogrio
Rasterio
Matplotlib
IPyKernel
pytest
```

Dependencies are not added solely because they are commonly used.

Each direct dependency must have a clear technical role and remain compatible with the validated project environment.

The reproducible dependency definition is maintained in:

```text
environment.yml
```

---

## Environment strategy

The public portfolio uses the dedicated Conda environment:

```text
mining-geospatial-analytics
```

Project-level dependencies are controlled through:

```text
environment.yml
```

The environment currently targets:

```text
Python 3.12
```

`conda-forge` is the preferred dependency source for the scientific and geospatial environment.

The environment strategy follows several principles:

- introduce dependencies incrementally
- prefer direct dependencies with a demonstrated requirement
- validate compatibility before relying on a package
- avoid installing the complete future GeoAI stack prematurely
- maintain reproducibility through `environment.yml`
- separate project requirements from unrelated Python environments

---

## Data strategy

LAB 01 preferentially uses:

- public geospatial data
- redistribution-safe data
- small synthetic spatial examples

The current recruiter-facing walkthroughs use synthetic examples so the spatial concepts can be reproduced without licensing, confidentiality, availability, or external-data dependencies.

Any external dataset introduced later should be reviewed for:

- source
- license
- attribution requirements
- redistribution permission
- CRS information
- spatial resolution
- update or version information
- known limitations

---

## Repository strategy

Communication, reusable code, and validation are intentionally separated.

Recruiter-facing and explanatory analyses are provided as notebooks.

Reusable logic is maintained under:

```text
src/geoai/
```

where it can be tested and reused by later laboratories.

The intended workflow is:

```text
problem
 ->
analysis
 ->
notebook
 ->
interpretation
 ->
reusable implementation
 ->
src/geoai/
 ->
tests
```

The portfolio therefore uses four complementary layers:

```text
1. COMMUNICATE
   Markdown + visual evidence

2. DEMONSTRATE
   executable analysis and results

3. ENGINEER
   reusable components under src/geoai/

4. VALIDATE
   pytest + pre-commit + Gitleaks
```

---

## Planned learning sequence

The LAB 01 progression is:

```text
1. Geospatial data concepts
        ->
2. Vector geometries
        ->
3. CRS and projections
        ->
4. Geometry validation
        ->
5. Spatial operations
        ->
6. Distance and area calculations
        ->
7. Raster foundations
        ->
8. Raster/vector integration
        ->
9. Geospatial visualization
        ->
10. Reusable utilities and tests
```

The sequence may evolve as later exercises reveal additional technical requirements.

---

## Quality controls

Applicable LAB 01 work should include:

- reproducible environment configuration
- CRS validation
- geometry validation
- explicit measurement units
- deterministic examples where appropriate
- assertions and automated tests
- source attribution
- documented assumptions
- documented limitations
- pre-commit validation
- Gitleaks scanning
- signed Git commits
- Pull Request integration

For reusable components, automated tests are preferred over relying only on notebook output.

---

## Definition of Done

LAB 01 will be considered technically complete when:

- [x] dependency compatibility has been assessed
- [x] the minimal geospatial environment has been installed
- [x] environment recreation has been validated
- [x] GeoPandas can read and manipulate vector geometries
- [x] CRS inspection and reprojection have been demonstrated
- [ ] geometry validation has been demonstrated
- [ ] spatial joins have been demonstrated
- [ ] buffering and overlay operations have been demonstrated
- [x] spatial distance calculations use appropriate units and CRS
- [ ] Rasterio can read and inspect raster metadata
- [ ] raster sampling has been demonstrated
- [ ] raster and vector CRS alignment has been demonstrated
- [x] basic geospatial visualizations have been generated
- [x] reusable utilities exist under `src/geoai/` where appropriate
- [x] tests cover reusable functionality
- [x] documentation explains assumptions and limitations
- [x] security and repository QA checks pass

LAB 01 remains **in progress** until the remaining vector, geometry, raster, and spatial-integration requirements are completed.

---

## Relationship with later laboratories

LAB 01 provides the technical foundation for:

```text
LAB 01 - Geospatial Python Foundations
        ->
LAB 02 - Spatial EDA
        ->
LAB 03 - Spatial Cross-Validation
        ->
LAB 04 - Geochemical CoDA
        ->
LAB 05 - Mineral Prospectivity Mapping
        ->
LAB 06 - Explainable GeoAI
        ->
LAB 07 - Uncertainty Quantification
        ->
LAB 08 - Remote Sensing
        ->
LAB 09 - Deep Learning for GeoAI
        ->
LAB 10 - Graph & Multimodal GeoAI
```

Incorrect spatial foundations would propagate errors into every later stage.

For that reason, LAB 01 emphasizes spatial correctness, validation, interpretation, reproducibility, and communication before predictive modelling.
