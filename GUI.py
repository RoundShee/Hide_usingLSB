import tkinter
import os
from tkinter import ttk
from crypt import out_decrypt, col_encrypt
from HideAndSeek import hide_in_bmp, seek_in_bmp


def frame_select(frame_list, n):
    """功能区显示部分"""
    # 选择框架
    for i in range(3):
        if i == n:
            frame_list[n].pack(side='bottom')
        else:
            frame_list[i].pack_forget()


def find_files(directory):
    """返回指定目录下的所有文件名"""
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(file)
    return file_list


def frame0_gene(frame, refresh=0):
    if refresh:
        # 清空当前框架过期所有
        for widget in frame.winfo_children():
            widget.destroy()
    # 加密隐藏功能区
    label = tkinter.Label(frame, text='【加密和隐藏】')
    label.place(x=0, y=0, anchor=tkinter.NW)
    label_0 = tkinter.Label(frame, text='选择其一作为载体:')
    label_0.place(x=0, y=20, anchor=tkinter.NW)
    label_1 = tkinter.Label(frame, text='选择要加密的密文:')
    label_1.place(x=350, y=20, anchor=tkinter.NW)
    label_2 = tkinter.Label(frame, text='如需自定义密码请输入:')
    label_2.place(x=560, y=420, anchor=tkinter.NW)
    # bmp单选框
    bmp_files = find_files("./resource/bmp")
    num_of_bmp = len(bmp_files)
    which_one = tkinter.StringVar()
    which_one.set(0)
    for i in range(num_of_bmp):
        radio = tkinter.Radiobutton(frame, variable=which_one, value=i, text=bmp_files[i])
        radio.place(x=0, y=40 + 20 * i, anchor=tkinter.NW)

    # 密文复选框
    secret_files = find_files("./resource/secret")
    num_of_secret = len(secret_files)
    fill_boxs = []
    for i in range(num_of_secret):
        fill_boxs.append(tkinter.IntVar())
        fill_boxs[i].set(0)
        check = tkinter.Checkbutton(frame, text=secret_files[i], variable=fill_boxs[i], onvalue=1, offvalue=0)
        check.place(x=350, y=40 + 20 * i, anchor=tkinter.NW)

    # 密码输入框
    entry_passwd = tkinter.StringVar()
    entry = tkinter.Entry(frame, width=20, textvariable=entry_passwd, show='*')
    entry_passwd.set('')
    entry.place(x=700, y=420, anchor=tkinter.NW)

    # 刷新按钮
    refresh_button = tkinter.ttk.Button(frame, text='刷新', command=lambda: frame0_gene(frame, refresh=1))
    refresh_button.place(x=750, y=0, anchor=tkinter.NW)
    # 生成
    gene_button = tkinter.ttk.Button(frame, text='生成',
                                     command=lambda: gene_bmp(bmp_files[int(which_one.get())],
                                                              secret_files, fill_boxs, entry_passwd.get()))
    gene_button.place(x=20, y=420, anchor=tkinter.NW)


def gene_bmp(bmp_name, secret_list, secret_list_of_bool, passwd):
    """连接前几天写的各种入口出口的函数
    @:param bmp_name:直接的名字，无路径
    @:param secret_list:密文文件列表
    @:param secret_list_of_bool:tkinter.IntVar()型的列表，对应上面密文是否被选中
    @:param passwd:密码str
    """
    # 进行加密处理
    list_name = []
    num_of_secret = len(secret_list)
    for i in range(num_of_secret):
        if secret_list_of_bool[i].get():
            list_name.append(secret_list[i])
    if passwd is None:
        col_encrypt(list_name)
    else:
        col_encrypt(list_name, passwd)
    # 进行隐藏
    path = "resource/bmp/" + bmp_name
    hide_in_bmp(path, "./resource/encrypted.bin")
    # 删除过程文件
    os.remove("./resource/encrypted.bin")


def frame1_gene(frame, refresh=0):
    """提取密文并解密"""
    if refresh:
        # 清空当前框架过期所有
        for widget in frame.winfo_children():
            widget.destroy()
    # 提取
    label = tkinter.Label(frame, text='【提取与解密】')
    label.place(x=0, y=0, anchor=tkinter.NW)
    label_0 = tkinter.Label(frame, text='选择含密文的BMP:')
    label_0.place(x=0, y=20, anchor=tkinter.NW)
    label_2 = tkinter.Label(frame, text='输入自定义密码:')
    label_2.place(x=600, y=420, anchor=tkinter.NW)
    # 刷新按钮
    refresh_button = tkinter.ttk.Button(frame, text='刷新', command=lambda: frame1_gene(frame, refresh=1))
    refresh_button.place(x=750, y=0, anchor=tkinter.NW)
    # bmp单选框
    bmp_files = find_files("./resource/bmp")
    num_of_bmp = len(bmp_files)
    which_one = tkinter.StringVar()
    which_one.set(0)
    for i in range(num_of_bmp):
        radio = tkinter.Radiobutton(frame, variable=which_one, value=i, text=bmp_files[i])
        radio.place(x=0, y=40 + 20 * i, anchor=tkinter.NW)
    # 密码输入框
    entry_passwd = tkinter.StringVar()
    entry = tkinter.Entry(frame, width=20, textvariable=entry_passwd, show='*')
    entry_passwd.set('')
    entry.place(x=700, y=420, anchor=tkinter.NW)
    # 解密
    decode_button = tkinter.ttk.Button(frame, text='解析',
                                       command=lambda: decode_bmp(bmp_files[int(which_one.get())], entry_passwd.get()))
    decode_button.place(x=20, y=420, anchor=tkinter.NW)


def decode_bmp(file_name, passwd):
    """将选中文件作为含密文载体进行解析"""
    path = "resource/bmp/" + file_name
    seek_in_bmp(path)
    # resource/temp.bin
    if passwd is None:
        out_decrypt()
    else:
        out_decrypt(passwd=passwd)
