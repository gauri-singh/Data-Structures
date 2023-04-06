# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file.

from typing import TypeVar
import math
import random

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

class Node:
	def __init__(self, key, val, rank: int = -1):
		self.key = key
		self.val = val
		self.rank = rank
		self.parent = None
		self.left = None
		self.right = None
	
	def __repr__(self):
		return str(self.key)
	
	def __str__(self):
		return str(self.key)

class ZipTree:
	def __init__(self):
		self.root = Node(None, None)
		self.num_nodes = 0
		self.height = 1
		self.lpath, self.rpath = [], []

	def __eq__(self, other):
		return self.key == other.key

	@staticmethod
	def get_random_rank() -> int:
		return int(math.log(1-random.random())/math.log(0.5))

	def find_route(self, node, root, parent):
		if root is None:
			node.parent = parent
			self.num_nodes += 1
			if node.key > parent.key:
				parent.right = node
			else:
				parent.left = node
			return root, parent
		if root.rank < node.rank:
			return root, parent

		elif (root.rank == node.rank and root.key > node.key):
			return root,parent

		elif node.key > root.key:
			return self.find_route(node, root.right, root)
		
		else:
			return self.find_route(node, root.left, root)

	def insert(self, key: KeyType, val: ValType, rank: int = -1):
		if rank == -1:
			rank = self.get_random_rank()
		
		new_node =  Node(key, val, rank)
		if self.root.key is None:
			self.root = new_node
			self.num_nodes += 1
		else:
			old_node, old_parent = self.find_route(new_node, self.root, None)
			if old_node is not None:
				P, Q = self.unzip(new_node, old_node)
				old_node.parent = new_node
				if old_parent is None:
					self.root = new_node
				else:
					if old_node.key > old_parent.key:
						old_parent.right = new_node
					else:
						old_parent.left = new_node
					new_node.parent = old_parent
				new_node.left = P
				new_node.right = Q
				self.num_nodes += 1


	def remove(self, key: KeyType):
		if self.root is None:
			return
		node, parent, depth = self.getKey(key, self.root,0,None)
		self.num_nodes -= 1
		if node is not None:
			res = self.zip(node)
			if res is not None:
				if parent is None:
					self.root = res
				else:
					if res.key > parent.key:
						parent.right = res
					else:
						parent.left = res
			else:
				if node.key > parent.key:
					parent.right = None
				else:
					parent.left = None

	def zip(self, x):
		def zipup(P, Q):
			if P is None:
				return Q
			if Q is None:
				return P
			if Q.rank > P.rank:
				Q.left = zipup(P, Q.left)
				return Q
			else:
				P.right = zipup(P.right, Q)
				return P
		return zipup(x.left, x.right)

	def unzip(self, x, y):
		def unzip_lookup(k, node):
			if node is None: return (None, None)
			if node.key < k:
				(P, Q) = unzip_lookup(k, node.right)
				node.right = P
				return (node, Q)
			else:
				(P, Q) = unzip_lookup(k, node.left)
				node.left = Q
				return (P, node)
		return unzip_lookup(x.key, y)
	
	def getKey(self, key:KeyType, node, depth,parent):
		if node.key > key:
			return self.getKey(key,node.left,depth+1,node)

		elif node.key == key:
			return node,parent,depth

		else:
			return self.getKey(key,node.right,depth+1,node)
	
	def find(self, key: KeyType) -> ValType:
		node = self.root
		while node:
			if node.key < key:
				node = node.right
			elif node.key > key:
				node = node.left
			else:
				return node.val

	def get_size(self) -> int:
		return self.num_nodes

	def calculate_height(self, node) -> int:
		if node is None:
			return 0
		return max(self.calculate_height(node.left), self.calculate_height(node.right))+1

	def get_height(self) -> int:
		return self.calculate_height(self.root)-1

	def get_depth(self, key: KeyType):
		return self.getKey(key, self.root,0,None)[2]

# feel free to define new classes/methods in addition to the above
# fill in the definitions of each required member function (above),
# and any additional member functions you define