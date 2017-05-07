#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#生成一个list[1,2,3,4,5,6,7,8,9,10]
print(list(range(1,11)))

#生成[1x1, 2x2, 3x3, ..., 10x10]
print([x*x for x in range(1,11)])
#for循环后面还可以加上if判断
L = [x*x for x in range(1,11) if x%2 == 0]
print(L)
#还可以使用两层循环，可以生成全排列
[m+n for m in 'ABC' for n in 'XYZ']


#列表生成式也可以使用两个变量来生成list
d= {'x':'A', 'y':'B', 'z':'C'}
l=[k + '=' + v for k,v in d.items()]
print(l)

#把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


#练习

#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
#使用内建的isinstance函数可以判断一个变量是不是字符串
#添加if语句保证列表生成式能正确地执行
L = ['Hello', 'World', 'IBM', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s,str)])