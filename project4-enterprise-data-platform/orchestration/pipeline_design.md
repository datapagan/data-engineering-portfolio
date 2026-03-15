# Pipeline Design

## Purpose
This document defines the end-to-end orchestration flow for loading BLS API data into the enterprise data platform.

## Pipeline Name
bls_api_to_curated_pipeline

## Pipeline Steps

### 1. API Ingestion
Run Python script:
`python/bls_api_ingest.py`

Output:
`data/sample_source_data/bls_time_series_raw.csv`

### 2. Raw Load
Load the raw CSV file into:
`RAW.BLS_TIME_SERIES_RAW`

### 3. Transform Load
Run SQL transformation:
`sql/transformations/01_transform_bls_time_series.sql`

Output table:
`TRANSFORM.BLS_TIME_SERIES_CLEAN`

### 4. Curated Load
Run curated SQL:
`sql/curated/01_load_curated_bls_metrics.sql`

Output table:
`CURATED.BLS_METRICS_MONTHLY`

### 5. Data Quality Validation
Run validation SQL:
`sql/data_quality/01_validate_bls_metrics.sql`

## Future Orchestration Target
Azure Data Factory