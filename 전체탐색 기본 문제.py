min_people = 2  #앉힐 수 있는 최소 사람수
max_people = 10 #앉힐 수 있는 최대 사람수
peoples = 100   #전체 사람의 수
memo = {}
#트리 : 노드의 값 / 엣지의 값
def problem(left_people, seated_people): #남은사람수, 앉힌사람수
    key = str([left_people, seated_people])
    #종료 조건
    if key in memo:
        return memo[key]
    if left_people < 0:  #무효하니 0리턴
        return 0
    if left_people == 0: #유효하니 1리턴
        return 1
    #재귀 처리
    count = 0
    for i in range(seated_people, max_people + 1):
        count += problem(left_people - i, i)
    #메모화 처리
    memo[key] = count
    #종료
    return count

print(problem(peoples, min_people))