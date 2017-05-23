# !/usr/bin.env python3
# -*- coding: utf-8 -*-

import urllib.request

#获取baidu.com主页，并显示其前300个字节。
with urllib.request.urlopen('http://www.baidu.com') as f:
	print('解码前:', f.read(300))


# 请注意，urlopen返回一个字节对象。这是因为urlopen无法确定HTTP服务器字节流的编码。
with urllib.request.urlopen('http://www.baidu.com') as f:	
	print('解码后:', f.read(50).decode('utf-8'))

#也可以直接赋值使用
f = urllib.request.urlopen('http://www.baidu.com')
print('第二种写法:',f.read(50).decode('utf-8'))