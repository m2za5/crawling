import urllib.request as req
from bs4 import BeautifulSoup

# 서버로부터 HTML 코드 받아오기
code = req.urlopen("http://www.cgv.co.kr/movies/?lt=1&ft=0")
#print(code.read())

# HTML 코드 예쁘게 정리하기
soup = BeautifulSoup(code, "html.parser")
#print(soup)

#내가 원하는 요소 가져오게 하기
# 속성명이 id= "#" , 속성명이 class= "."
# 속성명이 이 두 개가 아니면 속성값도 쓸 수 없다
# ~의 자손 : ">"
# ~의 후손 : " "

#title = soup.select_one("ol div.box-contents > a > strong.title")
#print(title.text)
title = soup.select("strong.title")
#print(title.text)
#title 리스트에 들어있는 원소들 하나씩 다 빼라.
#근데 그 원소가 HTML 요소니까, 그 HTML 요소의 내용 출력해라.
#리스트형은 for문
num=1
f = open("무비차트.txt", "w") # "w" : 쓰기모드
for i in title:
    print(f"{num}위 : {i.text}")
    f.write(f"{num}위 : {i.text}\n") # "\n" 개행문자
    num += 1
f.close()