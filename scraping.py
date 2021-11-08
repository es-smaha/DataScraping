import numpy as np 
import pandas as pd
import uuid 
from bs4 import BeautifulSoup
import requests

# read url
def gethtmlContent():
    html =  requests.get(f'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population').text
    sup = BeautifulSoup(html,'html.parser')
    return sup 

def scrap():
    columns = []
    d=[]
    content = gethtmlContent()
    table = content.find('table',{'class':'wikitable sortable'})
    rows = table.find_all('tr')
    for row in rows:
        a = row.find_all('td')
        if len(a)>1:
            country_link = a[1].find('a').text.strip()
            

# save to a dataframe

    
