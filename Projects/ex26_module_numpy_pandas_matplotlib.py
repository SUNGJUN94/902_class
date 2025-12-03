import numpy as np

aa=np.array([10,20,30])
bb=np.array([4,5,6])

print(aa)
print(bb)
cc= aa+bb
print(cc)

# 리스트와의 차이점 . 산수 덧셈을 하면 배열의 요소끼리 덧셈을 수행함

print(aa.shape)
print(cc.shape)
print("*"*50)
# 2차원 표구조

aaaa= np.array([ [100,200,300,400] , [500,600,700,800] ])
print(aaaa.shape)
print("*"*50)

bbbb = np.array([
    [3,4,5,6],[7,8,9,0]
])

print(bbbb.shape)

print("*"*50)

cccc = aaaa+bbbb
print(cccc.shape)
# 연산할때 주의 .. 행렬 요소끼리 연산이기에.. 개수가 다르면

# dddd = np.array([[10,20,30,40] ,[40,50,60]])
# print(dddd.shape)

#출력되지 않음. 행렬이 같아야함.
print("*"*50)

# 2) pandas - 데이터 분석할때 n차원 행렬(2차원구조 표 형태가 가장 흔함)의 구조를 용이하게 만들어주는 모듈
# pandas 외부모듈 설치

import pandas as pd

a = pd.Series(['sam' , 'kim' , 'hong'])
print(a)

print("*"*50)

b = pd.Series(['seoul' , 'dokyo' , 'paris'] , index=['korea' , 'japan' , 'france'])
print(b)

print("*"*50)

cc = pd.DataFrame(['aa' , 'bb' , 'cc' , 'dd'] , ['11','22','33','44'])
print(cc)

print("*"*50)

dd = pd.DataFrame({"aa":[10,20,30] , "bb":[100,200,300] , "cc":[1000,2000,3000]})

print(dd)

print("*"*50)

# csv 파일을 읽어와서  DataFrame 만들기

ee = pd.read_csv("./files/scores.csv")
print(ee)
print("*"*50)


print(ee.head())
print(ee.shape)
print(ee.columns)
print(ee.index)
print("*"*50)
# 데이터프레임의 구조정보를 한번에 알려주는 기능 함수

print(ee.info())

print("*"*50)

print(ee['국어'].mean())
print(ee['영어'].max())
print("*"*50)
# 정우성의 영어점수 출력
print(ee['영어'][ee['이름']=='정우성'])

# 데이터분석(숫자데이터)에 많이 사용되는 평균 , max 등
print("*"*50)
print(ee.describe())
print("*"*50)

# 여러개의 컬럼을 동시에 보기

print(ee[['영어' , '수학']])
print("*"*50)

row=ee.loc[0:2] #0번째 인덱스 줄
print(type(row))
print(row)

import matplotlib.pyplot as plt
# 시간별 온도 데이터셋 필요
plt.rcParams['font.family']='Malgun Gothic'


hours = [6,9,12,15,18,21,24] # x축
temperature = [10,14,18,20,17,13,11] # y축

# plt.plot(hours,temperature , marker='|')

# plt.title(" day 온도")
# plt.xlabel("time")
# plt.ylabel("'c")
# plt.show()

print("*"*50)

# students = ['홍길동' , '김길동' , '박길동' , '문성준' , '서성준' , '김깁머']
# score = [45,65,34,13,45,65]

# plt.bar(students , score , color='skyblue')
# plt.title("gkrtod")
# plt.xlabel("time")
# plt.ylabel("'c")


# plt.show()

data = {
    '월': ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
    '매출액(만원)': [4200, 3900, 4500, 4700, 5200, 5800, 6100, 6400, 5900, 5500, 5300, 5000]
}

df = pd.DataFrame(data)
print("롯데리아 매출 데이터")
print(df)

plt.figure(figsize=(8,5))
plt.scatter(df['월'] , df['매출액(만원)'] , marker="o" )
plt.title('롯데리아에 2025 월별 매출액')
plt.xlabel("월")
plt.ylabel("매출액")
plt.grid(True)

# 각 점위에 숫자 표시

for i , value in enumerate(df['매출액(만원)']):
    plt.text(i,value+50 , f'{value}' , ha='center')

plt.show()







