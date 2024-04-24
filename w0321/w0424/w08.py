import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By  #요소선택할 때
from selenium.webdriver.common.keys import Keys #키워드 입력할 때
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

url = "http://www.naver.com"

browser=webdriver.Chrome()
browser.maximize_window()
browser.get(url)
# 네이버 페이지 이동
# 검색창에 네이버 항공권 입력
# 검색창 엔터키 입력 - 네이버항공권 검색 이동
# 네이버항공권 클릭 - 네이버항공권 페이지 이동
# 출발 지역 선택  - 김포
# 도착 지역 선택 - 제주
# 가는 날 선택 (5월5일)
# 오는 날 선택 (5월6일)
# 인원 성인 2인 선택
# 항공권 검색 버튼 클릭
# 검색하는 동안 대기
# 검색된 항공권 스크롤 해서 하단 이동 반복
# 13만원 이하인 항공권 검색한 것 정보저장