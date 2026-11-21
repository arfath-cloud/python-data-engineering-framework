from etl_framework.pipeline import run_pipeline

def test_pipeline_writes_output(tmp_path):
    source = tmp_path / "input.csv"
    target = tmp_path / "out" / "clean.csv"
    source.write_text("order_id,customer_id,order_date,amount\nO-1,C-1,2026-01-01,10\n", encoding="utf-8")
    metrics = run_pipeline(source, target)
    assert metrics == {"records_read": 1, "records_written": 1}
    assert "10.00" in target.read_text(encoding="utf-8")
