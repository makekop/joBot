# JoBot

JoBot is a simple Python script that scrapes the current job openings from the [Metacore Careers page](https://metacoregames.com/careers) and prints them to the command line. You can copy this code and edit it to a company website of your liking.

## Features

✅ Fetches live job openings using a GET request  
✅ Removes unnecessary text and query parameters (e.g., `?duplicate=true`)  
✅ Displays a clean and readable list of jobs in the terminal

## How to Use

1. Clone the repository:

```

git clone https://github.com/makekop/joBot.git

```

2. Navigate into the project folder:

```

cd joBot

```

3. Install required dependencies:

```

pip install -r requirements.txt

```

4. Run the script:

```

python3 jobot.py

```

## Requirements

-   Python 3.x
-   BeautifulSoup4
-   requests

## Future Improvements

-   Add notification when new jobs appear
-   Save and compare job data between runs
-   Support email, Slack, or desktop notifications

## License

MIT License

⚠ DISCLAIMER:
This script uses BeautifulSoup, which only parses static HTML.
It does NOT execute or render JavaScript on the page.
If the website uses JavaScript to load or update data dynamically,
the script may miss important content.
For such cases, consider using a browser automation tool like Playwright or Selenium.
I'm currently working on playwright version in this same branch.
