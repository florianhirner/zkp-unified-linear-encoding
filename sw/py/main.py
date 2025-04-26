###################################################################################################
# Company: 
# - Institute of Information Security (ISEC) 
# - Graz Universtiy of Technology
# Engineer: 
# - Florian Hirner
# - Florian Krieger
###################################################################################################

import random
import sys

from params import *
from polynomial_commitment import *

#--------------------------------------------------------------------------------------------------

def main():
  args = sys.argv[1:]
  print(f'[MAIN] > {len(args)} : {args}')

  lg_k   = int(args[0])
  lg_d   = int(args[1])
  deg1_r = 10 # int(args[2])
  deg1_l = 20 # int(args[3])
  deg2_r = 42 # int(args[4])
  deg2_l = 26 # int(args[5])

  lg_N = lg_k + lg_d

  print(f'[MAIN] > {lg_k  =}')
  print(f'[MAIN] > {lg_d  =}')
  print(f'[MAIN] > {lg_N  =}')
  print(f'[MAIN] > {deg1_r=}')
  print(f'[MAIN] > {deg1_l=}')
  print(f'[MAIN] > {deg2_r=}')
  print(f'[MAIN] > {deg2_l=}')
  print(f'')

  # msg = [[random.randint(0, 10) for _coef in range(2**lg_d)] for _row in range(2**lg_k)]
  msg = [[ExtensionField() for _coef in range(2**lg_d)] for _row in range(2**lg_k)]
  # msg = [[ExtensionField(0, 10) for _coef in range(2**lg_d)] for _row in range(2**lg_k)]

  PC = PolynomialCommitment(lg_k, lg_d)
  PC.init_expander_graph()
  PC.commit(msg=msg)
  PC.prove()
  PC.verify()

  return 0

# python main.py <lg_k> <lg_d> <deg1_r> <deg1_l> <deg2_r> <deg2_l> 
# python main.py 7 8 10 20 42 26

if __name__ == "__main__":
    main()