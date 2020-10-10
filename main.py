import argparse
import time
import json
import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs



########################################
#                  Variables           #

link = "https://www.facebook.com/mercantilbancooficial/photos/a.2349868978660093/2635386846774970/"

html_name= "test"

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

with open(f'./{html_name}.html',"w", encoding="utf-8") as file:
    file.write(str(bs_data.prettify()))
    file.close()