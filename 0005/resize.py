#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image

def change_size(picPath, iPhoneSize):
	img = Image.open(picPath)
	width, height = img.size
	changeWidth = float(width) / iPhoneSize[0]
	changeHeight = float(height) / iPhoneSize[1]
	
	# 判断分辨率是否满足
	if changeWidth > 1 or changeHeight > 1:
		change = changeWidth if changeWidth > changeHeight else changeHeight
		print('changed size is: ' + str(int(width / change)) + ', ' + str(int(height / change)))
		img.resize((int(width / change), int(height / change))).save('result.jpg')
	else:
		print('nothing should be changed')
		
if __name__ == '__main__':
	change_size('source.jpg', (1136, 640))