import tkinter
import os
from tkinter import ttk


# 界面根基
root = tkinter.Tk()
root.title('Encrypt Hide && Seek Decrypt')
root.geometry('854x480')


def frame_select(frame_list, n):
    """功能区显示部分"""
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


# 功能区框架列表
frame_list = []
for i in range(3):
    frame_i = tkinter.Frame(root, height=451, width=854)
    frame_list.append(frame_i)
# 顶部按钮
top_button_0 = tkinter.ttk.Button(root, text='加密隐藏', command=lambda: frame_select(frame_list, 0))
top_button_0.place(x=10, y=0, anchor=tkinter.NW)

top_button_1 = tkinter.ttk.Button(root, text='提取解密', command=lambda: frame_select(frame_list, 1))
top_button_1.place(x=97, y=0, anchor=tkinter.NW)

top_button_2 = tkinter.ttk.Button(root, text='帮助', command=lambda: frame_select(frame_list, 2))
top_button_2.place(x=184, y=0, anchor=tkinter.NW)

# 加密隐藏功能区
label = tkinter.Label(frame_list[0], text='【加密和隐藏】')
label.place(x=0, y=0, anchor=tkinter.NW)
label_0 = tkinter.Label(frame_list[0], text='选择其一作为载体:')
label_0.place(x=0, y=20, anchor=tkinter.NW)
label_1 = tkinter.Label(frame_list[0], text='选择要加密的密文:')
label_1.place(x=350, y=20, anchor=tkinter.NW)
# bmp单选框
bmp_files = find_files("./resource/bmp")
num_of_bmp = len(bmp_files)
which_one = tkinter.StringVar()
which_one.set(0)
for i in range(num_of_bmp):
    radio = tkinter.Radiobutton(frame_list[0], variable=which_one, value=i, text=bmp_files[i])
    radio.place(x=0, y=40+20*i, anchor=tkinter.NW)
# 测试单选框功能
# test_button = tkinter.ttk.Button(frame_list[0], text='which_one', command=lambda: print(which_one.get()))
# test_button.place(x=600, y=0, anchor=tkinter.NW)

# 密文复选框
secret_files = find_files("./resource/secret")
num_of_secret = len(secret_files)
fill_boxs = []
for i in range(num_of_secret):
    fill_boxs.append(tkinter.IntVar())
    fill_boxs[i].set(0)
    check = tkinter.Checkbutton(frame_list[0], text=secret_files[i], variable=fill_boxs[i], onvalue=1, offvalue=0)
    check.place(x=350, y=40+20*i, anchor=tkinter.NW)
# 测试复选框功能
# test_button = tkinter.ttk.Button(frame_list[0], text='box0', command=lambda: print(fill_boxs[0].get()))
# test_button.place(x=600, y=0, anchor=tkinter.NW)


root.mainloop()
