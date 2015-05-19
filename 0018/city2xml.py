#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlrd
from xml.dom import minidom, Node

def open_xls(file_path):
	excel = xlrd.open_workbook(file_path)
	city_sheet = excel.sheet_by_name('city')
	city_content = {}
	for row in range(city_sheet.nrows):
		row_value = city_sheet.row_values(row)
		city_content[str(row+1)] = row_value[1:]
	return city_content
	
def build_xml(content):
	doc = minidom.Document()
	root = doc.createElement('root')
	doc.appendChild(root)
	cities = doc.createElement('cities')
	root.appendChild(cities)
	cities.appendChild(doc.createComment("城市信息"))
	cities.appendChild(doc.createTextNode(str(content)))
	
	with open('cities.xml', 'wb') as city_xml:
		city_xml.write(doc.toprettyxml().encode('utf-8'))
		
		
if __name__ == '__main__':
	content = open_xls('../0015/city.xls')
	build_xml(content)