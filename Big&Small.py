number=float(input("Enter the number: "))
if number>0:
  if number<1:
    print("The number is postive and small")
  elif number>1000:
    print("The number is postive and large")
  else:
    print("The number is postive")
elif number<0:
  number=number*-1
  if number<1:
    print("The number is negative and small")
  elif number>1000:
    print("The number is negative and large")
  else:
    print("The number is negative")
else:
  print("The number is zero")