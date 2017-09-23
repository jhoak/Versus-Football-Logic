from Player import Player
import os, sys

class Team:

  def __init__(self, roster):
    # Get players from file
    with open(roster) as p:
      self.Players = []
      for stats in p:
        stats.split(',')
        self.Players.append(Player(stats))
