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

    with py7zr.SevenZipFile('./resource/temp.bin', 'r', password=passwd) as archive:
        archive.extractall(path="./resource/out")


# test
# list_name = ['secret.txt', 'test2.png']
# col_encrypt(list_name)
# out_decrypt()
