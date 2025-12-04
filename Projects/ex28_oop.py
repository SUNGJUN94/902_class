name1 = 'sam'
name2 = 'robin'
kor1 = 90
kor2 = 85
eng1 = 80
eng2 = 95
math1 = 100
math2 = 90
aver1 = (kor1 + eng1 + math1) / 3
aver2 = (kor2 + eng2 + math2) / 3
print(name1, kor1, eng1, math1, aver1)
print(name2, kor2, eng2, math2, aver2)

# class를 사용하려고 하는데 선생님이 class를 사용하는 이유에 대해서 설명을 하고있는데 잘 이해가 안가.
# class를 사용하는 이유에 대해서 설명해줘.
# class는 객체 지향 프로그래밍(OOP)의 핵심 개념 중 하나로, 코드의 재사용성과 유지보수성을 높이기 위해 사용됩니다.
# class를 사용하면 관련된 데이터와 기능(메서드)을 하나의 단위로 묶을 수 있습니다.
# 이를 통해 코드의 구조를 더 명확하게 만들고, 동일한 구조를 가진 여러 객체를 쉽게 생성할 수 있습니다.
# 예를 들어, 학생 정보를 다루는 프로그램에서 학생마다 이름, 국어, 영어, 수학 점수를 저장하고 평균을 계산하는 기능이 필요할 때,
# class를 사용하면 학생 객체를 쉽게 생성하고 관리할 수 있습니다.
print("*"*50)
aaa = ['sam' , 70,80,90,80.0]
bbb = ['robin' , 40,30,50,60,50.0]
print(aaa)
print(bbb)

print("학생의 국어 성적:" , aaa[1])
print("학생 2 의 국어 성적 : " , bbb[1])
print("*"*50)