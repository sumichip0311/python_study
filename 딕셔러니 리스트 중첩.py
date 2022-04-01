# type("문자열") is str -> 문자열인지 확인
# type([]) is list -> 리스트인지 확인
# type({}) is dict -> 딕셔너리인지 확인
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is list:
        for key_list in character[key]:
            print("{} : {}".format(key, key_list))
    elif type(character[key]) is dict:
        for key_dict in character[key]:
            print("{} : {}".format(key_dict, character[key][key_dict]))
    else:
        print("{} : {}".format(key, character[key]))