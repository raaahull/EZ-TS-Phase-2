class Node:
    def _init_(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
        return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)
def search(root,key):
    if root is None or root.val==key:
        return root
    if root.val<key:
        return search(root.right,key)
    return search(root.left,key)


n=int(input("enter the size"))
for i in range(0,n):
    if i==0:
        r=Node(int(input("enter  element")))
        
    else:
        r=insert(r,int(input("enter element")))
print("Inorder of Created BST:",end=" ")
inorder(r)
se=int(input("enter the element to search"))
re=search(r,se)
print("")
if re:
    print("Found")
else:
    print("Not Found")