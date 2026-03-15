import json
from datetime import datetime

import pandas as pd
import requests

SERIES_ID = "LNS14000000"
URL = f"https://api.bls.gov/publicAPI/v2/timeseries/data/{SERIES_ID}"

response = requests.get(URL, timeout=30)
response.raise_for_status()

data = response.json()
records = data["Results"]["series"][0]["data"]

df = pd.DataFrame(records)

df["series_id"] = SERIES_ID
df["period_name"] = df["periodName"]
df["value_raw"] = df["value"]
df["footnotes_raw"] = df["footnotes"].apply(json.dumps)
df["load_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

df = df[
    [
        "series_id",
        "year",
        "period",
        "period_name",
        "latest",
        "value_raw",
        "footnotes_raw",
        "load_timestamp",
    ]
]

output_path = "project4-enterprise-data-platform/data/sample_source_data/bls_time_series_raw.csv"
df.to_csv(output_path, index=False)

print(f"File created: {output_path}")
print(df.head())