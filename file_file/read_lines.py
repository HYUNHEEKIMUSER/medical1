# readline
f = open("str.txt",'r',encoding = 'utf8')
while True:
    txt = f.readline()
    if txt=="": break
    print(txt, end = ' ')
    
print("모든 파일을 읽어왔습니다.")    

# readlines

f=open("str.txt",'r',encoding ='utf8')
txt_list = f.readlines() #read랑 같음
print(txt_list)
print(txt_list[0])
f.close()  #파일 종료 꼭 적기

# f = open("str.txt",'r',encoding='utf8')
with open("str.txt",'r',encoding='utf8') as f:
    txt_list=f.readlines()
    for txt in txt_list:
        print(txt, end = '')
    print()
    
# 1. 파일열기 
# read(): 모든 문자열을 가져옴
# readline(): 한 줄씩 가져옴
# readlines(): 한 줄씩 리스트 타입에 입력해서 모두 가져옴
# 3. 파일닫기
# 4. 파일확인
import os
if not os.path.exists("str.txt"):
    print("파일이 존재하지 않습니다.")