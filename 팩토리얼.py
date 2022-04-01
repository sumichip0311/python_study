#재귀함수 팩토리얼
def factorial(n):
    if n == 0:
        return 1
    #조기리턴 형식 esle 를 해도 되고 안해도됨 
    return n * factorial(n-1)
number = int(input("정수 입력 : "))
print("{}의 팩토리얼은 {}입니다.".format(number, factorial(number)))