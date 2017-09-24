-- Load helpers
local state = require('readstate')
local inspect = require('inspect')

function save_results()
  -- operates on "commands" local
  -- Write 'SET' commands
  -- dude n^2 lmao
  io.output("result.txt","w")
  for key,value in pairs(env.commands) do
    -- linemen set commands
    if(value[1] == "C" or value[1] == "LG" or value[1] == "RG" or value[1] == "LT" or value[1] == "RT") then
      io.write("SET,", value[1], ",", key, "\n")
    end
    -- Receiver set commands
    if(value[1] == "R") then
      io.write("SET,R,",key, ",", value[2], ",", value[3], "\n")
    end

    --QB set command
    if(value[1] == "QB") then
      io.write("SET,QB,", key, ",", value[2], "\n")
    end
  end
end

function ai_timer()
  if os.clock() - start_time > 0.04 then
    print "Time is up!"
    save_results(env.commands)
    os.exit()
  end;
end
-- Pass state as arg1 and pass team folder as arg 2
function run_ai()

-- Load gamestate
  local game_state_l = state.readstate(arg[1])

-- Init Env
  local passtable = {}
  passtable["insert"] = table.insert
  env = {
    print = print,
    pairs = pairs,
    table = passtable,
    game_state = game_state_l,
    commands = {}
  }

-- Compile Code
  loaded_ai = loadfile(arg[2] .. "/run.lua","t",env)
-- Start the clock.
  start_time  = os.clock()
  debug.sethook(ai_timer, "l")
-- TODO: if this is nil, then it didn't compile.
  loaded_ai()
  save_results()
end

run_ai()