# Zip Tree Implementation
This repository contains an implementation of the ZipTree data structure in Python.

## Usage
We have a node class called FibNode which we  use to create the nodes within the Fibonacci heap. 

`any variable` annotated with KeyType should use the same type for each tree, and should be comparable.
`ValType` is for any additional data to be stored in the nodes.

`get_random_rank(): `returns a random node rank, chosen independently from a geometric distribution of mean 1.

`insert():` inserts item with parameter key, value, and rank into tree. If rank is not provided, a random rank should be selected by using ZipTree.`get_random_rank()`.

`remove():` removes item with parameter key from tree. We have assumed that the item exists in the tree.

`find():` returns the value of item with parameter key. We have assumed that the item exists in the tree.

`get_size():` returns the number of nodes in the 
tree.

`get_height():` returns the height of the tree.

`get_depth():` returns the depth of the item with parameter key. We have assumed that the item exists in the tree.



## Testing
You can use the provided project3_tests.py file when testing your implementation.