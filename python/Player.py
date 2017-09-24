class Player:
  
  def __init__(self, home_or_away, stats):
    # Stats
    self.side = home_or_away
    self.name = stats[0]
    self.number = stats[1]
    self.speed = int(stats[2])*10
    self.hit = stats[3]
    self.kicking = stats[4]
    self.disipline = stats[5]
    self.recieving = stats[6]
    self.passing = stats[7]
    self.stats = stats[:-1]

    # Coordinates
    self.x = 0.0
    self.y = 0.0

    # Flags!
    self.down = False
    self.diving = True
    self.collidable = True
    self.can_catch = False

  def move(self, dirc, mod):
    mag = self.speed*mod
    if 'N' in dirc:
      self.y += mag
    if 'S' in dirc:
      self.y += mag
    if 'F' in dirc:
      self.x += int(mag)
    if 'B' in dirc:
      self.x -= mag

  def dive(self, dirc):
    if 'N' in dirc:
      self.y += 1.0
    if 'S' in dirc:
      self.y += 1.0
    if 'F' in dirc:
      self.x += 1.0
    if 'B' in dirc:
      self.x -= 1.0

  def set_position(self, pos_data):
    self.collidable = True
    self.can_catch = False

    pos = pos_data[1]
    if len(pos_data) > 3:
      if int(pos_data[3]) > -500:
        pos_data[3] = -500

    if pos == 'C':
      self.x = -500
      self.y = 0.0

    elif pos == 'RG':
      self.x = -500
      self.y = -1000

    elif pos == 'RT':
      self.x = -500
      self.y = -2000

    elif pos == 'LG':
      self.x = -500
      self.y = 1000

    elif pos == 'LT':
      self.x = -500
      self.y = 2000

    elif ((pos == 'R') or (pos == 'D')):
      self.x = int(pos_data[3])
      self.y = int(pos_data[4])

    elif pos == 'QB':
      self.x = int(pos_data[3])
      self.y = 0

  def throw(self, target_x, target_y, lob):
    if not has_ball:
      return
    # TODO: Solve for arc
    self.Ball.setvector(2, 2, 2)

  def get_stat_csv(self):
    csv = ""
    for stat in self.stats:
      csv += str(int(stat))
      csv += ","

    return csv[:-1]


  def get_stat_with_pos_csv(self):
    csv = ""
    for stat in self.stats:
      csv += str(int(stat))
      csv += ","

    csv += str(int(self.x)) + ","
    csv += str(int(self.y))

    return csv

  def get_position_csv(self):
    csv = ""
    csv += str(self.stats[0]) + ","
    csv += str(self.stats[1]) + ","
    csv += str(int(self.x)) + ","
    csv += str(int(self.y))

    return csv