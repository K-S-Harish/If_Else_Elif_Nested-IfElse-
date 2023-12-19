# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

#***** on every year that is divisible by 4 with no remainder
#***** except every year that is evenly divisible by 100 with no remainder
#***** unless the year is also divisible by 400 with no remainder
if year % 4 == 0:

  if year % 100 != 0:
    print("Leap year")

  elif year % 100 == 0:

    if year % 400 == 0:
      print("Leap year")

    else:
      print("Not leap year")
else:
    print("Not leap year")

      
    
    