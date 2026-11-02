"""Entry point to customize after copying this package."""

from common.paths import RAW_DATA_DIR, PROCESSED_DATA_DIR


def main() -> None:
    print(f"Network workspace: {__package__}")
    print(f"Raw data: {RAW_DATA_DIR}")
    print(f"Processed data: {PROCESSED_DATA_DIR}")


if __name__ == "__main__":
    main()
