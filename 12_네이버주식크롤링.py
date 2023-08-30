import urllib.request as req
from bs4 import BeautifulSoup

code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code, "html.parser", from_encoding="euc-kr")
price = soup.select("ul#exchangeList span.value")
name = soup.select("ul#exchangeList h3.h_lst")
for i in range(len(price)):
    print(f"{name[i].text} : {price[i].text}")