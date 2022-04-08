#파일은 크게 텍스트 파일과 바이너리 파일로 나뉜다.
#파일 열기는 open()함수를 사용한다.
#파일 객체 = open(문자열: 파일 경로, 문자열: 모드)
#파일 모드 w = write 모드(새로 쓰기)
#        a = append 모드(뒤에 이어서 쓰기)
#        r = read 모드(읽기 전용)
#파일을 닫을때는 close()함수 사용한다.
#파일 객체.close()

file = open("test.txt", "w")    #파일을 오픈 합니다.
file.write("Hello Python Programming...!")  #파일에 텍스트를 씁니다.
file.close()    #파일을 닫습니다.

#with 키워드는 자동으로 파일을 닫아줘서. 파일을 열고 닫지 않는 실수를 줄일 수 있다.
#with open(문자열: 파일경로, 문자열: 모드) as 파일 객체:
#   문장

with open("test.txt", "w") as file: #파일을 오픈 합니다.
    file.write("Hello Python Programmin...!")   #파일에 텍스트를 씁니다.
    
with open("test.txt", "r") as file: #read() 함수는 데이터를 모두 읽어 출력합니다.
    contents = file.read()
print(contents)