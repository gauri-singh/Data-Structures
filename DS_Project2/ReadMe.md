# Fibbonaci Heap Implementation
The FibHeap class is an implementation of a Fibonacci heap in Python. This README provides information on how to use the class and its public member functions.

## Usage
We have a node class called FibNode which we  use to create the nodes within the Fibonacci heap. 

`init():` Initializes the Fibonacci heap as an empty heap with no nodes. We have predefined a few variables for you. Feel free to use them or define your own.

`get_roots(): `Returns a list of all the root nodes in the heap. This will be used to check the correctness of the heap structure.
Methods to be Completed
The following methods need to be completed:

`insert(value):` Inserts an item with the specified value to the Fibonacci heap. You want to return the node that you created. You can assume that the value is not already in the heap.

`delete_min():` Deletes the minimum node from the Fibonacci heap. We have assumed that the heap is non-empty when this is called.

`find_min():` Returns the node with the minimum value in the Fibonacci heap. We have assumed that the heap is non-empty when this is called.

`decrease_priority(node, new_val): `
Decreases the priority of the specified node to the new value. We have assumed that the new value is less than the current value and that it will not decrease to a pre-existing priority in the heap.


## Testing
You can use the provided project2_tests.py file when testing your implementation.