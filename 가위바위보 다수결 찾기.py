peoples = 100   #사람수
def rock_scissors_paper(total_num):
    count = 0
    for rock in range(0, total_num + 1):    #바위
        r_num = total_num - rock
        for scissors in range(0, r_num + 1):    #가위
            paper = r_num - scissors    #보
            rsp_list = [rock, scissors, paper]
            if rsp_list.count(max(rsp_list)) == 1: #리스트로 만들어 최대값이 1나인수를 찾는다
                count += 1
    return count
print(rock_scissors_paper(peoples))