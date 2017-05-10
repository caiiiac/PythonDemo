#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#关键字lambda表示匿名函数,冒号前面的x表示函数参数
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
print(list(map(lambda x: x*x, [1,2,3,4])))


#也可以把匿名函数作为返回值返回

def build(x, y):
    return lambda: x * x + y * y
