import argparse
import logging
from .pipeline import run_pipeline

def main() -> None:
    parser = argparse.ArgumentParser(description="Run the sample CSV ETL pipeline")
    parser.add_argument("--input", required=True, help="Source CSV path")
    parser.add_argument("--output", required=True, help="Destination CSV path")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    metrics = run_pipeline(args.input, args.output)
    print(f"Completed: {metrics['records_written']} records written")

if __name__ == "__main__":
    main()
