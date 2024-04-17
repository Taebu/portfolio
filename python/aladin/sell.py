from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = driver = webdriver.Chrome()
url='https://www.google.com/'
itemid='337377907'
url = 'https://www.aladin.co.kr/shop/wproduct.aspx?ItemId='+itemid
driver.get(url)

body = driver.find_element(By.CSS_SELECTOR,'body')

# 15번 페이지 다운 
# 페이지 다운을 하지 않으면 가져오지 않는 데이터가 존재

for i in range(1, 4): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)


for i in range(1, 9): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)


print(driver.title)
 
# 내용 펼치기 
driver.execute_script('$j("#div_PublisherDesc_All").show();')

# 책 소개 모든 내용 가져오기 
print("책 소개 모든 내용 가져오기")
div_PublisherDesc_All = driver.find_element(By.ID, 'div_PublisherDesc_All')
print(div_PublisherDesc_All.text)



# 책소개 내용 가져오기
print("책소개 내용 가져오기")
div_PublisherDesc_Short = driver.find_element(By.ID, 'div_PublisherDesc_Short')
print(div_PublisherDesc_Short.text)


# 목차 펼치기 
driver.execute_script('$j("#div_TOC_All").show();')

# 목차 내용 가져오기
print("목차 내용 가져오기")
div_TOC_Short = driver.find_element(By.ID, 'div_TOC_Short')
print(div_TOC_Short.text)


Ere_prod_mconts_R = driver.find_element(By.CLASS_NAME, 'Ere_prod_mconts_R')
print(Ere_prod_mconts_R.text)

# 책 소개 가져오기 
Ere_prod_mconts_box = driver.find_element(By.CLASS_NAME, 'Ere_prod_mconts_box')
print(Ere_prod_mconts_box.text)

