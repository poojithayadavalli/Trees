"""

Arjun is learning about binary trees and binary search trees.He got confused and constructed a binary tree instead of binary search Tree.So your task is given below

Given a Binary Tree(level order traversal) with N nodes, convert it to a Binary Search Tree. The conversion must be done in such a way that keeps the original structure of Binary Tree.

Input:

Firstline contains the total number of nodes N
next line contains the bfs of binary tree

Output:
print the inorder traversal of Binary Search Tree

Example 1:

Input:

5
10 2 7 8 4

Output:

2 4 7 8 10

Example 2:

Input:

5
10 30 15 20 5

Output:

5 10 15 20 30

"""
class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def storeInorder(root, inorder):
    if root is None: 
        return
    
    storeInorder(root.left, inorder)
    
    inorder.append(root.data)
    
    storeInorder(root.right, inorder)
def arrayToBST(arr, root): 
    if root is None: 
        return 
    arrayToBST(arr, root.left)
    root.data = arr[0] 
    arr.pop(0)
    arrayToBST(arr, root.right)

def countNodes(root): 
    if root is None: 
        return 0
  
    return countNodes(root.left) + countNodes(root.right) + 1

def binaryTreeToBST(root):
    if root is None: 
        return 
    n = countNodes(root) 
    arr = [] 
    storeInorder(root, arr)
    arr.sort()
    
    arrayToBST(arr, root)
def printInorder(root,l):
    if root is None: 
        return
    printInorder(root.left,l) 
    l.append(root.data)  
    printInorder(root.right,l)

def insertLevelOrder(arr, root, i):
    n=len(arr)
    if i < n: 
        root = Node(arr[i])
        root.left = insertLevelOrder(arr, root.left,2 * i + 1)
        root.right = insertLevelOrder(arr, root.right,2 * i + 2) 
    return root
array=list(map(int,input().split()))
root=None
root=insertLevelOrder(array,root,0)
binaryTreeToBST(root)
l=[]
printInorder(root,l)
print(*l)
