"""
try:
    예외가 발생할 가능성이 있는 구문
except 예외의 종류 as 예왜 객체를 활용할 변수 이름:
    예외가 발생했을 때 실행할 구문
"""
#예외의 종류가 뭔지 모를 때는 모든 예외의 종류를 칭하는 Exception을 사용합니다.
#except 구문은 여러개 사용 가능하다.
list_number = [52, 273, 32, 72, 100]
try:
    #숫자를 입력 받음
    number_input = int(input("0 ~ 4의 정수를 입력하세요: "))
    #리스트 요소 출력
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as e:
    #ValueError가 발생하는 경우
    print("정수를 입력해 주세요!!!")
    print(type(e), e)
except IndexError as e:
    #IndexError가 발생하는 경우
    print("0 ~ 4의 정수만 입력해 주세요!!!")
    print(type(e), e)
except Exception as e:
    #이외의 예외가 발생한 경우
    print("알 수 없는 예외가 발생했습니다!!!")   
