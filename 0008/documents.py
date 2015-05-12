#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def get_content(domain):
	source = requests.get(domain)
	text = source.text
	html = BeautifulSoup(text, 'lxml')
	content = html.find(id='link-report')
	for string in content.strings:
		print(repr(string) + '\n')


if __name__ == '__main__':
	domain = 'http://www.douban.com/note/384034502/'
	get_content(domain)