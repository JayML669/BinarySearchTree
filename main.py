from tree import Tree
from node import Node
import random

tree_size = 250
tree = Tree()

for i in range(tree_size):
    tree.add_value(random.randint(0, 10000))
print('Tree of size '+str(tree_size)+' has been created...\n')

#tree.print_tree(tree.root, 'root:')
# tree.traverse()
# print(tree.search(8))

while True:
    action = input(
        'Type sort or search to sort the tree or search for a number or exit to close the program\n')

    if action == 'sort':
        tree.traverse()
    elif action == 'search':
        while True:
            try:
                num = int(input('What number would you like to search the tree for...\n'))
            except ValueError:
                print('Hmm... something doesnt seem quite right please only search for positive integers')
                continue
            else:
                print(tree.search(num))
                break
    elif action == 'exit':
        break
    else:
        print('Hmm... something doesnt seem quite right make sure you typed one of the options')
