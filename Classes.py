# This file is where I am storing all of my classes, which I use in the main file, keeping them here allows for me to easily manage them and make changes if needed.
class Room(object):
# The room class needs to have a lot of different attributes and the init magic function allows me to define that,
# so it has: an item list, x and y position, a list of all exits, a description of the room, which item has use in the room,
# and the room name, these allow me to management movement and room updating, picking up, dropping and using items and print the story to the player.
    def __init__(self,items,positionx,positiony,exits,description,lockUse,name):
        self.items = items;
        self.positionx = positionx;
        self.positiony = positiony;
        self.exits = exits;
        self.description = description;
        self.lockUse = lockUse
        self.name = name;
# The str magic function essentiually allows me to print the user the room description and I use this everytime the room is updated when the player moves into one.
    def __str__(self):
        RoomEnterDescription = ("You are"+ self.description)
        return str(RoomEnterDescription)
# This function allows me to check through all of the items in the room, by looping through them and adding the name to a str and then appening a list.
# This function is used when picking up items since it checks if the word is equal to an item in the list.
    def ItemsInRoom(self):
        Itemlist = []
        ItemNames = ""
        for i in self.items:
            ItemNames = ""
            ItemNames += str(i.name)
            Itemlist.append(ItemNames)
        return Itemlist

# The character allows for the player to have all of the attributes which are important such as their inventory (item list) and x and y position.
class Character(object):
    def __init__(self, itemsHeld,positionx,positiony):
        self.itemsHeld = itemsHeld;
        self.positionx = positionx;
        self.positiony = positiony;
# The str magic function here is used for when the player checks their inventory, since it makes a str and for each item in their inventory,
# it runs the loop adds it to the str variable along with a comma to split an object from others.
    def __str__(self):
        ItemNames = ""
        for i in self.itemsHeld:
            ItemNames += str(i.name + " , ")
        return ("Check you pockets to find : "+ItemNames)
# The item check function works the same as the items in room function which the room class has, runs a loop for every item, adding them to a str and appending to a list.
# This is used when using and dropping an item since a check is made to make sure the player does have the item first.
    def ItemCheck(self):
        Itemlist = []
        ItemNames = ""
        for i in self.itemsHeld:
            ItemNames = ""
            ItemNames += str(i.name)

            Itemlist.append(ItemNames)
        return Itemlist
# The Item class is used to give attributes to items, this being their description, the name of the item and finally their usage text (description of how the item was used).
class Item(object):
    def __init__(self,name,itemDesc,Use):
        self.name = name;
        self.itemDesc = itemDesc;
        self.Use = Use;
# The str magic function is used to tell the player what was picked up
    def __str__(self):
        return ("You picked up "+self.name)
