from Field import Field
from Clock import Clock
from Team import Team
import subprocess

class GameState:

  def __init__(self, team1, team2, halfsecs, ticktime):

    # Start in the first half
    self.half = 1
    self.ticks_left = halfsecs/ticktime
    # Create the teams from the rosters
    self.hometeam = team1
    self.awayteam = team2
    self.clock = Clock(halfsecs, ticktime)
    self.field = Field("sss","ddd")
    self.down = 1
    self.to_go = 10
    self.yardline = 20
    self.ball_in_play = False
    self.gameover = False

  def update(self):
    # ----------- Pre-Snap ---------------

    offense = self.get_offense()
    defense = self.get_defense()

    with open('state1.txt','w') as sone:
      sone.write("DECLARE OFFENSE\n\n")
      with open(offense.roster) as rone:
        for line in rone:
          sone.write(line)
      self.footer(sone, offense, defense)


    subprocess.call(['lua5.3', 'run_ai.lua', 'state1.txt', offense.ai],shell=False)

    o_players = []

    with open('result.txt') as res:

      for l in res:
        line = l.split(',')
        offense.players[int(line[2])-1].set_position(line)
        o_players.append(offense.players[int(line[2])-1])

    with open('state2.txt','w') as stwo:
      stwo.write("DECLARE DEFENSE\n\n")
      for pl in o_players:
        stwo.write(pl.get_stat_csv()+"\n")
      stwo.write("\n")
      with open(defense.roster) as rtwo:
        for line in rtwo:
          stwo.write(line)
      self.footer(stwo, offense, defense)

    subprocess.call(['lua5.3', 'run_ai.lua', 'state2.txt', defense.ai],shell=False)

    d_players = []
    
    with open('result.txt') as res:
      for l in res:
        line = l.split(',')
        defense.players[int(line[2])-1].set_position(line)
        d_players.append(defense.players[int(line[2])-1])

    self.ball_in_play = True
    self.field.ball.set_position
    # ------------- During Play --------------
    # Offense State
    p = 99
    while self.ball_in_play:
      p+=1
      with open('state'+str(p)+'.txt','w') as sth:
        sth.write("MOVE OFFENSE\n\n")
        for opl in o_players:
          sth.write(opl.get_stat_with_pos_csv()+"\n")
        sth.write("\n")
        for dpl in d_players:
          sth.write(dpl.get_position_csv()+"\n")
        sth.write("\nBALL,"+ self.field.ball.get_status()+"\n")
        self.footer(sth, offense, defense)

      subprocess.call(['lua5.3', 'run_ai.lua', 'state'+str(p)+'.txt', offense.ai],shell=False)

      with open('result.txt') as res:
        for l in res:
          line = l.split(",")
          self.action(line[0], offense, defense)

      with open('state4.txt','w') as sth:
        sth.write("MOVE DEFENSE\n\n")
        for opl in o_players:
          sth.write(opl.get_position_csv()+"\n")
        sth.write("\n")
        for dpl in d_players:
          sth.write(dpl.get_stat_with_pos_csv()+"\n")
        sth.write("\nBALL,"+ self.field.ball.get_status()+"\n")
        self.footer(sth, offense, defense)

      subprocess.call(['lua5.3', 'run_ai.lua', 'state4.txt', defense.ai],shell=False)

      with open('result.txt') as res:
        for l in res:
          line = l.split(",")
          self.action(line, offense, defense)


      # Update the field
      #self.field.update()

      # Tick the Clock
      self.clock.update()
      self.ticks_left-=1

    # ----------- End of play -------------------

    # Mom~, is it over yet?
    if self.clock.time <= 0:
      if self.half == 1:
        # Let's all go to the lobby;
        # Let's all go to the lobby;
        # Let's all go to the lobby
        # To get ourselves a treat.
        self.halftime()
      else:
        # GG
        # NO RE
        self.endgame()

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

  def action(self, act, side, offense, defense):
    f_dir = self.get_direction(side)
    if act[0] == "MOVE":
      if side == 'def':
        defense.players[int(act[1])-1].move(act[2][0], f_dir, offense.players)
      elif side == 'off':
        offense.players[int(act[1])-1].move(act[2][0], f_dir, defense.players)
    elif act[0] == "THROW":
      held = self.field.ball.held
      if self.field.ball.held:
        self.field.ball.held.player_hold()
        self.field.ball.throw(act[1], act[2])


  def get_direction(self, side):
    #TODO: Conditions
    if side == 'off':
      return 1
    else:
      return -1

  def halftime(self):
    self.half = 2

  def endgame():
    self.gameover = True

  def get_offense(self):
    if self.hometeam.hasball:
      return self.hometeam
    return self.awayteam

  def get_defense(self):
    if self.hometeam.hasball:
      return self.awayteam
    return self.hometeam

  def footer(self, file, offense, defense):    
    file.write("\n")
    file.write(str(self.down)+",DOWN\n")
    file.write(str(self.to_go)+",TOGO\n")
    file.write(str(100-self.yardline)+",TOTD\n")
    file.write(str(int(self.ticks_left))+",TICK\n")
    file.write(str(self.half)+",HALF\n")
    file.write(str(offense.score)+",OFFENSIVE_SCORE\n")
    file.write(str(defense.score)+",DEFENSIVE_SCORE")

#-------------------------------------------------------

home = Team("Patrick", "home", '../team/patrick/roster.txt', '../team/patrick')
away = Team("xXx_TeAm_NaMe_xXx", "away", '../team/dumb/roster.txt', '../team/dumb')

gs = GameState(home, away, 300.0, 0.1)

while not gs.gameover:

  gs.update()
