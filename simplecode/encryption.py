"""
改进后的凯撒密码加解密实现
采用13错位的方法
加解密可使用相同的代码

version:0.1
author:Jason
date: 2019-06-13
"""


def main():
    code = input('请输入明文')
    for i in code:
        if 'a' <= i <= 'z':
            print(chr(ord('a') + (ord(i) - ord('a') + 13) % 26), end='')
        elif 'A' <= i <= 'Z':
            print(chr(ord('A') + (ord(i) - ord('A') + 13) % 26), end='')
        else:
            print(i, end='')


if __name__ == '__main__':
    main()
