import requests
from bs4 import BeautifulSoup as bs
import pandas
import re
from scripts import get_pages, urlparser, urlbooks


url = "https://books.toscrape.com/index.html"
url_cat = "https://books.toscrape.com/catalogue/category/books_1/index.html"
req = requests.get(url)
soup = bs(req.text, "html.parser")

print(urlbooks(url))

print("\n")

categories_urls = [url_cat + x.get('href') for x in soup.find_all("a", href=re.compile("catalogue/category/books"))]
categories_urls = categories_urls[1:]
print(categories_urls)

print("\n")

pages = get_pages("http://books.toscrape.com/catalogue/category/books_1/page-",50)
pages
del pages[0]
pages.insert(0, url)
print (pages)

url_allbooks = []
for page in pages:
    url_allbooks.extend(urlbooks(page))


print("\n")
print(url_allbooks)
