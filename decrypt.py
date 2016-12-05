from PIL import Image
import sys
import os

def decrypt() :
	path = os.getcwd() + "/encrypted/"
	for filename in os.listdir(path) :
		img = Image.open(path + filename)
		pixelsRGB = img.load()
		for i in range(1,img.size[0]) :
			for j in range(1,img.size[1]) :
				if pixelsRGB[i,j][0] % 2 == 0 :
					pixelsRGB[i,j] = tuple([255,255,255])
				else :
					pixelsRGB[i,j] = tuple([0,0,0])
		new_img = Image.new("RGB",img.size)
		for i in range(1,img.size[0]) :
			for j in range(1,img.size[1]) :
				new_img.putpixel((i,j),pixelsRGB[i,j])
		new_img.save(path + "enc-"+filename)
	return

	
	return

decrypt()