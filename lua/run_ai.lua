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
    -- Receiver set commands (same as D)
    if(value[1] == "R") or (value[1] == "D") then
      io.write("SET,",value[1],",",key, ",", value[2], ",", value[3], "\n")
    end

    --QB set command
    if(value[1] == "QB") then
      io.write("SET,QB,", key, ",", value[2], "\n")
    end

    --Move command
    if(value[1] == "MOVE") then
      io.write("MOVE,", key, ",", value[2], "\n")
    end
  end
  -- Save memory string.
  file = io.open(arg[2] .. "/memory", "w")
  file:write(env.memory)
end

function ai_timer()
  if os.clock() - start_time > 0.04 then
    print "Time is up!"
    save_results(env.commands)
    os.exit()
  end;
end

function file_exists(name)
   local f=io.open(name,"r")
   if f~=nil then io.close(f) return true else return false end
end

function read_all(file)
  local f = io.open(file, "rb")
  local content = f:read("*all")
  f:close()
  return content
end

-- Pass state as arg1 and pass team folder as arg 2
function run_ai()

-- Load gamestate
  local game_state_l = state.readstate(arg[1])



-- Load Memory from Disk. AI user can do whatever with it. Limit to string for now.

  mem_path = arg[2] .. "/memory"

  if(file_exists(mem_path)) then
    memory = read_all(mem_path)
  else
    memory = ""
  end

-- Init Env
  local passtable = {}
  local strtable = {}

  passtable["insert"] = table.insert
  strtable["gmatch"] = string.gmatch

  env = {
    print = print,
    pairs = pairs,
    table = passtable,
    string = strtable,
    game_state = game_state_l,
    commands = {},
    tostring = tostring,
    memory = memory
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