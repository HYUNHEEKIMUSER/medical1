a_list=[1,2,3]
try:
    print(a_list[5])
    print(1/0)
    txt = int(input("숫자를 입력하세요"))
    print(txt)
except IndexError:  # 해당 에러에 대한 에러 메세지가 나옴
    print("리스트 주소가 잘못 입력되었습니다")
except Exception as e:
    print("--예외가 발생했습니다")
    print("타입 : ",type(e))
    print(e)
    
# raise 강제로 에러를 발생시키고 싶을 때
# 프로그램 실행 시 알수없는 오류로 인한 프로그램 종료를 방지하기 위해
# try: 프로그램에서 오류가 발생될 것 같은 소스
# except: 예외발생 시 처리 구문소
# else: 예외 발생이 되지 않을 시
# finally: 무조건 실행되는 소스
# except Exception as e: 예외발생 시 예외가 발생이 되었는 지 확인 가능
# valueError, Index, ZeroDivisionError...etc 최고부모: Exception
# raise: 예외를 강제로 발생 시킴 raise: "메모내용"

# try, except, else, finally
print("1. 학생성적입력")
print("2. 학생성적출력")
print("3. 학생성적수정")

num = int(input("순서를 입력하세요 >>"))
if num == 1:
    print("학생성적입력 완성")
    
elif num == 2:
    print("김과장이 해야 할 부분")
    raise "김과장에게 소스를 받아야 함"  # 강제로 에러를 시켜서 알림을 주고 싶을 때
    
elif num == 3:
    print("이대리가 해야 할 부분")
    