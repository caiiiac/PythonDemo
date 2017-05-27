# !/usr/bin.env python3
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse

' Get请求 '

params = urllib.parse.urlencode({'FORM' : Z9LH2})
url = "http://cn.bing.com/academic/?%s" % params
with urllib.request.urlopen(url) as f:
	print(f.read().decode('utf-8'))

# Get请求 and 添加header头

# data = {}
# data['FORM'] = 'Z9LH2'
# url_values = urllib.parse.urlencode(data)
# print(url_values)  # The order may differ from below.  

# url = 'http://cn.bing.com/academic/'
# full_url = url + '?' + url_values

# req = urllib.request.Request(full_url)
# req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
# data = urllib.request.urlopen(req)
# print(data.read().decode('utf-8'))

#获取baidu.com主页，并显示其前300个字节。
# with urllib.request.urlopen('http://www.baidu.com') as f:
# 	print('解码前:', f.read(300))


# 请注意，urlopen返回一个字节对象。这是因为urlopen无法确定HTTP服务器字节流的编码。
# with urllib.request.urlopen('http://www.baidu.com') as f:	
# 	print('解码后:', f.read(50).decode('utf-8'))


#也可以直接赋值使用
# f = urllib.request.urlopen('http://daily.zhihu.com/')
# print('第二种写法:',f.read().decode('utf-8'))

#添加HTTP请求头
# req = urllib.request.Request('http://daily.zhihu.com/')
# req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
# f = urllib.request.urlopen(req)
# print(f.read().decode('utf-8'))
