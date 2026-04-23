from pathlib import Path  # For cross-platform file path handling
import requests  # For making HTTP requests to download remote files

# Base URL for NYC taxi data from AWS CloudFront
BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data"

# List of parquet files to download from the remote source
FILES_TO_DOWNLOAD = [
    "yellow_tripdata_2023-01.parquet",
    "yellow_tripdata_2023-02.parquet",
]

# Define the raw data directory path relative to this script's location
RAW_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"

print("Script started")


def download_file(file_name: str) -> None:
    """Download a single parquet file from the remote source to local storage."""
    # Ensure the raw data directory exists, creating parent directories if needed
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Construct the full remote URL for the file
    url = f"{BASE_URL}/{file_name}"
    # Determine the local output path for the file
    output_path = RAW_DATA_DIR / file_name

    # Skip download if the file already exists locally
    if output_path.exists():
        print(f"Skipped (already exists): {output_path.name}")
        return

    # Fetch the file from the remote URL with a 60-second timeout
    print(f"Downloading: {file_name}")
    response = requests.get(url, timeout=60)
    response.raise_for_status()

    # Write the downloaded content to the local file system
    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"Saved: {output_path}")


def run() -> None:
    """Iterate through all files and download each one, handling errors gracefully."""
    for file_name in FILES_TO_DOWNLOAD:
        try:
            download_file(file_name)
        except Exception as e:
            # Log errors without stopping the entire process
            print(f"Failed to download {file_name}: {e}")


if __name__ == "__main__":
    run()