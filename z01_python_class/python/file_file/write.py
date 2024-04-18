# str.txt 파일의 내용을 모두 출력하시오
f = open('str.txt','r',encoding='utf-8')
content = f.read()
while True:
    content = f.readline()
    if content.strip() == "": break
    print(content,end="")
f.close()
# str.txt 파일 내용을 읽어와서 str1.txt에 그 내용을 추가해보세요.
f = open('str.txt','r',encoding='utf-8')
ff = open('str1.txt','a',encoding='utf-8')
while True:
    if content.strip() == "": break
    ff.write(content)
    
f.close()    
ff.close()
         
             