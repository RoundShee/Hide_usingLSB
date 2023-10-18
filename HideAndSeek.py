"""使用LSB替换算法将信息隐藏在BMP图像中"""

import cv2 as cv


def p_t_pix_pos(pointer, shape):
    """将密文位流指针位置转化像素空间位置"""
    row, colum, deep = shape
    at_d = pointer // (row*colum)
    pointer = pointer % (row*colum)
    at_c = pointer // row
    at_r = pointer % row
    return at_r, at_c, at_d


def hide_in_bmp(file_bmp, file_secret):
    """将小于2160*4069*3----4k的图像作为载体，进行隐藏
    输入两个字符串路径
    成功返回1，一切失败返回0
    """
    try:
        img = cv.imread(file_bmp)
    except FileNotFoundError:
        print(file_bmp + '文件未找到!\n')
        return 0
    else:
        if img is None:
            print(file_bmp + "文件不正确")
            return 0
    # 计算可替换的数据量
    x, y, d = img.shape
    img_shape = (x, y, d)
    can_replace_size = x * y * 3    # 针对只用最低位,计算可替换大小bit
    if can_replace_size > 2160*4069*3:
        print("所选载体图片超出预设大小!\n")
        return 0    # 暂时为0
    pointer_pic = 25    # 用于图像位置顺序索引r,c,  b,g,r
    # log2(2160*4096*3)=24.66 用于存储结尾信息，便于提取

    # 下面是按字节读取密文
    try:
        raw_wait_hide = open(file_secret, "rb")
    except FileNotFoundError:
        print(file_secret + ' 文件未找到!\n')
        return 0
    for i in raw_wait_hide.read():  # 一次8位
        never_give_up = bin(i)[2:]  # 成功解决低于8bit的byte问题
        num = len(never_give_up)
        for k in range(8):  # 一次一位
            if k < 8-num:
                j = 0
            else:
                j = never_give_up[k-8+num]
            x, y, d = p_t_pix_pos(pointer_pic, img_shape)
            pix_value = img[x][y][d]
            if (not int(j)) and (not (pix_value % 2)):  # 密文0,pic偶数不变
                img[x][y][d] = pix_value
            elif (not int(j)) and (pix_value % 2):    # 密文0,pic奇数减一
                img[x][y][d] = pix_value - 1
            elif int(j) and (not (pix_value % 2)):    # 密文1,pic偶数加一
                img[x][y][d] = pix_value + 1
            else:                           # 密文1,pic奇数不变
                img[x][y][d] = pix_value
            if pointer_pic >= can_replace_size:
                print('加密信息过长\n')
                return 0  # 仍暂时为定返回值
            else:
                pointer_pic = pointer_pic + 1
    # 密文写入完成,关闭文件
    raw_wait_hide.close()
    # 处理将要写入头部25位的尾部结束指针
    pointer_pic = str(bin(pointer_pic)[2:])
    add_zero = 25 - len(pointer_pic)
    if add_zero > 0:
        pointer_pic = add_zero * '0' + pointer_pic
    # print(int(pointer_pic, 2))  # test
    # 此时pointer_pic为字符串类型
    for i in range(25):
        x, y, d = p_t_pix_pos(i, img_shape)
        pix_value = img[x][y][d]
        # print(pix_value)    # test
        if (not int(pointer_pic[i])) and (not (pix_value % 2)):  # 密文0,pic偶数不变
            img[x][y][d] = pix_value
        elif (not int(pointer_pic[i])) and (pix_value % 2):  # 密文0,pic奇数减一
            img[x][y][d] = pix_value - 1
        elif int(pointer_pic[i]) and (not pix_value % 2):  # 密文1,pic偶数加一
            img[x][y][d] = pix_value + 1
        else:
            img[x][y][d] = pix_value
        # print(str(img[x][y][d])+' changed'+str(i))   # test
    new_name = file_bmp[0:-4] + '_Hi.bmp'
    cv.imwrite(new_name, img)
    print('完成隐藏!')
    return 1


def seek_in_bmp(file_bmp):
    """将file_bmp中的信息提取出来"""
    try:
        img = cv.imread(file_bmp)
    except FileNotFoundError:
        print(file_bmp + '文件未找到!\n')
        return 0
    else:
        if img is None:
            print(file_bmp + "文件无信息\n")
            return 0
    img_shape = img.shape
    end_of_secret = ''
    # 尝试获取密文结尾指针信息
    for i in range(25):
        row, colum, dim = p_t_pix_pos(i, img_shape)   # 得到当前矩阵位置信息
        pix_value = img[row][colum][dim]
        if pix_value % 2:    # pix_value是奇数
            end_of_secret = end_of_secret + '1'
        else:
            end_of_secret = end_of_secret + '0'
    end_of_secret = int(end_of_secret, 2)       # 将01字符串以二进制转换为int型
    # 创建结果文件
    file = open('./resource/temp.bin', 'wb')
    for pointer_pix in range(25, end_of_secret, 8):  # 写入只能以byte形式进行
        byte_secret = ''
        for i in range(8):  # i为偏移
            row, colum, dim = p_t_pix_pos(pointer_pix+i, img_shape)   # 找出富含信息的图像坐标
            pix_value = img[row][colum][dim]
            if pix_value % 2:  # pix_value是奇数
                byte_secret = byte_secret + '1'
            else:
                byte_secret = byte_secret + '0'
        se_hex = int(byte_secret, 2)
        file.write(se_hex.to_bytes(1, 'little'))
    file.close()
    print('提取完成')


# 测试隐藏功能可用
# hide_in_bmp("resource/bmp/raw_picture.bmp", "resource/encrypted.bin")
# 测试seek代码
# seek_in_bmp("resource/bmp/hidden_pic.bmp")
