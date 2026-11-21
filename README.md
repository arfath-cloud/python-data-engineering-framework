# Project 03 — Python Data Engineering Framework

A small, reusable batch ETL framework that reads CSV files, validates required fields, standardizes data, writes clean output, and records run metrics.

## Requirements
- Python 3.10+
- Install: `pip install -r requirements.txt`
- Run: `python -m etl_framework.cli --input data/orders.csv --output output/orders_clean.csv`
- Test: `pytest -q`

## Concepts demonstrated
Modules and packages, functions, classes, custom exceptions, loops, comprehensions, type hints, logging, CLI arguments, CSV processing, and pytest.

All input data is synthetic. The framework uses Python's standard library; pytest is used for tests.
