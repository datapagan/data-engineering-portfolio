# MES Production CSV Pipeline

## Overview
This data source extends Project 4 by adding a Manufacturing Execution System (MES) production CSV pipeline into the enterprise operational data platform.

## Pipeline Flow
MES CSV → Python Validation → Snowflake Stage → RAW → TRANSFORM → CURATED → Data Quality

## Purpose
This pipeline loads production data from MES CSV files and standardizes it for enterprise reporting, operational analytics, and future cross-source integration.

## Folder Structure
- `data/` raw and sample files
- `python/` ingestion and validation scripts
- `sql/` Snowflake objects and transformations
- `docs/` mapping, assumptions, and flow documentation