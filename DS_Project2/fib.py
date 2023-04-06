# explanations for member functions are provided in requirements.py
from __future__ import annotations
import math

class FibNode:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNode):
        return self.val == other.val

class FibHeap:
    def __init__(self):
        # you may define any additional member variables you need
        self.roots = []
        self.minimum_ptr = None
        self.nodes_in_tree = 0
        

    def get_roots(self) -> list:
        return self.roots

    def update_min(self, new_node):
        # if first node, set to min
        # else set to minimum of current min and this value

        if not self.minimum_ptr or new_node.val < self.minimum_ptr.val:
            self.minimum_ptr = new_node
             

    def insert(self, val: int) -> FibNode:
        # creates a new Node object

        new_node = FibNode(val)
        self.roots.append(new_node)
        # new min could be this one, so do a quick comparison
        self.update_min(new_node)
        self.nodes_in_tree += 1
        return new_node
    

    def rearrange(self):
        R = self.roots
        C = [None] * self.nodes_in_tree 

        while len(R):
            x = R.pop()
            if C[len(x.children)] is None:
                C[len(x.children)] = x
            else:
                y = C[len(x.children)]
                C[len(x.children)] = None
                if x.val < y.val:
                    x.children.append(y)
                    y.parent = x
                    R.append(x)
                else:
                    y.children.append(x)
                    x.parent = y
                    R.append(y)
                    
        self.roots = []
        for n in C:
            if n is not None:
                self.roots.append(n)

    def delete_min(self) -> None:

        for child in self.minimum_ptr.children:
            # set up the children as roots
            child.parent = None
            child.flag = False
            self.roots.append(child)

        # delete the min pointer from roots
        self.roots.remove(self.minimum_ptr)
        self.minimum_ptr = None
        self.nodes_in_tree -= 1
        self.rearrange()

        # once that is done, tranverse through roots to find new minimum ptr
        min = None
        min_val = math.inf
        for node in self.roots:
            if node.val < min_val:
                min = node
                min_val = node.val
        self.minimum_ptr = min


    def find_min(self) -> FibNode:
        return self.minimum_ptr

    def promote(self, node):
        
        if node not in self.roots:
            p = node.parent
            if node is None:
                print("Parent is null here ---> debugging")
                print(node.val)
                print(node.children)
                print(node.parent)
                print(self.roots)
            
            
            p.children.remove(node)

            node.flag = False
            node.parent = None
            self.roots.append(node)
            # since a new oot is created, make sure min_pts is updated if necesary 
            self.update_min(node)

            if p not in self.roots:
                if p.flag:
                    self.promote(p)
                else:
                    p.flag = True
            
    def decrease_priority(self, node: FibNode, new_val: int) -> None:
        node.val = new_val
        if node in self.roots:
            if node.val < self.minimum_ptr.val: 
                self.minimum_ptr = node
        else:
            self.promote(node)


