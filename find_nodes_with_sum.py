#!/usr/bin/python
#http://en.wikipedia.org/wiki/Binary_search_tree

from util import Stack

def find_nodes_with_sum(root, _sum):
    """find 2 nodes that their sum is _sum in a binary search tree.

    algorithm:
      basically 2 pointer for the left and right side of the list and move
    it closer based on the sum of the 2 nodes.
    """

    #stack1 = Stack([], name="ascend ", debug=True)
    stack1 = Stack([], name="ascend ")
    #stack2 = Stack([], name="descend", debug=True)
    stack2 = Stack([], name="descend")

    p1 = p2 = root
    while (p1 or stack1) and (p2 or stack2):
        while p1:
            stack1.append(p1)
            p1 = p1.left

        while p2:
            stack2.append(p2)
            p2 = p2.right

        p1 = stack1[-1]
        p2 = stack2[-1]

        if p1 == p2: #same node
            stack2.pop()
            p2 = p2.left
            p1 = None
            continue

        if p1.value + p2.value > _sum:
            stack2.pop()
            p2 = p2.left
            p1 = None
        elif p1.value + p2.value < _sum:
            stack1.pop()
            p1 = p1.right
            p2 = None
        else:
            return (p1.value, p2.value)

def find_nodes_with_sum_2(root, _sum):
    """find 2 nodes that their sum is _sum in a binary search tree.

    algorithm:
      basically 2 pointer for the left and right side of the list and move
    it closer based on the sum of the 2 nodes.
    """

    def inorder_traverse(root, order="L"):
        stack = []
        node = root
        while True:
            while node:
                stack.append(node)
                if order == "L":
                    node = node.left
                else:
                    node = node.right

            if not stack:
                return

            node = stack.pop()
            yield node

            if order == "L":
                node = node.right
            else:
                node = node.left

    lo_iter = inorder_traverse(root, order="L")
    hi_iter = inorder_traverse(root, order="R")
    lo = lo_iter.next()
    hi = hi_iter.next()
    while lo.value < hi.value:
        v = lo.value + hi.value

        if v == _sum:
            return lo.value, hi.value

        if v < _sum:
            lo = lo_iter.next()
        else:
            hi = hi_iter.next()

#======================================================================
if __name__ == "__main__":
    from test import test_root
    from print_tree import print_tree

    root = test_root()
    d = locals().copy()
    l = [ d[attr] for attr in d
                if callable(d[attr]) and "with_sum" in attr]
    l.sort()

    for f in l:
        print "\n------------------------------------------------------"
        print f.__doc__
        print_tree(root)
        for _sum in [-1, 1, 2, 3, 4, 4.5, 5, 6, 7, 8, 10, 11, 12, 13, 14, 20]:
            r = f(root, _sum)
            if r is not None:
                x, y = r
                print "%d+%d=%d" % (x, y, _sum)
            else:
                print "no 2 nodes sum to %s" % repr(_sum)


