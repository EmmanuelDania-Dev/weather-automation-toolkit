# Weather Automation Toolkit

An asynchronous Python application that collects current weather data from multiple cities using the [Open-Meteo API](https://open-meteo.com/), processes the collected data, generates analytics, and saves structured output reports.

## Features

- **Asynchronous data collection:** Fetches weather information from multiple cities using `httpx.AsyncClient`.
- **Automatic retries:** Retries failed API requests up to three times.
- **Concurrent execution:** Collects weather data from multiple cities using `asyncio.gather()`.
- **Weather analytics:** Calculates average temperature, average humidity, total precipitation, and identifies the hottest and coldest cities.
- **Failure handling:** Tracks unsuccessful city requests without stopping the entire collection process.
- **Logging:** Records application events, collection results, and errors.
- **Output generation:** Exports collected data and analytics to JSON.
- **Validation reporting:** Generates a text report summarising pipeline execution.
- **Automated testing:** Uses pytest, including asynchronous tests and mocking.

## Technologies Used

- Python
- asyncio
- HTTPX
- pytest
- pytest-asyncio
- unittest.mock
- JSON

## Project Structure

```text
weather-automation-toolkit/
├── app/
│   ├── __init__.py
│   ├── collector.py
│   ├── analytics.py
│   ├── config.py
│   └── reporting.py
├── tests/
│   ├── test_analytics.py
│   ├── test_collector.py
│   └── test_reporting.py
├── outputs/
│   ├── weather_output.json
│   └── validation_report.txt
├── main.py
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/EmmanuelDania-Dev/weather-automation-toolkit.git
cd weather-automation-toolkit
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the pipeline from the project root:

```bash
python main.py
```

The application collects weather data, generates analytics, displays a report, and saves its output files.

## Output Files

### `outputs/weather_output.json`

Contains:
- Generation timestamp
- Pipeline execution status
- Collection summary
- Successfully collected weather data
- Weather analytics
- Failed city requests

### `outputs/validation_report.txt`

Contains:
- Pipeline execution status
- Expected number of cities
- Successful collection count
- Failed collection count
- Details of unsuccessful requests

### `weather_toolkit.log`

Records application activity, including startup, collection results, analytics generation, and failures.

## Running Tests

Run the automated test suite:

```bash
python -m pytest -v
```

The test suite covers:

- Weather analytics calculations
- Empty-data handling
- Weather report output
- Successful API requests
- Retry behaviour
- Complete request failure
- Partial collection failures
- JSON output generation
- Validation report generation

## Weather Data Source

Weather information is retrieved from the [Open-Meteo API](https://open-meteo.com/).

The configured locations include Lagos, London, New York, Tokyo, and Nairobi.

## Demo Recording

This is the demo recording of the toolkit running successfully:

https://drive.google.com/file/d/1d8mWMEQruj2FMM_qDyDvYOgaR_c5xV-0/view?usp=sharing

## Author

**Emmanuel Dania**

[GitHub Profile](https://github.com/EmmanuelDania-Dev)