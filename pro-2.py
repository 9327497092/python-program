term=int(input("enter any natural number : "))
sum=0
for i in range(1,term+1):
    sum=sum+i
    
print("First Way : {0} natural number sum is : {1}".format(term,sum))
sum=int(term*(term+1)/2)
print("Second Way : {0} natural number sum is: {1}".format(term,sum))