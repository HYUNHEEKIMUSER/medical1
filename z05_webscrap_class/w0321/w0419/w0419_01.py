capitalletter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
smallletter= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word=[]
reverse_list=[]

myword = input("단어를 입력하세요 >>")

reversed_word="".join(reversed(myword))
print("거꾸로된 단어: ",reversed_word)
word.append(myword)
reverse_list.append(reversed_word)
print("거꾸로된 단어를 넣은 리스트: ",reverse_list)
a = reverse_list.split(sep=",")
print(a)
# for i in range(len(reverse_list)):
#    if reverse_list[i] in capitalletter:
#       print("소문자만 됩니다.")
#       break
#    else:
#          for i in range(len(reverse_list)):
#             if reverse_list[i]==word[i]:
#                 print("true")
#             else:
#                 print("false")
    