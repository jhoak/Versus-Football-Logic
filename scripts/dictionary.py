from PIL import Image
import os

def Dictionary(file_name,ethnicity):
	looper = 0
	while looper <= 1:

		if ethnicity == "black":
			subfolder = "/black"
		else:
			subfolder = "/white"

		folder_sel = "PlayerColorized" + subfolder

		os.path.join(os.getcwd(), folder_sel)
		sprites = {}
		for file in os.listdir(folder_sel):
			if file.endswith(".png"):

				im = Image.open(os.path.join(os.getcwd(), folder_sel, file))

				sprites[file] = im

		is_black = True			
		looper += 1

	out_img = sprites[file_name + ".png"]
	out_img.save("test.png","PNG")