"""
try:
    에외가 발생할 가능성이 있는 코드
except:
    에외가 발생했을 때 실행할 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
finally:
    예외가 발생하든 않하든 무조건 실행할 코드
"""
#try excpet else finally 구문으로 예외 처리
def equation_of_a_circle():
    try:
        #숫자로 변환합니다.
        number_input_a = int(input("정수를 입력하세요 : "))
        #출력합니다.
        print("원의 반지름: {}".format(number_input_a))
        print("원의 둘례: {}".format(2 * 3.14 * number_input_a))
        print("원의 넓이: {}".format(3.14 * number_input_a * number_input_a))
    except:
        print("정수를 입력하세요!!!")
    else:
        print("예외가 발생하지 않았습니다.")
    finally:
        print("프로그램이 종료 되었습니다.")
        print()
#except 구문에 pass 사용하면 예외가 발생해도 넘어가게 됩니다.
def except_pass():
    list_input_b = ["52", "273", "32", "스파이", "103"] 
    list_number = []
    for item in list_input_b:
        #숫자로 변환해서 리스트에 추가합니다.
        try:   
            float(item) #예외가 발생하면 알아서 다음으로 진행 안 되겠지?
            list_number.append(item) #예외 없이 통과했으면 리스트에 넣기
        except:
            pass
    print("{} 내부에 있는 숫자는".format(list_input_b))
    print("{} 입니다.".format(list_number))
    print()
#finally 활용
def write_text_file(filename, text):
    try:
        #파일을 엽니다.
        file = open(filename, "w")
        return #return 을 해주면 빠져 나가게 됩니다.
        #텍스트를 입력합니다.
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        #중간에 오류로 빠져나가도 무조건 파일을 닫게 됩니다.
        file.close()
equation_of_a_circle()
except_pass()