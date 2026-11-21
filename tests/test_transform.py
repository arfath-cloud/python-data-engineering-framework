import pytest
from etl_framework.transform import transform_record
from etl_framework.exceptions import DataValidationError

def test_transform_normalizes_amount():
    result = transform_record({"order_id":" O-1 ","customer_id":" C-1 ","order_date":"2026-01-01","amount":"12.5"})
    assert result["order_id"] == "O-1"
    assert result["amount"] == "12.50"

def test_transform_rejects_negative_amount():
    with pytest.raises(DataValidationError):
        transform_record({"order_id":"O-2","customer_id":"C-2","order_date":"2026-01-01","amount":"-1"})
