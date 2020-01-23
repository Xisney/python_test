"""
暑期python学习
目前内容：利用tkinter进行简单gui编程
https://blog.csdn.net/ahilll/article/details/81531587
version:0.1
author:Jason
date: 2019-08-11
"""
import tkinter as tk

# 创立主窗口对象
win = tk.Tk()
# 标题
win.title('windows')
# 设置窗口大小
win.geometry('500x300')
# 设置标签并放置
label = tk.Label(win, text='    ', bg='green')
label.pack()
counter = 0


def do_job():
    global counter
    label.config(text='do' + str(counter))
    counter += 1


# 创建一个菜单栏，理解为一个容器，位于窗口的上方
menubar = tk.Menu(win)
# 创建一个file菜单项（默认不下拉，包含new,open,save,exit功能）
filemenu = tk.Menu(menubar, tearoff=0)
# 将空菜单命名为File，并放入菜单栏，即装入容器
menubar.add_cascade(label='File', menu=filemenu)

# 向菜单项中加入功能项
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()  # 添加一条分割线
filemenu.add_command(label='Exit', command=do_job)
# 创建一个edit菜单项（默认不下拉，含有cut,copy,paste功能）
editmenu = tk.Menu(menubar, tearoff=0)
# 将菜单栏命名为edit,并放入菜单栏，即放入那个容器
menubar.add_cascade(label='Edit', menu=editmenu)

# 在edit中加入功能项
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

# 创建二级菜单
submenu = tk.Menu(filemenu)
# 将创建的二级菜单放入filemenu中
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
# 创建二级菜单中的菜单命令
submenu.add_command(label='submenu_1', command=do_job)

# 创建edit的子菜单
editmenu.add_separator()  # 添加下划线
submenu1 = tk.Menu(editmenu)
editmenu.add_cascade(label='all', menu=submenu1)
submenu1.add_command(label='add', command=do_job)
# 创建完毕，配置让菜单栏显示
win.config(menu=menubar)
# 开启主循环
win.mainloop()
