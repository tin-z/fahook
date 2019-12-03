import angr

def find_avoid_hook(proj_name, find_addr, avoid_addr=[], hooks=[]):
  ''' find_avoid_hook( 
        proj_name: executable name path, 
        find_addr: list of address that you want all to be match,
        avoid_addr: list of any address that you list to avoid from jumping in,
        hooks:  symbols to hook from plt 
        )  -> returns the tuple Project, Simgr
        
        Just as the name say, it Finds, Avoid and Hook
  '''
  try:
    proj = angr.Project(proj_name, auto_load_libs=False)
    base_address=proj.loader.main_object.min_addr
    state = proj.factory.entry_state()
    simgr = proj.factory.simulation_manager(state)
    simgr.use_technique(angr.exploration_techniques.DFS())

    main_obj = obj = proj.loader.main_object
    hook_by = get_right_hook(str(proj.arch))

    [proj.hook(main_obj.plt[x], hook_by) for x in hooks]
    print("[+] hook done, starting explore..")
    simgr.explore(find=find_addr, avoid=avoid_addr)
    print("[+] All si done here, returning..")
    return (proj, simgr)
  except Exception as ex:
    print("Exception caught.. {0}".format(ex.message))


def ret0_x64(state):
  state.regs.rax = 0
  state.regs.rip = state.mem[state.regs.rsp].uint64_t.resolved
  state.regs.rsp = state.regs.rsp + 8

def ret0_x86(state):
  state.regs.eax = 0
  state.regs.eip = state.mem[state.regs.esp].uint32_t.resolved
  state.regs.esp = state.regs.esp + 4

def ret0_armel(state):
  state.regs.r0 = 0
  state.regs.pc = state.regs.lr
  state.regs.lr = state.mem[state.regs.r11].uint32_t.resolved

def get_right_hook(arch_now):
    archs = {"<Arch X86 (LE)>":ret0_x86, "<Arch AMD64 (LE)>":ret0_x64, "<Arch ARMEL (LE)>":ret0_armel}
    try: 
      rets = archs[arch_now]
    except:
      raise Exception("The Arch {0} is not supported\nYou can implement it by yourself and than update the archs list")
    return rets



def example(looking_for=b"flag{"):
  proj_name = "test1"
  # if you recompile the binary thant remember to change those value
  avoid_addr = [0x400000 + 0x784]
  find_addr = [0x400000 + 0x720]
  hooks = ['sleep', 'srand', 'rand', 'time']
  proj, stashes = find_avoid_hook(proj_name, find_addr, avoid_addr, hooks) 

  if stashes.found is []:
    print("Nothing found")
    return

  simgr = proj.factory.simulation_manager(stashes.found[0])
  simgr.explore(find=lambda s: looking_for in s.posix.dumps(1))
  print(simgr.found[0].posix.dumps(1))

