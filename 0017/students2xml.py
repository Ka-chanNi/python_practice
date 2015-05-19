#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlrd
from xml.dom import minidom, Node

def open_xls(file_path):
	excel = xlrd.open_workbook(file_path)
	student_sheet = excel.sheet_by_name('student')
	sheet_content = {}
	for row in range(student_sheet.nrows):
		row_value = student_sheet.row_values(row)
		for i in range(len(row_value)):
			if type(row_value[i]) == float:
				row_value[i] = int(row_value[i])
		sheet_content[str(row+1)] = row_value[1:]
	return sheet_content
	
def build_xml(content):
	doc = minidom.Document()
	root = doc.createElement('root')
	doc.appendChild(root)
	students = doc.createElement('students')
	root.appendChild(students)
	students.appendChild(doc.createComment("学生信息\"id\" : [名字，数学，语文，英语]"))
	students.appendChild(doc.createTextNode(str(content)))
	
	with open('students.xml', 'wb') as student_xml:
		student_xml.write(doc.toprettyxml().encode('utf-8'))
		
		
if __name__ == '__main__':
	content = open_xls('../0014/student.xls')
	build_xml(content)