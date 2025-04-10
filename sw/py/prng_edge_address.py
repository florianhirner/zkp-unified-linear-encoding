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

trivium64_so_file_address = "./../c++/trivium/pythonConnector64_address.so"

CHandler_PRNG_64_address = CDLL(trivium64_so_file_address)

def trivium64_address_setseed(seed, seq):
    CHandler_PRNG_64_address.trivium64_setseed(c_uint64(seed), c_uint64(seq))

def trivium64_address_next():
    CHandler_PRNG_64_address.trivium64_next.restype = c_uint64
    return CHandler_PRNG_64_address.trivium64_next()

###################################################################################################

class PrngEdgeAddress:

  # Class variables
  
  #----------------------------------------------------------------------------
  # Initializing of class
  #----------------------------------------------------------------------------

  def __init__(self, seed):
    self.name = "Prng Edge Class"
    self.version = "1.0"

    trivium64_address_setseed(seed, 0) # std = 0

  #----------------------------------------------------------------------------
  # routines
  #----------------------------------------------------------------------------
  
  def random(self):
    # return random.randint(0, 2**32-1)
    return trivium64_address_next()

###################################################################################################

prng_edge_address_singleton = PrngEdgeAddress(PrngSeed.SEED_ADDR)