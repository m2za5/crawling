from selenium import webdriver
from chromedriver_autoinstaller import install
import time

browser = webdriver.Chrome(install())
browser.get("https://logins.daum.net/accounts/loginform.do?status=-401&url=https%3A%2F%2Fwww.daum.net")

browser.find_element_by_xpath('//*[@id="mArticle"]/div/div/div/div[2]/a/span[2]').click()

my_id = browser.find_element_by_css_selector("input#id_email_2.tf_g.tf_email")
my_id.send_keys("아이디 입력")
pw = browser.find_element_by_css_selector("input#id_password_3.tf_g")
pw.send_keys("비번 입력")
button = browser.find_element_by_css_selector("button.btn_g.btn_confirm.submit")
button.click()
time.sleep(2) # 로그인이 다 될때까지 기다리기

# 이메일함으로 이동
browser.get("https://mail.daum.net/")
time.sleep(2) # 이메일함이 다 뜰때까지 기다리기
title = browser.find_elements_by_css_selector("strong.tit_subject")
for i in title:
    print(i.text)
browser.close()