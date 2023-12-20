print("Welcome to the  RollerCoaster!. ")
height = int(input("\n\nWhat is your height in cm? "))
bill = 0 #Variable created to hold initial value

if height >= 120:
  print("\n\nCongrats! You can ride the Rollercoaster!")
  
  age = int(input("\nNow What's is your age? : "))

  if age < 12:
    bill = 5 #assigning the value to our variable for sp. conditions
    print("\nChildrens Ticket are $5. ")
  elif age<=18:
    bill = 7
    print("\nTeenager Tickets are $7.")
  elif age>=45 and age<=55: #using and operator
    print(f"\nRide free.") #no need to call the bill variable as the ride is free and the intial value given was also 0.
  else:
    bill = 12
    print("\nAdult Tickets are $12.")

  want_pic = input("\nWould you like to get a picture taken? Y or N.  ")

  if want_pic == "Y": #Calling a new if statement for pictures, this will run after the previous statements are finished executing.
    bill+=3 
  print(f"\nThe Total Bill Amount is ${bill}")

else:
  print("\n\nYou cannot ride.\n")