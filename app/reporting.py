
import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Any

from app.config import CITIES


def save_pipeline_outputs(
    weather_data: list[dict[str, Any]],
    failed_cities: list[dict[str, str]],
    analytics: dict[str, Any],
    output_dir: Path = Path("outputs")
) -> tuple[Path, Path]:

    output_dir.mkdir(exist_ok=True)

    total_cities: int = len(CITIES)
    successful: int = len(weather_data)
    failed: int = len(failed_cities)

    if failed == 0:
        status: str = "SUCCESS"
    elif successful > 0:
        status = "PARTIAL SUCCESS"
    else:
        status = "FAILED"

    generated_at: str = datetime.now(timezone.utc).isoformat()

    output: dict[str, Any] = {
        "generated_at": generated_at,
        "status": status,
        "collection_summary": {
            "total_cities": total_cities,
            "successful": successful,
            "failed": failed
        },
        "weather_data": weather_data,
        "analytics": analytics,
        "failed_cities": failed_cities
    }

    json_path: Path = output_dir / "weather_output.json"

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(output, file, indent=4)

    report_path: Path = output_dir / "validation_report.txt"

    with open(report_path, "w", encoding="utf-8") as file:
        file.write("WEATHER PIPELINE VALIDATION REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Generated: {generated_at}\n")
        file.write(f"Status: {status}\n")
        file.write(f"Expected cities: {total_cities}\n")
        file.write(f"Successful collections: {successful}\n")
        file.write(f"Failed collections: {failed}\n")

        if failed_cities:
            file.write("\nFAILED CITIES:\n")

            for failure in failed_cities:
                file.write(
                    f"- {failure['city']}: {failure['error']}\n"
                )

    return json_path, report_path
