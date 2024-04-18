import os 
# # # 폴더가 존재하는 지 확인
# if os.path.exists("hello"):
#     os.mkdir("hello")
# else:
#     os.rmdir("hello")
    
# # # # 파일생성 1
# with open ("students.txt","w") as f:
#     f.write("1,'홍길동',100,99,87,286,95.33,2")

# # encoding="utf-8" -> 한글이 깨져서 나올 때는 이 코드를 넣어주면 잘 나옴

# # # # # 파일생성 2
# f = open ("students.txt","w",encoding="utf-8") 
# f.write("1,'홍길동',100,99,87,286,95.33,2\n")
# f.write("2,'유관순',98,93,87,278,92.67,3")
# f.close()  #파일 닫기

# # 파일 읽어오기
t_list = []

out_f = open("students.txt","r",encoding="utf-8")
while True:
    txt = out_f.readline() #한 줄씩 읽어오기
    if txt == "":
        break
    print(txt, end = '')
    t_list.append(txt)
print()
print(t_list)

out_f.close() #삭제 전 닫아주기

# 파일삭제
os.remove("studnets.txt")