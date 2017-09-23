from Field import Field
from Clock import Clock
from Team import Team
from Ball import Ball

class GameState:
  # Start in the first half
  half = 1

  def __init__(self, halfmins):
    # Total minutes per half
    self.halfmins = halfmins
    self.hometeam = Team("roster.txt")
    self.awayteam = Team("roster.txt")

  def update(self):
    
