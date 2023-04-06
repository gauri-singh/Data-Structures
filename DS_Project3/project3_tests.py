import requirements

from typing import TypeVar, NamedTuple
from copy import deepcopy

# Instructions
# Some test cases for the ZipTree class can be found in the main block below.
#
# Note that passing the test cases here does not necessarily mean that your zip tree
# is correctly implemented / will pass other cases. It is a good idea to try and create different
# test cases for both.

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

class InsertType(NamedTuple):
	key: KeyType
	val: ValType
	rank: int

def create_tree_with_data(data: [InsertType]) -> requirements.ZipTree:
	tree = requirements.ZipTree()
	for item in data:
		tree.insert(item.key, item.val, item.rank)

	return tree

def zip_tree_tests():
	print('testing ZipTree')

	data = [InsertType(4, 'a', 0), InsertType(5, 'b', 0), InsertType(2, 'c', 2), InsertType(1, 'd', 1)]
	tree = create_tree_with_data(data)

	print(f'find(4): {tree.find(4)}, Expected: a')
	print(f'get_size(): {tree.get_size()}, Expected: 4')
	print(f'get_height(): {tree.get_height()}, Expected: 2')
	print(f'get_depth(2): {tree.get_depth(2)}, Expected: 0')
	print(f'get_depth(1): {tree.get_depth(1)}, Expected: 1')
	tree.insert(0, 'e', 1)
	print(f'get_size(): {tree.get_size()}, Expected: 5')
	print(f'get_height(): {tree.get_height()}, Expected: 2')
	print(f'get_depth(2): {tree.get_depth(2)}, Expected: 0')
	print(f'get_depth(1): {tree.get_depth(1)}, Expected: 2\n')

	data2 = [InsertType(4, 'a', 2), InsertType(5, 'b', 3), InsertType(2, 'c', 1), InsertType(1, 'd', 0), InsertType(0, 'e', 1)]
	tree2 = create_tree_with_data(data2)

	print(f'find(4): {tree2.find(4)}, Expected: a')
	print(f'get_size(): {tree2.get_size()}, Expected: 5')
	print(f'get_height(): {tree2.get_height()}, Expected: 4')
	print(f'get_depth(2): {tree2.get_depth(2)}, Expected: 3')
	print(f'get_depth(1): {tree2.get_depth(1)}, Expected: 4')

	print('\ntesting random rank generation')
	rank_sum = 0
	num_ranks = 10000
	for _ in range(num_ranks):
		rank_sum += requirements.ZipTree.get_random_rank()

	rank_mean = rank_sum / num_ranks

	print(f'random rank mean: {rank_mean}, Expected: ~1')

	# add new tests...

if __name__ == '__main__':
	zip_tree_tests()
