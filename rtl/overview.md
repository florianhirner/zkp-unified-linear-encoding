# Overview

compute_core_wrapper                                ccw
    control_state_register                          csr
    compute_core                                    cc 
        computer_core_control                       cc_ctrl
        dma_hbm                                     ...
            dma_control
            dma_channel
                dma_channel_control
                dma_r_channel
                dma_w_channel
        dma_ddr                                     ...
            dma_control
            dma_channel
                dma_channel_control
                dma_r_channel
                dma_w_channel
        linear_encoder_array                        lea
            linear_encoder_array_control            lea_ctrl
            linear_encoder_channel                  lec
                linear_encoder_channel_control      lec_ctrl
                linear_encoder-unit                 leu
                    linear_encoder_unit_control     leu_ctrl
                    prng_weight                     pw
                    mod_mul_0                       mm0
                    mod_mul_1                       mm1
                    mod_mul_2                       mm2
                    mod_mul_3                       mm3
