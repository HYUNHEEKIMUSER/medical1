while True:
  word = input("영어단어를 입력하세요 >>")
  if word.isalpha():
    word = word.lower()
    chk = 0
    for i in range(len(word)//2):
      if word[i] == word[len(word)-i-1]:
        chk += 1
        print(word[i],chk)
      else:
        print("팰린드롬이 아닙니다")
        break
    if len(word)//2 == chk:
      print("팰린드롬입니다")
  else:
    print("영어단어가 아닙니다. 다시 입력하세요")
    break