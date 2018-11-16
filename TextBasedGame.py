GameEnded = False

def InputCheck(Input):
    AvaliableCommands = ["move", "check", "use" , "talk","quit"]
    Command = Input.split()
    print(Command)
    for i in Command:
        if (len(Command) == 1):
            word1 = (Command[0])
            if (word1 in AvaliableCommands):
                if word1 == "move":
                    word2 = (str(input("Enter a direction : "))).lower()
                    Move(word1,word2)
                    print("It did it once")
                    break
                elif word1 == "quit":
                    GameEnded = True
                    break
            else:
                print("Unknown Command")

        elif (len(Command) == 2):
            word1 = (Command[0])
            word2 = (Command[1])
            if (word1 in AvaliableCommands) or (word2 in AvaliableCommands):
                if (word1 == "move") or (word2 == "move"):
                    Move(word1,word2)
                    print("It did it once")
                    break
                elif (word1 == "quit") or (word2 == "quit"):
                    GameEnded = True
                    break
            else:
                print("Unknown Command")

        
def Move(word1,word2):
    print("Moving Works")

while (GameEnded == False):
    UserInput = str(input("Please enter a command : "))
    InputCheck(UserInput.lower())
