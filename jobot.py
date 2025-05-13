#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests


def main():

    url = "https://metacoregames.com/open-positions"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    header_printed = False

    for link in doc.find_all("a", href=True):
        text = link.get_text(strip=True)
        href = link["href"].replace("?duplicate=true", "").strip()

        if "/open-positions/" in href.lower():
            cleaned_text = (
                text.replace("Helsinki", "")
                .replace("Berlin", "")
                .replace("Tech", "")
                .replace("Data & Analytics", "")
                .replace("New GamesMarketing", "")
                .replace("Merge", "")
                .replace(",", "")
                .replace("Art & Animation", "")
                .replace("Production", "")
                .replace("Product Management", "")
                .replace("PartnerPeople & Talent Acquisition", "")
                .replace("Marketing", "")
                .replace("General", "")
                .replace("Game Design", "")
                .replace("Mansion &", "")
                .replace("&", "")
                .strip()
            )

            if not header_printed:
                print("Here are the current job openings: ")
                header_printed = True

            print(f"{cleaned_text}: www.metacoregames.com{href}")


if __name__ == "__main__":
    main()
