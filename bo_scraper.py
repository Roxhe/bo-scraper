import requests
from bs4 import BeautifulSoup
import csv

#website-setup
url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
page = requests.get(url) 
soup = BeautifulSoup(page.content, 'html.parser')

#add-all-pages
sample_page = "http://books.toscrape.com/catalogue/category/books_1/page-"

def get_pages(sample_page, nb):
    pages = []
    for i in range(1,nb+1):
        j = sample_page + str(i) + ".html"
        pages.append(j)
    return pages
pages = get_pages(sample_page,20)
del pages[0]
pages.insert(0, url)
print(pages)

#book-titles
class_name_titles = "product_pod"
titles = soup.find_all("h3")
for title in titles:
    print(title.string)

#transformed-titles
titles_string = []
for title in titles:
    titles_string.append(title.string)
print(titles_string)

#data.csv-setup
heading = ["title"]
with open('data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(heading)
    for book_titles in zip(titles_string):
        writer.writerow([book_titles])
