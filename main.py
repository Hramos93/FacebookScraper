import argparse
import time
import json
import csv
import requests
import urllib.request

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs



########################################
#                  Variables           #

link = "https://www.facebook.com/mercantilbancooficial/photos/a.2349868978660093/2635386846774970/"

file_name= "cambioclave"

# Credenciales
with open('facebook_credentials.txt') as file:
    EMAIL = file.readline().split('"')[1]
    PASSWORD = file.readline().split('"')[1]

def login(email, contraseña):
    """[Login]
    metodo para conectar, solo requiere las credenciales 
    de conexión de facebook, deben estar cargardas en 
    las variables de entorno
    Args:
        email ([str]): email de conexion
        contraseña ([str]): contraseña de conexion
    """

    
    browser.get("http://facebook.com")
    browser.maximize_window()
    browser.find_element_by_name("email").send_keys(email)
    browser.find_element_by_name("pass").send_keys(contraseña)
    browser.find_element_by_id('u_0_b').click()
    time.sleep(5)
    return browser


browser = webdriver.Chrome(executable_path="./chromedriver")
login(EMAIL, PASSWORD)
browser.get(link)
source_data = browser.page_source
bs_data = bs(source_data, 'html.parser')

with open(f'./assets/{file_name}.html',"w", encoding="utf-8") as file:
    file.write(str(bs_data.prettify()))
    file.close()


html = open(r"./assets/%s.html" %file_name,"r", encoding= "utf-8")
soup = bs(html.read(), 'html.parser')

nombres =[]
comentarios = []
#* busca comentarios 
search = soup.findAll('div', attrs={'class':'tw6a2znq'})
for comments in search:
    if comments.find(class_="d2edcug0") is None:
        continue
    #* busqueda de nombres 
    findNames = comments.find('span', class_ = 'd2edcug0')
    if findNames is None:
        continue
    nombres.append(findNames.text)

    if comments.find(class_="kvgmc6g5") is None:
        continue
    #* busqueda de comentarios 
    findComments = comments.find('div', class_ = 'kvgmc6g5')
    if findComments is None:
        continue
    comentarios.append(findComments.text)
#* limpieza de elementos 
nombrelst = [s.strip() for s in nombres]
comentlst = [s.strip() for s in comentarios]

#* construcción de csv
result = dict(zip(nombrelst, comentlst))
with open(f'./assets/{file_name}.csv', 'w', encoding='utf-8') as f:
    w = csv.DictWriter(f, result.keys())
    w.writeheader()
    w.writerow(result)
    f.close()
