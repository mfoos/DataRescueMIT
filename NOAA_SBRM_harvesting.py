from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import time
import wget
import os

baseURL = "http://www.nefsc.noaa.gov/femad/fsb/SBRM"
html = urlopen(baseURL)
soup = BeautifulSoup(html.read(), 'html.parser')

section = soup.find(id="wide").find_all('li')
section.extend(soup.find_all("div", {"class":"container"}))

urllist = set()
for result in section:
    for item in result.find_all('a'):
        url = item.get('href')
        if url[:4] == "http":
            pass
        elif url[0] == "/":
            url = baseURL + url
        else:
            url = baseURL + "/" + url
        urllist.add(url)

for url in urllist:
    filename = url.split("/")[-1]
    if not os.path.isfile(filename.replace(" ","%20")):
        time.sleep(1)
        if url[-3:] == "pdf":
            response = requests.get(url)
            if not response.status_code > 400:
                url = url.replace(" ","%20")
                wget.download(url)
                print("Downloading: " + url)
            else:
                print("404 for this guy: " + url)
        elif url[-3:] == "html":
            print(url)
            response = requests.get(url)
            if not response.status_code > 400:
                url = url.replace(" ","%20")
                wget.download(url)
                print("Downloading: " + url)
            else:
                print("404 for this guy: " + url)
        elif url[-1] == "/":
            p = re.compile("(crd\d{4})")
            m = p.search(url)
            url = url + m.group() + ".pdf"
            url = url.replace(" ","%20")
            response = requests.get(url)
            if not response.status_code > 400:
                wget.download(url)
                print("Downloading: " + url + "\n")
            else:
                print("404 for this guy: " + url)
    
                





