#!/usr/bin/python
# -*- coding: utf-8 -*-

total = 0

def p(a):
	global total
	total += a
	 
def executor(f, a):
	f(a)
	
print total
executor(p, 2)
print total
executor(p, 2)
print total
