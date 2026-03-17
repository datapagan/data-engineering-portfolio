from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
STAGING_DATA_DIR = BASE_DIR / "data" / "staging"
CURATED_DATA_DIR = BASE_DIR / "data" / "curated"

CURATED_DATA_DIR.mkdir(parents=True, exist_ok=True)


def transform_file(file_path: Path) -> Path:
    print(f"Cleaning file: {file_path.name}")

    df = pd.read_parquet(file_path)

    # Keep only expected clean files
    if "_clean" not in file_path.name:
        raise ValueError(f"Input file is not a clean file: {file_path.name}")

    # Standardize datetime columns
    if "tpep_pickup_datetime" in df.columns:
        df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"], errors="coerce")

    if "tpep_dropoff_datetime" in df.columns:
        df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"], errors="coerce")

    # Add derived fields
    if {"tpep_pickup_datetime", "tpep_dropoff_datetime"}.issubset(df.columns):
        df["trip_duration_minutes"] = (
            (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]).dt.total_seconds() / 60
        )

    if "tpep_pickup_datetime" in df.columns:
        df["pickup_date"] = df["tpep_pickup_datetime"].dt.date
        df["pickup_year"] = df["tpep_pickup_datetime"].dt.year
        df["pickup_month"] = df["tpep_pickup_datetime"].dt.month
        df["pickup_day"] = df["tpep_pickup_datetime"].dt.day
        df["pickup_hour"] = df["tpep_pickup_datetime"].dt.hour

    # Optional additional business filters
    if "trip_duration_minutes" in df.columns:
        df = df[df["trip_duration_minutes"].notna()]
        df = df[df["trip_duration_minutes"] > 0]
        df = df[df["trip_duration_minutes"] < 1440]  # less than 24 hours

    if "trip_distance" in df.columns:
        df = df[df["trip_distance"].notna()]
        df = df[df["trip_distance"] >= 0]

    if "fare_amount" in df.columns:
        df = df[df["fare_amount"].notna()]
        df = df[df["fare_amount"] >= 0]

    output_file = CURATED_DATA_DIR / f"{file_path.stem.replace('_clean', '')}_cleaned.parquet"
    df.to_parquet(output_file, index=False)

    print(f"Saved cleaned curated file: {output_file.name}")
    print(f"Rows written: {len(df)}")

    return output_file


def run() -> None:
    files = sorted(STAGING_DATA_DIR.glob("*_clean.parquet"))

    if not files:
        print("No clean parquet files found in data/staging.")
        return

    for file_path in files:
        transform_file(file_path)


if __name__ == "__main__":
    run()