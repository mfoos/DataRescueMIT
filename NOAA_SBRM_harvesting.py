from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import time

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

for i in urllist:
    if url[-3:] == "pdf":
        wget.download(url)
    else if url[-3:] == "html":
        wget.download(url)
    else if url[-1] == "/":
        p = re.compile("(crd\d{4})")
        m = p.match(url)
        wget.download(url + m.group + ".pdf")





