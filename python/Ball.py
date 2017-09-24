from Player import Player

class Ball:
  # Position
  x=y=z=0
  # Speed vector
  x_speed=y_speed=z_speed=0
  # A held flag
  held = False
  # Passed
  passed = False

  def __init__(self):
    pass

  def setvector(self, x, y, z):
    self.held = False
    self.x_speed = x
    self.y_speed = y
    self.z_speed = z

  def update(self):
    if held:
      # TODO
      pass
    x += x_speed

  def player_hold(self, player):
    self.held = player
    self.x = player.x
    self.y = player.y
    self.z = 1.5

  def get_status(self):
    if self.held:
      return self.held.side + str(self.held.number)
    else:
      t_p = (self.x, self.y, self.z)
      t_v = (self.y_speed, self.y_speed, self.y_speed)
      return str(t_p) + "," + str(t_v)