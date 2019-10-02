 
import time
print("Welcome to *Game Title*!")

x = input("Where would you like to go?")
print ("Okay, transporting you to", x)

time.sleep(2)

if x == "The Castle":{

  print("You are at the foot of a drawbridge of a large English castle.")
}

if x == "The Ocean":{
print('''
    //|\\
   //_|_\\
  ____|____
  \_o_o_o_/
 ~~~~ | ~~~~~
____________
You are on a ship in the middle of the pacific. What do you do?''')
}
time.sleep(1)
y = input("You may go North, South, East, or West.")
if y == ("North", "South", "East" or "West"):{
    
  print("You are now travelling", y)
}

time.sleep(1)

if x == ("The Ocean"):{

  print("You have encountered a shark.")
}

if x == ("The Castle"):{

  print("You have two options. You can jump into the water, or try to jump acrosss the drawbridge.")
  
}
  
z = input("Jump into water or jump across bridge?")

if z == ("Jump into water"):{
  
  print("You dead lmao")
}

if z == ("Jump across bridge"):{
 
  print("The drawbridge breaks, and you fall into the moat of alligators.")
}
