from Field import Field
from Clock import Clock
from Team import Team
import subprocess

class GameState:

  def __init__(self, halfsecs, ticktime):

    # Start in the first half
    self.half = 1
    self.ticks_left = halfsecs/ticktime
    # Create the teams from the rosters
    self.hometeam = Team("lua/roster1.txt")
    self.awayteam = Team("lua/roster2.txt")
    self.clock = Clock(halfsecs, ticktime)
    self.field = Field()
    self.down = 1
    self.to_go = 10
    self.yardline = 20

  def update(self, commands):
    # Update the field
    self.field.update()

    # Tick the Clock
    self.clock.update()
    self.ticks_left-=1
    # Mom~, is it over yet?
    if self.clock.time <= 0:
      if self.half == 1:
        # Let's all go to the lobby;
        # Let's all go to the lobby;
        # Let's all go to the lobby
        # To get ourselves a treat.
        DO_HALFTIME()
        self.half = 2
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
  def get_down(self):
    return str(self.down)
  
  def get_to_go(self):
    return str(self.to_go)

  def get_to_td(self):
    return str(100-self.yardline)

  def get_ticks_left(self):
    return str(ticks_left)

  def get_half(self):
    return str(half)


gs = GameState(300.0, 0.1)

while True:

  with open('lua/state1.txt') as sone:
    sone.write("DECLARE OFFENSE\n\n")
    with open('lua/roster1.txt') as rone:
      for line in rone:
        sone.write(line)
    sone.write("\n")
    sone.write(gs.field.get_down()+",DOWN\n")
    sone.write(gs.field.get_to_go()+",TOGO\n")
    sone.write(gs.field.get_to_td()+",TOTD\n")
    sone.write(gs.field.get_ticks_left()+",TICK\n")
    sone.write(gs.field.get_half()+",HALF\n")

  with open('lua/state2.txt') as stwo:
    stwo.write("DECLARE DEFENSE\n\n")
    with open('lua/roster2.txt') as rtwo:
      for line in rtwo:
        stwo.write(line)
    stwo.write("\n")
    stwo.write(gs.field.get_down()+",DOWN\n")
    stwo.write(gs.field.get_to_go()+",TOGO\n")
    stwo.write(gs.field.get_to_td()+",TOTD\n")
    stwo.write(gs.field.get_ticks_left()+",TICK\n")
    stwo.write(gs.field.get_half()+",HALF\n")

  subprocess.call()
  gs.update()


