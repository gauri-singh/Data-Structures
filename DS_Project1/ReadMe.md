# Cuckoo Hash Implementation
This project contains an implementation of the Cuckoo Hash algorithm, which is a hash table data structure with constant-time complexity for insert, lookup, and delete operations. The cuckoo_hash.py file contains the implementation of the CuckooHash class, which provides the functionality of the hash table.

## Usage
To use this implementation of Cuckoo Hash, you can create an instance of the CuckooHash class by importing it from the cuckoo_hash module:


```
from cuckoo_hash import CuckooHash
ch = CuckooHash(init_sizes=10)
```
The init_sizes parameter is used to specify the initial size of the hash table. The CuckooHash class provides the following public member functions:

init(): initializes the cuckoo hash tables as a list with dimensions 2 by init_sizes, and fills both tables with None entries. 

CYCLE_THRESHOLD denotes the threshold for the number of evictions for detecting cycles in the insert() method. Do not change the value of this variable.

get_table_contents(): will be used during testing to check the correctness of the table contents.

hash_func(): takes as input the key and the table id (0 or 1), and returns the hash value for that key in the specified table.

The following methods need to be completed:

insert(key): insert an item with the specified key to the cuckoo hash. If a cycle is found during the insertion, stop and return False. Otherwise, return True after inserting the item. If a cycle is found, do not rehash afterwards; only return False. To determine if there is a cycle, use the provided CYCLE_THRESHOLD value, i.e., if the number of evictions is greater than CYCLE_THRESHOLD, you may assume there is a cycle.

lookup(key): return True if an item with the specified key exists in the cuckoo hash, and False otherwise.

delete(key): delete the item with the specified key from the cuckoo hash and replace it with a None entry.

rehash(new_table_size): update self.tables such that both tables are of size new_table_size, and all existing elements in the old tables are rehashed to their new locations.

## Testing
We have provided a project1_tests.py file that contains some simple test cases to give an idea of how we will be running your code. Please use that file when testing your implementation.