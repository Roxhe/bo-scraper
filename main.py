from pandas.core.frame import DataFrame
import requests
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas
import re
from functions import get_pages, urlparser, urlbooks, url_to_jpg

print("Work in progress, can take few minutes")
print("...")
url = "https://books.toscrape.com/index.html"
url_cat = "https://books.toscrape.com/catalogue/category/books_1/index.html"
req = requests.get(url)
soup = bs(req.content, "html.parser")

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
    upc_pext = []
    for upcpext in soup.find_all('td', class_=False):
        upc_pext.append(upcpext.string)
        
    universal_product_code.append(upc_pext[0])
    price_excluding_tax.append(upc_pext[2])
    title.append(soup.find("div", class_ ="product_main").h1.text)
    price_including_tax.append(soup.find("p", class_="price_color").text)
    number_available.append(re.sub("[^0-9]", "", soup.find("p", class_ = "instock availability").text))
    product_description.append((soup.find_all('p')[3]).spring)
    category.append((soup.find_all('a', href=True)[3]).string)
    review_rating.append(soup.find("p", class_ = re.compile("star-rating")).get("class")[1])
    image_url.append(url.replace("index.html", "") + soup.find("img").get("src"))
 
pd_image_url = pandas.DataFrame({'Images Url': image_url})
pd_image_url.to_csv(r"image_url.csv", index=False, header=True)

filename = "image_url.csv"
file_path = 'images/'

bookcover_url = pandas.read_csv(filename)

for i, url in enumerate(bookcover_url.values):
    url_to_jpg(i, url[0], file_path)

result = pandas.DataFrame({'title': title,'upc':universal_product_code,'price(£) including tax': price_including_tax,'price(£) excluding tax':price_excluding_tax,'number available':number_available, 'product description': product_description,'category': category,'review rating': review_rating,'image url' : image_url})
result.head()

result["category"].unique()

