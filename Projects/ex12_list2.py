# 리스트를 다루는 파이썬의 내장된 함수들...

#1] 리스트나 튜플의 요소들 중 최소값,최대값,합계를 구해주는 함수
score_list= [48,100,85,72,64,23,5,18]
print('최소값 :', min(score_list) )
print('최대값 :', max(score_list) )
print('총합 :', sum(score_list) )
print('평균 :', sum(score_list)/len(score_list))

print(min(10,50,60,70,80,10,50,5))
print(max(10,50,60,70,80,10,50,5))
#print(sum(10,50,60,70,80,10,50,5)) #error

# 딕셔너리는? key를 계산함... 즉.. 원하는 값을 계산하지 않음.. 그러니 사용안함.
aaa={'a':10, 'b':20, 'c':30}
print(min(aaa)) 
print(max(aaa))
print()


#2] 리스트나 튜플의 for 반복할때 인덱스번호와 값을 동시에 주는 함수
aaa= ['sam','robin','hong','park']
for value in aaa:
    print(value)
print()

for idx, value in enumerate(aaa):
    print(idx, ":", value)
print()


#3] 요소의 순서를 뒤바꾸는 함수


