# 네이버 셀레니움 로그인
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# import chromedriver_autoinstaller
from chromedriver_autoinstaller import install
import pyperclip  # pyperclip 모듈 설치!
import time


# 아이디, 패스워드를 입력해주는 함수
def input_id_pw(browser, css, user_input):
    # user_input(ID/PW) 을 복사
    pyperclip.copy(user_input)  # input을 클립보드로 복사

    # 입력 칸 클릭
    browser.find_element_by_css_selector(css).click()

    # 붙여넣기 : 키보드 버튼 누르기
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()  # 윈도우 : Ctrl+V 전달
    # ActionChains(browser).key_down(Keys.LEFT_SHIFT).key_down(Keys.INSERT).key_up(Keys.LEFT_SHIFT).key_up(Keys.INSERT).perform()  # 맥 : shift+insert 전달


'''chrome_path = chromedriver_autoinstaller.install() # 추가
browser = webdriver.Chrome(chrome_path) # 추가'''
browser = webdriver.Chrome(install())

# 네이버 로그인 창 이동
browser.get("https://nid.naver.com/nidlogin.login")

# 아이디 처리
input_id_pw(browser, "#id", "아이디 입력")  # 아이디
time.sleep(1)

# 패스워드 처리
input_id_pw(browser, "#pw", "비번 입력")  # 비밀번호
time.sleep(1)

# 로그인 버튼 클릭
browser.find_element_by_css_selector("button.btn_login").click()
time.sleep(3)