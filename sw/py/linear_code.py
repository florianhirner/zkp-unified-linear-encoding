###################################################################################################
# Company: 
# - Institute of Information Security (ISEC) 
# - Graz Universtiy of Technology
# Engineer: 
# - Florian Hirner
# - Florian Krieger
###################################################################################################

from params import *
from expander_graph import *

class LinearCode:

  # Class variables
  size_message = 0
  size_codeword = 0

  # Expanders
  ExpanderGraphs = []

  #----------------------------------------------------------------------------
  # Initializing of class
  #----------------------------------------------------------------------------

  def __init__(self, size):
    self.name = "Linear Code Class"
    self.version = "1.0"
    self.size_message = size
    self.size_codeword = int(size * Params.r)

    print(f"[LC][INIT] {self.size_message  =}")
    print(f"[LC][INIT] {self.size_codeword =}")
    print(f"[LC][INIT] {Params.distance_threshold =}")
    print(f'')

    # size = self.size_message
    # while size > Params.distance_threshold:
    #   print(f"> {size=}")
    #   size = int(size * Params.alpha)
    #   print(f">> {size=}")

    #######################

    round_ctr = 0
    round_info = []
    round_addr = []
    
    n_in = self.size_message
    n_out = n_in
    ns = []

    rd_addr = 0
    wr_addr = self.size_message

    # Right Expander / Recursion down

    # for round_ctr in range(rounds):
    while n_in > Params.distance_threshold:
      print(f"[LC][R] {round_ctr=}")
      ns.append(n_in)

      # run expander
      n_new = int(Params.alpha * n_in)
      n_out += n_new
      deg_r = Params.cn

      L, R = n_in, n_new
      print(f'[LC][R] > {n_in=}, {n_out=}, {rd_addr=}, {wr_addr=}')
      # print(f'L = {L},   R = {R},   d1 = {deg_r}')

      # EG = ExpanderGraph(L, R, deg_r, 0)
      self.ExpanderGraphs.append(ExpanderGraph(round_ctr, L, R, deg_r, 0))

      round_info.append([n_in, n_in, n_new, rd_addr, deg_r])

      rd_addr += n_in
      wr_addr += R
      round_addr.append([rd_addr, wr_addr])

      n_in = n_new    

      round_ctr += 1
      print(f'')
    print(f'')

    # Left Expander / Recursion up

    for _recursion in range(len(ns)):
      print(f"[LC][L] {round_ctr=}")

      n_in = ns.pop()
      n_new = int(Params.alpha * n_in)
      if _recursion != 0:
          n_new = int(Params.r * n_new)
      r = int(n_in * (Params.r - 1)) - n_new
      n_out += r
      deg_r = Params.dn

      L, R = n_new, r
      print(f'[LC][L] > {n_in=}, {n_out=}, {rd_addr=}, {wr_addr=}')
      # print(f'>> L = {L}, R = {R}, d1 = {deg_r}')

      # EG = ExpanderGraph(L, R, deg_r, 0)
      self.ExpanderGraphs.append(ExpanderGraph(round_ctr, L, R, deg_r, 0))

      round_info.append([n_in, n_new, r, rd_addr, deg_r])

      rd_addr -= n_in
      wr_addr += R
      round_addr.append([rd_addr, wr_addr])

      round_ctr += 1
      print(f'')
    print(f'')

    return

  #----------------------------------------------------------------------------
  # routines
  #----------------------------------------------------------------------------
  
  # ROM_LC_LNODES.mem
  # ROM_LC_RNODES.mem

  # ROM_LC_EG_LNODE_DEGREES.mem
  # ROM_LC_EG_RNODE_DEGREES.mem

  def write_to_memory(self):
    print(f"[LC][W2M] write all expander graphs to memory")

    for _i, _ExpanderGraph in enumerate(self.ExpanderGraphs):
      print(f'[LE][W2M] > {_i=} {_ExpanderGraph.lnodes=}, {_ExpanderGraph.rnodes=}')
      _ExpanderGraph.write_to_memory()
  
    ROM_LC_LNODES = []
    ROM_LC_RNODES = []

    ROM_LC_LDEGREES = []
    ROM_LC_RDEGREES = []

    for _i, _ExpanderGraph in enumerate(self.ExpanderGraphs):
      print(f'[LE][INIT] > {_i=} \n\t-lnodes/ldegree: {_ExpanderGraph.lnodes}/{_ExpanderGraph.ldegree}\n\t-rnodes/rdegree: {_ExpanderGraph.rnodes}/{_ExpanderGraph.rdegree}')
      ROM_LC_LNODES.append(_ExpanderGraph.lnodes)
      ROM_LC_RNODES.append(_ExpanderGraph.rnodes)
      ROM_LC_LDEGREES.append(_ExpanderGraph.ldegree)
      ROM_LC_RDEGREES.append(_ExpanderGraph.rdegree)
    #   #
    #   # print(f'>> #El: {len(_ExpanderGraph.El)}')
    #   for _lnode in _ExpanderGraph.El:
    #     for _edge in _lnode:
    #       ROM_LC_EG_LNODE_DEGREES.append(_edge)
    #   #
    #   # print(f'>> #Er: {len(_ExpanderGraph.Er)}')
    #   for _rnode in _ExpanderGraph.Er:
    #     for _edge in _rnode:
    #       ROM_LC_EG_RNODE_DEGREES.append(_edge)
    #   #
    # #   print(f'>> {len(ROM_LC_EG_LNODE_DEGREES)}')
    # #   print(f'>> {len(ROM_LC_EG_RNODE_DEGREES)}')
      # print(f'')
    print(f'')

    # # print(f'> {len(ROM_LC_EG_LNODE_DEGREES)}')
    # # print(f'> {len(ROM_LC_EG_RNODE_DEGREES)}')

    # # create memory file(s)

    f = open(f"rom/linear_code/ROM_LC_LNODES.mem", "w")
    for _ in ROM_LC_LNODES:
      hex_str = "{:08x}".format(_) + "\n"
      f.write(hex_str)

    f = open(f"rom/linear_code/ROM_LC_LDEGREES.mem", "w")
    for _ in ROM_LC_LDEGREES:
      hex_str = "{:08x}".format(_) + "\n"
      f.write(hex_str)
    
    f = open(f"rom/linear_code/ROM_LC_RNODES.mem", "w")
    for _ in ROM_LC_RNODES:
      hex_str = "{:08x}".format(_) + "\n"
      f.write(hex_str)

    f = open(f"rom/linear_code/ROM_LC_RDEGREES.mem", "w")
    for _ in ROM_LC_RDEGREES:
      hex_str = "{:08x}".format(_) + "\n"
      f.write(hex_str)

    return
  
###################################################################################################

# > n_in = 256,      L = 256,        R = 60,         ptr = 0,        d1 = 42
# > n_in = 60,       L = 60,         R = 14,         ptr = 256,      d1 = 42
# > n_in = 14,       L = 14,         R = 3,          ptr = 316,      d1 = 42
# > n_in = 14,       L = 3,          R = 7,          ptr = 330,      d2 = 26
# > n_in = 60,       L = 24,         R = 19,         ptr = 316,      d2 = 26
# > n_in = 256,      L = 103,        R = 81,         ptr = 256,      d2 = 26