from PIL import Image, ImageDraw, ImageFont
from os import listdir, system
from os.path import isfile, join

# quick and dirty gameplay display
def read_offense_file(i):
	fname = "gameframes/state" + str(100+i) +".txt"
	if not isfile(fname):
		return False 

	d = {}
	lines =  open(fname).readlines()

	for i in range(11):
		d["o"+str(i+1)] = [int(lines[i+2].split(",")[-2]),int(lines[i+2].split(",")[-1])]
		d["d"+str(i+1)] = [int(lines[i+14].split(",")[-2]),int(lines[i+14].split(",")[-1])]

	d["down"] = lines[28].split(",")[0]
	d["togo"] = int(lines[29].split(",")[0])
	d["totd"] = int(lines[30].split(",")[0])
	d["tick"] = int(lines[31].split(",")[0])
	d["offense_score"] = lines[33].split(",")[0]
	d["defense_score"] = lines[34].split(",")[0]

	if(len(lines[26].split(",")) == 7):
		d["ballvec"] = [int(lines[26].split(",")[1]), int(lines[26].split(",")[2])]
	else:
		d["ballplayer"] = [lines[26].split(",")[1], lines[26].split(",")[2]]
	return d
# Converts all offensive gamestate files in /gfx/tmp
def to_movie():
	field = Image.open("field.png")
	o = Image.open("o.png")
	x = Image.open("x.png")
	ball = Image.open("ball.png")
	i = 1
	while True:
		f = read_offense_file(i)
		if not f:
			break
		frame = Image.new("RGB",field.size)
		frame.paste(field, [0,0])

		# i yd = 10 px
		center = [100 + ((100-f["totd"])*10),100]
		fd = center[0] + ((f["togo"])*10)

		draw = ImageDraw.Draw(frame)
		draw.line((center[0], 0, center[0], 200), fill="blue")
		draw.line((fd, 0, fd, 200), fill="yellow")

		if "ballvec" in f:
			vec = f["ballvec"]
			ball_pos = [int(vec[0]/100) + center[0] +-3, int(vec[1]/100) + center[1]+-3]
			frame.paste(ball,ball_pos)

		for player in range(11):
			d_coord = f["d" +str(player+1)]
			o_coord = f["o" +str(player+1)]
			# In milliyards. Divide by 100 to get 1/10 yard (aka pixel)
			# Top left means sub 5 px
			d_px = [int(d_coord[0]/100) + center[0] +-5, int(d_coord[1]/100) + center[1]+-5]
			o_px = [int(o_coord[0]/100) + center[0] +-5, int(o_coord[1]/100) + center[1]+-5]
			frame.paste(o,d_px)
			frame.paste(x,o_px)

		# get a font
		fnt = ImageFont.truetype('font.ttf', 10)

		# draw text, half opacity
		draw.text((10,10), "Offense:" + f["offense_score"], font=fnt, fill=(0,0,0,255))
		# draw text, full opacity
		draw.text((10,30), "Defense:" + f["defense_score"] , font=fnt, fill=(0,0,0,255))

		draw.text((10,70), "Down:" + f["down"] , font=fnt, fill=(0,0,0,255))

		draw.text((10,90), "Time:" + str(int(f["tick"] / (600))) + ":" + str(int((f["tick"] % 600)/10)), font=fnt, fill=(0,0,0,255))

		frame.save('tmp/' + str(i).zfill(5) + '.png')
		i += 1

	system('ffmpeg -f image2 -r 10 -i tmp/%05d.png -vcodec mpeg4 -y movie.mp4')

to_movie()
