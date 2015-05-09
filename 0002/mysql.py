#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb

def store_mysql(filepath):
	conn = MySQLdb.connect(user='root', passwd='080012', db='showmecode')
	cursor = conn.cursor()
	
	# 判断表是否已经存在
	cursor.execute('show tables in showmecode;')
	tables = cursor.fetchall()
	findtables = False
	for table in tables:
		if 'code' in table:
			findtables = True
			break
	if not findtables:
		cursor.execute('''
                CREATE TABLE `showmecode`.`code` (
                `id` INT NOT NULL AUTO_INCREMENT,
                `code` VARCHAR(10) NOT NULL,
                PRIMARY KEY (`id`));
        ''')
		
	f = open(filepath, 'rb')
	for line in f.readlines():
		code = line.strip()
		code = code[:10]
		print(code)
		cursor.execute('insert into code values(%s);', [code])
		
	conn.commit()
	cursor.close()
	conn.close()
	
if __name__ == '__main__':
	store_mysql('../0001/invatation_code.txt')