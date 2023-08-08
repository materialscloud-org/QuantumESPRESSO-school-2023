# Description

This example show how to use `kcp.x` to compute the electronic structure of the ozone molecule (O<sub>3</sub>). 
The entire calculation is split down into three steps:

* init: Contains the inputs for the initial DFT calculation
* calc_alpha: Contains the input for the calculation of the KI screening coefficient
* final: Contains a template of the inputs for the final KI calculation (you need to 
         open it and insert the value of alpha calculated in the previous step).
