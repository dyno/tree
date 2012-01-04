#!/usr/bin/env python

from util import Stack
from node import Node
from traversal import VISIT_LEFT, VISIT_RIGHT, VISIT_SELF

#======================================================================
#http://www.geocities.com/acmearticles/treerec.htm
def reconstruct_tree(preorder, inorder):
    """reconstruct_tree

    @param: preorder traversal list
    @param: inorder traversal list
    @return: root node

    algorithm:
      recursive
    """
    if not preorder:
        return

    value = preorder[0]
    idx = inorder.index(value)
    left = reconstruct_tree(preorder[1:idx+1], inorder[:idx])
    right = reconstruct_tree(preorder[idx+1:], inorder[idx+1:])
    return Node(left, right, value)

#----------------------------------------------------------
def reconstruct_tree_2(preorder, inorder):
    """reconstruct_tree_2

    @param: preorder traversal list
    @param: inorder traversal list
    @return: root node

    algorithm:
      nonrecursive
    """
    cur_pre_idx, pre_pre_idx = 0, -1
    #stack = Stack([], debug = True)
    stack = Stack([])
    while cur_pre_idx < len(preorder) or stack:
        if cur_pre_idx != pre_pre_idx:
            value = preorder[cur_pre_idx]
            #node
            node = Node(None, None, value)
            #split scheme
            idx = inorder.index(value)
            if stack:
                parent_range = stack[-1][1]
                parent_operation = stack[-1][2]
            else:
                parent_range = (0, len(inorder), -1)
                parent_operation = VISIT_LEFT
            if parent_operation == VISIT_LEFT:
                _range = (parent_range[0], idx, parent_range[1])
            else:
                _range = (parent_range[1], idx, parent_range[2])
            #current operation
            operation = VISIT_LEFT

            #push
            stack.append([ node, _range, operation])
            pre_pre_idx = cur_pre_idx

        #check next value and continue build the stack
        if cur_pre_idx < len(preorder) -1:
            next_value = preorder[cur_pre_idx + 1]
            next_in_idx = inorder.index(next_value)
        else:
            next_value = None
            next_in_idx =  -1

        node, _range, operation = stack[-1]
        if operation == VISIT_LEFT and _range[0] <= next_in_idx < _range[1]:
                cur_pre_idx += 1
                continue
        elif operation == VISIT_RIGHT and _range[1] <= next_in_idx < _range[2]:
                cur_pre_idx += 1
                continue

        r = stack.pop()
        if not stack:
            return r[0]

        if stack[-1][2] == VISIT_LEFT:
            stack[-1][0].left = r[0]
            stack[-1][2] = VISIT_RIGHT
        elif stack[-1][2] == VISIT_RIGHT:
            stack[-1][0].right = r[0]
            stack[-1][2] = VISIT_SELF

#======================================================================
if __name__ == "__main__":
    from print_tree import print_tree

#          4           
#         / \          
#        /   \         
#       /     \        
#      /       \       
#     1         6      
#    / \       / \     
#   /   \     /   \    
#  0     3   5     8   
#       /         /    
#      2         7     
    inorder = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    preorder = [4, 1, 0, 3, 2, 6, 5, 8, 7]


    d = locals().copy()
    l = [ d[attr] for attr in d
                if callable(d[attr]) and "reconstruct" in attr]
    l.sort()

    for f in l:
        root = f(preorder, inorder)
        print_tree(root)

