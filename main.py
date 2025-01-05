import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find('title').text
print(title)