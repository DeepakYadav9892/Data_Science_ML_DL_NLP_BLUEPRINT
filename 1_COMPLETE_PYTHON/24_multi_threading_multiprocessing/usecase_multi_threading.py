"""
Real World Example : multithreading for IO bound tasks 
Scenario:web scraping 
web Scraping often involves makin g numerous network requests to 
fetch web pages. these tasks are IO bound bcz they spnd a lot of 
time waiting fo rresponses from serves. Multithreading can signigicantly
improve the performance by alllowing multiple web pages to be fetched concurrently.

"""
import threading
import requests
from bs4 import BeautifulSoup

urls = ["https://quotes.toscrape.com",
        
        "https://en.wikipedia.org/wiki/Web_scraping",
        "https://www.scrapethissite.com/pages/?utm_source=chatgpt.com"
        
        
        
        ]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters form {url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All the webpages of fetched ")
