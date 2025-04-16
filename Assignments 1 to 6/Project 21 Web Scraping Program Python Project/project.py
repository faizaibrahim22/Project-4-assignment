import requests
from bs4 import BeautifulSoup

URL = "http://quotes.toscrape.com"

response = requests.get(URL)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        print(f'"{text}" — {author}')
else:
    print("Failed to retrieve data")
