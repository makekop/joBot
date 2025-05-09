#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from playwright.sync_api import sync_playwright


def main():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://metacoregames.com/open-positions")
        page.wait_for_selector(".job-title")
        content = page.content()
        browser.close()

    doc = BeautifulSoup(content, "html.parser")

    header_printed = False

    for link in doc.find_all("a", href=True):
        text = link.get_text(strip=True)
        href = link["href"].replace("?duplicate=true", "").strip()

        if "/open-positions/" in href.lower():
            cleaned_text = (
                text.replace("Helsinki", "")
                .replace("Tech", "")
                .replace("Data & Analytics", "")
                .replace("New GamesMarketing", "")
                .replace("Merge MansionProduct Management & Berlin", "")
                .replace(",", "")
                .replace("People & Talent AcquisitionBerlin", "")
                .replace("Production", "")
                .replace("General", "")
                .replace("Game Design", "")
                .replace("Berlin", "")
                .replace("Art & Animation", "")
                .replace("Product Management &", "")
                .strip()
            )
            if not header_printed:
                print("Here are the current job openings: ")
                header_printed = True

            print(f"{cleaned_text}: www.metacoregames.com{href}")


if __name__ == "__main__":
    main()
