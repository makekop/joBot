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
            parts = [p.strip() for p in text.split(",")]
            job_title = parts[0]
            print(job_title)  # printing to see the result

            if not header_printed:
                print("Here are the current job openings: ")
                header_printed = True

            # print(f"{job_title}: www.metacoregames.com{href}")


if __name__ == "__main__":
    main()
