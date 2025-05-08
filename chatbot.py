from bs4 import BeautifulSoup
import requests
import re

url = "https://metacoregames.com/careers"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

question = input("What jobs do you have available? ").lower()

# More comprehensive pattern to match job-related questions
job_pattern = re.compile(r"\b(jobs?|positions?|openings?|careers?|hiring|opportunities?|roles?)\b")

if job_pattern.search(question):
    found = True
    for link in doc.find_all("a", href=True):
        text = link.get_text(strip=True)
        href = link["href"]
        # Check if href contains job-related terms or points to open-positions
        if ("job" in href.lower() or 
            "position" in href.lower() or 
            "career" in href.lower() or
            "/open-positions/" in href.lower()):
            # Format the URL correctly
            print(f"{text}: {href}")
            found = True

    if not found:
        print("I couldn"t find any job openings, but feel free to check the career page here: https://metacoregames.com/careers")
else:
    print("Currently, I can only help with job openings")


#This below is the one that returns the positions
"""for link in doc.find_all("a", href=True):
    text = link.get_text(strip=True)
    href = link["href"]
    if "job" in href.lower() or "position" in href.lower():
        print(f"{text}: {href}")"""
