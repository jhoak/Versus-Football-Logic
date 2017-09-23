-- Load helpers
local state = require('readstate')
local inspect = require('inspect')

function ai_timer()
  print(env.commands)
end
-- Pass state as arg1 and pass team folder as arg 2
function run_ai()
  
  local game_state_l = state.readstate(arg[1])

--
  local passtable = {}
  passtable["insert"] = table.insert


  --print(inspect(game_state_l))

  env = {
    print = print,
    pairs = pairs,
    table = passtable,
    game_state = game_state_l,
    commands = {}
  }

  loaded_ai = loadfile(arg[2] .. "/run.lua","t",env)
-- Start the clock.
  debug.sethook(ai_timer, "l")
-- Run.
-- TODO: if this is nil, then it didn't compile.
  loaded_ai()
end

run_ai()