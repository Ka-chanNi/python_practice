#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis

def store_redis(filepath):
	r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)
	f = open(filepath, 'r')
	for line in f.readlines():
		code = line.strip()
		r.lpush('code', code)
	f.close()
		
if __name__ == '__main__':
	store_redis('../0001/invatation_code.txt')
	