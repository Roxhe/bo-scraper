def get_pages(sample_url, nb):
    """ Description of what get_pages does.
    
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