in_file = None
out_file = None
# 파일열기
in_file = open("C:\workspace\medical1\mem.txt","rb")
# in_file = open("C:\workspace\medical1\jjj.jpg","rb")
# out_file = open('C:\workspace\medical1\jjj.jpg',"wb")
out_file = open("C:/a/m1.txt","wb")
# 역슬래쉬말고 슬래쉬로 하면 작업이 됨

# 파일읽기, 쓰기
while True:
    bin = in_file.read(1)
    if not bin: break
    out_file.write(bin)

# 파일닫기
in_file.close()
out_file.close()
print("복사가 완료되었습니다.")
