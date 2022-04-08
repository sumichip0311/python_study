#랜덤 함수를 가져온다.
import random
#한글 리스트를 만듭니다.
hanguls = list("가나다라마바사아자차카타파하")
#파일을 쓰기 모드로 엽니다.
with open("info.txt", "w") as file:
    for i in range(1000):
        #랜덤값으로 변수를 생성
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        #텍스트를 씁니다.
        file.write("{}, {}, {}".format(name, weight, height))