from re import search
from flask import jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # 크롬 브라우저가 열리지 않도록 
from selenium.webdriver.common.keys import Keys # 검색할 내용 넣기 
from selenium.webdriver.common.by import By # find_element()에서 By.TAG_NAME
import urllib.request
import time

class SearchImage: # 실제로 크롬 드라이버를 이용해서 이미지를 가져오는 클래스  
    def __init__(self) -> None: # 생성자
        pass

        option = Options()
        option.add_argument('headless')
        option.add_argument('--window-size=1920,1080')   
        
        global driver 
        driver = webdriver.Chrome('C:/Users/USER/OneDrive - 서울과학기술대학교/touch_my_coding_back/chromedriver.exe', options=option)  

        global img_url # 최종 이미지 url 리스트 
        img_url = []


    def search(self, max=51): # 이미지 스크래핑 
        # 크롬 브라우저가 열리지 않고 실행 
        driver.get(self.getKey()) # url 가져오기 
        self.scroll()
        for i in range(1,max):
            try: # 제거하면 에러떠서 안 된다. 
                button = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img')
                driver.execute_script("arguments[0].click();",button)
                img_url.append(driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute('src')+'\n')
            except:
                continue
        with open("img_url.txt", "w") as file:
            file.writelines(img_url)

    
    def scroll(self, max=50): # 사용자가 이미지를 추가 요청했을 때 이미지 개수가 부족하다면 호출 
        count = 0
        # 더이상 스크롤 할 게 없을 때까지 내리기 
        elem = driver.find_element(By.TAG_NAME, "body")
        elem.send_keys(Keys.PAGE_DOWN)


    def getImage(self): # 이미지 가져오기 
        return 0

    
    def getKey(self): # 사용자 페이지 검색 
        key = input("원하는 이미지를 검색하세요:") 

        url1 = 'https://www.google.co.kr/search?q='
        url2 = '&sxsrf=APq-WBu5Rj8lmav8YXfFLnw-5SD0bFzq1g:1645699917865&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjh94r4lZj2AhV3sFYBHQoXCxQQ_AUoAXoECAEQAw&biw=1920&bih=937&dpr=1'
        url = url1+key+url2

        return url


a = SearchImage()
a.search()

        
