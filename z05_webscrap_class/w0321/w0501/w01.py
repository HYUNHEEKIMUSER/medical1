import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

def connection():
    conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    cursor = conn.cursor() # 커서생성 - 명령어 입력받는 함수
def close(cursor,conn):
    cursor.close()
    conn.close()

while True:
    print("1. 이름으로 검색")
    print("2. 근무사원 조회")
    choice = input("원하는 번호")
    if choice == '-1':
        break
    elif choice =='1':
        search = input("이름 입력")
        sql = ''
        conn.cursor = connection()
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            print(d[0],end='\t')
            print(d[1],end='\t')
            print(d[2],end='\t')
            
        close(cursor,conn)

    elif choice =='2':
        search = input("이름")
        sql = ""
        conn.cursor = connection()
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data :
            print(d[0])
            
    close(cursor,conn)






