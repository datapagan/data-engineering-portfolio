# Project 3: Data Quality Monitoring Framework for Snowflake Pipelines

## Overview

This project implements a **Data Quality Monitoring Framework** for a Snowflake-based data pipeline. The framework validates data loaded from an external API and records the results of automated quality checks into monitoring tables.

The objective is to simulate a real-world enterprise data engineering pattern where ingestion pipelines are validated using automated data quality controls.

The framework performs multiple validation checks including:

- Row count validation
- Critical null checks
- Duplicate record detection
- Numeric value validation
- Data freshness verification

The results of these checks are logged into dedicated monitoring tables for auditing and troubleshooting.

---

## Architecture

The data quality framework sits between the raw ingestion layer and downstream analytics tables. It validates data immediately after ingestion to ensure the pipeline produced valid and reliable data.

Pipeline flow:

API Source  
↓  
RAW_WORKFORCE_API_DATA (Raw ingestion table)  
↓  
Data Quality Validation Rules  
↓  
DQ Monitoring Tables  
↓  
Monitoring and troubleshooting

The framework logs the results of each validation rule execution into Snowflake monitoring tables.

---

## Monitoring Tables

The framework uses a dedicated monitoring schema:

`PROJECT3_DQ_MONITORING`

Three tables support the monitoring framework.

### DQ_PIPELINE_RUNS

Tracks each execution of the data quality framework.

| Column | Description |
|------|-------------|
| RUN_ID | Unique pipeline execution ID |
| PIPELINE_NAME | Name of the pipeline |
| TARGET_TABLE | Table validated |
| RUN_TIMESTAMP | Execution timestamp |
| RUN_STATUS | Overall pipeline result |
| TOTAL_CHECKS | Number of rules executed |
| PASSED_CHECKS | Number of successful rules |
| FAILED_CHECKS | Number of failed rules |

---

### DQ_RULE_RESULTS

Stores the results of each data quality rule executed during a pipeline run.

| Column | Description |
|------|-------------|
| RULE_RESULT_ID | Unique rule execution ID |
| RUN_ID | Pipeline execution reference |
| RULE_NAME | Name of the validation rule |
| TARGET_TABLE | Table validated |
| RULE_TYPE | Type of validation rule |
| RULE_STATUS | PASS or FAIL result |
| EXPECTED_VALUE | Expected condition |
| ACTUAL_VALUE | Observed result |
| CHECK_TIMESTAMP | Time the rule was evaluated |

---

### DQ_FAILED_RECORDS

Optional table designed to capture row-level failures for detailed troubleshooting.

---

## Data Quality Rules

The framework currently implements five core validation rules.

### 1. Row Count Validation
Ensures that the pipeline loaded data successfully.

Rule:
Row count must be greater than zero.

---

### 2. Critical Null Check
Ensures key fields required for analysis are populated.

Fields validated:

- SERIES_ID
- YEAR
- PERIOD
- METRIC_VALUE

---

### 3. Duplicate Record Detection
Detects duplicate records using the natural business key.

Business key:

SERIES_ID + YEAR + PERIOD

---

### 4. Numeric Value Validation
Ensures the `METRIC_VALUE` column can be converted to a numeric value.

This prevents invalid metric data from propagating into downstream analytics tables.

---

### 5. Data Freshness Check
Validates that the table contains recently loaded data using the `LOAD_TS` column.

This rule ensures the ingestion pipeline executed successfully.

---

## SQL Framework Structure

The project is organized into modular SQL scripts.

```text
project3-data-quality-framework
│
├── sql
│   ├── 01_create_dq_objects.sql
│   ├── 02_dq_rules.sql
│   ├── 03_test_queries.sql
│   └── 04_log_dq_results.sql
│
├── architecture
│
└── python
```

### 01_create_dq_objects.sql

Creates the monitoring schema and tables.

### 02_dq_rules.sql

Defines the core data quality validation rules.

### 03_test_queries.sql

Contains queries used to test the validation rules during development.

### 04_log_dq_results.sql

Logs validation results into monitoring tables for audit and troubleshooting.

---

## Key Concepts Demonstrated

This project demonstrates several core data engineering practices:

- Designing a **data quality validation framework**
- Implementing **automated validation rules** for data pipelines
- Using **Snowflake monitoring tables** for pipeline auditing
- Structuring SQL projects using **modular scripts**
- Managing code with **Git and GitHub**
- Developing SQL workflows using **VS Code**

This framework simulates how production data pipelines are monitored to ensure reliable data delivery for analytics and reporting.