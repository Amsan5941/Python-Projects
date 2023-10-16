#Amsan Naheswaran
#ICS4U0-B
#Mr. Veera
#BORING BUSINESS J4 2011 CCC
#February 23, 2021

x_coordinates = [-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10] #x values of the gird
y_coordinates = [-1,-2,-3,-4,-5,-6,-7,-8] #y values of the grid
final_coordinates=[] #Empty list that will hold the final coordinates
ans=[] #Empty list contains that will print all the answers

starting=[-1,-5] # Starting point of that tranlations

condition=True #Boolean variable to keep while loop running
cond=True #Boolean variable to stop loop from running if final_coordinates are in danger zone
count=0 #Counter

while (condition==True): #Loop that runs the code allows the user to input values until the boolean variable is false 

  coordinate=input('Enter:') #Asks user for directions input
  
  x=coordinate.split(' ') #Splits the input into elements that are seperated by a space
  
  count+=1 # increases counter value by 1
  
  if (cond==False): #If the cond variable is false, the loop stops
    break

  if (count==1): #This count variable is for the first input only

    if (x[0]=='l'): #Checks to see if the first element in input equals "l"
    
      final_coordinates=[starting[0]-int(x[1]),starting[1]] #Subtracts the x value of the starting position by the value given from the input
    
    if (x[0]=='d'):#Checks to see if the first element in input equals "d"
    
      final_coordinates=[starting[0],starting[1]-int(x[1])] #Subtracts the y value of the starting position by the value given from the input

    if (x[0]=='r'):#Checks to see if the first element in input equals "r"
      final_coordinates=[starting[0]+int(x[1]),starting[1]] #Adds the x value of the starting position by the value given from the input

    if (x[0]=='u'):#Checks to see if the first element in input equals "u

      final_coordinates=[starting[0],starting[1]+int(x[1])]#Adds the y value of the starting position by the value given from the input

    ans.append(final_coordinates+['safe']) #This appends the final coordinates into a new list for the first input

  else: #If the count variable does not equal 1, meaning it is not the first input

    if (x[0]=='l'): #Checks to see if the first element in input equals "l"

      final_coordinates=[final_coordinates[0]-int(x[1]),final_coordinates[1]] #Subtracts the x value of the final position by the value given from the input
      if (final_coordinates[0] in x_coordinates and final_coordinates[1] in y_coordinates): #Checks to see if both x and y coordinates are in the safe zone

        ans.append(final_coordinates+['safe']) #If true, it appends the final coordinates plus the string

      else: #If final coordinates not in safe zone

        ans.append(final_coordinates+['danger']) #Appends the final coordinates plus the string

        cond=False # Boolean variable turns false since the driling has reached danger making the code end

    if (x[0]=='d'): #Checks to see if the first element in input equals "d"

      final_coordinates=[final_coordinates[0],final_coordinates[1]-int(x[1])] #Subtracts the y value of the final position by the value given from the input

      if (final_coordinates[0] in x_coordinates and final_coordinates[1] in y_coordinates): #Checks to see if both x and y coordinates are in the safe zone

        ans.append(final_coordinates+['safe']) #If true, it appends the final coordinates plus the string

      else:
        ans.append(final_coordinates+['danger'])  
        cond=False # Boolean variable turns false since the driling has reached danger making the code end

    if (x[0]=='r'): #Checks to see if the first element in input equals "r"

      final_coordinates=[final_coordinates[0]+int(x[1]),final_coordinates[1]] #Adds the x value of the final position by the value given from the input

      if (final_coordinates[0] in x_coordinates and final_coordinates[1] in y_coordinates): #Checks to see if both x and y coordinates are in the safe zone
        ans.append(final_coordinates+['safe']) #If true, it appends the final coordinates plus the string

      else: #If final coordinates not in safe zone

        ans.append(final_coordinates+['danger'])

        cond=False # Boolean variable turns false since the driling has reached danger making the code end

    if (x[0]=='u'): #Checks to see if the first element in input equals "u"

      final_coordinates=[final_coordinates[0],final_coordinates[1]+int(x[1])] #Adds the y value of the final position by the value given from the input

      if (final_coordinates[0] in x_coordinates and final_coordinates[1] in y_coordinates): #Checks to see if both x and y coordinates are in the safe zone
        ans.append(final_coordinates+['safe']) #If true, it appends the final coordinates plus the string

      else:
        ans.append(final_coordinates+['danger'])  

        cond=False # Boolean variable turns false since the driling has reached danger making the code end

    if (x[0]=='q'): #When user enters the letter q the program will end (break) since that is the command to stop the program 
      condition=False # Boolean variable turns false so that the program will stop running

for row in ans: #This loop goes through each final position coordinates in the list

  values = ','.join(str(element) for element in row) #Using list comprehension, each final position value changes into a string. Then using the join function, each final position list will print on a new line. The ',' indcates when it is a new element in the list
  
  print(values) #This print statement prints each final position list on a seperate line