# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:34:14 2019

@author: Companion Box
"""

import urllib2
from bs4 import beautifulsoup


qoute_page="https://www.bloomberg.com/quote/SPX:IND"
page=urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')




try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

html = urlopen("https://www.bloomberg.com/quote/SPX:IND")
print(html.read())




import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url_medicament = 'https://comenzi.farmaciatei.ro/farmacie/sistemul-respirator/analgezice/nurofen-forte-400mg-24-drajeuri-reckitt-benkiser-healthcare-p328447'

page = urllib.request.urlopen(url_medicament)

soup = BeautifulSoup(page, 'html.parser')

print(soup)




name_box=soup.find('h1')
print(name_box)


price_box=soup.find('div', attrs={"class":'price-box'})
#price=price_box.text
print(price_box)



compozitie=soup.find('div', attrs={"class":'product-desc'})
print(compozitie)



#### Fieare trebuie sa mai extragem cate un medicament, de pus pe github, pana cu oo secunda inainte de luni

#####Medicament Eliza - paracetamol

url_medicament ='https://comenzi.farmaciatei.ro/farmacie/sistemul-respirator/ameliorare-simptome-raceala-si-gripa/paracetamol-polisano-500-mg-20-comprimate-polisano-p342806'
page = urllib.request.urlopen(url_medicament)

soup = BeautifulSoup(page, 'html.parser')

print(soup)
##Nume Paracetamol
name_box=soup.find('h1')
print(name_box)
##Pret
price_box=soup.find('div', attrs={"class":'price-box'})
print(price_box)

###Compozitie
compozitie=soup.find('div', attrs={"class":'product-desc'})
print(compozitie)











