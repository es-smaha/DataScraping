
from bs4 import BeautifulSoup
import requests
import pandas as pd 


price =[]
dec =[]
for page in range(3,20):
    response = requests.get('https://www.avito.ma/fr/maroc/immobilier-%C3%A0_vendre?o={page}')
    # strat scraping 
    sup = BeautifulSoup(response.text, 'html.parser')
    bigdiv = sup.find('div',{'class':'sc-1nre5ec-0 gYGzXe listing'})
    div = bigdiv.find_all('div',{'class':'oan6tk-0 gFtuUo'})
    for i in div:
        if(len(i)>1):
         d = i.find_all('a')
         for m in d :
            l = m.find('div',{'class':'oan6tk-4 hydTnW'})
           # print(l)
            for g in l :
                price.append(g.find('div').text.strip())
                
                description = g.find_all('span',{'class':'sc-1x0vz2r-0 iKjEZZ oan6tk-16 ioBmdO'})
                for desc in description:
                    dec.append(desc.find(class_='oan6tk-17 fqRwgz').text.strip())
     

p = price[0::2]
# save to a dataframe

output = pd.DataFrame({
                       'prix': p,
                       'descriptin':dec})
print(output)
output.to_csv('sub1.csv', index=False)







