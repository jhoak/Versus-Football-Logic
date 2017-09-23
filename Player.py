class Player:
  
  def __init__(self, stats):
    # Stats
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

  def do_action(self, action, params):
    if action == 'MOVE':
      self.move(params[0])
    elif action == 'DIVE':
      self.dive(params[0])
    elif action == 'THROW':
      self.throw(params[0], params[1], params[2])
    elif action == 'PUNT':
      self.punt()
    elif action == 'FG':
      self.fieldgoal()

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
    
