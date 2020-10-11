import requests
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime as dt
import csv 

# Lectura del html  
html = open(r"test.html","r", encoding= "utf-8")
soup = BeautifulSoup(html.read(), 'html.parser')

#* Busqueda de nombres en los comentarios

nombres =[]
comentarios = []
search = soup.findAll('div', attrs={'class':'tw6a2znq'})
for comments in search:
    if comments.find(class_="d2edcug0") is None:
        continue
    findNames = comments.find('span', class_ = 'd2edcug0')
    if findNames is None:
        continue
    nombres.append(findNames.text)

    if comments.find(class_="kvgmc6g5") is None:
        continue
    findComments = comments.find('div', class_ = 'kvgmc6g5')
    if findComments is None:
        continue
    comentarios.append(findComments.text)

nombrelst = [s.strip() for s in nombres]
comentlst = [s.strip() for s in comentarios]
result = dict(zip(nombrelst, comentlst))

with open('facebookcommit.csv', 'w', encoding='utf-8') as f:
    w = csv.DictWriter(f, result.keys())
    w.writeheader()
    w.writerow(result)
    f.close()

