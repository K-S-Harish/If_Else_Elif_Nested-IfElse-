#!/usr/bin/env python
# coding: utf-8

# ### Love Calculator (My Version):

# In[2]:


print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

#Coverting the names into lower string
name1 = name1.lower()
name2 = name2.lower()

#   T  R  U  E   L  O  V  E --- These are the words which we need to calculate the count of

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")
l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")

# Adding up the repective letters and converting them to string in  order to concatenate
true_count = str(t + r + u + e)
love_count = str(l + o + v + e)

#Adding them and converting it back to integer
score = int(true_count + love_count)

if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")

elif 40<=score<=50:
  print(f"Your score is {score}, you are alright together.")

else:
  print(f"Your score is {score}.")


# ### Angelas Version:

# In[4]:


print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# Your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

