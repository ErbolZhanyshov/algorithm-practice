# LEETCODE PRACTICE - TESTED CODES

'''
1. same tree
'''

class Tree:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def isSameTree(p,q):

    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)


# test 1
p = Tree(1)
p.left = Tree(2)
p.right = Tree(3)

q = Tree(1)
q.left = Tree(2)
q.right = Tree(3)

print("1)", isSameTree(p,q))   # True



'''
2. symmetric tree
'''

class Symmetric:

    def isSymmetric(self,root):

        def check(l,r):

            if l==None and r==None:
                return True

            if l==None or r==None:
                return False

            if l.val != r.val:
                return False

            return check(l.left,r.right) and check(l.right,r.left)

        if root==None:
            return True

        return check(root.left,root.right)


root = Tree(1)
root.left = Tree(2)
root.right = Tree(2)
root.left.left = Tree(3)
root.right.right = Tree(3)

print("2)", Symmetric().isSymmetric(root))  # True



'''
3. pow(x,n)
'''

class Solution:

    def myPow(self,x,n):

        def f(x,n):

            if n==0:
                return 1

            if n%2==0:
                return f(x*x,n//2)

            return x*f(x*x,(n-1)//2)

        res = f(x,abs(n))

        if n<0:
            return 1/res

        return res


sol = Solution()

print("3)", sol.myPow(2,10))   # 1024
print("3)", sol.myPow(2,-2))   # 0.25



'''
4. max depth
'''

def maxDepth(root):

    if root==None:
        return 0

    l = maxDepth(root.left)
    r = maxDepth(root.right)

    return l+1 if l>r else r+1


t = Tree(1)
t.left = Tree(2)
t.left.left = Tree(4)
t.right = Tree(3)

print("4)", maxDepth(t))   # 3



'''
5. invert tree
'''

def invert(root):

    if root==None:
        return None

    root.left, root.right = root.right, root.left

    invert(root.left)
    invert(root.right)

    return root


t2 = Tree(4)
t2.left = Tree(2)
t2.right = Tree(7)

invert(t2)

print("5)", t2.left.val, t2.right.val)   # 7 2



'''
6. palindrome
'''

def isPal(s):

    s2 = ""

    for i in s:
        if i.isalnum():
            s2 += i.lower()

    l=0
    r=len(s2)-1

    while l<r:
        if s2[l]!=s2[r]:
            return False
        l+=1
        r-=1

    return True


print("6)", isPal("A man a plan a canal Panama"))  # True
print("6)", isPal("hello"))  # False



'''
7. fibonacci
'''

def fib(n):

    if n==0:
        return 0
    if n==1:
        return 1

    return fib(n-1)+fib(n-2)


print("7)", fib(6))  # 8



'''
8. valid parentheses
'''

def valid(s):

    st=[]

    for i in s:

        if i in "([{":
            st.append(i)

        else:

            if len(st)==0:
                return False

            top = st.pop()

            if (top=="(" and i!=")") or (top=="[" and i!="]") or (top=="{" and i!="}"):
                return False

    return len(st)==0


print("8)", valid("()[]{}"))   # True
print("8)", valid("(]"))       # False



'''
9. merge sorted arrays
'''

def merge(a,b):

    res=[]
    i=0
    j=0

    while i<len(a) and j<len(b):

        if a[i]<b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1

    while i<len(a):
        res.append(a[i])
        i+=1

    while j<len(b):
        res.append(b[j])
        j+=1

    return res


print("9)", merge([1,2,4],[1,3,4]))  # [1,1,2,3,4,4]



'''
10. binary search
'''

def bs(nums,target):

    l=0
    r=len(nums)-1

    while l<=r:

        mid = (l+r)//2

        if nums[mid]==target:
            return mid

        if nums[mid]<target:
            l=mid+1
        else:
            r=mid-1

    return -1


print("10)", bs([1,2,3,4,5,6],4))  # 3
print("10)", bs([1,2,3],10))       # -1