import os
#폴더를 읽어 들이는 함수
def read_folder(path):
    #폴더의 요소 읽어 들이기
    output = os.listdir(path)
    #폴더 요소 구분하기
    for item in output:
        if os.path.isdir(path + "/" + item):
            #폴더라면 계속 읽어 들이기
            print("폴더: ", item)
            read_folder(path + "/" + item)
        else:
            #파일이면 출력하기
            print("파일: ", item)            
read_folder(".")
        