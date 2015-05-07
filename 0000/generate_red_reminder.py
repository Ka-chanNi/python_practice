from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def add_num(avatar):
	drawavatar = ImageDraw.Draw(avatar)
	
	width, height = avatar.size
	myFont = ImageFont.truetype("C:/windows/fonts/Arial.ttf", size = 20)
	
	drawavatar.text((width - 20, 0), "5", fill = '#ff0000', font = myFont)
	avatar.save('result.png')
	
	return 0
if __name__ == '__main__':
	sourcepic = './gentama.png'
	avatar = Image.open(sourcepic)
	add_num(avatar)