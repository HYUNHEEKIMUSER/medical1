# 파일열기
f = open("c:/workspace/medical1/h0327/aaa/member2.csv",'r',encoding='utf8')
# f = open("h0327/aaa/member2.csv",'r',encoding='utf8')도 가능
# with open("member.csv",'r',encoding='utf8') as f:면 close안해도 됨
# 파일읽기
# 상대경로:  medical1 폴더 안 member.csv  medical1>h0327>aaa 폴더 안 h0327/aaa/member2.csv 
# 절대경로: c:/workspace/medical1/h0327/aaa/member2.csv
while True:
    content = f.readline()
    if content =='':break
    mem = content.split(",")
    print(mem[0],mem[1])
# 파일닫기
f.close()