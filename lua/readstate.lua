local inspect = require('inspect')

local readstate = {}

local function split(inputstr, sep)
  local t={} ; i=1
  for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
          t[i] = str
          i = i + 1
  end
  return t
end

local function read_team_players()
  local players = {}
  local player = io.read("*line")

  while (player ~= "") do
    local stats = split(player, ",")
    local player_table = {}
    player_table["name"] = stats[1]
    player_table["number"] =  stats[2]
    player_table["speed"] = stats[3]
    player_table["hit"] =  stats[4]
    player_table["kick"] = stats[5]
    player_table["disp"] =  stats[6]
    player_table["recv"] = stats[7]
    player_table["pass"] =  stats[8]
    player_table["x"] =  stats[9]
    player_table["y"] =  stats[10]
    player = io.read("*line")
    table.insert(players,player_table)
  end
  return players
end

local function game_state()
  local game = {}
  game["down"] = split(io.read("*line"), ",")[1]
  game["togo"] = split(io.read("*line"), ",")[1]
  game["totd"] = split(io.read("*line"), ",")[1]
  game["tick"] = split(io.read("*line"), ",")[1]
  game["half"] = split(io.read("*line"), ",")[1]
  return game
end

function readstate.readstate(infile)
  io.input(infile)
  local state_type = io.read("*line")
  -- read a newline
  io.read("*line")
  local output = {}
  output["status"] = state_type

  if state_type == "DECLARE OFFENSE" then
    output["players"] = read_team_players()
  end

  if state_type == "DECLARE DEFENSE" then
    output["opponent"] = read_opposing_players()
    output["players"] = read_team_players()
  end

  if state_type == "MOVE OFFENSE" then
    output["players"] = read_team_players()
    output["opponent"] = read_opposing_players()
    output["ball"] = read_ball()
  end
  
  if state_type == "MOVE DEFENSE" then
    output["opponent"] = read_opposing_players()
    output["players"] = read_team_players()
    output["ball"] = read_ball()
  end

  output["game"] = game_state()
  return output
end




local function read_opposing_players()
  local players = {}
  local player = io.read("*line")

  while (player ~= "") do
    local stats = split(player, ",")
    local player_table = {}
    player_table["name"] = stats[1]
    player_table["number"] =  stats[2]
    player_table["x"] =  stats[3]
    player_table["y"] =  stats[4]
    player = io.read("*line")
    table.insert(players,player_table)
  end
  return players
end

local function read_ball()
  local ball = split(io.read("*line")," ")
  io.read("*line")
  if #ball == 2 then
    return ball[2]
  else
    local vector = {}
    vector["x"] = ball[2]
    vector["y"] = ball[3]
    vector["z"] = ball[4]
    return vector
  end
end

return readstate
--Tests
--print(inspect(readstate("state1.txt")))
--print(inspect(readstate("state2.txt")))
--print(inspect(readstate("state3.txt")))
--print(inspect(readstate("state4.txt")))
