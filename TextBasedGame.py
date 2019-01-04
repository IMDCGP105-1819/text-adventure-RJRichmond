from Classes import *
from StoryAndDescriptions import *

GameEnded = False
Rooms = []
#x 1 east -1 west y 1 north -1 south
Rooms.append(Room([Item("",Placeholder,Placeholder)],0,0,[[0,1]],StartingRoomDescription,"","OutsideHouse")) # Starting room / Outside House
Rooms.append(Room([Item("picture",PictureDescription,PictureUse),Item("",Placeholder,Placeholder)],0,1,[[-1,1],[0,0],[0,2]],PorchDescription,"","Porch")) # Porch
Rooms.append(Room([Item("knife",KnifeDescription,knifeUse)],-1,1,[[0,1]],KitchenDescription,"picture","Kitchen")) # Kitchen
Rooms.append(Room([Item("key",keyDescription,keyUse),Item("",Placeholder,Placeholder)],-1,2,[[-1,1]],StudyDescription,"","Study")) # Study
Rooms.append(Room([Item("",Placeholder,Placeholder)],0,2,[[0,1],[1,2]],LivingRoomDescription,"key","Living Room")) # Living Room
Rooms.append(Room([Item("",Placeholder,Placeholder)],1,2,[[0,2]],DiningRoomDescription,"lighter","Dining Room")) # Dining Room
Rooms.append(Room([Item("",Placeholder,Placeholder),Item("",Placeholder,Placeholder)],1,3,[[2,3]],CellerDescription,"","Celler")) # Celler
Rooms.append(Room([Item("",Placeholder,Placeholder)],2,3,[[1,3]],CaveDescription,"knife","Cave enterance")) # Cave Enterance

def InputCheck(Input):
    CurrentRoom = TheRoom(Character.positionx,Character.positiony)
    AvaliableCommands = ["move", "check", "use", "pickup","drop","help","quit"]
    Command = Input.split()
    for i in Command:
        if (len(Command) == 1):
            word1 = (Command[0])
            if (word1 in AvaliableCommands):
                if word1 == "move":
                    word2 = (str(input("Enter a direction : "))).lower()
                    Move(word1,word2)

                    break
                elif word1 == "check":
                    print (CurrentRoom)
                    print ("To check something specific please use : Check [what you would like to check]")
                    break
                elif word1 == "use":
                    word2 = (str(input("Enter what you would like to use : "))).lower()
                    if word2 in Character.ItemCheck():

                        ItemUsing(word2);
                        break
                    else:
                        print("You don't have this item!")
                        break
                elif word1 == "drop":
                    word2 = Input(str("What do you want to drop?"))
                    if word2 in Character.ItemCheck():

                        ItemDrop(word2);
                        break
                elif word1 == "quit":

                    GameEnding();
                    break
                elif word1 == "help":
                    print("You can enter these commands : ",AvaliableCommands)
                    break
            else:
                print("Unknown Command")

        elif (len(Command) == 2):
            word1 = (Command[0])
            word2 = (Command[1])
            if (word1 in AvaliableCommands) or (word2 in AvaliableCommands):
                if (word1 == "move") or (word2 == "move"):
                    Move(word1,word2)
                    break
                elif word1 == "check":
                    if word2 == "room":
                        print(CurrentRoom)
                        break
                    elif word2 == "inv":

                        print(Character)
                        break
                    elif word2 in Character.ItemCheck():

                        ItemCheck(word2);
                        break
                    else:
                        print("You cannot check this!")
                        break

                elif word1 == "pickup":
                    if word2 in CurrentRoom.ItemsInRoom():
                        for i in CurrentRoom.items:

                            if (word2 == str(i.name)):

                                Character.itemsHeld.append(i)
                                if (i.name == "picture"):
                                    CurrentRoom.description = PorchDescription2
                                if (i.name == "key"):
                                    CurrentRoom.description = StudyDescription2
                                print("You have picked up a " + i.name)
                                CurrentRoom.items.remove(i)
                                return

                    else:
                        print("You cannot pick this up!")
                        break
                elif word1 == "use":
                    if word2 in Character.ItemCheck():

                        ItemUsing(word2);
                        break
                    else:
                        print("You don't have this item!")
                        break

                elif word1 == "drop":
                    if word2 in Character.ItemCheck():

                        ItemDrop(word2);
                        break
                elif (word1 == "quit") or (word2 == "quit"):
                    GameEnding();

            else:
                print("Unknown Command")
                break
        else:
            print("Please only enter 1 - 2 words. Enter help to see avaliable commands")

