###################################################################################################
# Company: 
# - Institute of Information Security (ISEC) 
# - Graz Universtiy of Technology
# Engineer: 
# - Florian Hirner
# - Florian Krieger
###################################################################################################

import time
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

  LC = None # Linear Code

  # MSG = None # Message
  # ENC = None # Endoded Message

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
    # self.LC.write_to_memory() # TODO fix

  def commit(self, msg):
    print(f"[PC][COMMIT] Commit to given msg ...")
    enc = []
    for _i, _row in enumerate(msg):
      print(f"[PC][COMMIT] > {_i=}/{len(msg)=}")
      _enc = self.encode(_row)
      enc.append(_enc)
    return enc

  def prove(self):
    print(f"[PC][PROVE ] Generate a proof ...")
    # Add proving logic here
    return 0

  def verify(self):
    print(f"[PC][VERIFY] Verify proof ...")
    # Add verification logic here
    return 0

  #----------------------------------------------------------------------------
  # subroutines
  #----------------------------------------------------------------------------
  
  def encode(self, row):
    print(f"[INFO] Encoding row ...")

    # encode with left to right evaluation
    start = time.time()
    enc = self.encode_l2r(row)
    end = time.time()
    print('Execution Time: {}'.format(end-start))

    # encode with right to left evaluation
    start = time.time()
    enc_inv = self.encode_r2l(row)
    end = time.time()
    print('Execution Time: {}'.format(end-start))
    
    # compare 
    error = 0
    for _i, _j in zip(enc, enc_inv):
      if (_i.real != _j.real or _i.img != _j.img):
        error += 1
        print(f'{str(_i)} != {str(_j)}')
    
    print(f'{error=}')
    return enc, enc_inv

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
  
  #----------------------------------------------------------------------------
  # subsubroutines
  #----------------------------------------------------------------------------
  
  def encode_l2r(self, row):
    # print(f'[PC][ENC][L2R] {len(row)} -> {int(len(row) * 1.72)}')
    enc = row + [ExtensionField(0, 0)] * int(len(row) * 1.72)
    for _expander, _expander_offset in zip(self.LC.ExpanderGraphs, self.LC.ExpanderGraphsOffset):
      # print(f'[PC][ENC][L2R][LC] {_expander.lnodes=} - {_expander.rnodes=} :  {_expander_offset=}')
      rd_offset, wr_offset = _expander_offset
      for _li, _lnode in enumerate(_expander.El):
        # print(f'[PC][ENC][L2R][LC][EG] {len(_lnode)=}:')
        for _ei, _edge in enumerate(_lnode):
          # print(f'[PC][ENC][L2R][LC][EG] > {_edge.lnode=} - {_edge.rnode=} - {_edge.weight=}')

          _rd_index = rd_offset + _edge.lnode
          _wr_index = wr_offset + _edge.rnode

          _lnode_val = enc[_rd_index]
          _rnode_val = enc[_wr_index]

          # add left node to right node
          # _acc = (_lnode_val * _edge.weight) + _rnode_val
          _acc = (_lnode_val * _edge.weight)
          _acc = _acc + _rnode_val
          # _acc = _acc % Prime.PRIME
          enc[_wr_index] = _acc

          # print(f'[PC][ENC][L2R][LC][EG] > {_rnode=} * {_edge.weight=} * {_lnode=}')
          # print(f'[PC][ENC][L2R][LC][EG] = {_acc=}')

    return enc
  
  def encode_r2l(self, row):
    # print(f'[PC][ENC][R2L] {len(row)} -> {int(len(row) * 1.72)}')
    enc = row + [ExtensionField(0, 0)] * int(len(row) * 1.72)
    for _expander, _expander_offset in zip(self.LC.ExpanderGraphs, self.LC.ExpanderGraphsOffset):
      # print(f'[PC][ENC][R2L][LC] {_expander.lnodes=} - {_expander.rnodes=} :  {_expander_offset=}')
      rd_offset, wr_offset = _expander_offset
      for _ri, _rnode in enumerate(_expander.Er):
        # print(f'[PC][ENC][R2L][LC][EG] {len(_rnode)=}:')
        _acc_val = ExtensionField(0, 0)
        for _ei, _edge in enumerate(_rnode):
          # print(f'[PC][ENC][R2L][LC][EG] > {_edge.lnode=} - {_edge.rnode=} - {_edge.weight=}')
          # print(f'[PC][ENC][R2L][LC][EG] = {_acc_val=}')

          _rd_index = rd_offset + _edge.lnode
          # _wr_index = wr_offset + _edge.rnode

          _lnode_val = enc[_rd_index]
          # _rnode_val = enc[_wr_index]          # accumulate left node
          # print(f'[PC][ENC][R2L][LC][EG] > {_lnode_val=} * {_rnode_val=}')

          # _res_val = (_lnode_val * _edge.weight) + _rnode_val
          # _res_val = _res_val % Prime.PRIME
          # enc[_wr_index] = _res_val

          _acc_val += (_lnode_val * _edge.weight)
          # _acc_val = _acc_val % Prime.PRIME

          # print(f'[PC][ENC][R2L][LC][EG] > {_lnode_val=} * {_edge.weight=} * {_res_val=}')
          # print(f'[PC][ENC][R2L][LC][EG] > {_lnode_val=} * {_edge.weight=} * {_acc_val=}')
          # print(f'[PC][ENC][R2L][LC][EG] = {_acc_val=}')
        # enc[_wr_index] = _acc_val
        enc[wr_offset + _ri] = _acc_val

    return enc
  
###################################################################################################
