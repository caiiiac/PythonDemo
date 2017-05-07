#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['M', 'S', 'T', 'B', 'J']

#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。
print('L[0:3] =', L[0:3])
#如果第一个索引是0，还可以省略
print('L[:3] =', L[:3])
#也可以从索引1开始，取出2个元素出来
print('L[1:3] =', L[1:3])
#支持L[-2]取倒数N个元素
print('L[-2:] =', L[-2:])

R = list(range(100))
#前十个数
print('R[:10] =', R[:10])
#后十个数
print('R[-10:] =', R[-10:])
#从10开始取20个数
print('R[10:20] =', R[10:20])
#前10个数,每两个取一个
print('R[:10:2] =', R[:10:2])
#所有数,每5个取一个
print('R[::5] =', R[::5])

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])

#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])
