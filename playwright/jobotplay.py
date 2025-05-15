#!/usr/bin/env python3

from playwright.sync_api import sync_playwright


def main():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://metacoregames.com/open-positions")
        page.wait_for_selector(".job-title")

        print("Here are the current job openings:\n ")

        for link in page.query_selector_all('a[href*="open-positions/"]'):
            text = link.inner_text().strip()
            href = link.get_attribute("href").replace("?duplicate=true", "").strip()
            split = text.split("\n")
            job = {
                "title": split[0].split(",")[0],
                "category": split[1],
                "location": split[2],
                "id": href,
                "url": f"www.metacoregames.com{href}",
            }

            print(f"{job["title"]}, {job['location']}: {job['url']}")


if __name__ == "__main__":
    main()
