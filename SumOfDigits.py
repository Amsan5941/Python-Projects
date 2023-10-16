
input="2222222222"
sum=0
for i in range (0,len(input)):
  if int(input[i])%2!=0:
    sum+=int(input[i])
    print(input[i])
print(sum)