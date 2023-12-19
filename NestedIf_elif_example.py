####  Conditional Statements  ######

print("Welcome to the  RollerCoaster!. ")
height = int(input("\n\nWhat is your height in cm? "))
if height >= 180:
  print("\n\nCongrats! You can ride the Rollercoaster!")
  #create a new parameter AGE to segregate the pricing depending ones age
  age = int(input("\nNow What's is your age? : "))
  if age < 12:
    print("\nPlease pay $100. ")
  elif 12<=age<=18:
    print("\nPlease pay $150.")
  else:
    print("\nPlease pay $200.")

else:
  print("\n\nYou cannot ride.\n")
