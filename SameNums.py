num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))

if num1==num2 and num2==num3 and num1==num3:
  print("All the same")
elif num1!=num2 and num2!=3 and num1!=num3:
  print("All different")
else:
  print("Neither")

#OR ANOTHER WAY FOR QUESTION 4

numbers=(2,2,2) #input the 3 numbers here

if numbers[0]==numbers[1] and numbers[0]==numbers[2] and numbers[1]==numbers[2]:
  print("All the same")
elif numbers[0]!=numbers[1] and numbers[0]!=numbers[2] and numbers[1]!=numbers[2]:
  print("All different")
else:
  print("Neither")