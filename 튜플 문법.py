#튜플은 리스트와 비슷한 자료형 이지만 한번 결정된 요소를 바꿀 수 없다.
tuple_test1 = (10, 20, 30) 
tuple_test2 = 40, 50, 60    #기본적으로 ()사용하지만 생략해도 된다
a, b, c = 1, 2, 3   #여러개 선언 가능
tuple_test3 = (70,) #요소를 하나만 가지는 튜플을 선언하려면 쉼표를 넣어야된다.
print(tuple_test1)
print(tuple_test2[0])
print("a: {} b: {} c: {}".format(a, b, c))

a, b = b, a #값 교환 가능
print("a:{}  b: {}".format(a, b))

def test(): #함수의 리턴에 튜플을 사용하면 여러 개의 값을 리턴하고 할당 가능
    return (100, 200)
j, k = test()
print("j: {} k: {}".format(j, k))