
import json

from app.reporting import save_pipeline_outputs


def test_save_pipeline_outputs(tmp_path):

    weather_data = [
        {
            "city": "Lagos",
            "current": {
                "temperature_2m": 30
            }
        }
    ]

    failed_cities = []

    analytics = {
        "average_temperature": 30,
        "hottest_city": "Lagos"
    }

    json_path, report_path = save_pipeline_outputs(
        weather_data,
        failed_cities,
        analytics,
        tmp_path
    )

    assert json_path.exists()
    assert report_path.exists()

    with open(json_path, encoding="utf-8") as file:
        output = json.load(file)

    assert output["status"] == "SUCCESS"
    assert output["collection_summary"]["successful"] == 1
    assert output["analytics"]["average_temperature"] == 30


def test_validation_report_contains_failure(tmp_path):

    weather_data = []

    failed_cities = [
        {
            "city": "London",
            "error": "Connection failed"
        }
    ]

    analytics = {}

    json_path, report_path = save_pipeline_outputs(
        weather_data,
        failed_cities,
        analytics,
        tmp_path
    )

    with open(report_path, encoding="utf-8") as file:
        report = file.read()

    assert "FAILED" in report
    assert "London" in report
    assert "Connection failed" in report
