stack_1=[]
stack_2=[]
def push():
    for i in range(5):
        element=int(input("enter the element"))
        if (element%2==0):
            stack_1.append(element)
        else:
            stack_2.append(element)
def pop_element():
    pop_what=input("1 or 2")
    if pop_what=="1":
        if not stack_1:
            print("Stack is empty")
        else:
            e=stack_1.pop()
            print("Removed element:",e)
            print(stack_1)
    else:
        if not stack_2:
            print("Stack is empty")
        else:
            e=stack_2.pop()
            print("Removed element",e)
            print(stack_2)
def show():
    what=input("1 or 2")
    if what=="1":
        print(stack_1)
    else:
        print(stack_2)
while True:
    print("select operation 1.push 2.pop 3.show 4.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        show()
    elif choice==4:
        break
    print("select the correct option")