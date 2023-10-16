#Amsan Naheswaran 
#CPS109
#Professor Harley
#Assignment 1
#October 19,2021
#Question for assignment 1: Create a financial calcutor that will help user know there monthly budget and help them save some of there monthly income. In order to calculate the users monthly budget you will need to know there monthly income, monthly expense, the percentage they want to save, and how long they want to continue in the saving/budgeting calcutor. The calculator will have two modes; mode 1 called "C" where all the information from the user is constant and doesnt change and mode "D" where the information changes every month. The amount the user saves everymonth can be calculated by finding the difference between their income and expense than multiplying by the percentage they want to save. If the users expenses are more than their income than the calcuator will tell the user that "the expenses are greater than the income". The user must input time must also be more or equal to 1. The output file must have the total amount the user has reamining, the total the user spent on expenses, and the total they have saved. Make sure the user can veiw the output while running the code so they can use the output file to keep track (if the expenses are greater than income than do not write that in the output file).

def Monthly_Calc (type,income,expenses,percent,time): #Function that will be used to calculate the users monthly budget
  for i in range (0,time): #A for loop that will be used to reiterate the amount of months (time) the user wants the calculator to run for 
    if type=="C": #If statment that will be used to determine if the user wants to run mode "C"
      percent=percent/100 #Divides the percent the user wants to save by 100
      left_over=income-expenses #Determines the users left over money that the user has by subtracting the income with the expenses
      if left_over<=0: #If statment that will be used to determine if the user has more expenses than income
        print ("The expenses are greater than the income") #Print statment that will be used to let the user know that there expenses are greater than their income so that they can change their monthly habbits
        break #Break fucntion that will be used to stop the loop since the users has no left over money
      else: #Else statment that continues when the the user has left over money
        left_over=left_over-(percent*left_over) #Subtracts the percentage that the user wants to save with thier left over money 
        print("The total amount of money you have left over is ${}for the first month".format(left_over)) #Prints the users left over money 
        left_over_total=left_over*time #Calculates the left over total depending on how long the user wants to continue the program
        total_expenses=expenses*time#Calculates the total expenses the user spent depending on how long the user wants to continue the program
        total_saved=(left_over*percent)*time #Calculates the total amount the user saved depending on how long the user wants to continue the program
        print("The left over money after {} months is ${}".format(time,left_over_total)) #Prints the left over money over the time the user wants so the user is informed how much money the user has left over
        print("The total expenses after {} months is ${}".format(time,total_expenses)) #Prints the total expesnes over the time the user wants so the user is informed how much money user has spent on expenses
        print("The total amount saved after {} month is ${}".format(time,total_saved)) #Prints the total amount of money the user has saved over the time the user wants so the user is informed how much money the user has saved
        break #Breaks the loop since the mode "C" has been calculated

    if type=="D": #If statment that will be used to determine if the user wants to run mode "D"
      if i==0:#When the loop is reiterating for the first month
        left_over=income-expenses #Calculates the left_over income in the first month 
        if left_over<0: #If statment that will be used to determine if the user has more expenses than income
          print ("The expenses are greater than the income") #Print statment that will be used to let the user know that there expenses are greater than their income so that they can change their monthly habbits
          break #Break fucntion that will be used to stop the loop since the users has no left over money
        percent=percent/100 #Divides the percent the user wants to save by 100
        left_over=left_over-(percent*left_over) #Calculates the total amount the user saved depending on how long the user wants to continue the program
        left_over_total=left_over #Makes the left_over_total equal to (same) as the left_over
        total_expenses=expenses #Makes total_expenses equal to (same) as expenses
        total_saved=((income-expenses)*percent) #Makes total_saved equal to the ((income-expenses)*percent)
   
      else: #When i dosent equal 0 
        income=int(input("Enter the income for month {}: ".format(i+1))) #User inputs a new income for the next month
        expenses=int(input("Enter the expense for month {}: ".format(i+1))) #User inputs a new expenses for the next month
        percent=int(input("Enter the percentage you will like to save for the month {}: ".format(i+1))) #User inputs a new percent that they want to save this month 
        left_over=income-expenses #Calculates the new left over income
        if left_over<0: #If statment that will be used to determine if the user has more expenses than income
          print ("The expenses are greater than the income") #Print statment that will be used to let the user know that there expenses are greater than their income so that they can change their monthly habbits
          break #Break fucntion that will be used to stop the loop since the users has no left over money
        else:
          percent=percent/100 #Divides the percent the user wants to save by 100
          left_over=left_over-(percent*left_over)#Calculates the left over money
          left_over_total+=left_over #Adds left_over_total with left_over
          total_expenses+=expenses #Adds the total expenses with expenses
          total_saved+=(percent*(income-expenses)) #Adds the total saved with (percent*(income-expenses))
  import sys
  sys.stdout=open("C:\\Users\\Amsan\\Documents\\output.txt","a")
  
  print("The total left over money after {} months is ${}".format(time,left_over_total)) #Prints the total left over money the user has
  print("The total of expenses after {} months is ${}".format(time,total_expenses)) #Prints the total expenses the amount of moeny user spends
  print("The total money saved after {} months is ${}".format(time,total_saved)) #Prints the total amount of money the user will save
  sys.stdout.close()



Monthly_Calc (input("Enter the type of calculating you will like to do: "),float(input("Enter your income for the month: ")),float(input("Enter your expenses for the month: ")),float(input("Enter the percentage you will like to save: ")),int(input("Enter time peroid for calculating: "))) #Recalls the function


