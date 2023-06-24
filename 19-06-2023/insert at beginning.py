#SLL insert at begin , at last, in between
#begin: create a new node , new node.next=currentnode ,head = newnode
def insert_beginning (self,data):
    nb=Node(data)
    nb.next=self.head
    self.head=nb
def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->", end=" ")
                temp=temp.next

# Create nodes
obj=insert_beginning()
n=Node(10)
obj.head=n

n1=Node(20)
obj.head.next=n1

n2=Node(30)
n1.next=n2

n3=Node(40)
n2.next=n3

obj.display()