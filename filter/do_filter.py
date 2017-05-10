#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#filter()函数用于过滤序列
#filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

#删掉list中的偶数
def isOdd(n):
	return n%2 == 1

print(list(filter(isOdd, [1,2,4,5,6,10,15])))

#删除空字符串
def notEmpty(s):
	return s and s.strip()

print(list(filter(notEmpty, ['a', ' ', None, 'r', '', '   T'])))
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

#求素数
def _odd_iter():
	n = 1
	while True:	
		n = n + 2
		yield n
def _not_divisible(n):
	return lambda x: x%n > 0
def primes():
	yield 2
	it = _odd_iter()
	while  True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)

# 打印100以内的素数
for x in primes():
 	if x < 100:
 	 	print(x)
 	else:
 	 	break


 #回文数
def is_palinrome(n):
	return str(n) == str(n)[::-1]

print(list(filter(is_palinrome,range(1,10000))))

