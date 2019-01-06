from Classes import * # All Classes Come from here
from StoryAndDescriptions import * # All descriptions and story from here.
# Here I am importing from the other python files I am using.

GameEnded = False
Rooms = [] #The list will contain all of the rooms.
#x 1 east -1 west y 1 north -1 south
Rooms.append(Room([Item("",Placeholder,Placeholder)],0,0,[[0,1]],StartingRoomDescription,"","OutsideHouse")) # Starting room / Outside House
Rooms.append(Room([Item("picture",PictureDescription,PictureUse),Item("",Placeholder,Placeholder)],0,1,[[-1,1],[0,0],[0,2]],PorchDescription,"","Porch")) # Porch
Rooms.append(Room([Item("knife",KnifeDescription,knifeUse)],-1,1,[[0,1]],KitchenDescription,"picture","Kitchen")) # Kitchen
Rooms.append(Room([Item("key",keyDescription,keyUse),Item("",Placeholder,Placeholder)],-1,2,[[-1,1]],StudyDescription,"","Study")) # Study
Rooms.append(Room([Item("",Placeholder,Placeholder)],0,2,[[0,1],[1,2]],LivingRoomDescription,"key","Living Room")) # Living Room
Rooms.append(Room([Item("",Placeholder,Placeholder)],1,2,[[0,2]],DiningRoomDescription,"lighter","Dining Room")) # Dining Room
Rooms.append(Room([Item("",Placeholder,Placeholder),Item("",Placeholder,Placeholder)],1,3,[[2,3]],CellerDescription,"","Celler")) # Celler
Rooms.append(Room([Item("",Placeholder,Placeholder)],2,3,[[1,3]],CaveDescription,"knife","Cave enterance")) # Cave Enterance
# Here I am appending all of the rooms to the list using the class room and then giving them the values needed so location on x and y, items (using the item class), the rooms description
# Any item which has a use in that room and the name.


# This is the largest function which I use and it manages all of the user input.
def InputCheck(Input):
    CurrentRoom = TheRoom(Character.positionx,Character.positiony)                  # This is setting the current room using "TheRoom" function (this returns the room which is equal to the players current x and y position).
    AvaliableCommands = ["move", "check", "use", "pickup","drop","help","quit"]     # All commands the player can input are here
    Command = Input.split()                                                         # Spliting user inputs at each word. Then I will make variables equal to each of the words the user inputted later on.
    for word in Command:                                                            # Starts a for loop which runs for the number of words in the user input
        if (len(Command) == 1):
# This is where I have split my user input into two, I decided earlier on that the user could either input one word for more simple responses or input two to do something more specific.
            word1 = (Command[0])
            if (word1 in AvaliableCommands):
# Here I am checking word1 (The first word in user inputted) against the avaliable commands list and then if it in equal to a word in that list. It will go through a check to see which command it is equal to.
                if word1 == "move":
                    word2 = (str(input("Enter a direction : "))).lower()
# If the first word is equal to move then it gets a direction (a second word) stored in word2, and then performs the move function taking both word variables.
                    Move(word1,word2)

                    break                                                           # Everytime I am using break it is stopping the loop.
                elif word1 == "check":
# If the word which is inputted is equal to "check", since the user hasn't inputted any specific object it checks the room by default. Printing the CurrentRoom's description.
                    print (CurrentRoom)
                    print ("To check something specific please use : Check [what you would like to check] , You can also checking your inventory using : Check inv")
                    break
                elif word1 == "use":
# If the first word is equal to "use, it then asks for a second word so what do you want to use and then if the word which they inputted is in the player inventory (Itemcheck), it will then perform the function "ItemUsing".
                    word2 = (str(input("Enter what you would like to use : "))).lower()
                    if word2 in Character.ItemCheck():

                        ItemUsing(word2);
                        break
                    else:                                                           # If the item isn't in the character inventory list then it will respond with that you dont have the item
                        print("You don't have this item!")
                        break

                elif word1 == "pickup":
# If the word is equal to "pickup" it then takes the second word (what you want you pickup), and then does an if statement to check if the item is in the room.
# It then the loops through the items in the room to find the item which matches the word. Once the item has been found it appends it to the character inventory list
# then it prints telling the player they have picked it up and removes it from the rooms item list.
                    word2 = (str(input("Enter what you would like to pickup:"))).lower()
                    if word2 in CurrentRoom.ItemsInRoom():
                        for item in CurrentRoom.items:
                            if (word2 == str(item.name)):

                                Character.itemsHeld.append(item)
                                if (item.name == "picture"):
                                    CurrentRoom.description = PorchDescription2
# If the item picked up is equal to picture or the key it changes the description to tell the player they have picked it up when they check or reenter the room.
                                if (item.name == "key"):
                                    CurrentRoom.description = StudyDescription2
                                print("You have picked up a " + item.name)
                                CurrentRoom.items.remove(item)
                                return

                    else:
                        print("You cannot pick this up!")
                        break
                elif word1 == "drop":
