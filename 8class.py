class Node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None

    def create(self,root,x):
        if(root==None):
            return Node(x)
        elif(root.data>x):
            root.left=self.create(root.left,x)
        else:
            root.right=self.create(root.right,x)
        return root
    def preorder(self,root):
        if(root):
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # def postorder(self,root):
    #     if(root):
    #         print(root.data,end=" ")
    #         self.postorder(root.left)
    #         self.postorder(root.right)

    def sum(self,root):
        if(root==None):
            return 0
        return root.data+self.sum(root.left)+self.sum(root.right)                  #preorder-traversal

    def evensum(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
            return root.data+self.evensum(root.left)+self.evensum(root.right)
        return self.evensum(root.left)+self.evensum(root.right)

    def oe(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
            return root.data+self.evensum(root.left)+self.evensum(root.right)
        return root.data-self.evensum(root.left)+self.evensum(root.right)


t=tree()
t.root=Node(2)
t.create(t.root,3)
t.create(t.root,5)
t.create(t.root,2)
# t.preorder(t.root)
# t.postorder(t.root)
print(t.sum(t.root))
print(t.evensum(t.root))
print(t.oe(t.root))

#print(t.sum(t.root.left))         #for adding left



'''class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
# Compare the new value with the parent node
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
               print("left")
            else:
               self.left.insert(data)
               print("Ro-Left")
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
                  print("Right")
               else:
                  self.right.insert(data)
                  print("R0-Right")
      else:
         self.data = data

# Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data)
      if self.right:
         self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res

# Preorder traversal
# Root -> Left ->Right
   def PreorderTraversal(self, root):
      res = []
      if root:
         res.append(root.data)
         res = res + self.PreorderTraversal(root.left)
         res = res + self.PreorderTraversal(root.right)
      return res

# Postorder traversal
# Left ->Right -> Root
   def PostorderTraversal(self, root):
      res = []
      if root:
         res = self.PostorderTraversal(root.left)
         res = res + self.PostorderTraversal(root.right)
         res.append(root.data)
      return res

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
print("inorder L-Ro-R ")
print(root.inorderTraversal(root))
print("preorder Ro-L-R")
print(root.PreorderTraversal(root))
print("postorder-L-R-Ro")
print(root.PostorderTraversal(root))'''