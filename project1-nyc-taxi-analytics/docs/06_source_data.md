@'
# Source Data

## Official Sources
1. NYC TLC Trip Record Data
2. Taxi Zone Lookup Table

## Initial Project Scope
The first build will use:
- Yellow taxi trip data
- Taxi zone lookup reference data

## Why these sources
- They are official public sources.
- They contain timestamps, fares, trip distance, payment details, and zone identifiers.
- They support business questions around demand, revenue, time trends, and zone performance.

## Join Logic
- Trip data.PULocationID = Taxi zone lookup.LocationID
- Trip data.DOLocationID = Taxi zone lookup.LocationID
'@ | Set-Content docs\06_source_data.md