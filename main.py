import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="weather_toolkit.log",
    filemode="a"
)
logging.getLogger("httpx").setLevel(logging.WARNING)

from app.collector import fetch_all_weather
from app.analytics import (
    generate_weather_analytics,
    display_weather_report
)
from app.reporting import save_pipeline_outputs


async def main():

    logging.info("Weather Automation Toolkit started")

    weather_data, failed_cities = await fetch_all_weather()

    logging.info(
        f"Weather collection completed. "
        f"Successful: {len(weather_data)}, Failed: {len(failed_cities)}"
    )

    if not weather_data:
        logging.error("Weather collection failed for all cities. No data available.")

    logging.info("Starting weather analytics generation")

    analytics = generate_weather_analytics(weather_data)

    json_path, report_path = save_pipeline_outputs(
    weather_data,
    failed_cities,
    analytics
    )

    logging.info(f"Output saved to {json_path}")
    logging.info(f"Validation report saved to {report_path}")

    print(f"\nOutput saved: {json_path}")
    print(f"Validation report saved: {report_path}")

    logging.info("Weather analytics generation completed")

    for failure in failed_cities:
        logging.warning(
            f"Weather collection failed for {failure['city']}: {failure['error']}"
        )

    logging.info("Generating weather analytics report")

    display_weather_report(analytics)

    logging.info("Weather analytics report displayed")


if __name__ == "__main__":
    asyncio.run(main())