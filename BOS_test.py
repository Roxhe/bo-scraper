import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/index.html"

response = requests.get(url)

if response.ok:
    books_links = []
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.findAll("article")
    for article in books:
        a = article.find("a")
        link = a["href"]
        books_links.append("https://books.toscrape.com/" + link)

    print(books_links)
    
    