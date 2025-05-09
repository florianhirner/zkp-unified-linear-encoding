###################################################################################################
# Company: 
# - ISEC, Graz Universtiy of Technology
# Engineer: 
# - Florian Hirner
# - Florian Krieger
###################################################################################################

from params import ExtensionField
from prng_edge_address import prng_edge_address_singleton
from prng_edge_weight import prng_edge_weight_singleton

###################################################################################################
#--------------------------------------------------------------------------------------------------

class GraphEdge:

  # Class variable 
  lnode = 0
  rnode = 0
  weight = 0

  def __init__(self, lnode, rnode, weight):

    self.lnode  =  lnode 
    self.rnode  =  rnode 
    self.weight = weight
    return

# endofclase

#--------------------------------------------------------------------------------------------------

class ExpanderGraph:

  # Class variable 
  id = 0

  lnodes  = 0
  rnodes = 0

  ldegree = 0
  rdegree = 0

  ldegree_min = 0
  rdegree_min = 0

  El = []
  Er = []

  #----------------------------------------------------------------------------
  # Initializing of class
  #----------------------------------------------------------------------------

  def __init__(self, id, L, R, DEG_L, DEG_R):
    self.name = "Expander Graph Class"
    self.version = "1.0"

    self.id = id
    self.lnodes = L
    self.rnodes = R

    self.ldegree = DEG_L
    self.rdegree = DEG_R

    self.ldegree_min = DEG_L
    self.rdegree_min = DEG_R

    print(f"[EG][INIT] {L=}, {R=}, {DEG_L=}, {DEG_R=}")

    # generate left node list to store reverse mapping
    self.El = []
    self.Er = [[] for _ in range(self.rnodes)]

    # connect left nodes to right nodes and store the corresponding edge informations
    for _lnode in range(self.lnodes):
      _El = []
      for _edge in range(self.ldegree):
        _edge_addr = prng_edge_address_singleton.random() % self.rnodes
        # _edge_weight = prng_edge_weight_singleton.random()
        _edge_weight = ExtensionField(prng_edge_weight_singleton.random(), prng_edge_weight_singleton.random())
        _edge_data = GraphEdge(_lnode, _edge_addr, _edge_weight)
        _El.append(_edge_data)
        self.Er[_edge_addr].append(_edge_data)
      self.El.append(_El)
      # print(f"[EG][INIT] > {_lnode=} {len(_El)}")

    print(f"[EG][INIT] > #self.El : {len(self.El)}, {len(self.El[0])}")
    print(f"[EG][INIT] > #self.Er : {len(self.Er)}, {len(self.Er[0])}")

    # calculate average degree of left node
    # print(f"")
    # print(f"{len(Er)}")
    rnode_average = 0
    for _rnode in self.Er:
      # print(f"{len(_rnode)}")
      rnode_average += len(_rnode)
    rnode_average = rnode_average // len(self.Er)
    self.rdegree   = rnode_average
    print(f"[EG][INIT] > average left node degree: {int(rnode_average)}")
    return

  #----------------------------------------------------------------------------
  # routines 
  #----------------------------------------------------------------------------

  def generate_l2r_graph(self):
    print(f"[EG][L2R-GG] Generate graph in left to right order")
    return
  
  def post_process_graph(self):
    print(f"[EG][R2L-PP] Post process r2l graph according to security analysis")
    return
  
  def generate_r2l_graph(self):
    print(f"[EG][R2L-GG] Generate graph in right to left order")
    return
  
  #----------------------------------------------------------------------------
  # dump to memory functions 
  #----------------------------------------------------------------------------

  def write_to_memory(self):
    print(f"[EG][W2M] write graph data to memory")

    ROM_EG_lnodes = []
    ROM_EG_rnodes = []

    ROM_EG_NUM_LEDGES = []
    ROM_EG_NUM_REDGES = []

    ROM_EG_NUM_LWEIGHTS = []
    ROM_EG_NUM_RWEIGHTS = []

    # left_2_right
    print(f"[EG][W2M] write graph (left_2_right) to memory")
    for _li, _lnode in enumerate(self.El):
      ROM_EG_lnodes.append(_li)
      for _legde in _lnode:
        ROM_EG_NUM_LEDGES.append(_legde.rnode)
        ROM_EG_NUM_LWEIGHTS.append(_legde.weight)

    print(f"[EG][W2M] > LNODES  : {len(ROM_EG_lnodes)}")
    print(f"[EG][W2M] > LEDGES  : {len(ROM_EG_NUM_LEDGES)}")
    print(f"[EG][W2M] > LWEIGHTS: {len(ROM_EG_NUM_LWEIGHTS)}")
    print(f"")

    f = open(f"rom/expander_graph/ROM_EG_{self.id}_LNODES.mem", "w")
    for _ in ROM_EG_lnodes:
      hex_str = "{:08x}".format(_) + "\n"
      f.write(hex_str)

    f = open(f"rom/expander_graph/ROM_EG_{self.id}_LADDR.mem", "w")
    for _ in ROM_EG_NUM_LEDGES:
      hex_str = "{:08x}".format(_) + "\n"
      f.write(hex_str)

    f = open(f"rom/expander_graph/ROM_EG_{self.id}_LWEIGHTS.mem", "w")
    for _ in ROM_EG_NUM_LWEIGHTS:
      hex_str = "{:08x}".format(_) + "\n"
      f.write(hex_str)

    # right_2_left
    print(f"[EG][W2M] write graph (right_2_left) to memory")
    for _ri, _rnode in enumerate(self.Er):
      ROM_EG_rnodes.append(_ri)
      for _regde in _rnode:
        ROM_EG_NUM_REDGES.append(_regde.lnode)
        ROM_EG_NUM_RWEIGHTS.append(_regde.weight)

    print(f"[EG][W2M] > RNODES  : {len(ROM_EG_rnodes)}")
    print(f"[EG][W2M] > REDGES  : {len(ROM_EG_NUM_REDGES)}")
    print(f"[EG][W2M] > RWEIGHTS: {len(ROM_EG_NUM_RWEIGHTS)}")
    print(f"")

    f = open(f"rom/expander_graph/ROM_EG_{self.id}_RNODES.mem", "w")
    for _ in ROM_EG_rnodes:
      hex_str = "{:08x}".format(_) + "\n"
      f.write(hex_str)

    f = open(f"rom/expander_graph/ROM_EG_{self.id}_RADDR.mem", "w")
    for _ in ROM_EG_NUM_REDGES:
      hex_str = "{:08x}".format(_) + "\n"
      f.write(hex_str)

    f = open(f"rom/expander_graph/ROM_EG_{self.id}_RWEIGHTS.mem", "w")
    for _ in ROM_EG_NUM_RWEIGHTS:
      hex_str = "{:08x}".format(_) + "\n"
      f.write(hex_str)

    # post_processing
    print(f"[EG][W2M] write graph (post_processing) to memory")
    # TODO implement post-processing
    print(f"")

    return
  
###################################################################################################
