import requests
from time import sleep
from selenium import webdriver
import chromedriver_binary

from bs4 import BeautifulSoup
import requests
import pandas as pd 
'''

chrome_drive ='C://Users/samah/Desktop/m2/INDEXING/tp/Lib/site-packages/selenium/chromedriver'
driver = webdriver.Chrome(chrome_drive)

sleep(5)
driver.maximize_window()
sleep(5)
driver.get("https://www.linkedin.com/")
sleep(5)

cookies_dict = {}
for cookie in driver.get_cookies():
        cookies_dict[cookie['name']] = cookie['value']
        

driver.close()

sleep(5)
resp = requests.get(f"https://www.linkedin.com/jobs/search?keywords=societe%20general&location=Worldwide&geoId=92000000&trk=organization_guest_jobs-search-bar_search-submit&position=1&pageNum=0",
                     cookies=cookies_dict,
                      headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                                   'accept-encoding': 'gzip, deflate, br',
                                                   'accept-language': 'en-US,en;q=0.9',
                                                   'upgrade-insecure-requests': '1',
                                                   'scheme': 'https'})


html = resp.text
'''
def getLinks():
        links =[]
        job = []
        societe =[]

       
        response = requests.get(f'https://www.linkedin.com/jobs/search?keywords=societe%20general&location=Worldwide&geoId=92000000&trk=organization_guest_jobs-search-bar_search-submit&position=1&pageNum=0')
         # strat scraping 
        sup = BeautifulSoup(response.text, 'html.parser')
    
        root = sup.find_all('span',{'class':'screen-reader-text'})
        for title in root:
                job.append(title.text.strip())
        city = sup.find_all('h4',{'class':'base-search-card__subtitle'})
        for city in city:
                societe.append(city.text.strip())

        return job , societe

     
        

                   
               
                
                


                
   
               
               
               
# iterate list 
def IterLinks(link):
        for l in link:
         response = requests.get(l)
         sup = BeautifulSoup(response.text, 'html.parser')

        print(sup.text)

job , societe = getLinks()
so = societe.pop()


output = pd.DataFrame({
                       'job': job,
                       'entreprise':societe})
print(output)
output.to_csv('stage.csv', index=False)



'''

HtmlPath = "C:/Users/samah/Desktop/DataPreprocessing/m.html"
page_fun = open(HtmlPath,'w',encoding='utf-8')
page_fun.write(html)
page_fun.close()

'''    