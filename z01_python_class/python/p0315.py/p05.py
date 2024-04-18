import p03
# 10명의 아이디,패스워드 정보 생성
member = p03.idpw()
print(member)

f = open('mem.txt','w',encoding='utf-8')
for m in member: f.write("{},{}\n".format(m[0],m[1]))
f.close()
print("파일이 저장되었습니다.")