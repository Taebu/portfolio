import os
import ssl
import urllib.request
from bs4 import BeautifulSoup
import argparse
import re

# 인자값을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description='사용법 테스트입니다.')
parser.add_argument("--itemid", help="Aladin itemid", default=None)
#출처: https://zosystem.tistory.com/282 [동방노트:티스토리]

# 입력받은 인자값을 args에 저장 (type: namespace)
args = parser.parse_args()
# 입력받은 인자값 출력 
print(args.itemid)

#저장할 이미지 경로 및 이름 (data폴더에 face0.jpg 형식으로 저장)

ItemId = args.itemid
imageStr = "data/"+ItemId+"/aladin_"

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 

createFolder('C:\\Users\\Taebu\\python\\data\\'+ItemId) 
url = "https://www.aladin.co.kr/shop/book/wletslookViewer.aspx?ItemId="+ItemId
# url = url + str(pageNum)
imageNum = 0
fp = urllib.request.urlopen(url)
source = fp.read();
fp.close()

soup = BeautifulSoup(source, 'html.parser')
soup = soup.find_all("img")


#이미지 경로를 받아 로컬에 저장한다.
for i in soup:
    imgURL = i["src"]
    if(imgURL.startswith("//")):
        imgURL = "https:" + imgURL

    if(imgURL.find("audio_play.png")>-1):
        continue
    
    imageNum += 1
    urllib.request.urlretrieve(imgURL,imageStr + str(imageNum) + ".png")
    print(str(imageNum)+" : " +imgURL)
# [출처] [python]웹사이트의 대량의 이미지 크롤링하기(2) / 파이썬 웹 크롤러|작성자 유알
