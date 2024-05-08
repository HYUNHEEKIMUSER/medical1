import operator

fruits = {'peach':'복숭아','orange':'오렌지','apple':'사과',"pear":"배",
          'grapes':'포도','mango':'망고','kiwi':'키위'}
answer = 0
wrong = 0
# 총 몇개 맞췄는 지
for f in fruits:
    eng_in = input("{}를 영어로 입력하세요".format(fruits[f]))
    if eng_in == f:
        print("정답입니다")
        answer +=1
    elif eng_in!=f:
        print("틀렸습니다. 정답은: {}입니다".format(fruits[f]))
        wrong +=1
print("[문제체크]")
print('총 :{}'.format(answer+wrong))
print("정답 {}".format(answer))
print("오답 {}".format(wrong)) 
       