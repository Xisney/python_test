from threading import Thread
import os
import math

"""
多线程模型应用。
实现一个统计文本文件中单词频率的程序。
将文本分为N段，每段交由一个独立的线程处理，
线程统计该段中单词的频率。主进程等待所有线程执行完毕，
通过各线程的输出结果来统计整体的单词频率。
"""


# 对每段的单词进行计数
def count(line):
    global res  # 使用字典存放最终结果
    for key in line:
        res[key] = res.get(key, 0) + 1  # 字典的key为单词本身，未得到item则为0

    return res


if __name__ == '__main__':
    try:
        f = open('demo.txt', 'r', encoding='utf-8')
    except FileNotFoundError:  # 捕获异常
        print('文件不存在！')
    except UnicodeEncodeError:
        print('解码错误！')
    else:

        c = list(f.readlines())
        length = len(c)
        content = []
        symbol = [',', '?', '.', ':', ';', '!', '"', "'"]
        res = {}  # 存放最终结果
        threads = []  # 用于存放线程

        for i in range(length):
            c[i] = c[i].strip()

        for i in range(6):  # 使得线程数最大值为六,将文本划分为六段
            content.append(c[:math.ceil(length / 6)])
            del c[:math.ceil(length / 6)]

        f.close()

        # 清洗数据，将非单词字符全部替换为空格
        for i in range(len(content)):
            t = content[i]
            flag = 0
            for j in symbol:
                if flag == 0:
                    t = ' '.join(t).replace(j, ' ')
                    flag = 1
                else:
                    t = t.replace(j, ' ')
            content[i] = t

        for i in range(len(content)):
            threads.append(Thread(target=count, args=(content[i].split(),)))
            threads[i].start()  # 开启进程

        for i in threads:
            i.join()  # 等待进程结束

        res = list(res.items())
        res.sort(key=lambda x: x[1], reverse=True)  # 按频率降序排列

        # 打印输出，左边为单词，右边为频率
        for k in res:
            print(k)
