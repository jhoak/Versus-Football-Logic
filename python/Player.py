class Player:
  
  def __init__(self, home_or_away, stats):
    # Stats
    self.side = home_or_away
    self.name = stats[0]
    self.number = stats[1]
    self.speed = stats[2]*10
    self.hit = stats[3]
    self.kicking = stats[4]
    self.disipline = stats[5]
    self.recieving = stats[6]
    self.passing = stats[7]
    self.stats = stats

    # Coordinates
    self.x = 0.0
    self.y = 0.0

    # Flags!
    self.down = False
    self.diving = True
    self.collidable = True
    self.can_catch = False

  def move(self, dir):
    if 'N' in dir:
      self.y += speed
    if 'S' in dir:
      self.y += speed
    if 'F' in dir:
      self.x += speed
    if 'B' in dir:
      self.x -= speed

  def dive(self, dir):
    if 'N' in dir:
      self.y += 
    if 'S' in dir:
      self.y += 1.0
    if 'F' in dir:
      self.x += 1.0
    if 'B' in dir:
      self.x -= 1.0

  def set_position(self, pos_data):
    self.collidable = True
    self.can_catch = False

    pos = pos_data[1]
    if pos_data[3] > -500:
      pos_data[3] = -500

    if pos is 'C':
      self.x = -500
      self.y = 0.0

    elif pos is 'RG':
      self.x = -500
      self.y = -1000

    elif pos is 'RT':
      self.x = -500
      self.y = -2000

    elif pos is 'LG':
      self.x = -500
      self.y = 1000

    elif pos is 'LT':
      self.x = -500
      self.y = 2000

    elif pos is 'R' or pos is 'D':
      self.x = pos_data[3]
      self.y = pos_data[4]

    elif pos is 'QB'
      self.x = pos_data[3]
      self.y = 0

  def throw(self, target_x, target_y, lob):
    if not has_ball:
      return
    # TODO: Solve for arc
    self.Ball.setvector(2, 2, 2)

  def get_stat_csv(self):
    csv = ""
    for stat in self.stats:
      csv += str(stat)
      csv += ","

    return csv[:-1]


  def get_stat_with_pos_csv(self):
    csv = ""
    for stat in self.stats:
      csv += str(stat)
      csv += ","

    csv += str(self.x) + ","
    csv += str(self.y)

    return csv

  def get_position_csv(self):
    csv = ""
    csv += str(self.stats[0]) + ","
    csv += str(self.stats[1]) + ","
    csv += str(self.x) + ","
    csv += str(self.y)

    return csv