#메모화를 위한 변수 생성
memo = {1: 1, 2: 1}

def fibonacci(n):
    #메모에 값이 있으면 그 값을 리턴해준다
    if n in memo:
        return memo[n]
    #값이 없으면 피보나치 수열을 계산하고 변수에 저장
    output = fibonacci(n - 1) + fibonacci(n - 2)
    #저장된 값을 메모에 저장
    memo[n] = output
    return output

num = int(input("정수를 입력 : "))
print("{}의 피보나치 수열의 값은 {}입니다.".format(num, fibonacci(num)))