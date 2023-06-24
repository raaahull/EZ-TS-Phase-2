r=int(input("Enter no of the rows:"))
c=int(input("Enter no of the columns:"))
matrix=[]
for i in range(r):
    a=[]
    for i in range(c):
        x=int(input("Enter the item:"))
        a.append(x)
    matrix.append(a)
print("The Matrix is:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
print("The diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i==j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Non diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i!=j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Upper diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i<j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Lower diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i>j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Transpose Matrix is:")
for i in range(r):
    for j in range(c):
        print(matrix[j][i],end=" ")
    print()
# print("The Addition ")