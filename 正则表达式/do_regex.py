# !/usr/bin/env python3
# -*- coding: utf-8 -*-


#Python可以使用r前缀，就不用考虑转义的问题了
#s='abc\\-001' <==> s=r'abc\001'

import re

if re.match(r'\d{3}\-\d{3,8}', '010-123456'):
	print('ok')
else:
	print('failed')


#切分字符串
print('a b   c'.split(' '))
#使用正则可以识别连续空格
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a, b  , c,d'))
print(re.split(r'[\s\,\;]+', 'a,b;  ;   c;d'))

#分组
#除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
m=re.match(r'^(\d{3})-(\d{3,897})$', '010-123456')
print(m.group(0))
print(m.group(1))
print(m.group(2))
#group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串

t = '08:08:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

#贪婪匹配
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
print(re.match(r'^(\d+)(0*)$', '102300').groups())
#('102300', '')

#由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
print(re.match(r'^(\d+?)(0*)$', '102300').groups())
#('1023', '00')

#编译
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：

    # 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；

    # 用编译后的正则表达式去匹配字符串。



# 出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用
#编译:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用:
print(re_telephone.match('010-12345').groups())
# ('010', '12345')
print(re_telephone.match('010-8086').groups())
#('010', '8086')

