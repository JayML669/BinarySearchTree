from node import Node


class Tree:

    def __init__(self):
        self.root = None

    def add_value(self, val):
        n = Node(val)
        if self.root == None:
            self.root = n
        else:
            self.root.add_node(n)

    def print_tree(self, node, args, layer=1):

        if node == None:
            print(layer, args, str(node), '\n')
        else:
            print(layer, args, str(node.val), '\n')
            layer += 1
            self.print_tree(node.right, 'right:', layer)
            self.print_tree(node.left, 'left:', layer)

    def traverse(self):
        self.root.visit()

    def search(self, num):
        return self.root.search(num)
