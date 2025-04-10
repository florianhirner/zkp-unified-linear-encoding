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

    print(f"[LC][init] {self.size_message  =}")
    print(f"[LC][init] {self.size_codeword =}")
    print(f"[LC][init] {Params.distance_threshold =}")

    # size = self.size_message
    # while size > Params.distance_threshold:
    #   print(f"> {size=}")
    #   size = int(size * Params.alpha)
    #   print(f">> {size=}")

    #######################

    round = 0
    round_info = []
    
    n_in = self.size_message
    n_out = n_in

    rd_addr = 0
    wr_addr = self.size_message

    ns = []


    print(f'')
    print(f'')

    # Right Expander / Recursion down

    # for round in range(rounds):
    while n_in > Params.distance_threshold:
      print(f"[LC][R] {round=}")
      round += 1
      ns.append(n_in)
      # run expander
      n_new = int(Params.alpha * n_in)
      deg_r = Params.cn

      n_out += n_new
      L = n_in
      R = n_new

      print(f'[LC][R] > {n_in=}, {n_out=}, {rd_addr=}, {wr_addr=}')
      # print(f'L = {L},   R = {R},   d1 = {deg_r}')

      EG = ExpanderGraph(L, R, deg_r, 0)

      round_info.append([n_in, n_in, n_new, rd_addr, deg_r])

      rd_addr += n_in
      wr_addr += R

      n_in = n_new    
      
      print(f'')
    print(f'')

    # Left Expander / Recursion up

    for _recursion in range(len(ns)):
      print(f"[LC][L] {round=}")
      round += 1

      n_in = ns.pop()
      n_new = int(Params.alpha * n_in)
      if _recursion != 0:
          n_new = int(Params.r * n_new)
      r = int(n_in * (Params.r - 1)) - n_new
      deg_r = Params.dn

      n_out += r
      L = n_new
      R = r

      print(f'[LC][L] > {n_in=}, {n_out=}, {rd_addr=}, {wr_addr=}')
      # print(f'>> L = {L}, R = {R}, d1 = {deg_r}')

      EG = ExpanderGraph(L, R, deg_r, 0)

      round_info.append([n_in, n_new, r, rd_addr, deg_r])

      rd_addr -= n_in
      wr_addr += R

      print(f'')
    print(f'')
    

  #----------------------------------------------------------------------------
  # routines
  #----------------------------------------------------------------------------
  
  def function(self):
    print(f"[INFO] function...")
    return
  
###################################################################################################

# > n_in = 256,      L = 256,        R = 60,         ptr = 0,        d1 = 42
# > n_in = 60,       L = 60,         R = 14,         ptr = 256,      d1 = 42
# > n_in = 14,       L = 14,         R = 3,          ptr = 316,      d1 = 42
# > n_in = 14,       L = 3,          R = 7,          ptr = 330,      d2 = 26
# > n_in = 60,       L = 24,         R = 19,         ptr = 316,      d2 = 26
# > n_in = 256,      L = 103,        R = 81,         ptr = 256,      d2 = 26