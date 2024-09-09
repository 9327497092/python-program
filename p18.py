import matrix_operation
t=True
while(t):
    print("1.Display Matrix:")
    print("2.Addition Matrix:")
    print("3.Multipication")
    print("3.Exit")
    c=int(input("Enter your choice:"))
    if(c==1):
        matrix_operation.Initialize_matrix()
    elif(c==2):
        matrix_operation.Addition_matrix()
    elif(c==3):
        matrix_operation.Multipicaton_matrix()
    elif(c==4):t=False