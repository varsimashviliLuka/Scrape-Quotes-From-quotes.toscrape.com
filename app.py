import requests
from bs4 import BeautifulSoup
import sqlite3
from time import sleep

conn = sqlite3.connect('quotes.db')
curs = conn.cursor()

curs.execute("CREATE TABLE IF NOT EXISTS quotes(quote TEXT, author TEXT)")
conn.commit()


def parse_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')


    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    for quote, author in zip(quotes, authors):
        curs.execute("INSERT INTO quotes(quote,author) VALUES (?,?)", (quote.text,author.text))
        conn.commit()
        print(f"Quote: {quote.text}")
        print(f"Author: {author.text}")
        print("=" * 40)


def parse_website(base_url, num_pages):
    for page_num in range(1, num_pages + 1):
        url = f"{base_url}/page/{page_num}"
        parse_page(url)
        sleep(5)


if __name__ == "__main__":
    base_url = 'http://quotes.toscrape.com'
    num_pages = 5

    parse_website(base_url, num_pages)