# if the word is equal to drop then it then asks for a second word being what do you want to drop, it then goes through the same routine of checking the item and then runs the item drop function
                    word2 = Input(str("What do you want to drop?"))
                    if word2 in Character.ItemCheck():

                        ItemDrop(word2);
                        break
                elif word1 == "quit":
# if the word is equal to quit then it runs the game end function to stop the loop.

                    GameEnding();
                    break
                elif word1 == "help":
# finally if the word is equal to help then it prints the avaliable commands list.
                    print("You can enter these commands : ",AvaliableCommands)
                    break
            else:
                print("Unknown Command")
# if the word is not in the command list it print thats its unknown

        elif (len(Command) == 2):
# This is now checking if the user inputs 2 words this works the same as the one word section however it doesn't ask for the second word when needed and allows for some more specific things.
            word1 = (Command[0])
            word2 = (Command[1])
# This now stores both words rather then just the one.
            if (word1 in AvaliableCommands):                                        # Does the same check to make sure word 1 is an avaliable command.
                if (word1 == "move"):
                    Move(word1,word2)                                               # Does the same as moving with one word.
                    break
                elif word1 == "check":
# Here it allows more much more things to be checked so if the word is equal to room it prints the room description.
                    if word2 == "room":
                        print(CurrentRoom)
                        break
                    elif word2 == "inv":
                        print(Character)                                            # If the word is equal to inv it prints the players current inventory
                        break
                    elif word2 in Character.ItemCheck():
                        ItemCheck(word2);                                           # Or if the word is in the characters current inventory it then performs the item check function.
                        break
                    else:
                        print("You cannot check this!")                             # Lastly if the word doesn't equal any of these then it tells the player they can't check what they are trying to.
                        break

                elif word1 == "pickup":                                             # This does the same as checking an item with the one word input but doesn't need to take in another word.
                    if word2 in CurrentRoom.ItemsInRoom():
                        for item in CurrentRoom.items:

                            if (word2 == str(item.name)):

                                Character.itemsHeld.append(item)
                                if (item.name == "picture"):
                                    CurrentRoom.description = PorchDescription2
                                if (item.name == "key"):
                                    CurrentRoom.description = StudyDescription2
                                print("You have picked up a " + item.name)
                                CurrentRoom.items.remove(item)
                                return

                    else:
                        print("You cannot pick this up!")
                        break
                elif word1 == "use":                                                # This is the same as using an item with the one word input, again not needing to take in another word.
                    if word2 in Character.ItemCheck():

                        ItemUsing(word2);
                        break
                    else:
                        print("You don't have this item!")
                        break

                elif word1 == "drop":                                               # This is the same as using an item with the one word input.
                    if word2 in Character.ItemCheck():

                        ItemDrop(word2);
                        break
                elif (word1 == "quit"):                                             # Finally this works exactly the same as quiting using one word, as the second word is not needed.
                    GameEnding();

            else:                                                                   # If the word is not in the avaliable commands then it will print saying that its an unknown command
                print("Unknown Command")
                break
        else:
            print("Please only enter 1 - 2 words. Enter help to see avaliable commands")
            break
# With the input system I decided I would take in the two different kinds of inputs being one word and two words. As I thought that it would allow the player to type in commands in the way they deemed were most comfortable.
# Thats why some of the sections repeat.

#-- Action Functions

def Move(word1,word2):
    Directions = ["north","n","east","e","south","s","west","w"]                    # All of the possible words which are used for directions.
# First we are getting the current room using "TheRoom" function so that we can use its exits later on. Then we are checking the second word against the directions in the list and
# if it equal to the of the words then it changes the x or y position accordingly.
    CurrentRoom = TheRoom(Character.positionx,Character.positiony)
    if (word2 in Directions):
        if (word2 == "north" or word2 == "n"):
             Character.positiony += 1                                               # North is plus on the y scale and south being negative.
        if (word2 == "east" or word2 == "e"):
            Character.positionx += 1                                                # East is plus on the x scale and west is negative. The idea being the same as a graph for axis.
        if (word2 == "south" or word2 == "s"):
            Character.positiony -= 1
        if (word2 == "west" or word2 == "w"):
            Character.positionx -= 1
# Now we get the characters x and y position and store them as list so we can compare them to the exits in the room the player is in, if the exit does exist then it checks against the exits.
        CharacterPosition = [Character.positionx,Character.positiony]
        if (str(CharacterPosition) in str(CurrentRoom.exits)):

                if (str(CharacterPosition) == str(CurrentRoom.exits[0])) or (str(CharacterPosition) == str(CurrentRoom.exits[1])) or (str(CharacterPosition) == str(CurrentRoom.exits[2])):
