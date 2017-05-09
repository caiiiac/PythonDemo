#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#可以直接作用于for循环的数据类型有以下几种：

#一类是集合数据类型，如list、tuple、dict、set、str等；

#一类是generator，包括生成器和带yield的generator function。

#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

#可以使用isinstance()判断一个对象是否是Iterable对象

from collections import Iterable, Iterator


def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))


#生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#可以使用isinstance()判断一个对象是否是Iterator对象：

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))


#小结

#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。