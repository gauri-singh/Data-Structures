# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List

class CuckooHash:
	def __init__(self, init_size: int):
		self.__num_rehashes = 0
		self.CYCLE_THRESHOLD = 10

		self.table_size = init_size
		self.tables = [[None]*init_size for _ in range(2)]
		self.count_evictions = 0
		self.curr_table = 0

	def hash_func(self, key: int, table_id: int) -> int:
		key = int(str(key) + str(self.__num_rehashes) + str(table_id))
		rand.seed(key)
		return rand.randint(0, self.table_size-1)

	def get_table_contents(self) -> List[List[int]]:
		return self.tables

	# you should *NOT* change any of the existing code above this line
	# you may however define additional instance variables inside the __init__ method.

	def insert(self, key: int) -> bool:
		# TODO
		self.curr_table=0
		self.count_evictions =0
		while self.count_evictions <=self.CYCLE_THRESHOLD:
			pos = self.hash_func(key,self.curr_table)
			if self.tables[self.curr_table][pos] is None:
				self.tables[self.curr_table][pos] = key
				break
			else:
			#insert the current key in the table and make the evicted item as the key and change the current table as the other table
				key,self.tables[self.curr_table][pos] = self.tables[self.curr_table][pos],key
				#change the current table value
				if self.curr_table == 1 :
					self.curr_table = 0
				else:
					self.curr_table = 1
				self.count_evictions+=1
			if self.count_evictions > self.CYCLE_THRESHOLD:
				print (' Too many loops! Cycle Exists')
				return False
		return True
				
		pass

	def lookup(self, key: int) -> bool:
		# TODO
		# Check if the key is in either of the tables
		if self.tables[0][self.hash_func(key,0)] == key or self.tables[1][self.hash_func(key,1)] == key:
			return True
		return False
		pass

	def delete(self, key: int) -> None:
		# TODO
		#if the key is present in either of the table, return true
		if self.tables[0][self.hash_func(key,0)] == key:
			self.tables[0][self.hash_func(key,0)] = None
		elif self.tables[1][self.hash_func(key,1)] == key:
			self.tables[1][self.hash_func(key,1)] = None
		else:
			return False
		return True
		pass

	def rehash(self, new_table_size: int) -> None:
		self.__num_rehashes += 1; self.table_size = new_table_size # do not modify this line
		#copying the content of previous table before rehashing
		prev_tables = self.tables.copy()
		self.tables = [[None]*self.table_size for _ in range(2)]

		for table in prev_tables:
			for element in table:
				if element is not None:
					self.insert(element)
		pass

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define

