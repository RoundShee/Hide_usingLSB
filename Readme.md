# 隐秘术-LSB替换
* 对24bit真彩色BMP图像进行最低为平面随机LSB替换算法嵌入和提取秘密信息的程序

## 一些细节
  在隐藏二进制流前加入预制区块，存储结束信息  
  ~~目前同一输出为bin格式~~  
  ~~文件头应该会有内容信息，如何获取~~  
  ~~RSA对文件加密需要AES密钥对文件加密，再使用RSA对密钥进行加密~~  
  ~~就目前预期工作量来看，仅仅完成RSA成功对文件加密与解密进行保存  配合hide and seek~~  
  使用加密压缩的库,直接将密文变为压缩包写入,使用默认密码RoundShee  
  
  
## 加密与隐藏
  指定为./resource/secret中放置多个要加密隐藏的文件  
  再通过设定密码进行AES加密打包处理  输出为./resource/encrypt.bin  
  再通过hide将encrypt.bin写入所选./resource/bmp/bmp_name.bmp图像中
  输出为./resource/bmp/bmp_name_hidden.bmp
  
## 提取与解密
  使用seek将指定目录./resource/bmp中有秘密信息的文件进行提取
  输出加密过的密文./resource/temp.bin
  decrypt利用密码解密temp.bin输出到./resource/out/