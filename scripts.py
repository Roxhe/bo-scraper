
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