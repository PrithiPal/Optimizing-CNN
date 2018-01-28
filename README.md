# Optimization

This repository attempts to optimize the implementation of a CNN(Convolutional Neural Networks)[1] and make it faster than original code. 

Procedure : 


[SINGLE MACHINE]

1. Benchmark invidual function. 
2. Create a framework for parallelization. Some strategies include threads for mutual exclusive areas, process for heavy tasks, communication between threads/processes.
3. Note the changes in the time.


[MULTIPLE MACHINES - CLUSTER]

1. Implementation of code at different computer nodes. The plan would be to identify independent areas, deploy at nodes and communicate between nodes .
2. Design a structures similar to P2P, master-slave or load-balancing. 


References : 

[1].  [CNN code] : https://github.com/siddharth950/Sparse-Autoencoder-Linear

