# JoBot (Playwright Edition)

**JoBot** is a simple Python script that scrapes open positions from Finnish Game companies using [Playwright](https://playwright.dev/python/). Jobot launches a headless browser to accurately capture up to date information on job postings from company websites.

---

## 🚀 Features

- ✅ Uses a headless Chromium browser for accuracy  
- ✅ Waits for job listings to fully load before scraping  
- ✅ Cleans up noisy job titles and query parameters  
- ✅ Outputs job listings in a readable format
- ✅ Company list:
    - Metacore
    - Rovio
    - Supercell
    - Small Giant Games

---

## 🛠️ How to Use

### 1. Clone the repository

```bash
git clone https://github.com/makekop/joBot.git
cd playwright
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Playwright browser binaries

```bash
playwright install
```

### 4. Run the script

```bash
python3 jobotplay.py
```

---

## 📦 Requirements

-   Python 3.x
-   [Playwright](https://playwright.dev/python/)

All required packages are listed in `requirements.txt`.

---

## 🧭 Future Improvements

-   Add multi-company support

---

## 🪦 Legacy Version

A simpler version using `requests` and `BeautifulSoup` is available in the `legacy/` folder.

---

## 📄 License

[MIT License](https://mit-license.org/)
