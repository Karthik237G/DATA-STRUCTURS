class Node:
  def __init__(self,key):
    self.left=None
    self.right=None
    self.key=key
  def traversepreorder(self):
    print(self.key,end='')
    if self.left:
      self.left.traversepreorder()
    if self.right:
      self.right.traversepreorder()
  def traverseinorder():
    if self.left:
      self.left.traversinorder()
    print(self.key,end='')
    if self.right:
      self.right.traverseinorder()
  def traversepostorder():
    if self.left:
      self.left.traversepostorder()
    if self.right:
      self.right.traversepostorder()
    print(self.key,end='')
class BinaryTree:
  def __init__ (self,root_key):
    self.root=Node(root_key)
  def insertleft(self,currentnode,key):
    if currentnode.
    
