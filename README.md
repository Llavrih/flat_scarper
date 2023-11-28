# Rental Listing Scraper and Responder

This Python project automates the process of checking for new rental listings on "huurwoningen.nl" and responding to them. It scrapes the website for new rental ads and automatically fills a response form for each new listing found.

## How It Works

The script has several key components:
- `check_new_ads(url)`: Scrapes the specified URL for new rental listings and checks if they've been seen before.
- `perform_action_on_ad(ad_details)`: Opens a browser using Selenium, navigates to the ad's contact page, and fills out a response form.
- `main()`: The main loop of the script, which repeatedly checks for new ads and responds to each one.

## Dependencies

- Python 3
- `requests` and `bs4` (BeautifulSoup) for web scraping.
- Selenium WebDriver for browser automation.
- Firefox and geckodriver (or any other preferred browser and its WebDriver).

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    ```
2. Install required Python packages:
    ```bash
    pip install requests bs4 selenium
    ```
3. Download and set up [geckodriver](https://github.com/mozilla/geckodriver/releases) (or WebDriver for your chosen browser).

## Running the Script

Navigate to the script's directory and run:
```bash
python script.py
