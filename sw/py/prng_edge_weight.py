###################################################################################################
# Company: 
# - Institute of Information Security (ISEC) 
# - Graz Universtiy of Technology
# Engineer: 
# - Florian Hirner
# - Florian Krieger
###################################################################################################

import random

from params import *
from ctypes import *

###################################################################################################

# Trivium PRNG with 64 bit

trivium64_so_file_weight = "./../c++/trivium/pythonConnector64_weight.so"

CHandler_PRNG_64_weight = CDLL(trivium64_so_file_weight)

def trivium64_weight_setseed(seed, seq):
    CHandler_PRNG_64_weight.trivium64_setseed(c_uint64(seed), c_uint64(seq))

def trivium64_weight_next():
    CHandler_PRNG_64_weight.trivium64_next.restype = c_uint64
    return CHandler_PRNG_64_weight.trivium64_next()

###################################################################################################

class PrngEdgeWeight:

  # Class variables

  #----------------------------------------------------------------------------
  # Initializing of class
  #----------------------------------------------------------------------------

  def __init__(self, seed):
    self.name = "Prng Weight Class"
    self.version = "1.0"

    trivium64_weight_setseed(seed, 0) # std = 0

  #----------------------------------------------------------------------------
  # routines
  #----------------------------------------------------------------------------
  
  def random(self):
    # return random.randint(0, 2**32-1)
    return trivium64_weight_next()

###################################################################################################

prng_edge_weight_singleton = PrngEdgeWeight(PrngSeed.SEED_WEIGHT)