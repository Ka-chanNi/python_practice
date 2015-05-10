#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

def count(filepath):
	f = open(filepath, 'rb')
	s = f.read()
	s = str(s)
	words = re.findall(r'[a-zA-Z0-9]+', s)
	return str(len(words))
	
if __name__ == '__main__':
	num = count('test.txt')
	print('The number is: '+ num)