def Move(word1,word2):
    Directions = ["north","n","east","e","south","s","west","w"]
    CurrentRoom = TheRoom(Character.positionx,Character.positiony)
    if (word1 in Directions) or (word2 in Directions):
        if (word1 == "north" or word1 == "n") or (word2 == "north" or word2 == "n"):
             Character.positiony += 1

        if (word1 == "east" or word1 == "e") or (word2 == "east" or word2 == "e"):
            Character.positionx += 1
        if (word1 == "south" or word1 == "s") or (word2 == "south" or word2 == "s"):
            Character.positiony -= 1
        if (word1 == "west" or word1 == "w") or (word2 == "west" or word2 == "w"):
            Character.positionx -= 1
        CharacterPosition = [Character.positionx,Character.positiony]

        if (str(CharacterPosition) in str(CurrentRoom.exits)):

            for rooms in CurrentRoom.exits:

                if (str(CharacterPosition) == str(CurrentRoom.exits[0])) or (str(CharacterPosition) == str(CurrentRoom.exits[1])) or (str(CharacterPosition) == str(CurrentRoom.exits[2])):
                            CurrentRoom = TheRoom(Character.positionx,Character.positiony)
                            print("You enter",str(CurrentRoom.name))
                            print("You move to the",word2)
                            print(CurrentRoom)
                            break
                else:
                    print("You cannot move in this direction")
        else:
            print("You cannot move in this direction")
            Character.positionx = CurrentRoom.positionx
            Character.positiony = CurrentRoom.positiony
    else:
        print("You have not entered a direction")

def TheRoom(positionx,positiony):
    for room in Rooms:
        if (room.positionx == Character.positionx) and (room.positiony == Character.positiony):
            return room


def ItemCheck(word2):
    for i in Character.itemsHeld:
        if (word2 == str(i.name)):
            print (i.itemDesc)


def ItemDrop(word2):
    CurrentRoom = TheRoom(Character.positionx,Character.positiony)

    for i in Character.itemsHeld:
        if (word2 == str(i.name)):
            CurrentRoom.items.append(i)
            print("You have dropped a " + i.name)
            Character.itemsHeld.remove(i)
            break

        

def ItemUsing(word2):
    CurrentRoom = TheRoom(Character.positionx,Character.positiony)
    if (word2 == str(CurrentRoom.lockUse)):

        CurrentRoom.locked = "n"
        for i in Character.itemsHeld:
            if (word2 == str(i.name)):
                print("You have used " + i.name)
                print(i.Use)
                Character.itemsHeld.remove(i)
                if (i.name == "picture"):
                    CurrentRoom.exits.append([-1,2])
                    CurrentRoom.description = KitchenDescription2
                elif (i.name == "key"):
                    CurrentRoom.items.append(Item("lighter",lighterDescription,lighterUse))
                    CurrentRoom.description = LivingRoomDescription2
                elif (i.name == "lighter"):
                    CurrentRoom.exits.append([1,3])
                    CurrentRoom.description = DiningRoomDescription2
                elif (i.name == "knife"):
                    Ending = open("Ending.txt","r")
                    print (Ending.read())
                    Ending.close()
                    GameEnding();

    else:
        print("Using this item has no effect.")

def GameEnding():
    global GameEnded
    GameEnded = True

print(StartingStory)
Character = Character([Item("",Placeholder,Placeholder)],0,0)
CharacterPosition = [0,0]

while True:
    if (GameEnded == True):
        print("Game Ended, Thanks for playing!")
        break
    UserInput = str(input("Please enter a command : "))
    InputCheck(UserInput.lower())
