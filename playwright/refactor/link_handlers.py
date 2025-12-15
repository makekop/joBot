def rovioLinkHandler(link):
    href = link.get_attribute("href").strip()

    if href.endswith("/open-positions/"):
        return None

    text = link.inner_text().strip()
    split = text.split(",")
    job = {"title": split[0], "url": href}

    return job


def metacoreGamesLinkHandler(link):
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

    return job


def supercellLinkHandler(link):
    title = link.query_selector(".Offers_title__y_jGJ").inner_text().strip()
    href = link.query_selector("a").get_attribute("href").strip()
    split = title.split(",")

    job = {
        "title": split[0],
        "url": f"https://www.supercell.com{href}",
    }

    print(f"{job["title"]}: {job["url"]}")


def supercellLinkHandler(link):
    title = link.query_selector(".Offers_title__y_jGJ").inner_text().strip()
    href = link.query_selector("a").get_attribute("href").strip()
    split = title.split(",")

    job = {
        "title": split[0],
        "url": f"https://www.supercell.com{href}",
    }

    print(f"{job["title"]}: {job["url"]}")
