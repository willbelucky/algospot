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
    
    def insert_key(self, problem, ramen):
        "Insert the key into the tree."
        self.insert_node(self._create_node(problem=problem, ramen=ramen))
    
    
    def insert_node(self, z):
        "Insert node z into the tree."
        y = self._nil
        x = self._root
        while x != self._nil:
            y = x
            if z._problem > x._problem and z._ramen > x._ramen:
                # x is not a nerd. So, delete x and try inserting z again.
                self.delete_node(x)
                self.insert_node(z)
                return
            elif z._problem <= x._problem and z._ramen >= x._ramen:
                x = x._left
            elif z._problem >= x._problem and z._ramen <= x._ramen:
                x = x._right
            else:
                return
        z._p = y
        if y == self._nil:
            self._root = z
        elif z._problem < y._problem:
            y._left = z
        else:
            y._right = z
        z._left = self._nil
        z._right = self._nil
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
            if not y._red and x != None:
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
                if not w._right._red and not w._left._red:
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
        while z._p._red:
            if z._p == z._p._p._left:
                y = z._p._p._right
                if y._red:
                    z._p._red = False
                    y._red = False
                    z._p._p._red = True
                    z = z._p._p
                else:
                    if z == z._p._right:
                        z = z._p
                        self._left_rotate(z)
                    z._p._red = False
                    z._p._p._red = True
                    self._right_rotate(z._p._p)
            else:
                y = z._p._p._left
                if y._red:
                    z._p._red = False
                    y._red = False
                    z._p._p._red = True
                    z = z._p._p
                else:
                    if z == z._p._left:
                        z = z._p
                        self._right_rotate(z)
                    z._p._red = False
                    z._p._p._red = True
                    self._left_rotate(z.p.p)
        self.root._red = False
    
    def _left_rotate(self, x):
        "Left rotate x."
        y = x._right
        x._right = y._left
        if y._left != self._nil:
            y._left._p = x
        y._p = x._p
        if x._p == self._nil:
            self._root = y
        elif x == x._p._left:
            x._p._left = y
        else:
            x._p._right = y
        y._left = x
        x._p = y


    def _right_rotate(self, y):
        "Left rotate y."
        x = y._left
        y._left = x._right
        if x._right != self._nil:
            x._right._p = y
        x._p = y._p
        if y._p == self._nil:
            self._root = x
        elif y == y._p._right:
            y._p._right = x
        else:
            y._p._left = x
        x._right = y
        y._p = x


    def check_invariants(self):
        "@return: True iff satisfies all criteria to be red-black tree."
        
        def is_red_black_node(node):
            "@return: num_black"
            # check has _left and _right or neither
            if (node._left and not node._right) or (node._right and not node._left):
                return 0, False

            # check leaves are black
            if not node._left and not node._right and node._red:
                return 0, False

            # if node is red, check children are black
            if node._red and node._left and node._right:
                if node._left._red or node._right._red:
                    return 0, False
                    
            # descend tree and check black counts are balanced
            if node._left and node._right:
                
                # check children's parents are correct
                if self._nil != node._left and node != node._left._p:
                    return 0, False
                if self._nil != node._right and node != node._right._p:
                    return 0, False

                # check children are ok
                left_counts, left_ok = is_red_black_node(node._left)
                if not left_ok:
                    return 0, False
                right_counts, right_ok = is_red_black_node(node._right)
                if not right_ok:
                    return 0, False

                # check children's counts are ok
                if left_counts != right_counts:
                    return 0, False
                return left_counts, True
            else:
                return 0, True
                
        num_black, is_ok = is_red_black_node(self._root)
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