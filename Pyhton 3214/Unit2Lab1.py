'''
Task 1: Implement a Binary Tree Node
• Define a Node class with three attributes: val, left, and right.
• Initialize the node with a value, and set left and right children to None.
Task 2: Build a Binary Tree
Using the Node class from Task 1, create the following binary tree:
 3
 / \
 1 4
 \
 2
Task 3: Implement Preorder, Inorder, and Postorder Traversals
Write functions for preorder, inorder, and postorder traversals of the binary tree.
Each function should print the values of the nodes in the order defined by the type of traversal.
Task 4: Implement Insertion
Write a function to insert new nodes into the binary tree. For simplicity, insert nodes to ensure the tree
remains a binary search tree (BST). In a BST, for every node, all values in the left subtree are less than
the node’s value, and all values in the right subtree are greater.
Insert the following values into your binary tree: 5, 0. Test your tree by performing an inorder traversal
to print the values in ascending order
'''
#Task 1
class Node: #creating class node
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

#Task 2
    def insert(self, data):#function to insert data
        
        if data < self.data:# if value is lesser than the value of the parent node
            if self.leftChild: # if we still need to move towards the left subtree
                self.leftChild.insert(data)#adds the value to the left subtree
            else:
                self.leftChild = Node(data)
                return
       
        else:  # if value is greater than the value of the parent node        
            if self.rightChild:#if we still need to move towards the right subtree
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return

#Task 3
    def PrintTreeInorder(self):#function to print inorder
        if self.leftChild:
            self.leftChild.PrintTreeInorder()
        print(self.data),
        if self.rightChild:
            self.rightChild.PrintTreeInorder()


    def PrintTreePreorder(self):#function to print preorder
        print(self.data),
        if self.leftChild:
            self.leftChild.PrintTreePreorder()
        if self.rightChild:
            self.rightChild.PrintTreePreorder()

    def PrintTreePostorder(self):#function to print postorder
        if self.leftChild:
            self.leftChild.PrintTreePostorder()
        if self.rightChild:
            self.rightChild.PrintTreePostorder()
        print(self.data),

#Task 4
    def insert(self, data):#function to insert data
        
        if data < self.data:# if value is lesser than the value of the parent node
            if self.leftChild: # if we still need to move towards the left subtree
                self.leftChild.insert(data)#adds the value to the left subtree
            else:
                self.leftChild = Node(data)#adds the value to the left
                return
        else:  # if value is greater than the value of the parent node
            if self.rightChild:#if we still need to move towards the right subtree
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return

# Creating root node
root = Node(3)
# Inserting values in BST
root.insert(1)
root.insert(4)
root.insert(2)

print("Inorder Traversal:") #printing inorder traversal
root.PrintTreeInorder()

print("Preorder Traversal:") #printing preorder traversal
root.PrintTreePreorder()

print("Postorder Traversal:") #printing postorder traversal
root.PrintTreePostorder()

root.insert(5)
root.insert(0)

print("Inorder Traversal:") #printing inorder traversal
root.PrintTreeInorder()