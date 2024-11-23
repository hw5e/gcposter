import urllib.request
from bs4 import BeautifulSoup

url = "https://groovecoaster.jp/material-world/"
req= urllib.request.Request(url)
sourcecode = urllib.request.urlopen(url).read()
soup=BeautifulSoup(sourcecode,"html.parser")

for href in soup.find("div",class_="list-wrap").find_all("li"):
    print(href.find("a")["href"])
