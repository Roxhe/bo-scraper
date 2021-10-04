import requests
from bs4 import BeautifulSoup as bs
import urllib.request
import re

def get_pages(sample_url, nb):
    """ 
    Args :
        sample_url (str): base of the url that will be copied to create the list.
        nb(int) = number of loop executions.
        
    Returns :
        list: list containing your created urls from the base."""
    pages = []
    for i in range(1,nb+1):
        j = sample_url + str(i) + ".html"
        pages.append(j)
    return pages

def urlparser(url):
    """
    Args :
        url (str): url you want to parse.
    
    Returns :
        soup: html code from the url arg."""
    req = requests.get(url)
    soup = bs(req.content, "html.parser")
    return soup


def urlbooks(url):
    """ 
    Args :
        url (str): page where are the books whose you want urls.
        
    Returns : list contained all the books url of one page"""
    soup = urlparser(url)
    return(["/".join(url.split("/")[:-1]) + "/" + x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")])


def url_to_jpg(i, url, file_path):
    """
    Args :
        i : number of image to download.
        url : url adress of one image
        file_path : file where the image will be save"""
    filename = 'image-{}.jpg'.format(i)
    full_path= '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)

    print('{} saved'.format(filename))
    
    return None

def books_data_parse(url_allbooks, url):
    """
    Args :
        url_allbooks (list) : all the books urls to scrape all the data
        url (str) : url used to parse
        
    Return : 
        books_data_dict (dict) : dictionary with all data from all books"""
    urlparser(url)

    universal_product_code = []
    title = []
    price_including_tax = []
    price_excluding_tax = []
    number_available = []
    product_description = []
    category = []
    review_rating = []
    image_url = []

    books_data_dict = {
    'universal_product_code' : universal_product_code,
    'title' : title,
    'price_including_tax' : price_including_tax,
    'price_excluding_tax' : price_excluding_tax,
    'number_available' : number_available,
    'product_description' : product_description,
    'category' : category,
    'review_rating' : review_rating,
    'image_url' : image_url
    }
    for url in url_allbooks:
        soup = urlparser(url)
        upc_pext = []
        
        for upcpext in soup.find_all('td', class_=False):
            upc_pext.append(upcpext.string)    

        title.append(soup.find("div", class_ ="product_main").h1.text)
        price_including_tax.append(soup.find("p", class_="price_color").text)
        number_available.append(re.sub("[^0-9]", "", soup.find("p", class_ = "instock availability").text))
        product_description.append((soup.find_all('p')[3]).string)
        category.append((soup.find_all('a', href=True)[3]).string)
        review_rating.append(soup.find("p", class_ = re.compile("star-rating")).get("class")[1])
        image_url.append(url.replace("index.html", "") + soup.find("img").get("src"))
        universal_product_code.append(upc_pext[0])
        price_excluding_tax.append(upc_pext[2])

    return books_data_dict
    

