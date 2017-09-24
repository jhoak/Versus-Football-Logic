class Clock(object):
	"""docstring for Clock"""
	def __init__(self, starttime, tickrate):
		# Time remaining in seconds
		self.time = starttime
		# Time moved per update cycle
		self.tick = tickrate
	
	def update(self):
		# Tick
		self.time -= self.tick