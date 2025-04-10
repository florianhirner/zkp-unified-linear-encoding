###################################################################################################
# Company: 
# - Institute of Information Security (ISEC) 
# - Graz Universtiy of Technology
# Engineer: 
# - Florian Hirner
# - Florian Krieger
###################################################################################################

from linear_code import *

class PolynomialCommitment:

  # Class variables
  lg_k = 7
  lg_d = 8
  lg_n = lg_k + lg_d

  k = pow(2, lg_k)
  d = pow(2, lg_d)
  n = pow(2, lg_n)

#   ldegree1 = 10
#   ldegree2 = 20

#   rdegree1 = 42
#   rdegree2 = 26

  LC = None

  #----------------------------------------------------------------------------
  # Initializing of class
  #----------------------------------------------------------------------------

  def __init__(self, lg_k, lg_d):
    self.name = "Polynomial Commitment Class"
    self.version = "1.0"
    self.lg_k = lg_k
    self.lg_d = lg_d
    self.lg_n = lg_k + lg_d
    self.LC = None # LinearCode(2**lg_d)

    print(f"[PC][INIT] {self.lg_k=}")
    print(f"[PC][INIT] {self.lg_d=}")
    print(f"[PC][INIT] {self.lg_n=}")
    print(f"")

    return

  #----------------------------------------------------------------------------
  # routines
  #----------------------------------------------------------------------------
  
  def init_expander_graph(self):
    print(f"[PC][INIT-EG] create expander graph ...")
    self.LC = LinearCode(2**self.lg_d)
    self.LC.write_to_memory()

  def commit(self, msg):
    print(f"[PC][COMMIT] Commit to given msg ...")
    for _row in msg:
      self.encode(_row)

  def prove(self):
    print(f"[PC][PROVE ] Generate a proof ...")
    # Add proving logic here

  def verify(self):
    print(f"[PC][VERIFY] Verify proof ...")
    # Add verification logic here

  #----------------------------------------------------------------------------
  # subroutines
  #----------------------------------------------------------------------------
  
  def encode(self, row):
    # print(f"[INFO] Encoding row ...")
    # TODO Add encoding logic here
    return

  def graph_generation(self):
    # print(f"[INFO] Generating graph for {self.name}...")
    # Add graph generation logic here
    return

  def post_process(self):
    # print(f"[INFO] Post-processing for {self.name}...")
    # TODO Add post-processing logic here
    return
  
  def merkle_hash(self):
    # print(f"[INFO] Generating Merkle hash for {self.name}...")
    # TODO Add Merkle hash generation logic here
    return
  
  def merkle_tree(self):
    # print(f"[INFO] Generating Merkle tree for {self.name}...")
    # TODO Add Merkle tree generation logic here
    return
  
###################################################################################################
