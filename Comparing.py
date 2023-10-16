x=[0,1,1,2]
pairs=[]
counter=0
for i in range (0,4):
  if x[counter]==x[len(x)-i-1]:
    print(x[counter],x[len(x)-i-1])
  