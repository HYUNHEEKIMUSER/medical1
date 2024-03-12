def multi(num1,num2):
    result_list =[] 
    result_list.append(num1+num2)
    result_list.append(num1-num2)
    return result_list

    
num1 = int(input("숫자를 입력하세요 >>"))
num2 = int(input("숫자를 입력하세요 >>"))
result_list= multi(num1,num2)
print("결과값: ",result_list)


# 전역변수 리스트르 매개변수로 전달 시 return을 받지 않아도 됨
