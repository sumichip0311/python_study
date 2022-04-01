#리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것]
#리스트 내포를 이용하여 1~100 사이에 있는 숭자중 2진수로 변환했을 때 0이 하나만 포함된 숫자를 찾고 그 숫자들의 합을 구함
#cont함수로 문자열을 찾음
ouput = [value for value in range(100+1) if "{:b}".format(value).count("0") == 1]

for i in range(1, 100+1):
    print("{} : {}".format(i, "{:b}".format(i)))
    
print("합계 : ", sum(ouput))