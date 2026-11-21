import logging
from pathlib import Path
from .reader import read_csv
from .transform import transform_records
from .writer import write_csv

logger = logging.getLogger(__name__)

def run_pipeline(input_path: str | Path, output_path: str | Path) -> dict[str, int]:
    logger.info("Starting ETL: %s -> %s", input_path, output_path)
    raw_records = read_csv(input_path)
    clean_records = transform_records(raw_records)
    write_csv(clean_records, output_path)
    metrics = {"records_read": len(raw_records), "records_written": len(clean_records)}
    logger.info("ETL completed: %s", metrics)
    return metrics
