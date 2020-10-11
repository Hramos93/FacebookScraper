# FacebookScraper

### Cómo funciona 
Este script funciona con las librerias selenium y bs4.
Para que puedas gestionar una página web con selenium necesitas los drivers 
del navegador que utilizaras, aquí utilizamos Google Chrome por lo que este driver 
puedes conseguirlo en [pip](https://chromedriver.chromium.org/) de acuerdo a 
la version de tu navegador 

Crea un archivo txt con las variables de ambiente 
por defecto se debe llamar facebook_credentials.txt

dentro del txt agrega 
```python 
email = ""
password = ""
```
### Configuración de la página que se le hará scrapping.

Por ahora solo se han añadido las variables link y file_name
```python
link = ""
file_name= ""
```
link es basicamente el link de facebook donde harás el scrapping

file_name es  el nombre de los archivos de salida que obtendras.

## License
[MIT](https://choosealicense.com/licenses/mit/)

