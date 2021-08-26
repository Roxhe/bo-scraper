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
    """ Description of what get_pages does.
    
    Args :
        sample_pages (str): base of the url that will be copied to create the list.
        nb(int) = number of loop executions.
        
    Returns :
        list: list containing your created urls from the base."""
    pages = []
    for i in range(1,nb+1):
        j = sample_page + str(i) + ".html"
        pages.append(j)
    return pages
pages = get_pages(sample_page,50)
del pages[0]
pages.insert(0, url)
print(pages)

#add-categories-pages
page_default1 = "https://books.toscrape.com/catalogue/category/books/default_15/index"
sample_page_default = "https://books.toscrape.com/catalogue/category/books/default_15/page-"
get_pages(sample_page_default, nb=2)
sample_page_default = get_pages(sample_page_default,8)
del sample_page_default[0]
sample_page_default.insert(0, page_default1)
print(sample_page_default)

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
