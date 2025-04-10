###################################################################################################
# Company: 
# - ISEC, Graz Universtiy of Technology
# Engineer: 
# - Florian Hirner
# - Florian Krieger
###################################################################################################

from prng_edge_address import prng_edge_address_singleton
from prng_edge_weight import prng_edge_weight_singleton

class ExpanderGraph:

  # Class variable 

  num_left_nodes  = 0
  num_right_nodes = 0

  degree_left = 0
  degree_right = 0

  El = []
  Er = []

  #----------------------------------------------------------------------------
  # Initializing of class
  #----------------------------------------------------------------------------

  def __init__(self, L, R, DEG_L, DEG_R):
    self.name = "Expander Graph Class"
    self.version = "1.0"

    self.num_left_nodes  = L
    self.num_right_nodes = R

    self.degree_left    = DEG_L
    self.degree_right   = DEG_R

    print(f"[EG][init] {L=}, {R=}, {DEG_L=}, {DEG_R=}")

    # generate left node list to store reverse mapping
    Er = [[] for _ in range(self.num_right_nodes)]

    # connect left nodes to right nodes and store the corresponding edge informations
    for _lnode in range(self.num_left_nodes):
      _El = []
      for _edge in range(self.degree_left):
        _edge_addr = prng_edge_address_singleton.random() % self.num_right_nodes
        _edge_weight = prng_edge_weight_singleton.random()
        _El.append([_edge_addr, _edge_weight])
        Er[_edge_addr].append(_lnode)
      self.El.append(_El)
      # print(f"[EG][init] > {_lnode=} {len(_El)}")

    # calculate average degree of left node
    # print(f"")
    # print(f"{len(Er)}")
    rnode_average = len(Er[0])
    for _rnode in Er:
      # print(f"{len(_rnode)}")
      rnode_average = (rnode_average + len(_rnode)) / 2
    print(f"[EG][init] > average left node degree: {int(rnode_average)}")

    # exit(0)

  #----------------------------------------------------------------------------
  # routines 
  #----------------------------------------------------------------------------
  
  def function(self):
    print(f"[INFO] function...")
    return
  
###################################################################################################
