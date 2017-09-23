class Ball:
  def __init__(self):
    # Position
    self.x = 0
    self.y = 0
    self.z = 0

    # Movement vector
    self.x_speed = 0
    self.y_speed = 0
    self.z_speed = 0

  def setvector(self, x, y, z):
    held = False
    self.x_speed = 0
    self.y_speed = 0
    self.z_speed = 0

  def update(self):
    if held:
      x = Player
    x += x_speed