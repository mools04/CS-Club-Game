import time
print("Welcome to *Game Title*!")

x = input("Where would you like to go?")
print ("Okay, transporting you to", x)

time.sleep(2)

if x == "The Castle":{

    print("You are at the foot of a drawbridge of a large English castle.")
}

if x == "The Ocean":{
    
    print("You are on a ship in the middle of the pacific. What do you do?")
}

else:{
    
    print("Please restart game")   
}

y = input("You may go North, South, East, or West")
if y == ("North" or "South" or "East" or "West"):{
    
    print("You are now travelling", y)
}
