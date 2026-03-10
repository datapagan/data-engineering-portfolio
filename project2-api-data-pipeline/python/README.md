# Python Extraction Script

## Purpose
This script extracts workforce time-series data from the BLS public API, flattens the JSON response, and writes the results to a CSV file for loading into Snowflake.

## Output
The script creates:

- `bls_workforce_data.csv`

## Data Included
The script currently extracts these BLS series:

- `CES3000000001` - Manufacturing employee count
- `CES3000000006` - Manufacturing production workers
- `CES3000000008` - Manufacturing average hourly earnings

## Process
1. Send a POST request to the BLS API
2. Retrieve JSON time-series response
3. Flatten the response into tabular rows
4. Write the rows to a CSV file
5. Use the CSV file for Snowflake stage upload and load

## Run Command
```bash
python bls_workforce_extractor.py
