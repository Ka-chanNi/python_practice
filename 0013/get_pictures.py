#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import os

def get_pictures(domain):
	source = requests.get(domain, headers={'Accept-Encoding': 'deflate'}).text
	html = BeautifulSoup(source, 'lxml')
	picture_url_list = html.find_all('img', class_='BDE_Image')

	if os.path.exists(os.path.join(os.getcwd(), 'pictures')):
		os.chdir(os.path.join(os.getcwd(), 'pictures'))
	else:
		os.mkdir('pictures')
		os.chdir(os.path.join(os.getcwd(), 'pictures'))
	for i in range(len(picture_url_list)):
		picture_name = str(i) + '.jpg'
		try:
			with open(picture_name, 'wb') as f:
				f.write(requests.get(picture_url_list[i].get('src')).content)
			print('Success to download ' + picture_name)
		except:
			print("Fail to download " + picture_name)
	print('All done, enjoy pictures')
	

if __name__ == '__main__':
	get_pictures("http://tieba.baidu.com/p/2166231880")
	