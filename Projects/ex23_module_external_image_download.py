import requests
address = "https://cdn.pixabay.com/photo/2025/11/14/17/32/pool-9957219_1280.jpg"
address = 'https://media.istockphoto.com/id/628097352/ko/%EC%82%AC%EC%A7%84/%EC%8B%A0%EC%84%A0%ED%95%9C-%EC%95%BC%EC%B1%84%EB%A9%B4.jpg?s=2048x2048&w=is&k=20&c=Y9kL6N79vsEF6YGuOkIjzUuiUFdiseJk4cwZFk1An3E='
address = input("다운로드를 원하는 링크주소를 입력하세요: ")
response= requests.get(address)
print("응답코드:" , response.status_code)
# print(response.text) # 이미지는 글씨가 아님. 당연히 알수없는 글씨들이 표시됨.
#이미지는 2진수의 픽셀정보를 가지고 있는 데이터 파일임.
print(response.content)
print()


# file= open("download/aaa.jpg" , "wb")
# file.write(response.content)
print()
# 위 작업은 파일명을 고정적으로 하기에 덮어씌워질 문제가 있다.
# 그래서 날짜와 시간정보를 이용하여 파일명을 생성하여보겠다.
import datetime
now=datetime.datetime.now()
print(now)



# print(str(now.year)+str(now.month)+str(now.second))


# file_name = 'ING_' + str(now)
# file_name = file_name.replace(' ', '').replace('-','').replace(':','').replace('.','')
# file_name = file_name + ".png"
# print(file_name)


# 간소화
file_name = 'IMG'+now.strftime('%y%m%d%H%M%S')+'.png'
print(file_name)




file=open('download/'+ file_name , "wb")
file.write(response.content) #바이너리 데이터를 파일에 쓰기(저장)
file.close()
