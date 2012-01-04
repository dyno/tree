#!/usr/bin/python

#http://en.wikipedia.org/wiki/Tree_traversal

from util import Stack, Queue

VISIT_LEFT=0
VISIT_RIGHT=1
VISIT_SELF=2

#======================================================================
def inorder_traverse(root):
    """inorder traversal
    """
    stack = Stack([], debug=True)
    p = root
    while p or stack:
        while p:
            stack.append(p)
            p = p.left

        p = stack.pop()
        yield p
        p = p.right

#----------------------------------------------------------
def preorder_traverse(root):
    """preorder traversal
    """
    if not root: return
    stack = Stack([root])
    while stack:
        p = stack.pop()
        yield p
        if p.right:
            stack.append(p.right)
        if p.left:
            stack.append(p.left)

#----------------------------------------------------------
#http://software-troubleshooter.blogspot.com/2008/10/non-recursive-algorithm-for-postorder.html
#postorder reverse -> (root, right, left)
def postorder_traverse(root):
    """postorder_traverse

    algorithm:
        postorder (left, right, root) is the reverse of (root, right, left)
    """
    stack = Stack([root])
    while stack:
        p = stack.pop()
        yield p
        if p.left: stack.append(p.left)
        if p.right: stack.append(p.right)

#----------------------------------------------------------
#http://forums.devarticles.com/c-c-help-52/non-recursive-tree-traversal-74033.html
def postorder_traverse_2(root):
    """postorder_traverse_2

    algorithm:
      improve postorder_traverse by using 2 stacks and make the output in the rite order.
    """
    stack1, stack2 = Stack([]), Stack([])
    stack1.append(root)
    while stack1:
        p = stack1.pop()
        stack2.append(p)
        if p.left: stack1.append(p.left)
        if p.right: stack1.append(p.right)

    while stack2:
        p = stack2.pop()
        yield p

#----------------------------------------------------------
#http://www.stewart.cs.sdsu.edu/cs310/fall05/ch18-2-lect.html
def postorder_traverse_3(root):
    """postorder_traverse_3

    algorithm:
      push/pop node to stack according to current node's state
    """
    ns = [root, VISIT_LEFT] #(node, state)
    #stack = Stack([], debug=True)
    stack = Stack([])
    while ns or stack:
        while ns:
            stack.append(ns)
            node, state = ns
            #ns[1] == VISIT_LEFT
            ns[1] = VISIT_RIGHT
            if node.left:
                ns = [node.left, VISIT_LEFT]
            else:
                ns = None

        ns = stack[-1]
        if ns[1] == VISIT_RIGHT:
            ns[1] = VISIT_SELF
            if ns[0].right:
                ns = [ns[0].right, VISIT_LEFT]
            else:
                ns = None
        elif ns[1] == VISIT_SELF:
            yield ns[0]
            stack.pop()
            ns = None

#----------------------------------------------------------
#http://hi.baidu.com/simk/blog/item/ef40a61c18b1a48886d6b62c.html
def postorder_traverse_4(root):
    """postorder_traverse_4

    algorithm:
      improve postorder_traverse_3 based on the fact that if last visited
    node is current node's right child, then current node should be popped up
    """
    p = root
    stack = Stack([], debug=True)
    last_visited = None
    while p or stack:
        while p:
            stack.append(p)
            p = p.left

        p = stack[-1]
        if not p.right or p.right == last_visited:
            yield p
            stack.pop()
            last_visited = p
            p = None
        else:
            p = p.right

#----------------------------------------------------------
def breadth_first_traverse(root):
    """breadth-first traversal or "level order traversal"

    algorithm:
      queue.
    """
    if not root:
        return

    #q = Queue([root], debug=True)
    q = Queue([root])
    while q:
        p = q.pop(0)
        yield p
        if p.left: q.append(p.left)
        if p.right: q.append(p.right)

#======================================================================
if __name__ == "__main__":
    from test import test_root
    from print_tree import print_tree

    root = test_root()
    d = locals().copy()
    l = [ d[attr] for attr in d
                if callable(d[attr]) and "traverse" in attr]
    l.sort()
    for f in l:
        print "\n%s" % ("-" * 72)
        print f.__doc__
        print_tree(root)
        print
        for node in f(root):
            print "%d " % node.value,
        print

