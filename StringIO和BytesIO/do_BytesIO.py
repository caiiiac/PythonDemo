# !/usr/bin/env python3
# -*- coding: utf-8 -*-

#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

from io import BytesIO

f=BytesIO()
f.write('你好'.encode('utf-8'))
print(f.tell())
print(f.getvalue())
#写入的不是str，而是经过UTF-8编码的bytes。


#BytesIO()初始化的seek起始是在0,如果此时进行write()会覆盖原来的
#可使用tell(),查看seek当前位置
t=BytesIO('大学生'.encode('utf-8'))
t.tell()
t.write(b'111')
print(t.getvalue())
#b'111\xe5\xad\xa6\xe7\x94\x9f'

t.readline()
print(t.tell())
t.write(b'666')
print(t.getvalue())
#b'111\xe5\xad\xa6\xe7\x94\x9f666'