result_travel = result.query('category == "Travel"')
result_travel.to_csv(r"travel.csv", index=False, header=True)
result_mystery = result.query('category == "Mystery"')
result_mystery.to_csv(r"mystery.csv", index=False, header=True)
result_historical_fiction = result.query('category == "Historical Fiction"')
result_historical_fiction.to_csv(r"historical_fiction.csv", index=False, header=True)
result_sequential_art = result.query('category == "Sequential Art"')
result_sequential_art.to_csv(r"sequential_art.csv", index=False, header=True)
result_classics = result.query('category == "Classics"')
result_classics.to_csv(r"classics.csv", index=False, header=True)
result_philosophy = result.query('category == "Philosophy"')
result_philosophy.to_csv(r"philosophy.csv", index=False, header=True)
result_romance = result.query('category == "Romance"')
result_romance.to_csv(r"romance.csv", index=False, header=True)
result_womens_fictions = result.query('category == "Womens Fiction"')
result_womens_fictions.to_csv(r"womens_fiction.csv", index=False, header=True)
result_fiction = result.query('category == "Fiction"')
result_fiction.to_csv(r"fiction.csv", index=False, header=True)
result_childrens = result.query('category == "Childrens"')
result_childrens.to_csv(r"childrens.csv", index=False, header=True)
result_religion = result.query('category == "Religion"')
result_religion.to_csv(r"religion.csv", index=False, header=True)
result_nonfiction = result.query('category == "Nonfiction"')
result_nonfiction.to_csv(r"nonfiction.csv", index=False, header=True)
result_music = result.query('category == "Music"')
result_music.to_csv(r"music.csv", index=False, header=True)
result_default = result.query('category == "Default"')
result_default.to_csv(r"default.csv", index=False, header=True)
result_science_fiction = result.query('category == "Science Fiction"')
result_science_fiction.to_csv(r"science_fiction.csv", index=False, header=True)
result_sportsandgames = result.query('category == "Sports and Games"')
result_sportsandgames.to_csv(r"sportsandgames.csv", index=False, header=True)
result_add_a_comment = result.query('category == "Add a comment"')
result_add_a_comment.to_csv(r"add_a_comment.csv", index=False, header=True)
result_fantasy = result.query('category == "Fantasy"')
result_fantasy.to_csv(r"fantasy.csv", index=False, header=True)
result_new_adult = result.query('category == "New Adult"')
result_new_adult.to_csv(r"new_adult.csv", index=False, header=True)
result_youg_adult = result.query('category == "Youg Adult"')
result_youg_adult.to_csv(r"youg_adult.csv", index=False, header=True)
result_science = result.query('category == "Science"')
result_science.to_csv(r"science.csv", index=False, header=True)
result_poetry = result.query('category == "Poetry"')
result_poetry.to_csv(r"poetry.csv", index=False, header=True)
result_paranormal = result.query('category == "Paranormal"')
result_paranormal.to_csv(r"paranormal.csv", index=False, header=True)
result_art = result.query('category == "Art"')
result_art.to_csv(r"art.csv", index=False, header=True)
result_psychology = result.query('category == "Psychology"')
result_psychology.to_csv(r"psychology.csv", index=False, header=True)
result_autobiography = result.query('category == "Autobiography"')
result_autobiography.to_csv(r"autobiography.csv", index=False, header=True)
result_parenting = result.query('category == "Parenting"')
result_parenting.to_csv(r"parenting.csv", index=False, header=True)
result_adult_fiction = result.query('category == "Adult Fiction"')
result_adult_fiction.to_csv(r"adult_fiction.csv", index=False, header=True)
result_humor = result.query('category == "Humor"')
result_humor.to_csv(r"humor.csv", index=False, header=True)
result_horror = result.query('category == "Horror"')
result_horror.to_csv(r"horror.csv", index=False, header=True)
result_history = result.query('category == "History"')
result_history.to_csv(r"history.csv", index=False, header=True)
result_foodanddrink = result.query('category == "Food and Drink"')
result_foodanddrink.to_csv(r"food_and_drink.csv", index=False, header=True)
result_christian_fiction = result.query('category == "Christian Fiction"')
result_christian_fiction.to_csv(r"christian_fiction.csv", index=False, header=True)
result_business = result.query('category == "Business"')
result_business.to_csv(r"business.csv", index=False, header=True)
result_biography = result.query('category == "Biography"')
result_biography.to_csv(r"biography.csv", index=False, header=True)
result_thriller = result.query('category == "Thriller"')
result_thriller.to_csv(r"thriller.csv", index=False, header=True)
result_contemporary = result.query('category == "Contemporary"')
result_contemporary.to_csv(r"contemporary.csv", index=False, header=True)
result_spirituality = result.query('category == "Spirituality"')
result_spirituality.to_csv(r"spirituality.csv", index=False, header=True)
result_academic = result.query('category == "Academic"')
result_academic.to_csv(r"academic.csv", index=False, header=True)
result_self_help = result.query('category == "Self Help"')
result_self_help.to_csv(r"self_help.csv", index=False, header=True)
result_historical = result.query('category == "Historical"')
result_historical.to_csv(r"historical.csv", index=False, header=True)
result_christian = result.query('category == "Christian"')
result_christian.to_csv(r"christian.csv", index=False, header=True)
result_suspense = result.query('category == "Suspense"')
result_suspense.to_csv(r"suspense.csv", index=False, header=True)
result_short_stories = result.query('category == "Short Stories"')
result_short_stories.to_csv(r"short_stories.csv", index=False, header=True)
result_novels = result.query('category == "Novels"')
result_novels.to_csv(r"novels.csv", index=False, header=True)
result_health = result.query('category == "Health"')
result_health.to_csv(r"health.csv", index=False, header=True)
result_politics = result.query('category == "Politics"')
result_politics.to_csv(r"politics.csv", index=False, header=True)
result_cultural = result.query('category == "Cultural"')
result_cultural.to_csv(r"cultural.csv", index=False, header=True)
result_erotica = result.query('category == "Erotica"')
result_erotica.to_csv(r"erotica.csv", index=False, header=True)
result_crime = result.query('category == "Crime"')
result_crime.to_csv(r"crime.csv", index=False, header=True)

result.to_csv(r"books_all_data.csv", index=False, header=True)
print(result)