"""
BM算法匹配字符串
"""


def get_table(text, p):
    # 返回坏符号移动表
    text = set(list(text))
    table = {}
    m = len(p)
    for i in text:
        table[i] = m
    for j in range(m - 1):
        if p[j] in text:
            table[p[j]] = m - 1 - j
    return table


def get_suffix(p: str) -> list:
    # 返回好后缀移动表
    suffix = []
    p = str(reversed(p))  # 模式串逆置
    for i in range(len(p) - 1):
        temp = p[:i]  # 得到后缀
        f = p.index(temp)
        if f:
            suffix.append(f)
        elif i == 0:
            suffix.append(len(p))
        else:
            suffix.append(suffix[i - 1])
    return suffix


def get_index(text, p):
    # 对字符串进行匹配
    table = get_table(text, p)
    suffix = get_suffix(p)

    for i in range(len(text)):
        flag = 0
        for k in range(len(p) - 1, -1, -1):
            if i + k >= len(text):
                return -1
            if text[i + k] == p[k]:
                flag += 1
            elif flag == 0:
                d1 = max([1, table[text[i + k]]])
                i += d1
                break
            else:
                d1 = max([1, table[text[i + k]]])
                d2 = suffix[flag]
                i += d1 if d1 > d2 else d2
                break
        if flag == len(p):
            return i
    return -1


if __name__ == '__main__':
    text = "ARUOWRHJFEWIOOGRW"
    p = input('请输入模式串:')
    res = get_index(text, p)
    if res == -1:
        print("匹配失败")
    else:
        print("匹配成功\n模式串在文本中的开头索引为%d" % res)
