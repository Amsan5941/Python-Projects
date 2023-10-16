numbers=(2,2,2) #input the 3 numbers here

if numbers[0]==numbers[1] and numbers[0]==numbers[2] and numbers[1]==numbers[2]:
  print("All the same")
elif numbers[0]!=numbers[1] and numbers[0]!=numbers[2] and numbers[1]!=numbers[2]:
  print("All different")
else:
  print("Neither")