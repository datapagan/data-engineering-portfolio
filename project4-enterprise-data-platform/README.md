## Architecture Layers

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

## Source Systems and Business Domains

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

## Core Business Use Cases

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

## Key KPIs

- Production Volume
- First Pass Yield (FPY)
- Defect Rate
- Scrap Rate
- Labor Hours
- Units per Labor Hour
- On-Time Delivery %

## Technology Stack

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

## Project Structure

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

## Platform Architecture

The enterprise operational data platform follows a layered data architecture.

### Data Flow

1. **Source Systems**
   - ERP
   - MES
   - Quality System
   - HR / Workforce
   - Flat Files

2. **Ingestion Layer**
   - Azure Data Factory pipelines extract data from source systems.
   - Batch ingestion loads data into the platform.

3. **Raw Data Layer**
   - Raw data is stored in Snowflake with minimal transformation.
   - This layer preserves source data for traceability and auditing.

4. **Transform Layer**
   - SQL transformations clean and standardize the data.
   - Data from multiple sources is joined and structured.

5. **Curated Layer**
   - Business-ready tables are created for analytics and reporting.
   - KPI calculations and business metrics are produced here.

6. **Consumption Layer**
   - Dashboards and reports are built using Power BI or Tableau.
   - Business users access trusted operational insights.

   ## Snowflake Data Architecture

The platform organizes data using layered schemas to support traceability, transformation, and analytics.

### Database
ENTERPRISE_DATA_PLATFORM

### Schemas

RAW
Stores ingested source data with minimal changes.

TRANSFORM
Contains cleaned and standardized datasets used for modeling.

CURATED
Stores analytics-ready tables used by dashboards and reporting.

DATA_QUALITY
Stores validation rules, monitoring results, and audit logs.

## Raw Layer Source Tables

The raw layer stores source data from multiple operational systems.

### 1. ERP_ORDERS_RAW
Order and delivery-related data from the ERP system.

Example fields:
- order_id
- order_date
- customer_id
- product_id
- plant_id
- ordered_quantity
- shipped_quantity
- delivery_date

### 2. MES_PRODUCTION_RAW
Production activity data from the MES system.

Example fields:
- production_date
- plant_id
- work_center_id
- product_id
- operation_id
- units_produced
- run_hours

### 3. QUALITY_EVENTS_RAW
Quality event and defect data from the quality system.

Example fields:
- event_id
- event_date
- plant_id
- product_id
- defect_type
- defect_quantity
- scrap_quantity
- rework_quantity

### 4. HR_LABOR_RAW
Workforce and labor data from the HR system.

Example fields:
- labor_date
- employee_id
- plant_id
- department_id
- labor_hours
- overtime_hours
- shift

### 5. FILE_TARGETS_RAW
Business targets and manual reference inputs from flat files.

Example fields:
- reporting_month
- plant_id
- kpi_name
- target_value

## Initial Data Sources

### API Source
BLS Public Data API

### File Source
BLS QCEW Open Data CSV files

### Reason for Selection
These sources allow the platform to demonstrate both API-based ingestion and file-based ingestion using real public labor and employment data.

## Data Source Profiling

### BLS API Example Fields

- seriesID
- year
- period
- periodName
- value

### Data Grain
seriesID + year + period

## Data Source Profiling

### BLS API Source
Sample series used for exploration: `LNS14000000`

### Observed Fields
- year
- period
- periodName
- latest
- value
- footnotes

### Data Characteristics
- `value` may contain non-numeric values such as `-`
- `footnotes` is a nested field
- monthly grain is represented by `year + period`
- one API response belongs to a specific series ID