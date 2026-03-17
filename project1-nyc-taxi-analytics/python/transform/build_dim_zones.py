from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
REFERENCE_DATA_DIR = BASE_DIR / "data" / "reference"
CURATED_DATA_DIR = BASE_DIR / "data" / "curated"

CURATED_DATA_DIR.mkdir(parents=True, exist_ok=True)


def run() -> None:
    source_file = REFERENCE_DATA_DIR / "taxi_zone_lookup.csv"

    if not source_file.exists():
        print(f"Reference file not found: {source_file}")
        return

    df = pd.read_csv(source_file)

    # Standardize column names
    df.columns = [col.strip().lower() for col in df.columns]

    rename_map = {
        "locationid": "location_id",
        "borough": "borough",
        "zone": "zone",
        "service_zone": "service_zone",
    }
    df = df.rename(columns=rename_map)

    expected_cols = ["location_id", "borough", "zone", "service_zone"]
    existing_cols = [col for col in expected_cols if col in df.columns]
    df = df[existing_cols].copy()

    df = df.drop_duplicates(subset=["location_id"])
    df = df.sort_values("location_id")

    output_file = CURATED_DATA_DIR / "dim_zones.parquet"
    df.to_parquet(output_file, index=False)

    print(f"Saved zone dimension: {output_file}")
    print(f"Rows written: {len(df)}")


if __name__ == "__main__":
    run()