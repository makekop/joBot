from link_handlers import (
    metacoreGamesLinkHandler,
    rovioLinkHandler,
    supercellLinkHandler,
)

companies = [
    {
        "name": "Metacore",
        "url": "https://metacoregames.com/open-positions",
        "querySelector": 'a[href*="open-positions/"]',
        "linkHandler": metacoreGamesLinkHandler,
    },
    {
        "name": "Rovio",
        "url": "https://rovio.com/open-positions",
        "querySelector": 'a[href*="open-positions/"]',
        "linkHandler": rovioLinkHandler,
    },
    {
        "name": "Supercell",
        "url": "https://supercell.com/en/careers/",
        "querySelector": 'li[data-test-id="open-position"]',
        "linkHandler": supercellLinkHandler,
    },
]
