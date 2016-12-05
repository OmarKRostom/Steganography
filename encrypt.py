from PIL import Image
import sys
import os

def encrypt() :
	try:
		imgOriginal = Image.open("original.png")
		imgSecret = Image.open("secret.png")
		pixelsOriginal = imgOriginal.load()
		pixelsSecret = imgSecret.load()
	except Exception as e:
		print "Image not found please check directory"
		return

	if imgSecret.size != imgOriginal.size :
		print "Original and Secret images sizes mismatch"
		return
	else :
		for i in range(1,imgOriginal.size[0]-1) :
			for j in range(1,imgOriginal.size[1]-1) :
				#Found a black pixel with a corresponding even pixel in RGB
				if pixelsOriginal[i,j][0]%2 == 0 and pixelsSecret[i,j][0] == 0 :
					badguy = list(pixelsOriginal[i,j])
					badguy[0] += 1
					pixelsOriginal[i,j] = tuple(badguy)
				#Found a white pixel with a corresponding odd pixel in RGB
				elif pixelsOriginal[i,j][0]%2 != 0 and pixelsSecret[i,j][0] == 255 :
					badguy = list(pixelsOriginal[i,j])
					badguy[0] -= 1
					pixelsOriginal[i,j] = tuple(badguy)
		new_img = Image.new("RGB",imgOriginal.size)
		for i in range(1,imgOriginal.size[0]-1) :
			for j in range(1,imgOriginal.size[1]-1) :
				new_img.putpixel((i,j),pixelsOriginal[i,j])
		new_img.save("encrypted.png")
	return

encrypt()
