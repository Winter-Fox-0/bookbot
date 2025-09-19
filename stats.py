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
