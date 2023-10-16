def find_two (A,target):
  store=[]
  for x in range (0,len(A)):
    for i in range (x+1,len(A)):
      if A[x]+A[i]==target:
        store.append("TRUE")
      else:
        store.append("FALSE")
      if x==(len(A)-1) or len(A)==0:
        if "TRUE" in store:
          return "TRUE"
        else:
          return "FALSE"
    

print(find_two([],6))