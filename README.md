# Project 1 — SFTP to Snowflake Data Pipeline
![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Platform-blue)
![SQL](https://img.shields.io/badge/SQL-Data%20Engineering-lightgrey)
![SnowSQL](https://img.shields.io/badge/SnowSQL-CLI%20Tool-blue)
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black)

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Step 1 — Create Database Objects](#step-1--create-database-objects)
- [Step 2 — Upload File to Stage](#step-2--upload-file-to-stage)
- [Step 3 — Load Data](#step-3--load-data)
- [Step 4 — Validate the Load](#step-4--validate-the-load)
- [Audit Logging](#audit-logging)
- [Key Concepts Demonstrated](#key-concepts-demonstrated)

## Overview

This project demonstrates a simple data ingestion pipeline that loads workforce data from a CSV file into Snowflake.  
The pipeline simulates a file arriving via secure transfer, staging the file in Snowflake, loading it into a raw table, validating the data, and recording the load in an audit log.

The SQL scripts are version controlled in GitHub and executed from a Git-connected Snowflake workspace.

---

## Architecture
## Pipeline Diagram
Local CSV File
      │
      │ SnowSQL PUT
      ▼
Snowflake Stage
(STG_WORKFORCE_FILES)
      │
      │ COPY INTO
      ▼
Raw Table
(WORKFORCE_RAW)
      │
      │ Validation Queries
      ▼
Audit Log
(LOAD_AUDIT_LOG)

---

## Technologies Used

- Snowflake
- SnowSQL CLI
- GitHub
- Snowflake Stages
- COPY INTO
- Stored Procedures
- SQL

---

## Project Structure
project1-sftp-snowflake-pipeline
│
├── sample_data
│ └── workforce_headcount.csv
│
├── sql
│ ├── 02_file_format_stage.sql
│ ├── 03_target_table.sql
│ ├── 04_copy_into.sql
│ ├── 05_validation_queries.sql
│ ├── 06_audit_table.sql
│ ├── 07_insert_audit_record.sql
│ └── 08_load_workforce_with_audit.sql
│
└── README.md


---

## Step 1 — Create Database Objects

Run these scripts in Snowflake:
03_target_table.sql
02_file_format_stage.sql
06_audit_table.sql
08_load_workforce_with_audit.sql


These scripts create:

- workforce table
- file format
- stage
- audit table
- load procedure

---

## Step 2 — Upload File to Stage

The sample workforce file was uploaded to the Snowflake internal stage using SnowSQL.

Example command:

```sql
PUT file://C:/Project/data_engineering_porfolio/sftp_pipeline/workforce_headcount.csvC:/Users/YourUser/Downloads/workforce_headcount.csv
@DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.STG_WORKFORCE_FILES
AUTO_COMPRESS=TRUE
OVERWRITE=TRUE;

Verify the file upload:
LIST @DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.STG_WORKFORCE_FILES;

This approach reflects a realistic command-line ingestion pattern for loading files into Snowflake before executing COPY INTO.

## Step 3 — Load Data
Run the stored procedure:
CALL DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.SP_LOAD_WORKFORCE_WITH_AUDIT();

This procedure:
- loads the data using COPY INTO
- records the load in the audit table

## Step 4 — Validate the Load
Example validation queries:
SELECT COUNT(*)
FROM DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.WORKFORCE_RAW;

SELECT department, COUNT(*)
FROM DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.WORKFORCE_RAW
GROUP BY department;

Audit Logging
Each pipeline run inserts a record into:
LOAD_AUDIT_LOG

This records:
- file name
- target table
- load timestamp
- number of rows loaded
- load status

Example query:
SELECT *
FROM DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.LOAD_AUDIT_LOG
ORDER BY audit_id DESC;

Key Concepts Demonstrated
- Snowflake data ingestion
- Internal stages
- File formats
- COPY INTO command
- SnowSQL file uploads
- Data validation
- Audit logging
- Git-based version control
