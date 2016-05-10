# NERD2
# Jaekyoung Kim (rlakim5521@naver.com)

class rbnode(object):
    """
    A node in a red black tree. See Cormen, Leiserson, Rivest, Stein 2nd edition pg 273.
    """
    
    def __init__(self, problem, ramen):
        "Construct."
        self._problem = problem
        self._ramen = ramen
        self._red = False
        self._left = None
        self._right = None
        self._p = None
    
    problem = property(fget=lambda self: self._problem, doc="The node's problem")
    ramen = property(fget=lambda self: self._ramen, doc="The node's ramen")
    red = property(fget=lambda self: self._red, doc="Is the node red?")
    left = property(fget=lambda self: self._left, doc="The node's left child")
    right = property(fget=lambda self: self._right, doc="The node's right child")
    p = property(fget=lambda self: self._p, doc="The node's parent")
    
    def __str__(self):
        "String representation."
        return str(self.problem) + " " + str(self.ramen)
    

    def __repr__(self):
        "String representation."
        return str(self.problem) + " " + str(self.ramen)


class rbtree(object):
    """
    A red black tree. See Cormen, Leiserson, Rivest, Stein 2nd edition pg 273.
    """
    
    
    def __init__(self, create_node=rbnode):
        "Construct."
        
        self._nil = create_node(problem=None, ramen=None)
        "Our nil node, used for all leaves."
        
        self._root = self.nil
        "The root of the tree."
        
        self._create_node = create_node
        "A callable that creates a node."
        
        self._size = 0


    root = property(fget=lambda self: self._root, doc="The tree's root node")
    nil = property(fget=lambda self: self._nil, doc="The tree's nil node")
    
    
    def size(self):
        return self._size
    
    def search(self, problem, x=None):
        """
        Search the subtree rooted at x (or the root if not given) iteratively for the key.
        
        @return: self.nil if it cannot find it.
        """
        if None == x:
            x = self.root
        while x != self.nil and problem != x.problem:
            if problem < x.problem:
                x = x.left
            else:
                x = x.right
        return x

    
    def minimum(self, x=None):
        """
        @return: The minimum value in the subtree rooted at x.
        """
        if None == x:
            x = self.root
        while x.left != self.nil:
            x = x.left
        return x

    
    def maximum(self, x=None):
        """
        @return: The maximum value in the subtree rooted at x.
        """
        if None == x:
            x = self.root
        while x.right != self.nil:
            x = x.right
        return x

    
    def insert_key(self, problem, ramen):
        "Insert the key into the tree."
        self.insert_node(self._create_node(problem=problem, ramen=ramen))
    
    
    def insert_node(self, z):
        "Insert node z into the tree."
        y = self._nil
        x = self._root
        while x != self._nil:
            y = x
            if z.problem > x.problem and z.ramen > x.ramen:
                # x is not a nerd. So, delete x and try inserting z again.
                self.delete_node(x)
                self.insert_node(z)
                return
            elif z.problem <= x.problem and z.ramen >= x.ramen:
                x = x.left
            elif z.problem >= x.problem and z.ramen <= x.ramen:
                x = x.right
            else:
                pass
        z._p = y
        if y == self.nil:
            self._root = z
        elif z.problem < y.problem:
            y._left = z
        else:
            y._right = z
        z._left = self.nil
        z._right = self.nil
        z._red = True
        self._insert_fixup(z)
        self._size = self._size + 1
        
    def delete_node(self, z):
        y = None
        x = None
        
        if z._left == self._nil or z._right == self._nil:
            y = z
        else:
            y = self.get_successor(z)
        
        if y._left == self._nil:
            x = y._right
        else:
            x = y._left
        
        if x != None and y != None:
            x._p = y._p
            if self._root == x._p:
                self._root._left = x
            else:
                if y == y._p._left:
                    y._p._left = x
                else:
                    y._p._right = x
        
        if y != z:
            if not y._red and x != None:
                self.delete_fixup(x)
            
            y._left = z._left
            y._right = z._right
            y._p = z._p
            y._red = z._red
            z._left._p = z._right._p = y
            if z == z._p._left:
                z._p._left = y
            else:
                z._p._right = y
        else:
            if not y.red and x != None:
                self.delete_fixup(x)
        
        if self._root == z:
            self._root = self._nil
            
        self._size = self._size - 1
    
    def delete_fixup(self, x):
        root = self._root._left
        w = None
        
        while not x._red and root != x:
            if x == x._p._left:
                w = x._p._right
                if w._red:
                    w._red = False
                    x._p._red = True
                    self._left_rotate(x.p)
                    w = x._p._right
                if not w._right._red and not w.left.red:
                    w._red = True
                    x = x._p
                else:
                    if not w._right._red:
                        w._left._red = False
                        w._red = True
                        self._right_rotate(w)
                        w = x._p._right
                    w._red = x._p._red
                    x._p._red = False
                    w._right._red = False
                    self._left_rotate(x._p)
                    x = root
            else:
                w = x._p._left
                if w._red:
                    w._red = False
                    x._p._red = True
                    self._right_rotate(x._p)
                    w = x._p._left
                if not w._right._red and not w._left._red:
                    w._red = True
                    x = x._p
                else:
                    if not w._left._red:
                        w._right._red = False
                        w._red = True
                        self._left_rotate(w)
                        w = x._p._left
                    w._red = x._p._red
                    x._p._red = False
                    w._left._red = False
                    self._right_rotate(x._p)
                    x = root
                    
        x._red = False
    
    def get_successor(self, x):
        y = None
        
        y = x._right
        if self._nil != y:
            while y._left != self._nil:
                y = y._left
            return y
        else:
            y = x._p
            while x == y._right:
                x = y
                y = y._p
            if y == self._root:
                return self._nil
            return y
    
    def _insert_fixup(self, z):
        "Restore red-black properties after insert."
        while z.p.red:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.red:
                    z.p._red = False
                    y._red = False
                    z.p.p._red = True
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self._left_rotate(z)
                    z.p._red = False
                    z.p.p._red = True
                    self._right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.red:
                    z.p._red = False
                    y._red = False
                    z.p.p._red = True
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self._right_rotate(z)
                    z.p._red = False
                    z.p.p._red = True
                    self._left_rotate(z.p.p)
        self.root._red = False
    
    def _left_rotate(self, x):
        "Left rotate x."
        y = x.right
        x._right = y.left
        if y.left != self.nil:
            y.left._p = x
        y._p = x.p
        if x.p == self.nil:
            self._root = y
        elif x == x.p.left:
            x.p._left = y
        else:
            x.p._right = y
        y._left = x
        x._p = y


    def _right_rotate(self, y):
        "Left rotate y."
        x = y.left
        y._left = x.right
        if x.right != self.nil:
            x.right._p = y
        x._p = y.p
        if y.p == self.nil:
            self._root = x
        elif y == y.p.right:
            y.p._right = x
        else:
            y.p._left = x
        x._right = y
        y._p = x


    def check_invariants(self):
        "@return: True iff satisfies all criteria to be red-black tree."
        
        def is_red_black_node(node):
            "@return: num_black"
            # check has _left and _right or neither
            if (node.left and not node.right) or (node.right and not node.left):
                return 0, False

            # check leaves are black
            if not node.left and not node.right and node.red:
                return 0, False

            # if node is red, check children are black
            if node.red and node.left and node.right:
                if node.left.red or node.right.red:
                    return 0, False
                    
            # descend tree and check black counts are balanced
            if node.left and node.right:
                
                # check children's parents are correct
                if self.nil != node.left and node != node.left.p:
                    return 0, False
                if self.nil != node.right and node != node.right.p:
                    return 0, False

                # check children are ok
                left_counts, left_ok = is_red_black_node(node.left)
                if not left_ok:
                    return 0, False
                right_counts, right_ok = is_red_black_node(node.right)
                if not right_ok:
                    return 0, False

                # check children's counts are ok
                if left_counts != right_counts:
                    return 0, False
                return left_counts, True
            else:
                return 0, True
                
        num_black, is_ok = is_red_black_node(self.root)
        return is_ok and not self.root._red
    
# Main function
if __name__ == "__main__":
    for _ in range(int(raw_input())):
        # Input
        N = int(raw_input())
        result = 0
        rbt = rbtree()
        
        # Solve
        for _ in xrange(N):
            p, q = map(int, raw_input().split())
            rbt.insert_key(p, q)
            result = result + rbt.size()
        
        # Output
        print result