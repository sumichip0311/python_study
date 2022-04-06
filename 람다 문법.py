#map(함수, 리스트) 함수는 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성해 주는 함수
#filter(함수, 리스트) 함수는 리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로 새로운 리스트를 구성해 주는 함수
def power(item): #기본 형식 함수
    return item * item
def under_3(item):
    return item < 3
#리스트 선언
list_input_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output_a = map(power, list_input_a)
output_b = filter(under_3, list_input_a)
#제네레이터라서 그냥 출력하면 object로 나오는데 list로 변환후 사용가능하다
print("map()함수 : {}".format(list(output_a)))  
print("filter()함수 : {}".format(list(output_b)))
#람다는 함수를 간단하게 선언하기 위한 방법입니다.
#lambda 매개변수: 리턴값
power_lambda = lambda x: x * x #람다 형식 함수
under_3_lambda = lambda x: x < 3
print("람다 형식 map(): {}".format(list(map(power_lambda, list_input_a))))
print("람다 형식 filter(): {}".format(list(filter(under_3_lambda, list_input_a))))
#람다를 사용하면 따로 함수를 사용안하고 바로 출력가능하다
print("바로 출력: {}".format(list(map(lambda x: x * x, list_input_a))))
print("바로 출력: {}".format(list(filter(lambda x: x < 3, list_input_a))))