# Quote Scraper 

This Python script demonstrates web scraping using `requests` and `BeautifulSoup` libraries to extract quotes and authors from a website (`http://quotes.toscrape.com`) across multiple pages. It also integrates with SQLite to store the extracted data in a local database (`quotes.db`).

## Features
- Scrapes quotes and authors from `http://quotes.toscrape.com`.
- Parses multiple pages of quotes (default: 5 pages).
- Stores quotes and authors into an SQLite database (`quotes.db`).

## Setup

1. **Install Dependencies**
   - Ensure Python 3.x is installed on your system.
   - Install required libraries using pip:
