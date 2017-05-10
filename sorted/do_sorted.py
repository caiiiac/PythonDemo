#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python内置的sorted()函数就可以对list进行排序
print(sorted([39,1,-18,67,0,-99]))

#还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([39,1,-18,67,0,-9], key=abs))

#默认情况下，对字符串排序，是按照ASCII的大小比较的('Z' < 'a')
#给sorted传入key函数,即可实现忽略大小写的被排序
print(sorted(['bo', 'Zero', 'credit', 'About'], key=str.lower))

#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bo', 'Zero', 'credit', 'About'], key=str.lower, reverse=True))


L = [('Bob', 75), ('Adam', 92), ('bart', 66), ('Lisa', 88)]

def by_name(t):
	return t[0].lower()

def by_score(t):
	return t[1]

print("按名字排序:",sorted(L, key=by_name))
print("按成绩排序:",sorted(L, key=by_score))

#另一种简单算法
print(sorted(L, key=lambda x: x[0].lower()))
print(sorted(L, key=lambda x: x[1], reverse=True))