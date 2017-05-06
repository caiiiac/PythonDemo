#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math


def daishu(a,b,c):
	if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float))):
		raise TabError('输入类型错误')

	if a==0:
		if b!=0:
			x1=x2=-c/b
			return x1,x2
		elif b==0:
			if c==0:
				return '0=0'
			else:
				return '无解'
	else:
		n=b*b-4*a*c
		if  n>=0:
			d=math.sqrt(n)
			x1=(-b+d)/(2*a)
			x2=(-b-d)/(2*a)
			return x1,x2
		else:
			return '无解'

a=float(input('请输入a的值:'))
b=float(input('请输入b的值:'))
c=float(input('请输入c的值:'))
print(daishu(a,b,c))
