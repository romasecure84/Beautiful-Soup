import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/index.html'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

page_count_string = soup.find('li', class_ = 'current').text
page_count = int(page_count_string.strip().split(' ')[-1])

for page in range(1, page_count + 1):
    print(f'page = {page}')
    page_url = f'https://books.toscrape.com/catalogue/page-{page}.html'
    response = requests.get(page_url)
    page_html = response.text
    soup = BeautifulSoup(page_html, 'html.parser')
    books = soup.find_all('article', class_ = 'product_pod')
    print(len(books))

# page_no = 45
# while True:
#     print(f'page = {page_no}')
#     page_url = f'https://books.toscrape.com/catalogue/page-{page_no}.html'
#     response = requests.get(page_url)
#     page_html = response.text
#     soup = BeautifulSoup(page_html, 'html.parser')
#     books = soup.find_all('article', class_='product_pod')
#     print(len(books))
#
#     next_button = soup.find('li', class_ = 'next')
#     if next_button is None:
#         break
#     else:
#         page_no += 1