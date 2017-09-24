from Ball import Ball

class Field:

  ball = Ball()

  def __init__(self, players):
    self.players = players
    self.play_ongoing = False

