#!/usr/bin/env python3

from playwright.sync_api import sync_playwright


def get_metacore_jobs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://metacoregames.com/open-positions")

        print("\nOpen Positions at Metacore:\n ")

        for link in page.query_selector_all('a[href*="open-positions/"]'):
            text = link.inner_text().strip()
            href = link.get_attribute("href").replace("?duplicate=true", "").strip()
            split = text.split("\n")
            job = {
                "title": split[0].split(",")[0],
                "category": split[1],
                "location": split[2],
                "id": href,
                "url": f"https://www.metacoregames.com{href}",
            }

            print(f"{job["title"]}: {job["url"]}")
        browser.close()


def get_rovio_jobs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.rovio.com/open-positions/")

        print("\nOpen Positions at Rovio:\n ")

        for link in page.query_selector_all('a[href*="open-positions/"]'):
            href = link.get_attribute("href").strip()
            if href.endswith("/open-positions/"):
                continue
            text = link.inner_text().strip()
            split = text.split(",")
            job = {"title": split[0], "url": href}

            print(f"{job['title']}: {job["url"]}")
        browser.close()


def get_supercell_jobs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://supercell.com/en/careers/")
        jobs = page.query_selector_all('li[data-test-id="open-position"]')

        print("\nOpen Positions at Supercell:\n")

        for job in jobs:
            title = job.query_selector(".Offers_title__y_jGJ").inner_text().strip()
            href = job.query_selector("a").get_attribute("href").strip()
            split = title.split(",")

            job = {
                "title": split[0],
                "url": f"https://www.supercell.com{href}",
            }

            print(f"{job["title"]}: {job["url"]}")
        browser.close()


def main():
    get_metacore_jobs()
    get_rovio_jobs()
    get_supercell_jobs()


if __name__ == "__main__":
    main()
