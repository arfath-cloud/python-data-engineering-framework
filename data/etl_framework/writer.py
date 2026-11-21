import csv
from pathlib import Path

FIELDNAMES = ["order_id", "customer_id", "order_date", "amount"]

def write_csv(records: list[dict[str, str]], path: str | Path) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(records)
