# 데이터 분석을 통한 서비스를 개발하려면.. 데이터 수집이 필요
#1. 회사나 개인이 가진 매출데이터, 설문데이터, 회원데이터 등 엑셀파일같은 형태의 데이터 [ 파일 입출력(표준함수 open) ]
#2. 날씨정보, 채용정보, 행사정보 등 웹을 통해 서비스 되는 데이터 [ urlib requst 모듈, 외부모듈(requests, BeautifuSoup)]

# 파이썬에서 웹의 데이터를 불러와서 분석하는 맛보기 수업.

#1) 네트워크 작업을 위한 모듈 추가
from urllib import request

# request라는 하위모듈이 가진 네트워크상의 파일을 열어주는 기능함수를 호출
address= 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/aaa.txt'
url= request.urlopen(address)
data= url.read()
print(data)
print()
#한글이 깨진다면.. UTF-8로 디코딩(해독)해야함. 
print( data.decode('UTF-8') )
print('-'*20)
print()


