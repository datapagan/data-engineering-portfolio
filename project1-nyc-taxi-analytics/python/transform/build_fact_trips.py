from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
CURATED_DATA_DIR = BASE_DIR / "data" / "curated"


def build_trip_id(df: pd.DataFrame) -> pd.Series:
    key_parts = []

    for col in [
        "vendorid",
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "pulocationid",
        "dolocationid",
    ]:
        if col in df.columns:
            key_parts.append(df[col].astype(str))
        else:
            key_parts.append(pd.Series([""] * len(df), index=df.index))

    return (
        key_parts[0] + "_"
        + key_parts[1] + "_"
        + key_parts[2] + "_"
        + key_parts[3] + "_"
        + key_parts[4]
    )


def run() -> None:
    trip_files = sorted(CURATED_DATA_DIR.glob("*_cleaned.parquet"))

    if not trip_files:
        print("No cleaned curated parquet files found.")
        return

    frames = []

    for file_path in trip_files:
        print(f"Reading cleaned trip file: {file_path.name}")
        df = pd.read_parquet(file_path)
        frames.append(df)

    fact_df = pd.concat(frames, ignore_index=True)

    fact_df.columns = [col.strip().lower() for col in fact_df.columns]
    fact_df = fact_df.loc[:, ~fact_df.columns.duplicated()]

    if "vendorid" in fact_df.columns:
        fact_df = fact_df.rename(columns={"vendorid": "vendor_id"})
    if "pulocationid" in fact_df.columns:
        fact_df = fact_df.rename(columns={"pulocationid": "pickup_location_id"})
    if "dolocationid" in fact_df.columns:
        fact_df = fact_df.rename(columns={"dolocationid": "dropoff_location_id"})

    fact_df["trip_id"] = build_trip_id(
        fact_df.rename(
            columns={
                "vendor_id": "vendorid",
                "pickup_location_id": "pulocationid",
                "dropoff_location_id": "dolocationid",
            }
        )
    )

    preferred_columns = [
        "trip_id",
        "vendor_id",
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "pickup_date",
        "pickup_year",
        "pickup_month",
        "pickup_day",
        "pickup_hour",
        "passenger_count",
        "trip_distance",
        "trip_duration_minutes",
        "ratecodeid",
        "store_and_fwd_flag",
        "pickup_location_id",
        "dropoff_location_id",
        "payment_type",
        "fare_amount",
        "extra",
        "mta_tax",
        "tip_amount",
        "tolls_amount",
        "improvement_surcharge",
        "total_amount",
        "congestion_surcharge",
        "airport_fee",
    ]

    final_columns = [col for col in preferred_columns if col in fact_df.columns]
    fact_df = fact_df[final_columns].copy()

    output_file = CURATED_DATA_DIR / "fact_trips.parquet"
    fact_df.to_parquet(output_file, index=False)

    print(f"Saved fact table: {output_file}")
    print(f"Rows written: {len(fact_df)}")


if __name__ == "__main__":
    run()