# If the characters new position is equal to one of the exits in the room then it updates the current room with the new room and it prints the room you have moved into, the direction you moved and the room description.
                            CurrentRoom = TheRoom(Character.positionx,Character.positiony)
                            print("You enter",str(CurrentRoom.name))
                            print("You move to the",word2)
                            print(CurrentRoom)

        else:
# If the character position isn't equal to any of the exits in the room it resets the characters position by making it equal to current rooms x and y position. And prints that the player cant move in that direction.
            print("You cannot move in this direction")
            Character.positionx = CurrentRoom.positionx
            Character.positiony = CurrentRoom.positiony
    else:
        print("You have not entered a direction")
# "TheRoom" function uses a for loop to check all of the rooms in room list and checks to see if any of them are equal to the players positions and returns the room which is.
# This is function is what I used to update which room the player is in.
def TheRoom(positionx,positiony):
    for room in Rooms:
        if (room.positionx == Character.positionx) and (room.positiony == Character.positiony):
            return room

# This function loops for each item in the players inventory and if the second word (word 2) is equal to the items name then it prints its description.
def ItemCheck(word2):
    for item in Character.itemsHeld:
        if (word2 == str(item.name)):
            print (item.itemDesc)

# The "ItemDrop" function first gets the current room so the item is dropped to the right place. Then it does a for loop for each item in the characters inventory list and if the second word equals the items name,
# it then appends the item to the current rooms item list and removes it from the character inventory. It also prints which item has been dropped.
def ItemDrop(word2):
    CurrentRoom = TheRoom(Character.positionx,Character.positiony)

    for item in Character.itemsHeld:
        if (word2 == str(item.name)):
            CurrentRoom.items.append(item)
            print("You have dropped a " + item.name)
            Character.itemsHeld.remove(item)
            break


# The "ItemUsing" functions works similar to the item dropped function, it starts by getting the current room and then checking if word 2 is equal to the current rooms lock use (the items which have a use in this room).
def ItemUsing(word2):
    CurrentRoom = TheRoom(Character.positionx,Character.positiony)
    if (word2 == str(CurrentRoom.lockUse)):
# If it is equal to it then it using a for loop to find the item with the same name as second word. It then prints you have used the item and its use description, then it removes the item from the player inventory list.
        for items in Character.itemsHeld:
            if (word2 == str(items.name)):
                print("You have used " + items.name)
                print(items.Use)
                Character.itemsHeld.remove(items)
# Here I am checking to see if the item used is any of the following since this is either for changing room descriptions, adding new exits (Secret rooms being discovered) or adding items (opening boxes).
                if (items.name == "picture"):
# For example this is appending a new exit since a room is now accessible.
                    CurrentRoom.exits.append([-1,2])
                    CurrentRoom.description = KitchenDescription2
                elif (items.name == "key"):
# This is adding a new item to the current rooms items and since the key only has one room it can be used on, it will always append to the right room.
                    CurrentRoom.items.append(Item("lighter",lighterDescription,lighterUse))
                    CurrentRoom.description = LivingRoomDescription2
                elif (items.name == "lighter"):
                    CurrentRoom.exits.append([1,3])
                    CurrentRoom.description = DiningRoomDescription2
                elif (items.name == "knife"):
# Using the knife is what triggers the ending, for this I decided to make a seperate text document and then open it and read it, using the open function. it then can print the contents of the text file,
# by printing the variable which has the file open and using the read function. After I have finished reading the file I then close it using the close function. Finally it runs the game end function to stop the while loop.
                    Ending = open("Ending.txt","r")
                    print (Ending.read())
                    Ending.close()
                    GameEnding();

    else:
# If word 2 is different then the lock use it prints that you are using the wrong item, and if wondering what about not having the item, in the input checking you can only use the function if the item is in the character inventory list.
        print("Using this item has no effect.")
# This function is very simple it is making the variable GameEnded a global variable so that when the while loop restarts it can check the if statement and see if the game has ended. It is also setting the GameEnded variable to true,
# since we want the game to stop.
def GameEnding():
    global GameEnded
    GameEnded = True

# -- Running the game

# Here I am printing the opening to the story, and I am also creating the character variable and setting the inventory to have a blank object since the way I have done the classes,
# the item checking, dropping and using, requires rooms and the player to atleast have an item in the lists. I have set the character's x and y position to 0.
print(StartingStory)
Character = Character([Item("",Placeholder,Placeholder)],0,0)
# I also set the character position variable to have a default of 0,0
CharacterPosition = [0,0]

# This while loop is what allows the game to play as it will keep running unless broken. So in this loop I have a check to see if the game has finished using the "GameEnded" function, I then have a variable which stores user inputs.
# and then I use the input checker function which goes through and makes everything word accordingly, I also make sure to set all of the user inputs to lowercase at it keeps all of the words consistent and doesn't cause trouble with caps.
while True:
    if (GameEnded == True):
        print("Game Ended, Thanks for playing!")
        break
    UserInput = str(input("Please enter a command : "))
    InputCheck(UserInput.lower())
