no=int(input("Enter any positive integer"))
for i in range(2,int(no/2+1)):
    if(no%i==0):
        break
if(i==int(no/2)):
    print(no," number is Prime")
else:
    print(no," number is not Prime")