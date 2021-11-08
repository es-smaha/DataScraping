import re
import requests
from selenium import webdriver


# url : https://www.randomlists.com/email-addresses?qty=100
# initialise google chrome
chrome_drive ='C://Users/samah/Desktop/m2/INDEXING/tp/Lib/site-packages/selenium/chromedriver'
driver = webdriver.Chrome(chrome_drive)
driver.get("https://www.randomlists.com/email-addresses?qty=100")

page_source = driver.page_source

# regex to find email adresses 
EMAIL_REGEX =  r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

list_em = []

#re for regularexression matchin 
for re_match in re.finditer(EMAIL_REGEX  , page_source):
    list_em.append(re_match.group())

for i , email in enumerate(list_em):
    print(f'{i+1} : {email}')