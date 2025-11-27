# 파일 처리(입출력) 를 위한 파이썬의 표준 내장 함수

#1. 파일에 데이터를 저장하기 - 파일명을 경로없이 쓰면.. 이 .py파일이 있는 곳과 같은 위치에 만들어짐. (이미 그 파일명이 있으면 덮어쓰기, 없으면 파일 생성)
file= open('aaa.txt', 'w', encoding='UTF-8') #mode : 'w' write, 'a' append, 'r' read

file.write('This is python programming.....한글도 되나??')

#파일쓰기 작업으 종료되면 반드시... 스트림을 닫아야 함. 리소스 낭비
file.close()
#---------------------------------------------------------------------

#2. 파일에서 텍스트 데이터 읽어오기...
file= open('aaa.txt', 'r', encoding='UTF-8') # 파일명이 없으면... 못 읽어오기에..만들어주지 않고.. 안 읽어짐.

contents= file.read()
print('파일에서 읽을 텍스트 :', contents) 

file.close()
print()
# ---------------------

#3. 파일 이어쓰기.. append mode
file= open('bbb.txt', 'a', encoding='UTF-8')
file.write('apple')
file.write('banana')
file.write('orange')
file.close()

file= open('ccc.txt', 'a', encoding='UTF-8')
file.write('apple\n')
file.write('banana\n')
file.write('orange\n')
file.close()

#(응용) 사용자로부터 한줄 리뷰를 계속 입력받아.. 파일에 저장. 단, 'quit'을 입력하면 입력을 종료하는 프로그램
file= open('ddd.txt', 'a', encoding='UTF-8')

while True:
    message= input('리뷰 입력 : ')
    if message=='quit' or message=='그만':
        break

    file.write(message+'\n')

file.close()
#-----------------------------------

#4. 파일경로에 폴더명 ....
file= open('files/aaa.txt', 'w') #files 폴더안에... [만약. files 라는 폴더가 없다면.. 에러!! 폴더(디렉토리)는 자동으로 만들어주지 않음.]
file.write('nice to meet you')
file.close()
# files 폴더를 직접 만들면 되지만.. 실제 이 프로그램이 실행되는 환경은 개발자 PC가 아니라.. 사용자 PC임.
# 그래서..파이썬에서..시스템의 폴더를 만들거나 삭제할 수 있음..이를 위한 별도의 라이브러리(모듈)가 존재함. os 라는 이름의 모듈

# 경로를 지정할때. 상대경로( .. 상위폴더를 지칭하는 경로)
file= open('../aaa.txt', 'w')
file.write('have a good day')
file.close()

# 경로를 모두 현재 위치를 기준으로 한 경로만 해봤음.. 이런 경로를 상대경로 라고 부름
# 특정 경로를 풀네임으로 지정할 수도 있음... 절대경로  라고 부름
#file= open('C:\\aaa.txt','w') # Permission denied: 'C:\\aaa.txt'
#file= open('C:\\Users\\aaa.txt','w') # Permission denied: 'C:\\Users\\aaa.txt'
file= open('C:\\Users\\Admin\\aaa.txt','w')
file.write('aaaa')
file.close()

# 경로에 대한 학습은.. 추후에 배울 모듈 수업에서 다시 소개...
#---------------------------

#5. 문자열 중에.. 여러줄 문자열 ''' ''' 이 것도 당연히 한번에 쓰기 가능함.
file= open('files/bbb.txt', 'w')
data=''' \
안녕하세요.
여러줄의 데이터를 써봅니다.
줄바꿈이 될까요?
this is multiple line message.
'''
file.write(data)
file.close()
#---------------------

#6. 보통 프로그램에서 저장할 데이터들을 ..리스트와 같은 형태로 다루어지는 경우가 많아요.. 
# 리스트데이터들을 저장해보기..-- 쉽게 보기 위해 한줄에 리스트 요소 하나씩 저장되도록..
names= ['강중구','김종경', '유지희', '최준영']
print(names)

#데이터를 원하는 형태로 전처리..
new_names= map( lambda s:s+'\n', names)
new_names= list(new_names)
print(new_names)

file= open('files/902호 학생들.txt', 'w', encoding='UTF-8')
#file.write(names) #error
file.writelines(new_names) # 줄바꿈을 자동으로 해주지 않음. [해결은 원본 데이터들에 줄바꿈 문자를 추가해서 저장]
file.close()
print()
# -----------------------------------------

#7. 파일 다룰때 주의할점.. close()를 잊지 않아야 함..개발자도 사람이라..실수의 여지가 있어서..
#   이를 보완하는 특별한 키워드 등장. with 키워드

with open('ggg.txt', 'w') as file:
    file.write('hello python..')
    
# close()를 안해도 자동으로 with 영역이 종료되면 file객체에게 close()를 요청해줌.




with open('files/long story.txt' , 'r' , encoding='UTF-16')as file:
    contents = file.read()
    print(contents)

print("------------------------------------")

# 대량의 데이터를 파일로부터 읽어서 분석하려면,,,
#일단 대부분의 경우 한줄 단위로 처리함.
#그러려면.. split('\n')을 통해서 한줄 단위로 분리하여 리스트로 만들어 처리
#이 작업이 번거로워서.. 다행히 file객체가 이미 한줄 단위씩
#읽어오는 기능 함수가 잇음.

with open("files/short story.txt" , "r"  , encoding="UTF-8")as file:
    #text = file.read()
    #print(text)
    line = file.readline() # 한줄읽기
    print("첫번째 줄 문자열 :" , line)
print("-"*30)
print()

print("--------------------")

with open("files/short story.txt" , "r" , encoding='utf-8')as f:
    print(f.read())