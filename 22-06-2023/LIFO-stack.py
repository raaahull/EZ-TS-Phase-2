stack=[]
def push():
    element =int(input("Enter the element:"))
    stack.append(element)
    print(stack)
    
def pop_element():
    if not stack:
        print("Stack is empty!!!")
    else:
        e=stack.pop()
        print("Removed element is:",e)
        print(stack)
def display():
    print(stack)
    
def top():
    if not stack:
        print("Stack is empty!!!")
    else:
        element=int(input("enter the elements:"))
        stack.append(element)
        print(stack)
        
while True:
    print("Select operation 1.Push 2.Pop 3.display 4.top 5.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        top()
    elif choice==5:
        break
    else:
        print("select correct option")

            
    