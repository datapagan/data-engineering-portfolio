# Project 4 – Enterprise Operational Data Platform

## Overview

This project demonstrates the design and implementation of an **enterprise-style operational data platform** that integrates data from multiple sources, processes it through layered transformations, and delivers curated datasets for analytics and reporting.

The platform follows modern data engineering principles including:

- layered data architecture
- reproducible ingestion pipelines
- separation of raw and transformed data
- data quality validation
- orchestration-ready design

The implementation uses **Python, SQL, Snowflake, and Azure Data Factory concepts**.

---

# Architecture Layers

### 1. Source Systems
Operational and business data comes from multiple systems such as ERP, MES, Quality, HR, and flat files.

### 2. Ingestion
Data is extracted and loaded into the platform through batch pipelines and file-based ingestion processes.

### 3. Raw Layer
Raw data is stored with minimal changes for traceability and auditability.

### 4. Transform Layer
Raw data is cleaned, standardized, joined, and transformed into usable business structures.

### 5. Curated Layer
Trusted analytics-ready tables are created for reporting, KPI tracking, and decision-making.

### 6. Consumption Layer
Business users access the data through dashboards, reports, and ad hoc analysis.

---

# Source Systems and Business Domains

### Source Systems
- ERP system
- MES system
- Quality management system
- HR / workforce system
- Flat files / Excel extracts

### Business Domains
- Production
- Quality
- Delivery
- Workforce
- Finance-support metrics

---

# Core Business Use Cases

The platform supports operational monitoring and performance management across manufacturing operations.

### Use Case 1 – Production Performance
Track production volume, throughput, and operational efficiency.

### Use Case 2 – Quality Monitoring
Monitor defect rates, scrap, and rework across production lines.

### Use Case 3 – Workforce Utilization
Analyze labor hours, staffing levels, and workforce productivity.

### Use Case 4 – Delivery Performance
Track on-time delivery and order fulfillment metrics.

---

# Key KPIs

- Production Volume
- First Pass Yield (FPY)
- Defect Rate
- Scrap Rate
- Labor Hours
- Units per Labor Hour
- On-Time Delivery %

---

# Technology Stack

### Cloud Platform
Azure

### Data Warehouse
Snowflake

### Orchestration
Azure Data Factory

### Data Processing
SQL and Python

### Data Storage Layers
Snowflake databases and schemas for raw, transform, and curated data

### Version Control
GitHub

### Visualization
Power BI / Tableau

### Data Quality
SQL validation rules and monitoring tables

---

# Project Structure

```text
project4-enterprise-data-platform/
│
├── README.md
├── architecture/
├── data/
│   ├── sample_source_data/
│   └── reference_data/
├── sql/
│   ├── ddl/
│   ├── ingestion/
│   ├── transformations/
│   ├── curated/
│   └── data_quality/
├── python/
├── orchestration/
├── dashboards/
└── docs/