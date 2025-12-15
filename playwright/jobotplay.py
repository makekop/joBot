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


from playwright.sync_api import sync_playwright


def get_supercell_jobs():
    IGNORE_PATHS = {
        "/en/careers",
        "/en/careers/living-helsinki/",
        "/en/careers/our-culture/",
        "/en/careers/benefits/",
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(
            "https://supercell.com/en/careers/?location=helsinki",
            wait_until="networkidle",
        )

        print("\nOpen Positions at Supercell (Helsinki):\n")
        for link in page.query_selector_all('a[href^="/en/careers/"]'):
            href = link.get_attribute("href")
            if not href:
                continue
            href = href.rstrip("/") + "/"
            if href in IGNORE_PATHS:
                continue
            text = link.inner_text().strip()
            if not text:
                continue
            if "helsinki" not in text.lower():
                continue
            title = text.split("\n")[0]
            print(f"{title}: https://supercell.com{href}")


def get_smallgiantgames_jobs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://job-boards.greenhouse.io/sggcareers")

        print("\nOpen Positions at Small Giant Games:\n ")

        for link in page.query_selector_all('a[href*="jobs/"]'):
            href = link.get_attribute("href").strip()
            text = link.inner_text().strip()
            title = text.split("\n")[0].strip()

            job = {
                "title": title,
                "url": (
                    href
                    if href.startswith("http")
                    else f"https://job-boards.greenhouse.io{href}"
                ),
            }
            print(f"{job["title"]}: {job["url"]}")
        browser.close()


def main():
    get_metacore_jobs()
    get_rovio_jobs()
    get_supercell_jobs()
    get_smallgiantgames_jobs()
    pass


if __name__ == "__main__":
    main()
