#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#把序列[1,3,5,7,9]-->整数13579
from functools import reduce

def fn(x, y):
	return x * 10 + y

print(reduce(fn, [1,3,5,7,9]))


#str --> int
def charToNum(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print(reduce(fn, map(charToNum, '13579')))

#简化版
def str2int(s):
	def fn(x, y):
	    return x * 10 + y
	def charToNum(s):
	    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(charToNum, s))			    


print(str2int('13579'))



def prod(L):
	return reduce(lambda x, y : x * y, L)

print('3 * 5 * 7 * 9 =',prod([3, 5, 7, 9]))

#字符串'123.456'转换成浮点数123.456
def str2float(s):
	def fn(x, y):
	    return x * 10 + y
	def charToNum(s):
	    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	def fx(x, y):
		return x * 0.1 + y
	[r1, r2]=s.split(".")
	s1 = reduce(fn, map(charToNum, r1))
	s2 = reduce(fx, map(charToNum, r2[::-1]))
	return s1 + 0.1*s2

print(str2float('123.456'))
