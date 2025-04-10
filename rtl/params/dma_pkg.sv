//////////////////////////////////////////////////////////////////////////////////
// Company: 
//  - Institute of Information Security (ISEC)
//  - Graz Universtiy of Technology (TUG)
// Engineer: 
//  - Florian Hirner
//  - Florian Krieger
//////////////////////////////////////////////////////////////////////////////////

`timescale 1 ns / 1 ps

package dma_pkg;

  // ----------------------------------------------------------------------
  // Memory based datatypes.

  localparam int N_DDR_PC                 = 2;
  localparam int N_HBM_PC                 = 32;
  localparam int XFER_WIDTH_IN_BITS       = 512;
  localparam int XFER_WIDTH_IN_BYTES      = 512/8; // 512=64, 256=32

  typedef logic [XFER_WIDTH_IN_BITS-1:0]  xfer_word_t;
  typedef logic [32:0]                    xfer_addr_t;
  typedef logic [3:0]                     xfer_len_t;

  localparam addr_t HBM_PC_SIZE_IN_BYTES  = 1 << 28; // 256 MB
  localparam addr_t HBM_PC_SIZE_IN_BYTES  = 1 << 29; // 512 MB
  localparam addr_t HBM_PC_SIZE_IN_BYTES  = 1 << 30; //   1 GB


  // ----------------------------------------------------------------------
  // State based datatypes.

  typedef enum {
    DMA_IDLE,
    DMA_INIT,
    DMA_EXEC,
    DMA_DONE
  } dma_state_e;

  // ----------------------------------------------------------------------
  // Others

  // TODO add more if needed

endpackage
