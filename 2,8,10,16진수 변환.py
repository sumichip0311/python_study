number = int(input("정수를 입력 : "))

binary_number = "{:b}".format(number)   #2진수
octal_number = "{:o}".format(number)    #8진수
hexadecimal_nuber = "{:x}".format(number)   #10진수
#int(문자열, 바꿀진수)로 10진수 변환
print("2진수 변환:{} -> 10진수 변환:{}".format(binary_number,int(binary_number, 2)))
print("8진수 변환:{} -> 10진수 변환:{}".format(octal_number,int(octal_number, 8)))
print("16진수 변환:{} -> 10진수 변환:{}".format(hexadecimal_nuber,int(hexadecimal_nuber, 16)))