import re
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

seen_ads = set()


def check_new_ads(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    listings = soup.find_all(
        "li", class_="search-list__item search-list__item--listing"
    )
    new_ads = []
    for listing in listings:
        title_element = listing.find("div", class_="listing-search-item__sub-title'")
        price_element = listing.find("div", class_="listing-search-item__price")

        title = title_element.get_text(strip=True) if title_element else None
        price_text = price_element.get_text(strip=True) if price_element else None
        price = "".join(re.findall(r"\d+", price_text)) if price_text else None

        link = listing.find("a")["href"] if listing.find("a") else None

        if link and link not in seen_ads:
            parts = link.split("/")
            for i, part in enumerate(parts):
                if part.isdigit():  # Check if the part is a number
                    number_index = i
                    break

            # Reconstruct the link by skipping the segment following the number
            modified_link = "/".join(
                parts[: number_index + 1] + parts[number_index + 2 :]
            )
            modified_link = (
                modified_link.replace("/huren/", "/contact/") + "nieuwstraat/vraag/"
            )

            ad_details = {"title": title, "price": price, "link": modified_link}
            new_ads.append(ad_details)
            seen_ads.add(link)  # Add the original link to seen ads

    return new_ads


def is_ad_already_stored(link):
    return link in seen_ads


def perform_action_on_ad(ad_details):
    # Path to your geckodriver executable
    geckodriver_path = r"C:\Users\gecko\geckodriver.exe"  # Update this path
    # Path to your Firefox executable
    firefox_binary_path = (
        r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Update this path
    )

    # Set up Firefox options with the binary location
    firefox_options = Options()
    firefox_options.binary_location = firefox_binary_path

    # Initialize the WebDriver for Firefox
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service, options=firefox_options)

    # Open the URL
    driver.get("https://www.huurwoningen.nl" + ad_details["link"])

    input("Press Enter after the page has loaded and you're ready to proceed.")

    # Wait for the page to load
    textarea = driver.find_element(By.ID, "listing_reaction_message_message")
    textarea.clear()

    # The message to input
    message = """
    Hello
    """

    # Input the message into the textarea
    textarea.send_keys(message)

    input("Review the entered information and press Enter to close the browser.")

    # Close the browser window
    driver.quit()


def main():
    while True:
        new_ads = check_new_ads(
            "https://www.huurwoningen.nl/in/amsterdam/?price=0-1000&since=1"
        )
        for ad in new_ads:
            perform_action_on_ad(ad)
            print(new_ads)

        time.sleep(1)


if __name__ == "__main__":
    main()
