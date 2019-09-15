"""
python慕课
中国大学排名定向网页爬取
version: 0.2
author: Jason
date: 2019-09-13
"""
from bs4 import BeautifulSoup
import requests
import bs4

url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"


def get_html_text(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        text = r.text
        return text
    except requests.HTTPError:
        print("发生异常，请重试!")


def fill_info(text, ulist):
    soup = BeautifulSoup(text, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])
    return ulist


def print_info(ulist, num):
    t_for = "{0:^6}\t{1:{3:}^10}\t{2:{4:}^10}"
    print(t_for.format('排名', '大学名称', '所在地', chr(12288), chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(t_for.format(u[0], u[1], u[2], chr(12288), chr(12288)))


if __name__ == '__main__':
    ulist = []
    text = get_html_text(url)
    num = eval(input("请输入你想查看的大学排名数量"))
    fill_info(text, ulist)
    print_info(ulist, num)
