from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup as bs
import pandas
from functions import get_pages, urlbooks, url_to_jpg, books_data_parse

print("Work in progress, can take few minutes")
print("...")
url = "https://books.toscrape.com/index.html"
req = requests.get(url)
soup = bs(req.content, "html.parser")

pages = get_pages("http://books.toscrape.com/catalogue/category/books_1/page-",50)
pages
del pages[0]
pages.insert(0, url)

url_allbooks = []
for page in pages:
    url_allbooks.extend(urlbooks(page))

books_data_funct = books_data_parse(url_allbooks, url)

result = pandas.DataFrame.from_dict(books_data_funct)
result.head()


pd_image_url = pandas.DataFrame({'Images Url': books_data_funct.get('image_url')})
pd_image_url.to_csv(r"image_url.csv", index=False, header=True)

filename = "image_url.csv"
file_path = 'images/'

bookcover_url = pandas.read_csv(filename)

for i, url in enumerate(bookcover_url.values):
    url_to_jpg(i, url[0], file_path)


list_category = result["category"].unique()

for cat in list_category:
    result_travel = result.query(f'category == "{cat}"')
    result_travel.to_csv(f"{cat}.csv", index=False, header=True)

result.to_csv(r"books_all_data.csv", index=False, header=True)