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
  def 
