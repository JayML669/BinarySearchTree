from tree import Tree
from node import Node
import random

tree = Tree()

for i in range(10):
    tree.add_value(random.randint(0, 10))

#tree.print_tree(tree.root, 'root:')
tree.traverse()
intree = tree.search(8)
