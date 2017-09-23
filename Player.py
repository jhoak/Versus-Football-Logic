class Player:
  
  def __init__(self, home_or_away, stats):
    # Stats
    self.side = home_or_away
    self.name = stats[0]
    self.number = stats[1]
    self.speed = stats[2]
    self.hit = stats[3]
    self.kicking = stats[4]
    self.disipline = stats[5]
    self.recieving = stats[6]
    self.passing = stats[7]

    # Coordinates
    self.x = 0.0
    self.y = 0.0

    # Flags!
    self.divestate = False

  def move(self, dir):
    if 'N' in dir:
      self.y += 1.0
    if 'S' in dir:
      self.y += 1.0
    if 'F' in dir:
      self.x += 1.0
    if 'B' in dir:
      self.x -= 1.0

  def dive(self, dir):
    if 'N' in dir:
      self.y += 1.0
    if 'S' in dir:
      self.y += 1.0
    if 'F' in dir:
      self.x += 1.0
    if 'B' in dir:
      self.x -= 1.0

  def throw(self, target_x, target_y, lob):
    if not has_ball:
      return
    # TODO: Solve for arc
    self.Ball.setvector(2, 2, 2)

