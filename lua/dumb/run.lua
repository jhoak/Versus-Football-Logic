-- The dumb ai (tm)--
players = {}

-- Pick players from roster randomly 
for key,value in pairs(game_state["players"]) do
  table.insert(players,value["number"])
  if #table == 11 then
    break
  end
end

if game_state["status"] == "DECLARE OFFENSE" or game_state["status"] == "DECLARE DEFENSE" then
  commands["C"] = players[1]
  commands["LG"] = players[2]
  commands["RG"] = players[3]
  commands["LT"] = players[4]
  commands["RT"] = players[5]
  commands["R1"] = {players[6],-500,3000}
  commands["R2"] = {players[7],-500,4000}
  commands["R3"] = {players[8],-500,7000}
  commands["R4"] = {players[9],-500,-3000}
  commands["R5"] = {players[10],-500,-4000}
  commands["QB"] = {players[11],5000}
end

print("Done!")