from tree import Tree
from node import Node
import random

tree = Tree()

for i in range(20):
    tree.add_value(random.randint(0, 100))

#tree.print_tree(tree.root, 'root:')
tree.traverse()
