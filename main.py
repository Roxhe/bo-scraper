import requests
from bs4 import BeautifulSoup as bs
import pandas
import re
from progress.bar import Bar
from scripts import get_pages, urlparser, urlbooks

print("Work in progress, can take few minutes")
print("...")
url = "https://books.toscrape.com/index.html"
url_cat = "https://books.toscrape.com/catalogue/category/books_1/index.html"
req = requests.get(url)
soup = bs(req.text, "html.parser")

categories_urls = [url_cat + x.get('href') for x in soup.find_all("a", href=re.compile("catalogue/category/books"))]
categories_urls = categories_urls[1:]

pages = get_pages("http://books.toscrape.com/catalogue/category/books_1/page-",50)
pages
del pages[0]
pages.insert(0, url)


url_allbooks = []
for page in pages:
    url_allbooks.extend(urlbooks(page))

universal_product_code = []
title = []
price_including_tax = []
price_excluding_tax = []
number_available = []
product_description = []
category = []
review_rating = []
image_url = []


for url in url_allbooks:
    soup = urlparser(url)
    universal_product_code.append(soup.find("tbody", class_ = "table table-striped"))
    title.append(soup.find("div", class_ ="product_main").h1.text)
    price_including_tax.append(soup.find("p", class_="price_color").text[1:])
    price_excluding_tax.append
    number_available.append(re.sub("[^0-9]", "", soup.find("p", class_ = "instock availability").text))
    product_description.append((soup.find_all('p')[3]).string)
    category.append((soup.find_all('a', href=True)[3]).string)
    review_rating.append(soup.find("p", class_ = re.compile("star-rating")).get("class")[1])
    image_url.append(url.replace("index.html", "") + soup.find("img").get("src"))




result = pandas.DataFrame({'title': title,'price including tax': price_including_tax,'number available':number_available, 'product description': product_description,'category': category,'review rating': review_rating,'image url' : image_url})
result.head()

result.to_csv (r"C:\Users\leoda\Desktop\books_data.csv", index= False, header= True)
print(result)