class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def traversepreorder(self):
        print(self.key, end='')
        if self.left:
            self.left.traversepreorder()
        if self.right:
            self.right.traversepreorder()

    def traverseinorder(self):
        if self.left:
            self.left.traverseinorder()
        print(self.key, end='')
        if self.right:
            self.right.traverseinorder()

    def traversepostorder(self):
        if self.left:
            self.left.traversepostorder()
        if self.right:
            self.right.traversepostorder()
        print(self.key, end='')


class BinaryTree:
    def __init__(self, root_key):
        self.root = Node(root_key)

    def insertleft(self, currentnode, key):
        if currentnode.left is None:
            currentnode.left = Node(key)
        else:
            newnode = Node(key)
            newnode.left = currentnode.left
            currentnode.left = newnode

    def insertright(self, currentnode, key):
        if currentnode.right is None:
            currentnode.right = Node(key)
        else:
            newnode = Node(key)
            newnode.right = currentnode.right
            currentnode.right = newnode



tree = BinaryTree(1)
tree.insertleft(tree.root, 2)
tree.insertright(tree.root, 3)
tree.insertleft(tree.root, 2)
tree.insertright(tree.root, 3)
tree.insertleft(tree.root, 3)
tree.insertright(tree.root, 3)
tree.root.left.traversepreorder()
print()
tree.root.left.traverseinorder()
print()
tree.root.left.traversepostorder()
