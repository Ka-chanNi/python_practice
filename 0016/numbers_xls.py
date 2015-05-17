#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlwt3
import json

def write_txt_to_xls(txt_file):
	with open(txt_file, 'rb') as f:
		file_content = f.read().decode('utf-8')
		file_json = json.loads(file_content)

	xls_content = xlwt3.Workbook()
	sheet = xls_content.add_sheet('numbers')
	for i in range(len(file_json)):
		data = file_json[i]
		for j in range(len(data)):
			sheet.write(i, j, data[j])
	xls_content.save('numbers.xls')
	
	
if __name__ == '__main__':
	write_txt_to_xls('numbers.txt')