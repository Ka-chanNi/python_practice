#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlwt3
import json

def write_txt_to_xls(txt_file):
	with open(txt_file, 'rb') as f:
		file_content = f.read().decode('utf-8')
		file_json = json.loads(file_content)
	
	xls_object = xlwt3.Workbook()
	sheet = xls_object.add_sheet('student')
	for i in range(len(file_json)):
		sheet.write(i, 0, i+1)
		data = file_json[str(i+1)]
		for j in range(len(data)):
			sheet.write(i, j+1, data[j])
	xls_object.save('student.xls')
	
	
if __name__ == '__main__':
	write_txt_to_xls('student.txt')