# Architecture - Project 2 API Workforce Data Pipeline

## Architecture Summary
This project uses a simple batch pipeline architecture to extract external workforce data from a public API, land the data in a raw layer, and transform it into a curated analytics-ready table in Snowflake.

The design follows a basic data engineering pattern:

External API  
→ Python extraction  
→ Local flat file output  
→ Snowflake stage  
→ Raw ingestion table  
→ Curated transformation table  
→ Validation queries

## Architecture Components

### 1. Public Workforce API
The source system is a public API that provides workforce-related time-series data. This represents an external upstream source that is controlled outside the enterprise environment.

### 2. Python Extraction Layer
A Python script is used to call the API, parse the JSON response, flatten the required fields, and write the results into a CSV file. This simulates an ingestion process that collects data from an external system and prepares it for loading.

### 3. Local Landing File
The extracted data is written to a local CSV file. This serves as the landing artifact between extraction and warehouse ingestion. In a production design, this could be replaced by cloud storage or an automated landing zone.

### 4. Snowflake Internal Stage
The CSV file is uploaded into a Snowflake internal stage. The stage acts as the controlled ingestion point before the data is loaded into warehouse tables.

### 5. Raw Table
The raw table stores the extracted API data with minimal transformation. This preserves the source structure as closely as possible and supports traceability, reloads, and validation.

### 6. Curated Table
The curated table applies business-friendly transformations such as:
- type casting
- date standardization
- metric naming
- filtering valid reporting periods
- preparing data for trend analysis

This layer represents the analytics-ready output of the pipeline.

### 7. Validation Layer
Validation queries are included to verify:
- row counts
- duplicate checks
- null checks
- date coverage
- transformed record quality

This supports confidence in the pipeline output and demonstrates data control thinking.

## Data Flow

### Step 1 - Extract
Python sends a request to the public workforce API and receives JSON data.

### Step 2 - Parse
The script parses the response and selects the required attributes for reporting.

### Step 3 - Land
The parsed data is written into a CSV file.

### Step 4 - Stage
The CSV file is uploaded to a Snowflake internal stage.

### Step 5 - Load Raw
A `COPY INTO` command loads the file into a raw Snowflake table.

### Step 6 - Transform
SQL transforms the raw records into a curated workforce trend table.

### Step 7 - Validate
Validation queries confirm that the pipeline loaded and transformed the data correctly.

## Design Principles

### Raw and Curated Separation
The solution keeps raw ingestion separate from curated reporting data. This improves auditability, supports reprocessing, and reflects common warehouse design practice.

### Minimal Raw Transformation
The raw layer is intentionally kept close to the source structure to preserve lineage and simplify troubleshooting.

### Business-Friendly Curated Output
The curated table is designed for downstream reporting and trend analysis rather than source preservation.

### Repeatable Load Pattern
The architecture supports a repeatable batch ingestion process. The same design could later be extended for scheduling, orchestration, and incremental logic.

## Future Enhancements
Possible future improvements include:
- automated scheduling
- incremental load logic
- API error logging
- load audit table
- retry handling
- cloud storage landing zone
- orchestration with Airflow or Azure Data Factory
- dashboard layer on top of the curated table

## Architecture Diagram

```text
+---------------------+
| Public Workforce API |
+----------+----------+
           |
           v
+----------------------+
| Python Extract Script |
+----------+-----------+
           |
           v
+------------------+
| Local CSV Output |
+---------+--------+
          |
          v
+---------------------------+
| Snowflake Internal Stage  |
+-------------+-------------+
              |
              v
+---------------------------+
| RAW_WORKFORCE_API_DATA    |
+-------------+-------------+
              |
              v
+---------------------------+
| CURATED_WORKFORCE_TRENDS  |
+-------------+-------------+
              |
              v
+---------------------------+
| Validation / Reporting    |
+---------------------------+
