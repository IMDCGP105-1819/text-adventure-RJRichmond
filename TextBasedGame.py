from Classes import *
from StoryAndDescriptions import *

GameEnded = False
Rooms = []
#x 1 east -1 west y 1 north -1 south
Rooms.append(Room([Item("",Placeholder,Placeholder)],0,0,[[0,1]],StartingRoomDescription)) # Starting room
Rooms.append(Room([Item("picture",PictureDescription,PictureUse),Item("",Placeholder,Placeholder)],0,1,[[-1,1],[0,0]],PorchDescription)) # Porch
Rooms.append(Room([Item("",Placeholder,Placeholder)],-1,1,[[0,1],[-1,2]],NewRoomDescription)) # Kitchen

def InputCheck(Input):
    CurrentRoom = TheRoom(Character.positionx,Character.positiony)
    AvaliableCommands = ["move", "check", "use", "pickup","drop", "quit"]
    Command = Input.split()
    print(Command)
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
                    break
                elif word1 == "check":
                    print(Character.ItemCheck())
                    if word2 == "room":
                        print(CurrentRoom)
                        break
                    elif word2 == "inv":
                        print("This is happening")
                        print(Character)
                        break
                    elif word2 in Character.ItemCheck():
                        print("This is checking properly")
                        ItemCheck(word2);
                        break
                    else:
                        print("You cannot check this!")
                        break

                elif word1 == "pickup":
                    if str(word2) in str(CurrentRoom.items[0]):
                        Character.itemsHeld.append(CurrentRoom.items[0])
                        print ("Works")
                        print("You have picked up a " + CurrentRoom.items[0].name)
                        CurrentRoom.items.remove(CurrentRoom.items[0])
                        break
                    else:
                        print("You cannot pick this up!")
                        break
                elif word1 == "drop":
                    if word2 in Character.ItemCheck():
                        print("Dropping an item")
                        ItemDrop(word2);
                        break
                        
                elif (word1 == "quit") or (word2 == "quit"):
                    GameEnded = True
                    break
            else:
                print("Unknown Command")
        else:
            print("Please only enter 1 - 2 words. Enter help to see avaliable commands")

def Move(word1,word2):
    Directions = ["north","n","east","e","south","s","west","w"]
    CurrentRoom = TheRoom(Character.positionx,Character.positiony)
    if (word1 in Directions) or (word2 in Directions):
        if (word1 == "north" or word1 == "n") or (word2 == "north" or word2 == "n"):
             Character.positiony += 1
             #print(Character.positiony)
        if (word1 == "east" or word1 == "e") or (word2 == "east" or word2 == "e"):
            Character.positionx += 1
        if (word1 == "south" or word1 == "s") or (word2 == "south" or word2 == "s"):
            Character.positiony -= 1
        if (word1 == "west" or word1 == "w") or (word2 == "west" or word2 == "w"):
            Character.positionx -= 1
        CharacterPosition = [Character.positionx,Character.positiony]
        #print(CharacterPosition)
        #if (str(CurrentRoom.exits) == str(CharacterPosition)):
        print(CharacterPosition)
        print(CurrentRoom.exits)
        if (str(CharacterPosition) in str(CurrentRoom.exits)):
            print("happens")
            for rooms in CurrentRoom.exits:
                print(CurrentRoom.exits[0])
                if (str(CharacterPosition) == str(CurrentRoom.exits[0])) or (str(CharacterPosition) == str(CurrentRoom.exits[1])):
                    CurrentRoom = TheRoom(Character.positionx,Character.positiony)
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
        print("item got")
        if (word2 == str(i.name)):
            print ("item found")
            print (i.itemDesc)
        else:
            print("not the right item")

def ItemDrop(word2):
    CurrentRoom = TheRoom(Character.positionx,Character.positiony)
    print(CurrentRoom.ItemsInRoom())
    for i in Character.itemsHeld:
        print("item got")
        if (word2 == str(i.name)):
            print ("item found")
            CurrentRoom.items.append(i)
            print("You have dropped up a " + i.name)
            Character.itemsHeld.remove(i)
            print(CurrentRoom.ItemsInRoom())

        else:
            print("not the right item")

print(StartingStory)
Character = Character([Item("",Placeholder,Placeholder)],0,0)
CharacterPosition = [0,0]

while (GameEnded == False):

    UserInput = str(input("Please enter a command : "))
    InputCheck(UserInput.lower())
