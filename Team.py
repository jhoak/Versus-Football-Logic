from Player import Player
import os, sys

class Team:

  def __init__(self, teamname, roster):
    # Get players from file
    with open(roster) as p:
      self.name = teamname
      self.Players = []
      for stats in p:
        stats.split(',')
        self.Players.append(Player(teamname, stats))
