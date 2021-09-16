import requests
from bs4 import BeautifulSoup as bs
import urllib.request

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

