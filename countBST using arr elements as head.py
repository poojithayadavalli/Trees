"""
Rohan is learning about Binary search Trees.He went through a task as follows:

Given an array arr[] of N integers. The task is to count the number of Binary Search Tree can be made using each node of element in arr[] as a root node.

Input:

Firstline contains size of array N
Next line contains elements of array

Output:

print the number of bsts possible with head as element

Example1:

Input:
3
20 10 30

Output:

1 2 2 

Example 2:

Input:
5
1 2 3 4 5

Output:
14 5 4 5 14 

Hint:For every element in arr[]:
Count the number of element(say c1) less than the current node.
Count the number of element(say c2) greater than the current node.
Then total number of Binary Search Tree(BST) can be formed using current element as a root node
is equals to the product of total number of BST formed using c1 elements and otal number of BST formed using c2 elements.
"""
def fact(n) : 
    res = 1  
    for i in range(1, n + 1):  
        res *= i  
    return res

def catalan(n): 
    return fact(2 * n)//(fact(n)*fact(n + 1)) 

n = int(input())
arr = list(map(int,input().split()))
for k in range(n):
    s = 0
    for i in range(n):
        if arr[i] < arr[k]:
            s+= 1
    catalan_leftBST = catalan(s)
    catalan_rightBST = catalan(n-s-1)
    totalBST = catalan_rightBST * catalan_leftBST
    print(totalBST, end =" ")

