score = int(input("숫자"))

if score >= 90:
    if 100 == score or score >=98:
        print("A+")
    elif 97<= score or score >=95 :
        print("A")
    elif 89 < score or score < 94 :
        print("A-")
elif score >= 80 :
    if 89>= score or score >= 88 :
        print("B+")
    elif 87<= score or score >= 85 :
        print("B")
    elif 79 < score or score >= 84 :
        print("B-")
elif score >= 70:
    if 79 >= score or score >= 78 :
        print("C+")
    elif 78<score or score >=75 :
        print("C")
    elif 69 < score or score >= 74:
        print("C-")
else :
    print("F")
    
