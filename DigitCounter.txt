number=int(input("Enter the integer: "))
number=abs(number)
print(number)

if number<10:
  print("The integer is 1 digit")
elif number<100:
  print("The integer is 2 digit")
elif number<1000:
  print("The integer is 3 digit")
elif number<10000:
  print("The integer is 4 digit")
elif number<100000:
  print("The integer is 5 digit")
else:
  print("lots")