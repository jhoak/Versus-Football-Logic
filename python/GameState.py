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
    self.hometeam = Team("Name", "home", 'example_io/roster1.txt', 'dumb')
    self.awayteam = Team("xXx_TeAm_NaMe_xXx", "away", 'example_io/roster1.txt', 'dumb')
    self.clock = Clock(halfsecs, ticktime)
    self.field = Field("sss","ddd")
    self.down = 1
    self.to_go = 10
    self.yardline = 20
    self.gameover = False

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

  def get_offense(self):
    if self.hometeam.hasball:
      return self.hometeam
    return self.awayteam

  def get_defense(self):
    if self.hometeam.hasball:
      return self.awayteam
    return self.hometeam

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

while not gs.gameover:
  # ------------ Pre-snap -----------------------
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

  o_players = []

  with open('result.txt') as res:

    for l in res:
      line = l.split(',')
      offense.players[int(line[2])-1].set_position(line)
      o_players.append(offense.players[int(line[2])-1])

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

  d_players = []
  
  with open('result.txt') as res:
    for l in res:
      line = l.split(',')
      defense.players[int(line[2])-1].set_position(line)
      d_players.append(defense.players[int(line[2])-1])

  # ------------- During Play --------------

  #while gs.field.ball_in_play:
  for p in range(100, 200):
    with open('state'+str(p)+'.txt','w') as sth:
      sth.write("MOVE OFFENSE\n\n")
      for opl in o_players:
        sth.write(opl.get_stat_with_pos_csv()+"\n")
      sth.write("\n")
      for dpl in d_players:
        sth.write(dpl.get_position_csv()+"\n")
      sth.write("\nBALL,"+ gs.field.ball.get_status()+"\n")
      footer(sth, gs, offense, defense)

    subprocess.call(['lua5.3', 'run_ai.lua', 'state'+str(p)+'.txt', offense.ai],shell=False)

    with open('result.txt') as res:
      for l in res:
        line = l.split(",")
        if line[0] == "MOVE":
          if (offense.side == 'home'):
            f_dir = 1
          else:
            f_dir = -1
          offense.players[int(line[1])-1].move(line[2][0], f_dir)

    with open('state4.txt','w') as sth:
      sth.write("MOVE DEFENSE\n\n")
      for opl in o_players:
        sth.write(opl.get_position_csv()+"\n")
      sth.write("\n")
      for dpl in d_players:
        sth.write(dpl.get_stat_with_pos_csv()+"\n")
      sth.write("\nBALL,"+ gs.field.ball.get_status()+"\n")
      footer(sth, gs, offense, defense)

    subprocess.call(['lua5.3', 'run_ai.lua', 'state'+str(p)+'.txt', defense.ai],shell=False)

    with open('result.txt') as res:
      for l in res:
        line = l.split(",")
        if line[0] == "MOVE":
          if (offense.side == 'home'):
            f_dir = 1
          else:
            f_dir = -1

          offense.players[int(line[1])-1].move(line[2][0], f_dir)


  gs.update('')
