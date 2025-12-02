import requests
address = "https://cdn.pixabay.com/photo/2025/11/14/17/32/pool-9957219_1280.jpg"
response= requests.get(address)
print("응답코드:" , response.status_code)
# print(response.text) # 이미지는 글씨가 아님. 당연히 알수없는 글씨들이 표시됨.
#이미지는 2진수의 픽셀정보를 가지고 있는 데이터 파일임.
print(response.content)
print()


file= open("download/aaa.jpg" , "wb")
file.write(response.content)
print()