import time
print("Welcome to *Game Title*!")

x = input("Where would you like to go?")
print ("Okay, transporting you to", x)

time.sleep(2)

if x == "The Castle":{

  print('''
                           -|             |-
         -|                  [-_-_-_-_-_-_-_-]                  |-
         [-_-_-_-_-]          |             |          [-_-_-_-_-]
          | o   o |           [  0   0   0  ]           | o   o |
           |     |    -|       |           |       |-    |     |
           |     |_-___-___-___-|         |-___-___-___-_|     |
           |  o  ]              [    0    ]              [  o  |
           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
_____----- |     ]              [ ||||||| ]              [     |
           |     ]              [ ||||||| ]              [     |
       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
      ( (__________------------_____________-------------_________) )

You are at the foot of a drawbridge of a large English castle.''')
}

elif x == "The Ocean":{
print('''
    //|\\
   //_|_\\
  ____|____
  \_o_o_o_/
 ~~~~ | ~~~~~
____________
You are on a ship in the middle of the pacific. What do you do?''')
}

else:{

    print("Please restart the game.")
}
time.sleep(1)
y = input("You may go North, South, East, or West.")
if y in ["North", "South", "East" "West"]:{
    
  print("You are now travelling", y)
}

time.sleep(1)

if x == ("The Ocean"):

  print('''You have encountered a humungous Great White Shark.

                (`.
                 \ `.
                  )  `._..---._
\`.       __...---`         o  )
 \ `._,--'           ,    ___,'
  ) ,-._          \  )   _,-'
 /,'    ``--.._____\/--''

''')
  time.sleep(1)
  print("You have two options. You can fight it, or try to sail away.")
  time.sleep(1)
  z = input("Fight or Sail?")

  if z == ("Fight"):
      print ("The shark won.")
  else:
      print ("You got away just in time.")


if x == ("The Castle"):

    print("You have two options. You can jump into the water, or try to jump acrosss the drawbridge.")
    time.sleep(1)
    z = input("Jump into water or jump across bridge?")

    if z == ("Jump into water"):
  
        print("The current pulls you away.")
        
    if z == ("Jump across bridge"):
 
        print("The drawbridge breaks, and you fall into the moat of alligators.")
