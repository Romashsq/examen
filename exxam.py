import requests
import fake_useragent
from bs4 import BeautifulSoup
url = 'https://allo.ua/ua/roboty-pylesosy/'

user = fake_useragent.UserAgent().random
print(user)
headers = {"user-agent":user}

response = requests.get(url, headers=headers)
#print(response.text)
soup = BeautifulSoup(response.text,"lxml")
#print(soup)
all_product = soup.find('div', class_='products-layout__container products-layout--grid')

product_list = all_product.find_all('div',class_='product-card')
#print(all_product)

for i in range(len(product_list)):
    product_title = product_list[i].find('a', class_='product-card__title')
    print(product_title.text)

    try:
        product_cost = product_list[i].find('div',class_="v-pb__old")
        price_list = product_list[i].find('div',class_="v-pb__cur")
        url_product = product_list[i].find("div", class_='product-card__content').url

        print(product_cost.text)
        print(product_title.text)
        print(price_list.text)
        print(url_product.text)

    except AttributeError:
        print("This item is out of stock")