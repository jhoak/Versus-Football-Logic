-- Patrick - Does a run and a pass play. Punts on 4th down.
-- Tries to pick good players
-- Plays man to man defense
-- Remembers what play was called

function split(inputstr, sep)
  local t={} ; i=1
  for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
          t[i] = str
          i = i + 1
  end
  return t
end

function QB_fit(a)
  return a["pass"] + a["kick"] + a["speed"]
end

function RB_fit(a)
  return a["speed"]
end

function WR_fit(a)
  return a["speed"] + a["recv"]
end

function LINE_fit(a)
  return a["hit"]
end

function DEF_fit(a)
  return a["speed"] + a["hit"] + a["pass"]
end

function pick(already_picked_nums,cmp)
  best = nil
  best_score = 0
  for key,value in pairs(game_state["players"]) do
    if not already_picked_nums[value["number"]] then
      if cmp(value) > best_score then
        best = value["number"]
        best_score = cmp(value)
      end
    end
  end
  already_picked_nums[best] = true
  return best
end

function setup_offense()
  local already_picked = {}
  commands[pick(already_picked,QB_fit)] = {"QB", 5000}

  commands[pick(already_picked,WR_fit)] = {"R",-1000,7000}
  commands[pick(already_picked,WR_fit)] = {"R",-1000,8500}

  commands[pick(already_picked,WR_fit)] = {"R",-1000,-7000}
  commands[pick(already_picked,WR_fit)] = {"R",-1000,-8500}

  commands[pick(already_picked,RB_fit)] = {"R",-5000,1500}

  commands[pick(already_picked,LINE_fit)] = {"C"}
  commands[pick(already_picked,LINE_fit)] = {"LG"}
  commands[pick(already_picked,LINE_fit)] = {"RG"}
  commands[pick(already_picked,LINE_fit)] = {"LT"}
  commands[pick(already_picked,LINE_fit)] = {"RT"}
end

function offense_run()
  tick = tonumber(memory.split(",")[1])
  for key,value in pairs(game_state["players"]) do
    --People at > -1000 move ahead, always.
    if(value["x"] > -1000) then
      commands[value["number"]] = {"MOVE","F"}
    -- QB to recvr
    elseif(value["x"] == -5000 and value["y"] == 0 and (tick - game_state["game"]["tick"]) == 10) then
      commands[value["number"]] = {"PASS",-5000,1500} 
    -- Always run if tick is 20
    elseif (tick - game_state["game"]["tick"] > 20) then
      commands[value["number"]] = {"MOVE","F"} 
    end
  end
end

function offense_pass()
  tick = tonumber(split(memory,",")[2])
  for key,value in pairs(game_state["players"]) do
    --People at > -3000 move ahead, always.
    if(value["x"] > -3000) then
      commands[value["number"]] = {"MOVE","F"}
    -- QB Passes to left at 20 ticks.
    elseif(tick - game_state["game"]["tick"] == 20) then
      commands[value["number"]] = {"PASS",18000,-7000} 
    -- Always run if tick is 20 
    end
  end
end

function offense_punt()
  --Everyone rushes forward, QB spams punt cmd
  tick = tonumber(memory.split(",")[1])
  for key,value in pairs(game_state["players"]) do
    --People at > -3000 move ahead, always.
    if(value["x"] > -3000) then
      commands[value["number"]] = {"MOVE","F"}
    else
      commands[value["number"]] = {"PUNT"} 
    end
  end
end

function setup_defense()
  memory = ""
  local already_picked = {}
  for key,value in pairs(game_state["opponent"]) do
    picked = pick(already_picked,DEF_fit)
    commands[picked] = {"D", -value["x"],value["y"]}
    memory = memory .. tostring(picked) .. "," .. tostring(value["number"]).. ","
  end
end

-- MAIN --

if game_state["status"] == "DECLARE OFFENSE" then
  setup_offense()
  memory = ""

  if(game_state["game"]["down"] == 4) then
    memory = "punt"
  elseif(game_state["game"]["togo"] < 7) then
    memory = "run"
  else
    memory = "pass"
  end
  memory = memory .. "," .. game_state["game"]["tick"]
end

if game_state["status"] == "DECLARE DEFENSE" then
  setup_defense()
end

if game_state["status"] == "MOVE OFFENSE" then
  print(memory)
  play = split(memory,",")[1]
  print(play)
  if(play == "run") then
    offense_run()
  elseif(play == "pass") then
    offense_pass()
  elseif(play == "punt") then
    offense_punt()
  end
end

if game_state["status"] == "MOVE DEFENSE" then
  
  for key,value in pairs(game_state["players"]) do
    commands[value["number"]] = {"MOVE","F"}
  end
end




print("Done!")