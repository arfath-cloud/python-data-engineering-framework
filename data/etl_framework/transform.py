from decimal import Decimal, InvalidOperation
from .exceptions import DataValidationError

def transform_record(record: dict[str, str]) -> dict[str, str]:
    """Normalize fields and reject invalid amounts or missing identifiers."""
    order_id = record["order_id"].strip()
    customer_id = record["customer_id"].strip()
    if not order_id or not customer_id:
        raise DataValidationError("order_id and customer_id must not be blank")
    try:
        amount = Decimal(record["amount"].strip()).quantize(Decimal("0.01"))
    except (InvalidOperation, AttributeError) as exc:
        raise DataValidationError(f"Invalid amount for order {order_id}") from exc
    if amount < 0:
        raise DataValidationError(f"Negative amount for order {order_id}")
    return {
        "order_id": order_id,
        "customer_id": customer_id,
        "order_date": record["order_date"].strip(),
        "amount": f"{amount:.2f}",
    }

def transform_records(records: list[dict[str, str]]) -> list[dict[str, str]]:
    return [transform_record(row) for row in records]
