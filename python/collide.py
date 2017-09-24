import math

# INPUTS:
# COORD: center coords of player to move, in milliyards.
# OTHER_COORDS: coords of other targets that can be collided with
# DELTA: how far that the player moves.

# OUTPUTS:
# if no collide, i send new coords, and a None. [Example [-3444,340509],None]
# if collide, i send new coords, and an index + degree of impact. [Example [-3444,340509],None]

# PROBLEMS:
# Uses a Naive Algorithm. I can make this faster by pruning distant players.
def collide(coord,other_coords,delta):

	# Helpers
	def sign(x):
		if x == 0:
			return 0
		if x < 0:
			return -1
		if x > 0:
			return 1

	def did_collide(a,b):
		# If the center points are both within 1000 you collided.
		x_collide = abs(a[0] - b[0]) <= 1000
		y_collide = abs(a[1] - b[1]) <= 1000
		return x_collide and y_collide


	# How many steps? Also, how far to go?
	step_delta = [sign(delta[0]),sign(delta[1])]
	steps = max([abs(delta[0]),abs(delta[1])])

	for i in range(steps):
		coord = [coord[0] + step_delta[0],coord[1] + step_delta[1]]
		for idx, other_coord in enumerate(other_coords):
			if did_collide(coord,other_coord):
				# Undo step
				coord = [coord[0] - step_delta[0],coord[1] - step_delta[1]]
				# Calculate collision angle
				angle = math.degrees(math.atan2(other_coord[1] - coord[1], other_coord[0] - coord[0]))
				# return index
				return [coord,[idx,angle]]

	return [coord,None]


# collide by running upward (90 degrees)
others = [[1000,5000],[-1000,3000],[3000,0]]
print(collide([1000,1000],others,[0,6000]))

# no collide 
others = [[1000,5000],[-1000,3000],[3000,0]]
print(collide([1000,1000],others,[1000,1000]))

# collide by running south east
others = [[1000,5000],[-2000,-3000],[3000,0]]
print(collide([0,1000],others,[-4000,-4000]))