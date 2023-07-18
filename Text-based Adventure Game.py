import time 

def intro():
  print("You feel something brush against your side as you struggle to gain consciousness. You open your eyes fighting the urge to lie there still and with great difficulty, sit up. The moonlit surrounding looks like an old human settlement with numerous poorly-built structures surrounding you. You are about to try and make sense of your condition when you see the dark figure of what appears to be an animal in the disatnce. You are still in pain as the figure keeps on getting bigger and much clearer. You realise it's a wolf coming for the kill and you.....(Choose your next action)"
        "\n"
         )
  
  time.sleep(1)
  print ("""  A. Scramble to find a rock nearby and haul it towards the wolf
  B. Scream as loud as you can
  C. Run and try to find a shelter""")

  choice = input("Enter choice: ") #Here is your first choice.
  if choice == "A":
    option_rock()
  elif choice == "B":
    print ("\n\nThe animal is startled at first but then pounces on you to tear you into pieces.\n")
    print ("You died!  :(")
  elif choice == "C":
    option_shelter()
  else:
    print ("Invalid input! Use only \"A\", \"B\" or \"C\".")
    intro()

def option_rock(): 
  print ("\n\nThe rock hits the approaching wolf and it lets out a gasp. It, however, continues towards you, albeit slowly. What do you do next?"
         "\n"
         )
  time.sleep(1)
  print ("""A. Try to find another rock and haul it towards the wolf\nB. Scream as loud as you can\nC. Run and try to find a shelter""")
  choice = input("Enter choice: ")
  if choice == "A":
    print ("\n\nThe animal manages to dodge the rock and pounces on you to tear you into pieces.\n")
    print ("You died!  :(")
  elif choice == "B":
    print ("\n\nThe animal is startled at first but then pounces on you to tear you into pieces.\n")
    print ("You died!  :(")
  elif choice == "C":
    option_shelter()
  else:
    print ("Invalid input! Use only \"A\", \"B\" or \"C\".")
    option_rock()

def option_shelter():
  print ("\n\nWith great difficulty, you manage to enter the cabin. It's dark inside. You try not to make a move and hope that the wolf goes away. Then, you"
  "\n")

  time.sleep(1)
  print ("""A. Open the door to check if the wolf has left
  B. Continue to wait without making movement
  C. Try feeling your way around the cabin""")
  choice = input("Enter choice: ")
  if choice == "A":
    print ("\n\nYou come face to face with the wolf who pounces on you to tear you into pieces.\n")
    print ("You died!  :(")
  elif choice == "B":
    option_wait()
  elif choice == "C":
    option_feel()
  else:
    print ("Invalid input! Use only \"A\", \"B\" or \"C\".")
    option_shelter()

def option_wait():
    print("\n\nSome time passes and there seems to be no activity around you. What do you do next?")

    time.sleep(1)
    print ("""  A. Open the door to check if the wolf has left
    B. Try feeling your way around the cabin""")

    choice = input("Enter choice: ")
    if choice == "A":
        print ("\n\nYou exit the cabin and try to walk away when you hear a growling sound behind you. Before you turn around, you feel immense pain around your neck and everything goes black.\n")
        print ("You died!  :(")
    elif choice == "B":
        option_feel()
    else:
        print ("Invalid input! Use only \"A\" or \"B\".")
        option_wait()

def option_feel():
    print("\n\nYou try and explore the cabin with your limbs. Suddenly, your foot comes in contact with something sharp and it gets a cut. You gasp in pain. It turns out to be a sword on the floor. A loud growling sound follows. What do you do?")

    time.sleep(1)
    print ("""  A. Pick up the sword
    B. Try to remain completely still""")

    choice = input("Enter choice: ")
    if choice == "A":
        print ("\n\nThe wolf bursts through the door and pounces on you but you defend yourself with your new-found weapon. A struggle between man and beast follows but you finally manage to kill the animal.\n")
        print ("You survived!  :)")
    elif choice == "B":
        print ("\nThe wolf bursts through the door and pounces on you.\n")
        print ("You died!  :(")
    else:
        print ("Invalid input! Use only \"A\" or \"B\".")
        option_feel()

intro()