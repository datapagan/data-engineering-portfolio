from pathlib import Path
from datetime import datetime, UTC
import pandas as pd

RAW_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"
STAGING_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "staging"


def load_raw_file(file_path: Path):

    print(f"Loading raw file: {file_path.name}")

    df = pd.read_parquet(file_path)

    # add ingestion metadata
    df["ingestion_timestamp"] = datetime.now(UTC)
    df["source_file"] = file_path.name

    return df


def save_to_staging(df, file_name):

    STAGING_DATA_DIR.mkdir(parents=True, exist_ok=True)

    output_path = STAGING_DATA_DIR / file_name

    df.to_parquet(output_path, index=False)

    print(f"Saved staged file: {file_name}")


def run():

    files = list(RAW_DATA_DIR.glob("*.parquet"))

    if not files:
        print("No parquet files found in raw folder")
        return

    for file_path in files:

        df = load_raw_file(file_path)

        save_to_staging(df, file_path.name)


if __name__ == "__main__":
    run()