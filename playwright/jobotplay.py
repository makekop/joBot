#!/usr/bin/env python3

from playwright.sync_api import sync_playwright


def main():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://metacoregames.com/open-positions")
        page.wait_for_selector(".job-title")

        header_printed = False

        for link in page.query_selector_all('a[href*="open-positions/"]'):
            text = link.inner_text().strip()
            href = link.get_attribute("href").replace("?duplicate=true", "").strip()
            parts = text.split("\n")
            job_title = parts

            if not header_printed:
                print("Here are the current job openings:\n ")
                header_printed = True

            print(f"{job_title[0]}: www.metacoregames.com{href}")


if __name__ == "__main__":
    main()
