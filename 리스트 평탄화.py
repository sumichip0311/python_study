def flatten(data):
    output = []
    for item in data:
        if type(item) == list: # 타입이 list이면 재귀함수로 다시 리스트 안으로 들어감
            output += flatten(item)
        else:
            #output.append(item)
            output += [item]
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본 : ", example)
print("변환 : ",flatten(example))