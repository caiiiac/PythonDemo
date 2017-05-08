#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#创建List和Generator的区别在于最外层的[]和()
L = [x*x for x in range(10)]
print(L)

G = (x*x for x in range(10))
print(G)

#generator如果要一个一个打印出来,可以通过next()函数获得下一个返回值
print(next(G))
#因为generator是可迭代的,所以使用for循环也可打印
for x in G:
	print(x)



def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
#把fib函数变成generator，只需要把print(b)改为yield b就可以了：	
def fib(max):
	n, a, b = 0, 0, 1
	while n<max:
		yield b
		a, b = b, a+b
		n = n+1
	return 'done'

for x in fib(6):
	print(x)



#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(5)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break


#杨辉三角
def triangles(num):
	L = [1]
	n=0
	while n < num:
		yield L
		L = [1] + [L[i] + L [i+1] for i in range(0,len(L)-1)] + [1]
		n+=1

for t in triangles(10):
	print(t)
	
