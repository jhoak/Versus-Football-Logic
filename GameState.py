from Field import Field
from Clock import Clock
from Team import Team

class GameState:
  # Start in the first half
  half = 1

  def __init__(self, halfsecs, ticktime):

    self.hometeam = Team("roster1.txt")
    self.awayteam = Team("roster2.txt")
    self.clock = Clock(halfsecs, ticktime)
    self.field = Field()

  def update(self, commands):
    # Update the field
    self.field.update()
    
    # Tick the Clock
    self.clock.update()
    # Mom~, is it over yet?
    if self.clock.time <= 0:
      if self.half = 1:
        # Let's all go to the lobby;
        # Let's all go to the lobby;
        # Let's all go to the lobby
        # To get ourselves a treat.
        DO_HALFTIME()
      else:
        # GG
        # NO RE
        DO_END_GAME()

    '''
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
    '''

gs = GameState(300.0, 0.1)

while True:

  gs.update()