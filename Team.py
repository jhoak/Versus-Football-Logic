from Player import Player
import os, sys

class Team:

  def __init__(self, teamname, home_or_away, roster):
    # Get players from file
    with open(roster) as p:
      self.name = teamname
      self.side = home_or_away

      self.Players = []

      for stats in p:
        stats.split(',')
        try:
          stats[1]
          self.Players.append(Player(home_or_away, stats))
        except:
          pass