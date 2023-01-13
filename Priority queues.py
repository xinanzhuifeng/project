import time
import random
import graphviz

import self as self


class Node:
           def __init__(self, key=None, next=None):
            self.key = key
            self.next = next
class CompleteBinaryTree:
                          def __init__(self):
                           self.root = None
def get_parent(self, i):
                             if i == 0:
                                        return None
                             return (i - 1) // 2
def get_left_child(self, i):
    return 2 * i + 1
def get_right_child(self, i):
    return 2 * i + 2
def get_size(self):
    if self.root is None:
        return 0
    size = 1
    curr = self.root
    return size
def get_node(self, i):
    curr = self.root
    for j in range(i):
        curr = curr.next
    return curr
 def swap(self, i, j):
     node_i = self.get_node(i)
     node_j = self.get_node(j)
     node_i.key, node_j.key = node_j.key, node_i.key


def insert(self, key):
    # create a new node and insert it at the end of the list
    new_node = Node(key)
    if self.root is None:
        self.root = new_node
           return
    curr = self.root
    while curr.next is not None:
                curr = curr.next
            curr.next = new_node
i = self.get_size() - 1
parent = self.get_parent(i)
while parent is not None and self.get_node(parent).key > self.get_node(i).key:
    self.swap(parent, i)
    i = parent
    parent = self.get_parent(i)




def delMin(self):
    min_node = self.root
    if self.root.next is None:
        self.root = None
    return min_node.key

prev = None
curr = self.root
    while curr.next is not None:
        prev = curr
        curr = curr.next
prev.next = None

self.root.key = curr.key
i = 0
while True:
         left_child = self.get_left_child(i)
         right_child = self.get_right_child(i)
         if left_child >= self.get_size():
         break
         if right_child >= self.get_size() or self.get_node(left_child).key < self.get_node(right_child).key:
            min_child = left_child
         else:
            min_child = right_child
         if self.get_node(i).key > self.get_node(min_child).key:
             self.swap(i, min_child)
         i = min_child
else:
      break
return    min_node.key



def benchmark_heap(heap):
    input_sizes = [10, 100, 1000, 10000, 100000]
    insert_times = []
    del_min_times = []
    for n in input_sizes:
        keys = list(range(n))
        random.shuffle(keys)
    start = time.time()
    for key in keys:
        heap.insert(key)
    end = time.time()
    insert_times.append(end - start)
    start = time.time()
    for _ in range(n):
        heap.delMin()
    end = time.time()
    del_min_times.append(end - start)
    return insert_times, del_min_times





heap = CompleteBinaryTree()
visualize_heap(heap)
insert_times, del_min_times = benchmark_heap(heap)
visualize_performance(insert_times, del_min_times)
