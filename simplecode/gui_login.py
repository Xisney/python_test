"""
暑期python学习
目前内容：融会贯通，综合实践
https://blog.csdn.net/ahilll/article/details/81531587
version:0.1(仿写于以上网址)
author:Jason
date: 2019-08-16
"""
import tkinter as tk
import tkinter.messagebox
import pickle  # 用于数据储存

# 实例化窗口
win = tk.Tk()
# 设置窗口
win.title('Welcome to my site!')
win.geometry('400x300')

# 创建画布并导入图像
canvas = tk.Canvas(win, width=400, height=115, bg='green')
image_file = tk.PhotoImage(file='pic.gif')
canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
tk.Label(win, text='Welcome', font=('Arial', 16)).pack()

# 设置输入的用户信息
tk.Label(win, text='User name:', font=('Arial', 14)).place(x=10, y=150)
tk.Label(win, text='Password:', font=('Arial', 14)).place(x=10, y=190)

# 建立entry输入框
# 用户名输入框
var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(win, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120, y=155)
# 密码输入框
var_usr_pas = tk.StringVar()
entry_usr_pas = tk.Entry(win, textvariable=var_usr_pas, font=('Arial', 14), show='*')
entry_usr_pas.place(x=120, y=195)


# 定义用户登录功能
def usr_login():
    # 定义变量用以获取用户输入的信息
    usr_name = var_usr_name.get()
    usr_pas = var_usr_pas.get()

    # 因第一次文件不存在，故而设置异常捕获
    # 利用pickle.dump()将输入的信息存入文件
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usr_info = pickle.load(usr_file)
    except FileNotFoundError:
        # 没有读取到文件，所以在这一步直接创建文件
        # 用字典来管理用户名和密码，用户名->密码
        with open('usrs_info.pickle', 'wb') as usr_file:
            usr_info = {'admin': 'admin'}
            # 将信息存入文件
            pickle.dump(usr_info, usr_file)
            usr_file.close()  # 此处必须先关闭，否则load()将产生异常，Why?????

    # 用户验证成功，跳出一个弹窗，并欢迎用户
    if usr_name in usr_info:
        if usr_pas == usr_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='好久不见' + usr_name)
        # 用户名存在，但输入密码错误，使用弹窗提醒
        else:
            tk.messagebox.showerror(message='您输入的密码有误，请重试！')
    # 若用户名不存在
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome', 'you have not sign up.Sign up now?')
        if is_sign_up:
            usr_sign_up()


# 用户注册
def usr_sign_up():
    def sign_up_to():
        # 得到用户输入的信息
        nn = new_usr.get()
        nps = new_pas.get()
        npc = new_pas_confirm.get()

        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'this user has existed!')
        elif nps != npc:
            tk.messagebox.showerror('Error', 'password and confirm password must be same!')
        else:
            exist_usr_info[nn] = nps
            usr_file = open('usrs_info.pickle', 'wb')  # 为什么打开方式不能是ab?????
            pickle.dump(exist_usr_info, usr_file)
            usr_file.close()
            tk.messagebox.showinfo('Welcome', 'you have signed up successfully')
            # 完成创建后销毁窗口
            sign_win.destroy()

    # 创建注册用户时的二级窗口
    sign_win = tk.Toplevel(win)
    sign_win.title('Please sign up')
    sign_win.geometry('300x200')

    # 位于二级窗口的三个部件，及其值的获取
    # user name
    new_usr = tk.StringVar()
    new_usr.set('example@python.com')
    tk.Label(sign_win, text='User name:').place(x=10, y=10)
    entry_new_usr = tk.Entry(sign_win, textvariable=new_usr)
    entry_new_usr.place(x=130, y=10)

    # password
    new_pas = tk.StringVar()
    tk.Label(sign_win, text='Password:').place(x=10, y=50)
    entry_new_pas = tk.Entry(sign_win, textvariable=new_pas, show='*')
    entry_new_pas.place(x=130, y=50)

    # confirm_password
    new_pas_confirm = tk.StringVar()
    tk.Label(sign_win, text='confirm password').place(x=10, y=90)
    entry_confirm_pas = tk.Entry(sign_win, show='*', textvariable=new_pas_confirm)
    entry_confirm_pas.place(x=130, y=90)

    # Button
    btn_confirm_sign_up = tk.Button(sign_win, text='Sign up', command=sign_up_to)
    btn_confirm_sign_up.place(x=180, y=120)


# 设置主窗口的login 和 sign up按钮
button_login = tk.Button(win, text='Login', command=usr_login)
button_sign_up = tk.Button(win, text='Sign up', command=usr_sign_up)
button_login.place(x=120, y=220)
button_sign_up.place(x=200, y=220)

# 开启主循环
win.mainloop()
