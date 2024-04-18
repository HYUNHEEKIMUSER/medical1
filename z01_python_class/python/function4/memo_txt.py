# 파일 1개 저장
# file open
file =open("memo.txt",'w',encoding='utf8')
try : 
# file write
    file.write("안녕하세요 1.\n")
    file.write("안녕하세요 2.\n")
    print(1/0)
    file.write("안녕하세요 3.\n")
    file.write("안녕하세요 4.\n")
except Exception as e:  #무슨 에러가 났는 지 설명해줌
    print("저장 시 에러가 났습니다.")
    print(e)
# 파일 닫기
finally:
    file.close() # 예외 발생 시 예외 발생하지 않아도 무조건 실행
    