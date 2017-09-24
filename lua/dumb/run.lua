-- The dumb ai (tm)--

if game_state["status"] == "DECLARE OFFENSE" or game_state["status"] == "DECLARE DEFENSE" then

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
else
  for key,value in pairs(game_state["players"]) do
    commands[value["number"]] = {"MOVE","F"} 
  end
end


while true do end

print("Done!")