class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add_node(self, node):
        if node.val < self.val:
            if self.left == None:
                self.left = node
            else:
                self.left.add_node(node)
        elif node.val > self.val:
            if self.right == None:
                self.right = node
            else:
                self.right.add_node(node)

    def __str__(self):
        return str(self.val)

    def visit(self):
        if self.left is not None:
            self.left.visit()
        print(self.val)
        if self.right is not None:
            self.right.visit()

    def search(self, num):
        if self.val == num:
            return 'Found ' + str(num)
        elif self.val < num:
            if self.right is not None:
                return self.right.search(num)
            else:
                return str(num)+' is not in the tree'
        else:
            if self.left is not None:
                return self.left.search(num)
            else:
                return str(num)+' is not in the tree'
