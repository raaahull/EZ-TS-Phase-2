class Node():
    def _init_(self,key):
        self.val = key
        self.left =None
        self.right = None
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
def printInorder(root):
    if root:
        #First recur on left child
        printInorder(root.left)
        #then print the data of node
        print(root.val,end=' ')
        #now recur on right child
        printInorder(root.right)
def search(root,key):
    c=0
    if root is None or root.val ==key:
        c=c+1
        return c
    elif root.val < key:
        return search(root.right,key)
    elif root.val > key:
        return search(root.left,key)
    return root
print('enter the no.of elements to insert:')
n=int(input())
for i in range(n):
    if i==0:
        print("\nenter the element to insert")
        val=int(input())
        r=Node(val)
    else:
        print("\nenter the element to insert")
        val=int(input())
        r=insert(r,val)
        
      

printInorder(r)
print('\nenter the search element')
key=int(input())
    
      



search(r,key)
if c==0:
    print('\nsucess ',key)
else:
    print('\nfailue')
