from pathlib import Path
import json
import requests

MANIFEST_URL = "https://www.eia.gov/opendata/bulk/manifest.txt"
DATASET_KEY = "ELEC"   # good starter dataset
TIMEOUT_SECONDS = 60


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    source_root = script_dir.parent
    landing_dir = source_root / "data" / "landing"
    landing_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = landing_dir / "eia_bulk_manifest.json"

    print("Downloading EIA bulk manifest...")
    response = requests.get(MANIFEST_URL, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    manifest_text = response.text
    manifest_path.write_text(manifest_text, encoding="utf-8")

    manifest = json.loads(manifest_text)

    if DATASET_KEY not in manifest:
        raise KeyError(f"Dataset key '{DATASET_KEY}' not found in EIA manifest.")

    dataset_info = manifest[DATASET_KEY]
    access_url = dataset_info["accessURL"]
    last_updated = dataset_info.get("last_updated", "unknown")

    zip_path = landing_dir / f"{DATASET_KEY}.zip"

    print(f"Downloading dataset: {DATASET_KEY}")
    print(f"Source URL: {access_url}")
    print(f"Last updated: {last_updated}")

    with requests.get(access_url, stream=True, timeout=TIMEOUT_SECONDS) as download_response:
        download_response.raise_for_status()
        with open(zip_path, "wb") as f:
            for chunk in download_response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

    print(f"Manifest saved to: {manifest_path}")
    print(f"ZIP file saved to: {zip_path}")
    print("Download complete.")


if __name__ == "__main__":
    main()