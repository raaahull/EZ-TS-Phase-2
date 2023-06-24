l=[]
while(True):
    print("Select the option")
    print("1.Insert 2.Delete 3.Search 4.Sort 5.Display 6.Exit 7.Create")
    o=int(input("Enter the option"))
    if(o==1):
        k=int(input("Enter the number"))
        l.append(k)
    elif(o==2):
        k=int(input("Enter the number"))
        if k not in l:
            print("Number is not in the list")
        l.remove(k)
    elif(o==3):
        k=int(input("Enter the number"))
        if k in l:
             print("Number is Found")
        else:
            print("Number is not found")
    elif(o==4):
        print("Sorted Array is: ",sorted(l))
    elif(o==5):
        print("The List is : ",l)
    elif(o==6):
        exit(0)
    elif(o==7):
        n=int(input("Enter the size"))
        if(n <0):
            print("Please enter positive number --------------------")
        elif(len(l)!=0):
            print("Array Already Exist")
        else:
            for i in range(n):
                k=int(input("Enter the number"))
                l.append(k)
    else:
        print("Enter Valid Option")