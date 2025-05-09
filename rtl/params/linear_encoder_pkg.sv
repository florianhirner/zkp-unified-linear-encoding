//////////////////////////////////////////////////////////////////////////////////
// Company: 
//  - Institute of Information Security (ISEC)
//  - Graz Universtiy of Technology (TUG)
// Engineer: 
//  - Florian Hirner
//  - Florian Krieger
//////////////////////////////////////////////////////////////////////////////////

`timescale 1 ns / 1 ps

package linear_encoder_pkg;

  // ----------------------------------------------------------------------
  // State based datatypes.

  typedef enum {
    DMA_IDLE,
    DMA_INIT,
    DMA_EXEC,
    DMA_DONE
  } linear_encoder_state_e;

  // ----------------------------------------------------------------------
  // Others

  // TODO add more if needed

endpackage
