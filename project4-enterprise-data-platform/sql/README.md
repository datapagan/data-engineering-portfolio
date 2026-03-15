# SQL Execution Order

This document defines the recommended execution order for SQL objects in the project.

## 1. Create Schemas
- `ddl/00_create_schemas.sql`

## 2. Create RAW Table
- `ddl/01_create_raw_bls_table.sql`

## 3. Create TRANSFORM Table
- `ddl/02_create_transform_bls_table.sql`

## 4. Create CURATED Table
- `ddl/03_create_curated_bls_metrics.sql`

## 5. Run TRANSFORM Load
- `transformations/01_transform_bls_time_series.sql`

## 6. Run CURATED Load
- `curated/01_load_curated_bls_metrics.sql`

## 7. Run Data Quality Validation
- `data_quality/01_validate_bls_metrics.sql`