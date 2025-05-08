#!/usr/bin/env python3

def main():
    from bs4 import BeautifulSoup
    import requests

    url = "https://metacoregames.com/careers"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    question = "job"


    header_printed = False
    found = False

    for link in doc.find_all("a", href=True):
        text = link.get_text(strip=True)
        href = link["href"].replace("?duplicate=true", "").strip()

        if ("/open-positions/" in href.lower()):
            cleaned_text = text.replace("Helsinki", "").replace("Tech", "").replace("Data & Analytics", "").replace("New GamesMarketing", "").replace("Merge MansionProduct Management & Berlin", "").replace(",", "").strip()
            if not header_printed:
                print(f"Here are the current job openings: " )
                header_printed = True
            
            print(f"{cleaned_text}: www.metacoregames.com{href}")
            found = True
if __name__ == "__main__":
    main()