# # a=input("문자를 입력하세요")
# # print("현재 입력한 문자길이: ",len(a))
a = [1234,11111,1,145,20,1323456547]
# print(len(str(a[0])))
# # print(len(a)) ->각 요소 갯수

for i in a:
    print(f"{len(str(i))} 문자 길이임") # 각 요소 안의 갯수
    
for i in a:
    if i%2 ==0:
        print("숫자 : {}, 길이 {}".format(i, len(str(i))))
        
title ="혼자공부하는파이썬수업"
for i in range(len(title)):
    print(title[i])
    
print(1,2,3,4,sep="*")
title = "안녕하세요"
for i in range(len(title)):
    print(title[(len(title)-1)-i], end = " ")
    
shape_list =['diamond',"spade",'heart','clover']
for i in shape_list:
    print(i.upper()) # 다 대문자
    print("-"*40)
    print(i.title()) # 앞에만 대문자
    print("-"*40)
    print(i.swapcase()) # 다 대문자
    print("-"*40)
    print(i.lower())
    print("-"*40)