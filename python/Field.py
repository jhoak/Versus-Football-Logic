from Ball import Ball

class Field:

  ball = Ball()

  def __init__(self, o_players, d_players):
    self.offense_players = o_players
    self.play_ongoing = False

