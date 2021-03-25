def generateDocument(characters, document):
    char_dict = string2dict(characters)
    doc_dict = string2dict(document)

    for key in doc_dict.keys():
        if key not in char_dict or char_dict[key] < doc_dict[key]:
            return False
    return True


def string2dict(string):
    res = {}
    for c in string:
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res


def generateDocument(characters, document):
    char_dict = string2dict(characters)

    # 利用-法 两个loop 就结束
    for c in document:
        if c not in char_dict or char_dict[c] == 0:
            return False
        char_dict[c] -= 1
    return True


def string2dict(string):
    res = {}
    for c in string:
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res