"""

Khan is learning about the Trees and he found that with the same set of nodes mutliple binary trees can be constructed.He wants to know

how many binary trees can be formed from a set of N distinct nodes.

Input:

Input contains the number of distinct nodes N

Output:

print the possible number of binary trees

Example 1:

Input:

5

Output:

5040

Example 2:

Input:
1

Output:
1

Hint:Total number of possible Binary Search Trees with n different keys (countBST(n)) = Catalan number Cn = (2n)! / ((n + 1)! * n!)
"""
def factorial(n) : 
    res = 1  
    for i in range(1, n + 1):  
        res *= i  
    return res  
  
def binomialCoeff(n, k):  
  
    res = 1 
    if (k > n - k):  
        k = n - k 
    for i in range(k):  
      
        res *= (n - i)  
        res //= (i + 1) 
      
    return res  

def catalan(n):
    c = binomialCoeff(2 * n, n) 
    return c // (n + 1)  
  
def countBST(n):
    count = catalan(n) 
    return count

def countBT(n):
    count = catalan(n)  
    return count * factorial(n)
x=int(input())
print(countBT(x))
