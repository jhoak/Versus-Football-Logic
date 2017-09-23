-- Load helpers
local state = require('readstate')
local inspect = require('inspect')

function ai_timer()
  --print(string.format("%.2f\n", os.clock()))
end
-- Pass state as arg1 and pass team folder as arg 2
function run_ai()
  print(arg[1])
  print(arg[2])

-- Run gamestate
  local game_state = state.readstate(arg[1])
-- Compile function, text only, in jail.
  local env = {} 
  loaded_ai = loadfile(arg[2] .. "/run.lua","t",env)
-- Start the clock.
  debug.sethook(ai_timer, "l")
-- Run.
  loaded_ai()
  loaded_ai.run(game_state,output)

end

run_ai()