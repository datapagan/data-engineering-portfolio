from pathlib import Path
import pandas as pd
from datetime import datetime

# Paths
BASE_DIR = Path(__file__).resolve().parents[2]
STAGING_DATA_DIR = BASE_DIR / "data" / "staging"
OUTPUT_SUMMARY_DIR = BASE_DIR / "outputs" / "summary"

OUTPUT_SUMMARY_DIR.mkdir(parents=True, exist_ok=True)


def check_file(file_path: Path) -> dict:
    print(f"\nChecking file: {file_path.name}")

    df = pd.read_parquet(file_path)
    total_rows = len(df)

    # --- RULES ---
    null_pickup = df["tpep_pickup_datetime"].isna().sum() if "tpep_pickup_datetime" in df.columns else 0
    null_dropoff = df["tpep_dropoff_datetime"].isna().sum() if "tpep_dropoff_datetime" in df.columns else 0
    negative_fare_mask = df["fare_amount"] < 0 if "fare_amount" in df.columns else pd.Series([False]*len(df))
    negative_distance_mask = df["trip_distance"] < 0 if "trip_distance" in df.columns else pd.Series([False]*len(df))

    negative_fare = negative_fare_mask.sum()
    negative_distance = negative_distance_mask.sum()

    # --- SPLIT DATA ---
    reject_mask = (
        negative_fare_mask |
        negative_distance_mask |
        df["tpep_pickup_datetime"].isna() |
        df["tpep_dropoff_datetime"].isna()
    )

    df_rejects = df[reject_mask]
    df_clean = df[~reject_mask]

    # --- SAVE OUTPUTS ---
    clean_file = STAGING_DATA_DIR / f"{file_path.stem}_clean.parquet"
    reject_file = STAGING_DATA_DIR / f"{file_path.stem}_rejects.parquet"

    df_clean.to_parquet(clean_file, index=False)
    df_rejects.to_parquet(reject_file, index=False)

    print(f"Clean rows: {len(df_clean)}")
    print(f"Rejected rows: {len(df_rejects)}")

    # --- RETURN DQ RESULTS ---
    return {
        "file_name": file_path.name,
        "total_rows": total_rows,
        "null_pickup": int(null_pickup),
        "null_dropoff": int(null_dropoff),
        "negative_fare": int(negative_fare),
        "negative_distance": int(negative_distance),
        "rejected_rows": int(len(df_rejects)),
        "clean_rows": int(len(df_clean)),
        "run_timestamp": datetime.now()
    }


def run() -> None:
    files = list(STAGING_DATA_DIR.glob("*.parquet"))

    if not files:
        print("No parquet files found in staging.")
        return

    results = []

    for file_path in files:
        # Avoid reprocessing already cleaned/rejected files
        if "_clean" in file_path.name or "_rejects" in file_path.name:
            continue

        result = check_file(file_path)
        results.append(result)

    # --- SAVE DQ SUMMARY ---
    if results:
        df_results = pd.DataFrame(results)
        output_file = OUTPUT_SUMMARY_DIR / "dq_rule_results.csv"
        df_results.to_csv(output_file, index=False)

        print(f"\nDQ summary saved to: {output_file}")


if __name__ == "__main__":
    run()