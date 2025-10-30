from common import handleLinks, visit
from playwright.sync_api import sync_playwright
from config import companies


def handle_company(c):

    print("\n\n***********************************************************************")
    print("Open Positions at:" + c["name"], end="\n\n")

    with sync_playwright() as p:

        page = visit(p, c["url"])

        handleLinks(page, c["querySelector"], c["linkHandler"])

        page.close()


# Suoritetaan ohjelma

for c in companies:
    handle_company(c)
