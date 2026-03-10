# Project 2 - Workforce API Data Pipeline to Snowflake

## Overview
This project demonstrates an end-to-end API data pipeline using public workforce data. The pipeline extracts labor statistics from an external API, stores the raw data in Snowflake, and transforms it into a curated table for workforce trend analysis.

## Objective
The objective of this project is to simulate a real-world workforce planning data pipeline by integrating external labor data into Snowflake using a structured raw and curated design.

## Business Scenario
Workforce planning teams often rely on external labor market indicators to support hiring strategy, labor trend analysis, and operational planning. This project simulates that use case by ingesting public workforce data and preparing it for analytics consumption.

## Pipeline Flow
API extraction using Python  
→ Local CSV output  
→ Snowflake internal stage  
→ Raw table load  
→ SQL transformation  
→ Curated workforce trend table

## Tools Used
- Python
- Snowflake SQL
- Snowflake internal stage
- CSV file handling
- Public workforce API

## Project Structure
- `architecture/` contains architecture notes and design summary
- `python/` contains the API extraction script
- `sql/` contains Snowflake setup, load, transform, and validation scripts
- `sample-data/` contains notes about generated or extracted sample files

## Key Capabilities Demonstrated
- API-based data extraction
- Handling external workforce data
- Loading files into Snowflake
- Raw and curated table design
- SQL-based transformations
- Basic data validation and quality checks

## Outcome
The final output is a curated workforce trend table that can be used for reporting, trend analysis, and downstream dashboard development.
