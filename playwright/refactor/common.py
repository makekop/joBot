def visit(p, url):
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    print("Visiting: " + url)
    page.goto(url)

    return page


def handleLinks(page, querySelector, handlerFunktio):
    jobs = []

    # loopataan linkit
    for link in page.query_selector_all(querySelector):

        # loopin sisällä
        job = handlerFunktio(link)
        if job == None:
            continue

        jobs.append(job)
        printJob(job)

    # seuraava askel, ..ei mitään?

    return jobs


def printJob(job):
    print(f"{job["title"]}: {job["url"]}")
