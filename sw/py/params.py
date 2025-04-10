###################################################################################################
# Company: 
# - ISEC, Graz Universtiy of Technology
# Engineer: 
# - Florian Hirner
# - Florian Krieger
###################################################################################################

# use the same distance parameter from brakedown

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

# PrimeField
class Prime:
  LOGQ = 64
  LOGP = 61
  PRIME = (1<<LOGP)-1

# Prng
class PrngSeed:
  SEED_ADDR   = 0
  SEED_WEIGHT = 1
