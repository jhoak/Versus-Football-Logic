from PIL import Image
import os

def colorize(folder, color_1, color_2):
	os.path.join(os.getcwd(), folder)
	for file in os.listdir(folder):
		if file.endswith(".png"):
			is_black = False
			looper = 0
			while looper <= 1:

				im = Image.open(os.path.join(os.getcwd(), folder, file))
				primary = color_1
				secondary = color_2
				black_skin = (160, 48, 0, 255)
				white_skin = (255, 200, 184, 255)
				purp = (255, 0, 255, 0)

				colorized = Image.new("RGBA", (16, 16))

				# (0,128,0) = Green = primary color
				# (255,255,255) = White = secondary color
				# (0,0,255) = Blue = skin color

				for pixel_y in range(16):
					for pixel_x in range(16):
						pixel = (pixel_x, pixel_y)
						color = im.getpixel(pixel)

						if color == (255, 0, 255, 255):
							colorized.putpixel(pixel, purp)
						elif color == (0, 128, 0, 255):
							colorized.putpixel(pixel, primary)
						elif color == (255, 255, 255, 255):
							colorized.putpixel(pixel,secondary)
						elif color == (0, 0, 255, 255):
							if is_black == True:
								colorized.putpixel(pixel, black_skin)
								skin_tone = "black"
							else:
								colorized.putpixel(pixel, white_skin)
								skin_tone = "white"

				colorized.save("PlayerColorized/" + skin_tone + "/" + file, "PNG")
				is_black = True
				looper += 1