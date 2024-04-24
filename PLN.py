# Web scraping, pickle imports
import requests
from bs4 import BeautifulSoup
import pickle
from time import sleep
import os

# Web Scrapes transcript data from blog
def url_to_transcript(url):
	'''Obtener los enlaces del blog de Hernan Casciari.'''
	page = requests.get(url).text
	soup = BeautifulSoup(page, "lxml")
	print('URL',url)
	enlaces = []
	for title in soup.find_all(class_="entry-title"):
           for a in title.find_all('a', href=True):
               print("Found link:", a['href'])
               enlaces.append(a['href'])
               return enlaces
base = 'https://editorialorsai.com/category/epocas/'
urls = []
anios = ['2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
for anio in anios:
    urls.append(base + anio + "/")
print(urls)

# Recorrer las URLs y obtener los enlaces
enlaces = [url_to_transcript(u) for u in urls]
print(enlaces)

def url_get_text(url):
    '''Obtener los textos de los cuentos de Hernan Casciari.'''
    print('URL',url)
    text=""
    try:
        page = requests.get(url).text
        soup = BeautifulSoup(page, "lxml")
        text = [p.text for p in soup.find(class_="entry-content").find_all('p')]
    except Exception:
        print('ERROR, puede que un firewall nos bloquea.')
        return ''
    return text

# Recorrer las URLs y obtener los textos
MAX_POR_ANIO = 50 # para no saturar el server
textos=[]
for i in range(len(anios)):
    arts = enlaces[i]
    arts = arts[0:MAX_POR_ANIO]
    textos.append([url_get_text(u) for u in arts])
print(len(textos))

## Creamos un directorio y nombramos los archivos por año
os.mkdir ('blog')

for i, c in enumerate(anios):
    with open("blog/" + c + ".txt", "wb") as file:
        cad=""
        for texto in textos[i]:
            for texto0 in texto:
                cad=cad + texto0
        pickle.dump(cad, file)
