# 함수(function 기능) : 특정 기능을 수행하는 코드를 모아놓은 코드영역
# 예) 로그인함수(==로그인 기능 코드들), 회원가입함수(==회원가입 코드들 영역), max함수(==최대값을 구해주는 기능 코드들)

#[ 특정 기능을 작성한 코드 영역을 필요할때 마다 언제든 호출(call)하여 그 코드영역이 실행되도록...]

# 파이썬 함수의 종류
#1. 표준(내장) 함수 : 이미 파이썬에서 만들어서 내장해 놓은 함수들 print(), input(), len(), max()....
#2. 외부 함수 : 기존 개발자 또는 업체들에서 만들어 라이브러리로 제공하는 함수. 내장되어 있지 않아서 그냥 사용불가능. 대신 그 모듈(함수들을 가진 폴더)을 파일에 삽입(import)하여 불러 사용함.  import datetime
#3. 개발자 정의 함수 (오늘 수업)

# 코드가 써있는 영역을 구분하기 위해 보통 함수의 이름을 영어로 작성(동사 v)
# 함수 이름(식별자)옆에 소괄호()가 반드시 있어야 함. 이를 통해 변수와 구별함
# age   <-- 변수
# login() <-- 함수

#1. 함수 정의 문법 def [define]
def show():
    print('show function.. hello')
    #코드 영역에 여러줄 코드 가능
    print('good')

# 함수를 정의했다고해서 코드가 실행되는 것은 아님. 함수를 사용하겠다고 호출해야 그 영역의 코드들이 실행됨.

print('함수 호출 연습')
#함수 호출 function call
show()
#필요할때 언제든 다시 함수를 호출할 수 있음. 그럼 그 코드영역이 다시 실행됨
show()
print()

# 함수 호출할때 마다 같은 글씨만 출력되는 기능은 효용성이 약해보임... 내가 전달한 값을 출력해주는 기능이 필요한 경우도 있음.

#2. 함수를 만들때 값을 전달받는 함수 만들기
def show_name(name): # name 처럼 소괄호()안에 전달된 값을 받기 위한 변수를 '매개변수'라고 부름. 영어로는 파라미터 parameter
    print('welcome!', name)

#함수를 호출하면서 매개변수에 값 전달..
show_name('sam')
show_name('robin')
print()

# 매개변수는 여러개 일수도 있음.
def output(a, b):
    print('a:', a)
    print('b:', b)

#함수 호출하면서 값 전달.
output(10, 20)
output(100,200)
#사용할때 주의할점. 함수호출할때 매개변수의 개수만큼 값을 줘야만 함.
#output(1000) #error
#output(1000,2000,3000) #error
print()

#결국 파라미터 개수만큼 반드시 값을 전달해야만 함..안하면 에러..
#근데.. 경우에 따라서는 값 전달하면 그 값을 보여주고.. 아니면 기본값 보여줘... 이를 위한 문법 [기본값 지정]

#3. 함수 파라미터의 default value 지정
def display(a=1, b=2):
    print('a의 값:', a)
    print('b의 값:', b)

display(100,200)
display(100) #a=100, b는 기본값
display() # a,b 모두 기본값
# 근데.. 값 1개 줄건데.. b에게 ... [ML 함수들 사용할때 꽤 많이 사용함.]
display(b=1000)
display(a=50, b=30)

def display2(a, b=2):
    print(a, b)

#display2() #error
display2(10)
display2(10,20)
#display2(b=50) #error

show()
show_name('hong')
output(5,3)
display(b=2000)
display2(10000,b=20000)
print()

# 기능을 만들다 보면.. 전달값이 몇개인지 특정하기 어려움 경우도 있음. 
# 예) 전달받은 모든 값 출력... 모든 값 덧셈..(총합)구하기..
#해결방법1) 여러개의 값을 받기 위해 리스트 1개로 받기..
def cal_total(number_list):
    print('전달받은 값의 총합:', sum(number_list))

cal_total([10,20])
cal_total([10,20,30,40,50])
cal_total([10,20,30,40,50,60,70])
#cal_total(10,20,30) #error

#4. 매개변수의 길이가 가변적인 파라미터 variable length arguments [가변 파라미터]
def nice( *values ): # 보기에는 그냥 변수 1개로 보이지만.. 사실 내부에서는 리스트로 만들어 줌.
    print('전달 받은 값의 개수 : ', len(values) )
    for v in values:
        print(v)

nice()
nice(10)
nice(10,20)
print()

# 표준 내장 함수 중에서 가변파라미터 를 사용하는 함수
aaa= [10,20,30]
m= max(aaa) #파라미터에 리스트 1개를 전달
print(m)

m= max(40,50,60,70) #파라미터에 값 4개를 전달
print(m)
print()
# ---------------------

# 함수를 정의할때 유의할 점.. 같은 이름의 함수를 또 정의하면?? 덮어쓰기..
def aaa():
    print('aaa function')

aaa()

def aaa():
    print('다시만든 aaa function')

aaa()

def aaa(num):
    print('aaa num:', num)

aaa(10)
#aaa() #error

#그래서 주의... 여러분은 모든 내장함수의 이름을 외우지 못함.
#하필.. 내장함수와 같은 이름의 함수를 만드는 경우가 있을 수 있음.
def max():
    print('내가만든 max()함수')

max()

#numbers = [3, 10, 7, 1]
#print(max(numbers)) #error

#변수 이름도 식별자여서.. 내장함수명을 변수명으로 덮어지기도 함.
min(10,5,3,6,9)
#min= 100
#min(10,5,3,6,9)

print()
# 함수의 호출문이... 함수 정의보다 먼저 되면 안됨!!!
#gg()#error

def gg():
    print('gggggg')

gg()
print()
#-------------------------------------------

#5. 리턴을 해주는 함수..










