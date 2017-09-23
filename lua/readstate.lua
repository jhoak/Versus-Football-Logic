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
    player_table["number"] =  tonumber(stats[2])
    player_table["speed"] = tonumber(stats[3])
    player_table["hit"] =  tonumber(stats[4])
    player_table["kick"] = tonumber(stats[5])
    player_table["disp"] =  tonumber(stats[6])
    player_table["recv"] = tonumber(stats[7])
    player_table["pass"] =  tonumber(stats[8])
    player_table["x"] =  tonumber(stats[9])
    player_table["y"] =  tonumber(stats[10])
    player = io.read("*line")
    table.insert(players,player_table)
  end
  return players
end

local function game_state()
  local game = {}
  game["down"] = tonumber(split(io.read("*line"), ",")[1])
  game["togo"] = tonumber(split(io.read("*line"), ",")[1])
  game["totd"] = tonumber(split(io.read("*line"), ",")[1])
  game["tick"] = tonumber(split(io.read("*line"), ",")[1])
  game["half"] = tonumber(split(io.read("*line"), ",")[1])
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
    player_table["number"] = tonumber(stats[2])
    player_table["x"] = tonumber(stats[3])
    player_table["y"] = tonumber(stats[4])
    player = io.read("*line")
    table.insert(players,player_table)
  end
  return players
end

local function read_ball()
  local ball = split(io.read("*line")," ")
  io.read("*line")
  if #ball == 2 then
    return tonumber(ball[2])
  else
    local vector = {}
    vector["x"] = tonumber(ball[2])
    vector["y"] = tonumber(ball[3])
    vector["z"] = tonumber(ball[4])
    return vector
  end
end

return readstate
--Tests
--print(inspect(readstate("state1.txt")))
--print(inspect(readstate("state2.txt")))
--print(inspect(readstate("state3.txt")))
--print(inspect(readstate("state4.txt")))
