from selenium import webdriver
from chromedriver_autoinstaller import install
import time


browser = webdriver.Chrome(install())
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net")

# 로그인 하기
id = browser.find_element_by_css_selector("input#id")
#id.send_keys("") #특정 문자열 입력
pw = browser.find_element_by_css_selector("input#inputPwd")
#pw.send_keys("")
button = browser.find_element_by_css_selector("button#loginBtn")
button.click()
time.sleep(2) # 로그인이 다 될때까지 기다리기

# 이메일함으로 이동
browser.get("https://mail.daum.net/")
time.sleep(2) # 이메일함이 다 뜰때까지 기다리기
title = browser.find_elements_by_css_selector("strong.tit_subject")
for i in title:
    print(i.text)
browser.close()