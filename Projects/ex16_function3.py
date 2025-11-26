#2. 함다 lambda함수

# def aaa(n):
#     return n*10

# num= aaa(5)
# print(num)
# print(aaa(3))

print("-------------------------------------------")

bbb = lambda n:n*10 #람다함수 정의
num2= bbb(5)
print(num2)
print(bbb(3))

print("-------------------------------------------")

ccc = bbb
print(ccc) #출력예시 : <function <lambda> at 0x0000021C3B2C8AF0>
print(bbb) #출력예시 : <function <lambda> at 0x0000021C3B2C8AF0>

# 함수를 변수에 대입할 수 있다면..
# 함수를 매개변수에 대입하는것도 가능하다.
# 쉽게 이야기를 하자면 함수를 전달인자로 넘길 수 있다는 이야기임.
# 예시를 들어보자면 다음과 같은 함수가 있다고 하자.
print("-------------------------------------------")

def eee(f):
    print('eeeeeeeeeee')

eee(10) #f 변수에 bbb함수가 대입되어서 호출됨.

print("-------------------------------------------")
eee(bbb) #함수를 전달인자로 넘김.
print("-------------------------------------------")
def www():
    print("nice to meet you")

eee(www())

print("-------------------------------------------")

# bbb = []
# for v in aaa:
#     bbb.append(v*v)
# print(bbb)

aaa = list(range(1,6))
print("-------------------------------------------")

# 리스트 컴프리핸션 리스트내포 기술사용
ccc = [ v*v for v in aaa ]
print(ccc)

print("-------------------------------------------")
# map 함수 사용
def cal_square(n):
    return n*n

ddd = map(cal_square, aaa)
print(list(ddd))
print('-------------------------------------------')

#추가요청) aaa 리스트의 각 요소마다 세제곱해준 리스트 만들어.

eee = map(lambda n:n**3 , aaa)
print(list(eee))
#추가요청) aaa 리스트의 각 요소를 10으로 나누기.. 리스트 만들어
fff = map(lambda n:n/10 , aaa)
print(list(fff))
print("--------------------------")
# filter(함수, 리스트)표준함수 - 특정조건에 해당하는 요소만 뽑아서 리스트로
aaa = [70,60,30,40,80,90,32,75]
vvv = filter(lambda n:n<60 , aaa)
print(list(vvv))
print("-----------")
www = [v for v in aaa if v<60]
print(www)