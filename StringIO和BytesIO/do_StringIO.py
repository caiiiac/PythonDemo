# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world!')

#getvalue()方法用于获得写入后的str。
print(f.getvalue())

#直接readlin()返回的将是空字符串
#利用seek()将stream position移动到0
f.seek(0)
print(f.readline())

h=StringIO('Hello\nHi\nGoodbye')
while  True:
	s=h.readline()
	if s=='':
		break
	print(s.strip())

