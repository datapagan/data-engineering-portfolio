import csv
import requests
from datetime import datetime

BLS_API_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

SERIES_IDS = [
    "CES3000000001",  # Manufacturing employee count
    "CES3000000006",  # Manufacturing production workers
    "CES3000000008",  # Manufacturing avg hourly earnings
]

START_YEAR = "2021"
END_YEAR = "2026"
OUTPUT_FILE = "bls_workforce_data.csv"
SOURCE_NAME = "BLS_API"


def get_bls_data():
    payload = {
        "seriesid": SERIES_IDS,
        "startyear": START_YEAR,
        "endyear": END_YEAR
    }

    response = requests.post(BLS_API_URL, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def flatten_bls_response(response_json):
    rows = []
    load_ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    results = response_json.get("Results", {})
    series_list = results.get("series", [])

    for series in series_list:
        series_id = series.get("seriesID")
        data_points = series.get("data", [])

        for item in data_points:
            year = item.get("year")
            period = item.get("period")
            period_name = item.get("periodName")
            metric_value = item.get("value")
            latest_flag = item.get("latest")
            footnotes = item.get("footnotes", [])

            footnote_texts = []
            for footnote in footnotes:
                text = footnote.get("text")
                if text:
                    footnote_texts.append(text)

            footnotes_joined = " | ".join(footnote_texts)

            rows.append([
                load_ts,
                SOURCE_NAME,
                series_id,
                year,
                period,
                period_name,
                metric_value,
                latest_flag,
                footnotes_joined
            ])

    return rows


def write_csv(rows, output_file):
    header = [
        "LOAD_TS",
        "SOURCE_NAME",
        "SERIES_ID",
        "YEAR",
        "PERIOD",
        "PERIOD_NAME",
        "METRIC_VALUE",
        "LATEST_FLAG",
        "FOOTNOTES"
    ]

    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


def main():
    response_json = get_bls_data()

    status = response_json.get("status")
    if status != "REQUEST_SUCCEEDED":
        raise ValueError(f"BLS API request failed. Response: {response_json}")

    rows = flatten_bls_response(response_json)
    write_csv(rows, OUTPUT_FILE)

    print(f"File created: {OUTPUT_FILE}")
    print(f"Rows written: {len(rows)}")


if __name__ == "__main__":
    main()
