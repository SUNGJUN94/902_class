# 100
# #이렇게 값만 끄면 화면에 데이터가 출력되지 않아요.
# #화면 출력... 데이터 유령에 따라 출력해보기.
# print(10)
# print(3.14)

# print("Hello, World!")
# # 여러 값을 한 줄에 출력할 때는 쉼표(,)로 구분합니다.
# print(10,20)
# print(10,20,"hello",3.14,False)

# #문자열 안에 작은 따옴표를 활용하여 문자열 안에 따옴표를 표현하기
# print("나는 '홍길동'입니다.")

# #문자열의 간격 맞추기
# print('이름' , '\t' , '국어' , '\t' , '영어' , '\t' , '수학')
# print('홍길동' , '\t' , 85 , '\t' , 90 , '\t' , 75)
# print('김철수' , '\t' , 100 , '\t' , 4 , '\t' , 72)

# # 위 방법 외에 간격 맞추기
# print('-' * 30)
# print('이름' , '국어' , '영어' , '수학', sep='\t')
# print('홍길동' , 85 , 90 , 75, sep='\t')
# print('김철수' , 100 , 4 , 72, sep='\t')


#-------------------

# print("나는 {}입니다.".format("홍길동"))

# # 이외 방법
# name = "홍길동"
# print(f"나는 {name}입니다.")
# print()


















# print("===================================")
# num1 = input("첫 번째 숫자를 입력하세요: ")
# num2 = input("두 번째 숫자를 입력하세요: ")

# print((num1)+(num2))  # 문자열 결합

# print(int(num1) + int(num2))  # 정수로 변환 후 덧셈

# print("===================================")

# num1 = input("숫자를 입력하세요.")

# for i in range(1,10):
#     print(f"{num1} x {i} = {num1}*{i}")

# print("===================================")

# import random
# print(random.randint(1,100))

print("===================================")

import random



# a = random.randint(1,100)
# b = random.randint(1,100)

# def total_damage(a,b):

#     if a > 30:
#         print(f"데미지가 무시되었습니다.")

#     elif 30<=a<=50:
#         print(f"1의 데미지가 들어갔습니다.")

#     elif 50<= a <= 100:
#         print(f"5의 데미지가 들어갔습니다.")
        
#     if b > 30:
#         print(f"데미지가 무시되었습니다.")

#     elif 30<=b<=50:
#         print(f"1의 데미지가 들어갔습니다.")

#     elif 50<= b <= 100:
#         print(f"5의 데미지가 들어갔습니다.")
#     else: 
#         print(f"{total_damage(a+b)}의 데미지가 들어갔습니다.")

# 위 코드를 완성 해 주세요.

a = random.randint(1,100)
b = random.randint(1,100)

total_damage = 0

if a > 30:
    damage_a = 0

elif 30 <= a <= 50:
    damage_a = 1

else:
    damage_a = 5

if b > 30:
    damage_b = 0

elif 30 <= b <= 50:
    damage_b = 1

else:
    damage_b = 5


total_damage = damage_a + damage_b

print(f"{total_damage}의 데미지가 들어갔습니다.")

if total_damage <= 6:
    c = random.randint(1,100)

    if c > 30:
        damage_c = 0

    elif 30 <= c <= 50:
        damage_c = 1

    else:
        damage_c = 5

    total_damage = total_damage + damage_c

    print(f"추가 공격으로 {damage_c}의 데미지가 들어갔습니다.")
    if total_damage == 6:
        print("최종 데미지가 6이 되어 보스를 가까스로 죽였습니다.")

    if total_damage < 6:
        print("최종 데미지가 6이 되지 않아 보스가 살아남았습니다.")

    if total_damage > 6:
        print("최종 데미지가 6을 넘겨 보스를 사망 시켰습니다.")    
else:
    print("보스를 사망 시켰습니다.")
    
