import csv
from pathlib import Path
from .exceptions import DataValidationError

REQUIRED_COLUMNS = {"order_id", "customer_id", "order_date", "amount"}

def read_csv(path: str | Path) -> list[dict[str, str]]:
    """Read CSV records and ensure the required columns exist."""
    source = Path(path)
    if not source.is_file():
        raise FileNotFoundError(f"Input file not found: {source}")
    with source.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing = REQUIRED_COLUMNS - columns
        if missing:
            raise DataValidationError(f"Missing required columns: {sorted(missing)}")
        return list(reader)
