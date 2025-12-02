import csv
with open('files/member.csv' , 'r' , encoding="UTF-8") as f:
    read = csv.reader(f)
    # for row in read:
    #     print(row)
    data= list(read)

print(data)

print("-"*29)


with open("files/dummy_large.csv" , "r" , encoding="UTF-8")as file:
    file = csv.reader(file)
    data = list(file)
# print(data)

# for i in data:
    # print(i)

# for row in enumerate(data):
#     print(row)

# for idx , row in enumerate(data):
#     if idx<10:
#         print(row)


print("-"*30)


for i,row in enumerate(data):
    if int(i)<10:
        print(i,row)

print("="*50)

for i in data[1:]:
    if i[3]=="daejeon" and 20<=int(i[2])<=30 and 50 <int(i[4])<60   :
        print(i)