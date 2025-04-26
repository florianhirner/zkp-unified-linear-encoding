###################################################################################################
# Company: 
# - ISEC, Graz Universtiy of Technology
# Engineer: 
# - Florian Hirner
# - Florian Krieger
###################################################################################################

# use the same distance parameter from brakedown

import math
import random

###############################################################################
# Params
class Params:
  r = 1.72
  cn = 10
  dn = 20
  beta = 0.1205
  alpha = 0.238
  rs_rate = 2
  column_size = 128
  target_distance = 0.07
  distance_threshold = int((1.0 / target_distance) - 1)


###############################################################################
# PrimeField
class Prime:
  LOGQ = 64
  LOGP = 61
  PRIME = (1<<LOGP)-1

###############################################################################
# ExtensionField
class ExtensionField:
  LOGQ = 64
  LOGP = 61
  PRIME = (1<<LOGP)-1

  real = 0
  img = 0

  # Initialize object
  def __init__(self, real=None, img=None):
    if real is not None and img is not None:
      self.real = real % self.PRIME
      self.img  = img  % self.PRIME
    else:
      self.real = random.randint(0, self.PRIME-1)
      self.img  = random.randint(0, self.PRIME-1)

  # represent class as string
  def __str__(self):
    return "{:016x}".format(self.real) + "." + "{:016x}".format(self.img)

  # overload add operation
  def __add__(self, other):
    # (a + bi) + (c  + di)
    # (a + c ) + (di + di)
    real = self.real + other.real % self.PRIME
    img  = self.img  + other.img  % self.PRIME
    return ExtensionField(real, img)

  # overload mul operation
  def __mul__(self, other):
    # (a + bi)(c + di)
    ac = self.real * other.real % self.PRIME
    bd = self.img  * other.img  % self.PRIME
    bc = self.img  * other.real % self.PRIME
    ad = self.real * other.img  % self.PRIME
    # ac - bd + (bc + ad)i
    real = ac - bd % self.PRIME
    img  = bc + ad % self.PRIME
    return ExtensionField(real, img)

###############################################################################
# Prng
class PrngSeed:
  SEED_ADDR   = 0
  SEED_WEIGHT = 1

