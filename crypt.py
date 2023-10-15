import py7zr


def col_encrypt(file_name_list, passwd='RoundShee'):
    """将./resource/secret下的指定的件列表进行加密
    @:param file_name_list 为./resource/secret/下的文件名string
    """

    # 创建加密处理后的文件
    with py7zr.SevenZipFile('./resource/encrypted.bin', 'w', password=passwd) as archive:
        for i in file_name_list:
            archive.write(('./resource/secret/'+i), arcname=i)


def out_decrypt(passwd='RoundShee'):
    """将seek输出结果提取到./resource/out中"""
    try:
        with py7zr.SevenZipFile('./resource/temp.bin', 'r', password=passwd) as archive:
            archive.extractall(path="./resource/out")
        return 1
    except FileNotFoundError:
        print('中间文件temp.bin未找到')
        return 0
    except Exception:
        print('文件无法解密,密码可能不正确 或 非密文!')
        return 0


# test
# list_name = ['secret.txt', 'test2.png']
# col_encrypt(list_name, passwd='123456')
# out_decrypt()
