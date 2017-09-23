class Ball:
  # Position
  x=y=z=0
  # Speed vector
  x_speed=y_speed=z_speed=0
  # A held flag
  held = False

  def __init__(self):
    pass

  def setvector(self, x, y, z):
    self.held = False
    self.x_speed = 0
    self.y_speed = 0
    self.z_speed = 0

  def update(self):
    if held:
      # TODO
      pass
    x += x_speed