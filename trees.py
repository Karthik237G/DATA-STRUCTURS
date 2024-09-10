# A Python class that represents
# an individual node in a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# Initialize and allocate memory for tree nodes
firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)

# Connect binary tree nodes
firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#binary search tree
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursively(node.left, key)
        else:  # Assuming no duplicate values
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursively(node.right, key)

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_recursively(node.left, key)
        return self._search_recursively(node.right, key)

    def inorder_traversal(self):
        return self._inorder_recursively(self.root)

    def _inorder_recursively(self, node):
        return self._inorder_recursively(node.left) + [node.val] + self._inorder_recursively(node.right) if node else []

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("In-order traversal of the BST:", bst.inorder_traversal())

    # Searching for a value
    search_value = 40
    result = bst.search(search_value)
    if result:
        print(f"Value {search_value} found in the BST.")
    else:
        print(f"Value {search_value} not found in the BST.")
