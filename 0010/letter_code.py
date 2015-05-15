#!/usr.bin/python
# -*- coding:utf-8 -*-
import string
import random
from PIL import Image, ImageDraw, ImageFont

def generate_picture():
	letters = ''.join([random.choice(string.ascii_letters) for i in range(4)])
	
	width = 100
	height = 40
	
	im = Image.new('RGB', (width, height), (255, 255, 255))
	
	dr = ImageDraw.Draw(im)
	myFont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', 30)
	for i in range(4):
		dr.text((5+i*20, 5), letters[i], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), font=myFont)
	del dr
	
	for x in range(width):
		for y in range(height):
			if im.getpixel((x, y)) == (255, 255, 255):
				im.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
				
	im.save('layout.png')
	
	
if __name__ == '__main__':
	generate_picture()