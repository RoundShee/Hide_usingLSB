from GUI import frame_select, frame0_gene, frame1_gene, frame2_gene
import tkinter
from tkinter import ttk


def main():
    # 界面根基
    root = tkinter.Tk()
    root.title('Encrypt Hide && Seek Decrypt')
    root.geometry('854x480')
    root.resizable(False, False)

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

    # 框架内容初始化-显示第一页
    frame0_gene(frame_list[0])
    frame1_gene(frame_list[1])
    frame2_gene(frame_list[2])
    frame_select(frame_list, 0)
    root.mainloop()


if __name__ == '__main__':
    main()
