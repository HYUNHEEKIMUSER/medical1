# 알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다.
# level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다

capitalletter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
smallletter= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list= []
# for j in capitalletter:
#     for i in range(26):
#         print(i)
    
# capitalletter = A-Z
# smallletter= a-z
word =input("단어를 입력하세요>> ")
list.append(word)

print(list)
for j in smallletter:
    if list[0]==list[-1]:
        print("펠렌트롬 단어입니다.")      
else:
    print("실행이 안됩니다.")  
        

# if list in smallletter:
#     if list[0]==list[-1] and list[1]==list[-2]:
#         print("펠렌트롬 단어입니다.")        
    
# else:
#     print("실행이 안됩니다.")
    