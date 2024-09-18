# Selenium Indeed Web Scraper

This project is a web scraper built using Python 3.9, Selenium, and ChromeDriver. It is designed to extract job data from **Indeed.com**.

## Prerequisites

- Python 3.9 or higher
- Selenium
- ChromeDriver
- Webdriver Manager for automatic ChromeDriver installation

## Installation

1. Clone this repository or download the script.
2. Install the required Python libraries:

   ```bash
   pip install selenium webdriver-manager
   ```

3. Ensure you have Chrome browser installed.

## Usage

1. Run the Python script:

   ```bash
   python Selenium_Indeed.py
   ```

2. The script will launch a Chrome browser instance and start scraping data from **Indeed.com**.

## Features

- Automatically downloads the latest version of ChromeDriver using `webdriver-manager`.
- Uses Selenium to navigate **Indeed.com** and scrape job information.
- Includes logging to track the scraping process.

## Customization

You can modify the script to scrape different job titles, locations, or other data by changing the search queries and XPaths in the script.

## License

This project does not have a specific license.
