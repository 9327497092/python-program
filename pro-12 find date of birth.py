#find date of birth
d={'milan':'05-04-2004',
  'ashwin':'02-12-2004',
  'jignesh':'30-03-2000',
  'nitesh':'13-05-1999'}


dob=input("Enter any month:")
if(dob.isnumeric()): 
  if(len(dob)==1):
    dob='0'+dob
  x=0
  for key,i in d.items():
    if(i[3:5]==dob):
      print('Date of birth:  {}:{}'.format(key,i))
      x=x+1
  if(x==0):
    print("Data not fond")