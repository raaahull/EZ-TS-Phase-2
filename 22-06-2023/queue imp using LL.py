class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
            return to_return
a_queue=Queue()
while True:
    print("enqueue <value>")
    print("dequeue")
    print("quit")
    do=input("what's ur choice::").split()
    print("do",do)
    print("do[0]",do[0])
    operation=do[0].strip().lower()
    if operation=="enqueue":
        a_queue.enqueue(int(do[1]))
    elif operation=="dequeue":
        dequeued=a_queue.dequeue()
        if dequeued is None:
            print("Queue is empty!!!")
        else:
            print("to_return value::",int(to_return))
    elif operation == "quit":
        break
