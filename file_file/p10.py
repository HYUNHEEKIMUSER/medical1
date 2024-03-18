# k001.cvs 파일에서 전국 인원수를 출력하세요
f = open('k001.csv','r',encoding='utf-8')

cnt = 0
sum = 0
while True:
    content = f.readline()
    if cnt==0:
        cnt +=1
        continue
    if content == '': break
    list = content.split(",")
    list[1] = int(list[1])
    sum += list[1]
print("총 합: ",sum)

f.close()