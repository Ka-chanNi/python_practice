#!/use/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def get_links(domain):
	source = requests.get(domain)
	source = source.text
	html = BeautifulSoup(source)
	links = html.find_all('a')
	for link in links:
		print(link.get('href'))
		

if __name__ == '__main__':
	domain = 'http://www.douban.com/note/384034502/'
	get_links(domain)