import requests
from time import sleep
from selenium import webdriver
import chromedriver_binary
import time
chrome_drive ='C://Users/samah/Desktop/m2/INDEXING/tp/Lib/site-packages/selenium/chromedriver'
driver = webdriver.Chrome(chrome_drive)
driver.get("https://www.linkedin.com/jobs/search?keywords=societe%20general&location=Worldwide&geoId=92000000&trk=organization_guest_jobs-search-bar_search-submit&position=1&pageNum=0")

time.sleep(10)
cookies_dict = {}
for cookie in driver.get_cookies():
        cookies_dict[cookie['name']] = cookie['value']
        

driver.close()

resp = requests.get("https://www.linkedin.com/jobs/search?keywords=societe%20general&location=Worldwide&geoId=92000000&trk=organization_guest_jobs-search-bar_search-submit&position=1&pageNum=0",
                     cookies=cookies_dict,
                     headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                                   'accept-encoding': 'gzip, deflate, br',
                                                   'accept-language': 'en-US,en;q=0.9',
                                                   'upgrade-insecure-requests': '1',
                                                   'scheme': 'https'})
        
html = resp.text
