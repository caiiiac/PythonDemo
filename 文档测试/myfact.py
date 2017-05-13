#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fact(n):
    '''
    阶乘函数，且文档测试
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    6
    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError: n should >= 1
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: n should >= 1
    '''
    if n<1:
        raise ValueError('n should >= 1')
    elif n==1:
        return 1
    return fact(n-1)*n

if __name__=='__main__':
    import doctest
doctest.testmod()