#*********Roller Coaster Ticket Price Calculator*********#

print("Welcome to the  RollerCoaster!. ")
height = int(input("\n\nWhat is your height in cm? "))
# Next we create a variable BILL to hold the value of the price of ticket. It'll be initiated at 0.
bill = 0

if height >= 160:
  print("\n\nCongrats! You can ride the Rollercoaster!")
  #create a new parameter AGE to segregate the pricing depending ones age
  age = int(input("\nNow What's is your age? : "))
  
  if age < 12:
    bill = 100#We'll assign the value 100 to BILL, for this condition
    print("\nChildrens Ticket are $100. ")
  elif age<=18:
    bill = 150#We'll assign the value 150 to BILL, if this condition applies
    print("\nTeenager Tickets are $150.")
  else:
    bill = 200#We'll assign the value 200 to BILL, if this condition applies
    print("\nAdult Tickets are $200.")
    
  #Creating a new variable to take and hold the passengers input
  want_pic = input("\nWould you like to get a picture taken? Y or N.  ")

  if want_pic == "Y":#This will run after the above conditions have been checked.
    bill+=5 #We'll add 5 to the bill if the passenger wants a picture. This is same as bill = bill + 5

  print(f"\nThe Total Bill Amount is ${bill}")

# Else" statement is not required here, but it's always a good practice to addit 

# NOTE: the print statement below will run after the if statement above has either been executed or not. If executed it'll show the new bill value, else will show the previously help value from the earlier if statement.
  
  
else:
  print("\n\nYou cannot ride.\n")