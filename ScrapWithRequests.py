#!/usr/bin/python

import bs4
import requests
from lxml import html

isbn=raw_input('ISBN:') # This will be changed with the feature that take the ISBN from barcode scanner.
root_url = 'http://www.toplukatalog.gov.tr'
index_url = root_url + '//index.php?_f=1&the_page=&cwid=2&keyword=%s&tokat_search_field=4&order=0&command=Tara#alt' %isbn

def get_book_names():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text)
    print (soup)
#   return [a.attrs.get('href') for a in soup.select('div.video-summary-data a[href^=/video]')]

print(get_book_names())
#print()

