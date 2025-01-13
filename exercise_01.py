import  requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')

first_element = soup.find('div', class_ = 'quote')
first_quote = first_element.span.text
print(first_quote)

first_author = first_element.small.text
print(first_author)


tags = first_element.find_all('a', class_ = 'tag')
for tag in tags:
    print(tag.text)

quotes = soup.find_all('div', class_ = 'quote')
print('List of elements: ' , len(quotes))

for quote in quotes:
    print(quote.span.text)
    print(quote.small.text)
    tags = quote.find_all('a', class_ = 'tag')
    for tag in tags:
        print(tag.text)
    print('\n')

for page in range(1, 11):
    print(f'page = {page}')
    page_url = f'https://quotes.toscrape.com/page/{page}/'
    response = requests.get(page_url)
    page_html = response.text
    soup = BeautifulSoup(page_html, 'html.parser')
    first_element = soup.find('div', class_='quote')
    first_author = first_element.small.text
    print(first_author)

