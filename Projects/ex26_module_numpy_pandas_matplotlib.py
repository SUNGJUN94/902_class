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