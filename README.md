# Unifing the Linear Encoding of Different Polynomial Commitments on Hardware Platforms

This is a repository for the paper "..." (https://ia.cr/2025/...). 


# Structure of this Repository

...

# Parameters

...


# Execution

Running the design on the hardware requires multiple step during execution. In the first step a python script needs to be executed to generate the expandergraph that is used for linear encoding. In the second step, the bitstream needs to be programmed with the generated bitstream. In the third step, the generated data needs to be send from the Host to the FPGA and the stard bit needs to be set. In the fourth and last step, the data needs to be loaded back from the FPGA to the Host and verified.

## Run python scripts

We prepared a toolchain that can be used to verify the functionality of the generated hardware. To generate your own test cases for a certain architecture and option you need to execute:

``
/bin/python3 sw/py/main.py <lg_k> <lg_d> <lg_N> <deg1_r=10> <deg1_l> <deg2_r> <deg2_l>
``

## Run Vivado project

We already prepared a Vivado project to simplify usage. You first have to source all Vivado-related scripts. After sourcing all related scripts you need to start with the appropriate project file. This can be done by using:  

```
source /opt/Xilinx/Vivado/2022.2/settings64.sh
vivado -source fpga/project_1/project_1.xpr
```

The command above starts Vivado which can take up to a few seconds. Now you can either start a simulation, synthesis, or implementation run. If you want to use the test cases generated by the python script to verify the behavior you just need to click `Run Simulation` on the left toolbar of Vivado. This will open a simulation form that runs the simulation behavior. We already prepared a waveform to simplify the process. Note, that only small parameter sets should be simulated due to the required time and memory.

## Run Vitis projects

To run the generated bitstream on the alveo u280 fpga ...

```
source /opt/Xilinx/Vitis/2022.2/settings64.sh
vitis -workspace fpga/project_1/project_1.vitis
```

Send data from Host to FPGA memory

```
./dma_h2c <file> <size>
```

Load data back from FPGA to Host memory

```
./dma_c2h <file> <size>
```

# Contributors

Florian Hirner - `florian.hirner@tugraz.at`

Florian Krieger - `florian.krieger@tugraz.at`

Sujoy Sinha Roy - `sujoy.sinharoy@tugraz.at`

The Authors are affiliated with the [Institute of Information Security](https://www.isec.tugraz.at/), [Graz University of Technology](https://www.tugraz.at/), Austria

-----

# License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Copyright (c) 2025 @ CryptoEngineering Group, ISEC, TU Graz 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.