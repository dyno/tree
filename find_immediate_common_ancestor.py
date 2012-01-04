#!/usr/bin/env python

from util import Stack
from node import Node

#======================================================================
def find_immediate_common_ancestor(root, value1, value2):
    """find_immediate_common_ancestor

    algorithm:
      in post-order, the stack holds all the ancestor node.
    record the 2 ancestor lists and compare them.
    """
    p = root
    #stack = Stack([], debug=True)
    stack = Stack([])
    last_visited = None
    count_found = 0
    while p or stack:
        while p:
            stack.append(p)
            p = p.left

        p = stack[-1]
        if not p.right or p.right == last_visited:
            stack.pop()
            #^#
            if p.value in (value1, value2):
                count_found += 1
                if count_found == 1:
                    parent_stack1 = stack[:]
                elif count_found == 2:
                    common_idx = -1
                    min_len = len(stack) < len(parent_stack1) and len(stack) or len(parent_stack1)
                    idx = 0
                    while idx < min_len:
                        if stack[idx] == parent_stack1[idx]:
                            common_idx = idx
                            idx += 1
                        else:
                            break
                    return stack[common_idx].value
            #$#
            last_visited = p
            p = None
        else:
            p = p.right

#----------------------------------------------------------
def find_immediate_common_ancestor_2(root, value1, value2):
    """find_immediate_common_ancestor_2

    algorithm:
      in post-order, the stack holds all the parent node
    when find the first value, the parent list only shrink on the
    road to find the 2nd value.
    """
    p, last_visited, immediate_ancestor = root, None, None
    #stack = Stack([], debug=True)
    stack = Stack([])
    while p or stack:
        while p:
            stack.append(p)
            p = p.left

        p = stack[-1]
        if not p.right or p.right == last_visited:
            stack.pop()
            #^#
            if p.value in (value1, value2):
                if not immediate_ancestor:
                    immediate_ancestor = stack[-1]
                else:
                    return immediate_ancestor.value
            if p == immediate_ancestor:
                if stack:
                    immediate_ancestor = stack[-1]
            #$#
            last_visited = p
            p = None
        else:
            p = p.right

#----------------------------------------------------------
def find_immediate_common_ancestor_3(root, value1, value2):
    """find_immediate_common_ancestor_3

    algorithm:
      post-order recursive
    """
    if not root:
        return (False, False, None)
    if root.value == value1:
        return (True, False, None)
    elif root.value == value2:
        return (False, True, None)

    left_value = find_immediate_common_ancestor_3(root.left, value1, value2)
    if left_value[0] and left_value[1]:
        return left_value

    right_value = find_immediate_common_ancestor_3(root.right, value1, value2)
    if right_value[0] and right_value[1]:
        return right_value

    _find1 = left_value[0] or right_value[0]
    _find2 = left_value[1] or right_value[1]
    if _find1 and _find2:
        return (True, True, root.value)

    return (_find1, _find2, None)

def find_immediate_common_ancestor_4(root, value1, value2, l, idx=0):
    """find_immediate_common_ancestor_4

    algorithm:
      pre-order recursive
    """
    if not root: return

    l[idx] = root.value
    if root.value == value1:
        print l[:idx],
    elif root.value == value2:
        print l[:idx],

    if root.left:
        find_immediate_common_ancestor_4(root.left, value1, value2, l, idx + 1)
    if root.right:
        find_immediate_common_ancestor_4(root.right, value1, value2, l, idx + 1)

def find_immediate_common_ancestor_5(root, value1, value2):
    """find_immediate_common_ancestor_5

    algorithm:
      pre-order traversal with value for each level
    """
    if not root:
        return

    ancestor, immediate_ancestor_level = {}, -1
    stack = Stack([(root, 0)])
    while stack:
        p, level = stack.pop()
        #^#
        ancestor[level] = p

        if p.value in (value1, value2):
            if immediate_ancestor_level == -1:
                immediate_ancestor_level = level - 1
            else:
                return ancestor[immediate_ancestor_level].value

        if immediate_ancestor_level > level - 1:
            immediate_ancestor_level = level - 1
        #$#
        if p.right:
            stack.append((p.right, level+1))
        if p.left:
            stack.append((p.left, level+1))

#======================================================================
if __name__ == "__main__":
    from test import test_root
    from print_tree import print_tree

    root = test_root()
    d = locals().copy()
    l = [ d[attr] for attr in d
                if callable(d[attr]) and "ancestor" in attr]
    l.sort()
    for f in l:
        print "\n%s" % ("-" * 72)
        print f.__doc__
        print_tree(root)
        for n1, n2 in [(2, 8), (5, 8), (0, 8), (0, 2), (1, 6), (-1, 6)]:
            print "\n(%d, %d)=>" % (n1, n2),
            if f == find_immediate_common_ancestor_4:
                _l = [-1] * 5
                ancestor = f(root, n1, n2, l)
            else:
                ancestor = f(root, n1, n2)
                print "%s" % repr(ancestor)

