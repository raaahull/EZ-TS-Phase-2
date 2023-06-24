'''LOGIC
1.using 'insert' creates BST
2.Input node to be deleted
3.Spot or find the node which u want to delete (search)
4.once u find the node
check it comes under which category of delete
5.apply thre delete concept
6.find inorder sucessor using separate function to replace with node to be deleted'''
class Node:
    def _init_(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key,end=" ",)
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
# Given a non_empty binary
#search tree,return the node
#with minimum key value
#found in that tree .Note that the
#entire tree does not need to be searched
def minValueNode(node):
    current=node
    while(current.left is not None):
        current=current.left
    return current


def deleteNode(root,key):
    if root is None:
        return root
    elif key < root.key:
        root.left=deleteNode(root.left,key)
    elif key > root.key:
        root.right=deleteNode(root.right,key)

    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minValueNode(root.right)
        root.key=temp.key
        root.right=deleteNode(root.right,temp.key)
    return root
root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)
print("IN order")
inorder(root)
print("\n delete 20")
root=deleteNode(root,20)
print("\nInorder modified")
inorder(root)