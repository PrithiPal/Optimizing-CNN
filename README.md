# Optimization

An optimized implementation of CNN(Convolutional Neural Networks)[1] that decreases execution time.


Procedure : 

[SINGLE MACHINE]

1. Benchmark invidual functions. 
2. Create a framework for parallelization. Some strategies include threads for mutually exclusive areas, processes for heavy tasks, communication between threads/processes.
3. Note the changes in the time.


[MULTIPLE MACHINES - CLUSTER]

1. Implement the optimized CNN in a distributed system. The plan would be to identify independent areas, deploy at nodes and initiate communication between them.
2. Design a structure similar to P2P, master-slave or load-balancing. 


References : 

[1].  [CNN code] : https://github.com/siddharth950/Sparse-Autoencoder-Linear

