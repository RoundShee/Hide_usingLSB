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


def main():
    """将小于2160*4069*3----4k的图像作为载体，进行隐藏"""
    img = cv.imread("raw_picture.bmp")
    # 计算可替换的数据量
    x, y, d = img.shape
    replace_size = x * y * 3
    if replace_size > 160*4069*3:
        print("所选载体图片超出预设大小!\n")
    print(replace_size)
    img_shape = (x, y, d)
    pointer_pic = 0     # 用于图像位置顺序索引r,c,  b,g,r

    # 下面是按字节读取密文
    raw_wait_hide = open("secret.txt", "rb")
    for i in raw_wait_hide.read():  # 一次8位
        for j in bin(i)[2:]:  # 一次一位
            x, y, d = p_t_pix_pos(pointer_pic, img_shape)
            pix_value = img[x, y, d]
            if not j and not pix_value//2:  # 密文0,pic偶数不变
                pass
            elif not j and pix_value//2:    # 密文0,pic奇数减一
                img[x, y, d] = pix_value - 1
            elif j and not pix_value//2:    # 密文1,pic偶数加一
                img[x, y, d] = pix_value + 1
            else:                           # 密文1,pic奇数不变
                pass
    raw_wait_hide.close()
    cv.imwrite("hidden_pic.bmp", img)


main()
