-- Patrick - Does a run and a pass play. Punts on 4th down.
-- Plays man to man defense
-- Remembers what play was called

if game_state["status"] == "DECLARE OFFENSE" then

  players = {}

  -- Pick players from roster randomly 
  for key,value in pairs(game_state["players"]) do
    table.insert(players,value["number"])
    if #table == 11 then
      break
    end
  end

  commands[players[1]] = {"C"}
  commands[players[2]] = {"LG"}
  commands[players[3]] = {"RG"}
  commands[players[4]] = {"LT"}
  commands[players[5]] = {"RT"}
  commands[players[6]] = {"R",-500,3000}
  commands[players[7]] = {"R",-500,4000}
  commands[players[8]] = {"R",-500,7000}
  commands[players[9]] = {"R",-500,-3000}
  commands[players[10]] = {"R",-500,-4000}
  commands[players[11]] = {"QB", 5000}
end

if game_state["status"] == "DECLARE DEFENSE" then
  players = {}

  -- Pick players from roster randomly 
  for key,value in pairs(game_state["players"]) do
    table.insert(players,value["number"])
    if #table == 11 then
      break
    end
  end

  commands[players[1]] = {"D",-500,5000}
  commands[players[2]] = {"D",-500,4000}
  commands[players[3]] = {"D",-500,3000}
  commands[players[4]] = {"D",-500,2000}
  commands[players[5]] = {"D",-500,1000}
  commands[players[6]] = {"D",-500,0000}
  commands[players[7]] = {"D",-500,-1000}
  commands[players[8]] = {"D",-500,-2000}
  commands[players[9]] = {"D",-500,-3000}
  commands[players[10]] = {"D",-500,-4000}
  commands[players[11]] = {"D",-500,-5000}
end

if game_state["status"] == "MOVE DEFENSE" or game_state["status"] == "MOVE OFFENSE" then
  for key,value in pairs(game_state["players"]) do
    -- Move Forward
    commands[value["number"]] = {"MOVE","F"} 
  end
end


while true do end

print("Done!")