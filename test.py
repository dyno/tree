#!/usr/bin/env python

from print_tree import print_tree
from node import Node

#======================================================================
def test_root():
    #DONNOT modify this node
    n0 = Node(None, None, 0)
    n2 = Node(None, None, 2)
    n5 = Node(None, None, 5)
    n7 = Node(None, None, 7)
    n3 = Node(n2, None, 3)
    n8 = Node(n7, None, 8)
    n1 = Node(n0, n3, 1)
    n6 = Node(n5, n8, 6)
    root = n4 = Node(n1, n6, 4)

    return root

#======================================================================
if __name__ == "__main__":
    root = test_root()
    print_tree(root)

