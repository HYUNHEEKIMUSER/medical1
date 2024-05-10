import os 

print("현재 운영체재: ",os.name)
print("현재 폴더위치: ",os.getcwd())
print("현재 폴더내 파일들을 표시: ",os.listdir())

# 폴더생성
# os.mkdir("hello")   # c 드라이브->workspace ->현재 폴더위치에 폴더를 생성해줌
# os.rmdir("hello")   # 폴더삭제

# 파일생성
with open ("students.txt","w") as f:
    f.write("1,'홍길동',100,99,87,286,95.33,2")
    
str1 = "1,'홍길동',100,99,87,286,95.33,2"
s_list = str1.split()
for i in s_list:
    print(i)