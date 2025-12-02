# 웹 스크래핑 : 웹 페이지에서 특정 정보를 추출하는 작업

# 외부 모듈 : requests, beautifulsoup4 [별도 설치 필요]

# 웹 페이지를 분석 - 웹 페이지를 만드는 문법 HTML, CSS, JavaScript

# 아주 간단한 웹페이지를 만들어보기. [ HTML, CSS, JavaScript 언어를 다뤄보기. (web-test)]

import requests
response= requests.get('https://2017mrhi.github.io/web-test/')
print(response.text)
print()

# html 웹문서를 분석.. 요소들을 찾아서 안에 있는 값을 뽑아내기 [외부 모듈 BeautifulSoup]
from bs4 import BeautifulSoup

# HTML분석가 객체를 생성
soup= BeautifulSoup(response.text, "html.parser")

# p요소들 모두를 찾아보기
p_list= soup.select('p')
print( len(p_list) )

print(p_list[0].string)
print(p_list[1].string)

# 아이디로 찾기 - 이미지경로 찾기
img= soup.select_one('#kk')
print('이미지 경로 :', img.get('src')) #src 속성의 값을 얻어오기

