import tkinter
from tkinter import ttk


# 界面根基
root = tkinter.Tk()
root.title('Encrypt Hide && Seek Decrypt')
root.geometry('1024x512')

top_select = tkinter.ttk.Menubutton(root)
top_select.place()

# 框架部件
label = tkinter.Label(root, text="原始BMP图像")
label.place(x=10, y=30, anchor=tkinter.NW)

label = tkinter.Label(root, text="待加密文件")
label.place(x=430, y=30, anchor=tkinter.NW)


root.mainloop()
