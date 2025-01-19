import requests
from bs4 import BeautifulSoup

url='https://tap.az/elanlar/neqliyyat/avtomobiller?keywords_source=typewritten&p%5B745%5D=3802&p%5B828%5D=4891'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}


response = requests.get(url, headers = headers)
print(response.status_code)


soup = BeautifulSoup(response.text, 'html.parser')

container = soup.find('div', class_ = 'js-endless-container')
products = container.find_all('div', class_ = 'products-i')

car = products[0]

name = car.find('div', class_ = 'products-name').text
print(name)

price = car.find('span', class_ = 'price-val').text
price_currency = car.find('span', class_ = 'price-cur').text
print('price: ' + price + ' ' + price_currency)




