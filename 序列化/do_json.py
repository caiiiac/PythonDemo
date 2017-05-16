# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, arg, score):
		self.name = name
		self.arg = arg
		self.score = score
	

s= Student('Mac', 20, 88)

# 序列化对象
print(json.dumps(s, default=lambda obj: obj.__dict__))



# 将JSON反序列化为Student对象
def dict2student(d):
	return Student(d['name'], d['arg'], d['score'])

json_str = '{"name": "jack", "score": 90, "arg": 18}'
print(json.loads(json_str, object_hook=dict2student))