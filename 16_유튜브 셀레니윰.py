from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chromedriver_autoinstaller import install
import time

# 셀레늄 초기화 : chrome driver 가져오기
browser = webdriver.Chrome(install())

# Youtube 특정 영상 URL 이동
browser.get("https://www.youtube.com/watch?v=BLVVRQTUIH4")
time.sleep(6)

# 스크롤 내리기
#browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN) # 스크롤 살짝 내리기 / Keys.END : 스크롤 끝까지 내리기
browser.find_element_by_css_selector("html").send_keys(Keys.END) # 댓글을 안 가져올 경우
time.sleep(6)

# 댓글 가져오기
comment = browser.find_elements_by_css_selector("yt-formatted-string#content-text")

idx = 0
while True: # 무한 루프
    # 예외 처리
    try: # 해보기
        print(comment[idx].text)
    except: # 에러가 뜰 경우 : 더 이상 댓글을 가져오지 못할 때
        print("--------- 크롤링 끝! ------------")
        break

    idx += 1
    if idx % 20 == 0: # idx가 20의 배수라면?
        browser.find_element_by_css_selector("html").send_keys(Keys.END)
        time.sleep(4)
        comment = browser.find_elements_by_css_selector("yt-formatted-string#content-text")