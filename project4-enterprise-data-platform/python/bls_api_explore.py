import requests
import pandas as pd

url = "https://api.bls.gov/publicAPI/v2/timeseries/data/LNS14000000"

response = requests.get(url)
data = response.json()

records = data["Results"]["series"][0]["data"]

df = pd.DataFrame(records)

print(df.head())
print(df.columns)