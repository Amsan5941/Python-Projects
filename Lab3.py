def Question_1(number):
  if number>0:
    return "The number is postive"
  elif number<0:
    return "The number is negative"
  else:
    return "The number is zero"

def Question_2(number):
  if number>0:
    if number<1:
      return "The number is postive and small"
    elif number>1000:
      return "The number is postive and large"
    else:
      return "The number is postive"
  elif number<0:
    number=number*-1
    if number<1:
      return "The number is negative and small"
    elif number>1000:
      return "The number is negative and large"
    else:
      return "The number is negative"
  else:
    return "The number is zero"

def Question_3(number):
  number=str(abs(number))
  if len(number)==1:
    return "The integer is 1 digit"
  elif len(number)==2:
    return "The integer is 2 digit"
  elif len(number)==3:
    return "The integer is 3 digit"
  elif len(number)==4:
    return "The integer is 4 digit"
  elif len(number)==5:
    return "The integer is 5 digit"
  else:
    return "Lots" 

def Question_4(num1,num2,num3):
  if num1==num2 and num2==num3 and num1==num3:
    return "All the same"
  elif num1!=num2 and num2!=num3 and num1!=num3:
    return "All different"
  else:
    return "Neither"

def Question_5(num1,num2,num3):
  if num1<num2 and num2<num3:
    return "Increasing"
  elif num1>num2 and num2>num3:
    return "Decreasing"
  else:
    return "Neither"

def Question_6(mode,num1,num2,num3):
  if mode=="strict":
      if num1<num2 and num2<num3:
        return "Increasing"
      elif num1>num2 and num2>num3:
        return "Decreasing"
      else:
        return "Neither"
  elif mode=="lenient":
    if num1<=num2 and num2<=num3:
      return "Increasing"
    elif num1>=num2 and num2>=num3:
      return "Decreasing"
    else:
      return "Neither"
  else:
    return "Enter the increasing/decreasing mode"

def Question_7(int1,int2,int3):
  if (int1<=int2 and int2<=int3) or (int1>=int2 and int2>=int3):
    return "In order"
  else:
    return "Not in order"

def Question_8(int1,int2,int3,int4):
  integers=[]
  integers.extend((int1,int2,int3,int4))
  for i in range (0,4):
    if integers.count(int1)==2 and integers.count(int2)==2 and integers.count(int3)==2 and integers.count(int4)==2:
      return "Two Pairs"
    elif integers.count(int1)==4:
      return "Two Pairs"
    else:
      return "Not Two Pairs"

def Question_9(temp_value,temp):
  if (temp_value=="C" and temp<=0) or (temp_value=="F" and temp<=32):
    return("Solid")
  elif (temp_value=="C" and temp>=100) or (temp_value=="F" and temp>=212):
    return("Gas")
  else:
    return("Liquid")

def Question_10(grade):
  if grade=="A":
    return "The numeric value of A is 4"
  elif grade=="A+":
    return "The numeric value of A+ is 4.3"
  elif grade=="A-":
    return "The numeric value of A- is 3.7"
  elif grade=="B":
    return "The numeric value of B is 3"
  elif grade=="B+":
    return "The numeric value of B+ is 3.3"
  elif grade=="B-":
    return "The numeric value of B- is 2.7"
  elif grade=="C":
    return "The numeric value of C is 2"
  elif grade=="C+":
    return "The numeric value of C+ is 2.3"
  elif grade=="C-":
    return "The numeric value of C- is 1.7"
  elif grade=="D":
    return "The numeric value of D is 1"
  elif grade=="D+":
    return "The numeric value of D+ is 1.3"
  elif grade=="D-":
    return "The numeric value of D- is 0.7"
  elif grade=="F":
    return "The numeric value of F is 0"
  else:
    return "Enter the correct letter grade"

def Question_11():
  sum=0
  for i in range (2,101,2):
    sum+=i
  return sum

def Question_12():
  sum=0
  for i in range (1,101):
    sum+=i**2
  return sum

def Question_13():
  power_list=[]
  for i in range (0,21):
    power=2**i
    power_list.append(power)
  return (power_list)
  

def Question_14(a,b):
  sum=0
  if a%2==0:
    for i in range (a+1,b+1,2):
      sum+=i
  else:
    for i in range (a,b+1,2):
      sum+=i
  return sum

def Question_15(input):
  input=str(input)
  sum=0
  for i in range (0,len(input)):
    if int(input[i])%2!=0:
      sum+=int(input[i])
  return sum

if __name__ == "__main__":
  print(Question_1(1000))
  print(Question_2(0.001))
  print(Question_3(-5000))
  print(Question_4(1,2,2))
  print(Question_5(5,4,3))
  print(Question_6("lenient",2,1,0))
  print(Question_7(3,5,3))
  print(Question_8(2,2,0,1))
  print(Question_9("C",50))
  print(Question_10("A+"))
  print(Question_11())
  print(Question_12())
  print(Question_13())
  print(Question_14(1,10))
  print(Question_15(32677))

