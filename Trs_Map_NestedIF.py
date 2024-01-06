line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
r = position[0].lower() #we are fetching the 1st charecter of given i/p
c = int(position[1]) # geting the 2nd item from i/p and converting it to INT form

if r == "a":
  if c == 1:
    line1[0] = "X"
  elif c == 2:
    line2[0] = "X"
  elif c == 3:
    line3[0] = "X"
    
elif r == "b":
  if c == 1:
    line1[1] = "X"
  elif c == 2:
    line2[1] = "X"
  elif c == 3:
    line3[1] = "X"

elif r == "c":
  if c  == 1:
    line1[2] = "X"
  elif c == 2:
    line2[2] = "X"
  elif c == 3:
    line3[2] = "X"
    
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")