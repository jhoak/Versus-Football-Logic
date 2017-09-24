import random

document = open("nflplayers.txt", "r")
search = document.read(1000000)
document.close()

endlook = False
first_names = []
last_names = []


for i in range(len(search)):
	char = search[i]
	if char == ',':
		first_startpos = i + 2
		last_endpos = i
		j = i
		while search[j] != ' ':
			j -= 1
		last_startpos = j + 1
		last_names.append(search[last_startpos:last_endpos])
		endlook = True


	if endlook == True and char == '\n':
		first_endpos = i
		first_names.append(search[first_startpos:first_endpos])
		endlook = False

playerstats = open("roster.txt", "w")
for i in range(32):
	playerstats.write(first_names[random.randint(0,1218)] + " " + last_names[random.randint(0,1219)] + "," + str(i + 1) + "," + str(random.randint(0,100)) + "," + str(random.randint(0,100)) + "," + str(random.randint(0,100)) + "," + str(random.randint(0,100)) + "," + str(random.randint(0,100)) + "," + str(random.randint(0,100)))
	if i != 31:
		playerstats.write("\n")
playerstats.close()

