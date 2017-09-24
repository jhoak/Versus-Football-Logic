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
    self.hometeam = Team("Name", "home", 'roster1.txt', 'dumb')
    self.awayteam = Team("xXx_TeAm_NaMe_xXx", "away", 'roster2.txt', 'dumb')
    self.clock = Clock(halfsecs, ticktime)
    self.field = Field("sss")
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
    if self.clock.time <= 0 and not self.ball_in_play:
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
    return str(int(self.ticks_left))

  def get_half(self):
    return str(self.half)

  def get_offense(self)
    if hometeam.hasball:
      return hometeam
    return awayteam

  def get_defense(self)
    if hometeam.hasball:
      return awayteam
    return hometeam

#--------------------------------------------------

def footer(file, gs, offense, defense):    
  file.write("\n")
  file.write(gs.get_down()+",DOWN\n")
  file.write(gs.get_to_go()+",TOGO\n")
  file.write(gs.get_to_td()+",TOTD\n")
  file.write(gs.get_ticks_left()+",TICK\n")
  file.write(gs.get_half()+",HALF\n")
  file.write(str(offense.score)+",OFFENSIVE_SCORE\n")
  file.write(str(defense.score)+",DEFENSIVE_SCORE")

#--------------------------------------------------

gs = GameState(300.0, 0.1)

while True:

  active_players = []

  offense = gs.get_offense()
  defense = gs.get_defense()

  with open('state1.txt','w') as sone:
    sone.write("DECLARE OFFENSE\n\n")
    with open(offense.roster) as rone:
      for line in rone:
        sone.write(line)
    footer(sone, gs, offense, defense)


  subprocess.call(['lua5.3', 'run_ai.lua', 'state1.txt', offense.ai],shell=False)

  with open('result1.txt') as res:

    for line in res:
      line.split(',')
      offense.players[line[2]-1].set_position(line)
      active_players.append(offense.players[line[2]-1])

  with open('state2.txt','w') as stwo:
    stwo.write("DECLARE DEFENSE\n\n")
    for pl in active_players:
      stwo.write(pl.get_stat_csv()+"\n")
    stwo.write("\n")
    with open(defense.roster) as rtwo:
      for line in rtwo:
        stwo.write(line)
    footer(stwo, gs, offense, defense)

  subprocess.call(['lua5.3', 'run_ai.lua', 'state2.txt', defense.ai],shell=False)

  with open('result2.txt') as res:
    for line in res:
      line.split(',')
      defense.players[line[2]-1].set_position(line)
      active_players.append(defense.players[line[2]-1])

  while gs.field.ball_in_play:
    with open('state3.txt','w') as sth:
      sth.write("MOVE DEFENSE\n\n")
      for i in range(11):
        sth.write(active_players[i].get_stat_with_pos_csv()+"\n")
      sth.write("\n")
      for j in range(11,22):
        sth.write(active_players[j].get_pos_csv()+"\n")
      sth.write("\n")

    gs.field.ball.get_status()



  gs.update('')
