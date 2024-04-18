txt = "파이썬 파일 중에 a.txt 이 폴더에 존재합니다.hwp"
print(txt.find('a.txt'))  #10번 줄에 있다.
print(txt.find("자바")) #없으면 -1출력
print(txt.count("파이썬")) #전체에 있는 갯수 출력
print(txt.count('.py')) #없으면 0
print(txt.endswith('.hwp')) #제일 뒤에 해당문자열로 끝나면 True
print(txt.endswith(".")) #