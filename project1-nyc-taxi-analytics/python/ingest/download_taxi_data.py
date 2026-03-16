from pathlib import Path
import requests

BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data"
FILES_TO_DOWNLOAD = [
    "yellow_tripdata_2023-01.parquet",
    "yellow_tripdata_2023-02.parquet",
]

RAW_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"

print("Script started")


def download_file(file_name: str) -> None:
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    url = f"{BASE_URL}/{file_name}"
    output_path = RAW_DATA_DIR / file_name

    if output_path.exists():
        print(f"Skipped (already exists): {output_path.name}")
        return

    print(f"Downloading: {file_name}")
    response = requests.get(url, timeout=60)
    response.raise_for_status()

    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"Saved: {output_path}")


def run() -> None:
    for file_name in FILES_TO_DOWNLOAD:
        try:
            download_file(file_name)
        except Exception as e:
            print(f"Failed to download {file_name}: {e}")


if __name__ == "__main__":
    run()