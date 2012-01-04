#!/usr/bin/env python

from util import Queue
from node import Node

#======================================================================
def print_tree(root):
    """print tree
    """
    if not root:
        return
    if not (root.left or root.right):
        print root.value

    #tree height
    tree_height = 0
    q = Queue([(root, 0)]) #node, layer
    while q:
        p, layer = q.pop(0)
        if p.left or p.right:
            tree_height = layer + 1
        if p.left:
            q.append((p.left, layer + 1))
        if p.right:
            q.append((p.right, layer + 1))

    node_width = 1
    #node_width = 2
    #   *
    #  / \
    # *   *
    tree_width = (2 ** (tree_height - 1)) * (node_width * 3 + 2) + 2 #2 extra space
    root_node_begin =  (tree_width - node_width) / 2

    #initialize line buffer
    count = 0
    for layer in range(1, tree_height + 1):
        count += 2 ** (tree_height - layer) #the edge
        count += 1                          #the node
    lines = []
    for i in range(0, count + 1):
        lines.append([" "] * tree_width)

    #draw the tree to the buffer
    q = [(root, root_node_begin, 0, 0)] #(node, node_begin, layer, line_idx)
    while q:
        p, node_begin, layer, line_idx = q.pop(0)
        #print current node to buffer
        line = lines[line_idx]
        for i,c in enumerate("%s" % p.value):
            line[node_begin + i] = c
        if p.left:
            next_line_idx = line_idx + 2 ** (tree_height - layer - 1) + 1
            #edge to left child
            next_node_begin = node_begin
            for i in range(line_idx + 1, next_line_idx):
                lines[i][next_node_begin - 1] = "/"
                next_node_begin -= 1
            next_node_begin -= node_width
            q.append((p.left, next_node_begin, layer + 1, next_line_idx))

        if p.right:
            next_line_idx = line_idx + 2 ** (tree_height - layer - 1) + 1
            #edge to right child
            next_node_begin = node_begin + node_width
            for i in range(line_idx + 1, next_line_idx):
                lines[i][next_node_begin] = "\\"
                next_node_begin += 1
            q.append((p.right, next_node_begin, layer + 1, next_line_idx))

    #print out the tree
    for line in lines:
        print "".join(line)

#======================================================================
if __name__ == "__main__":
    from test import test_root
    root = test_root()
    print_tree(root)
