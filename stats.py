def word_counter(string):
    return len(string.split())

def char_count(string):
    char_dic = {}
    get_char = list(string.lower())
    for char in get_char:
        if char not in char_dic:
            char_dic[char] = 0
        char_dic[char] += 1
    return char_dic

def split(dic):
    char_list = []
    for char in dic:
        obj = {"char":char,"num":dic[char]}
        char_list.append(obj)
    char_list.sort(key=get_num,reverse=True)
    return char_list

def get_num(item):
    return item["num"]
