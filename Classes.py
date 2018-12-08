class Room(object):
    def __init__(self,items,positionx,positiony,exits,description):
        self.items = items;
        self.positionx = positionx;
        self.positiony = positiony;
        self.exits = exits;
        self.description = description;

    def __str__(self):
        RoomEnterDescription = ("You are"+ self.description)
        return str(RoomEnterDescription)

    def RoomDescription(self):
        Description = self.description
        return str(Description)

class Character(object):
    def __init__(self, itemsHeld,positionx,positiony):
        self.itemsHeld = itemsHeld;
        self.positionx = positionx;
        self.positiony = positiony;
    def __str__(self):
        ItemNames = ""
        for i in self.itemsHeld:
            ItemNames += str(i.name + " ")
        return ("Check you pockets to find : "+ItemNames)
    def ItemCheck(self):
        Itemlist = []
        ItemNames = ""
        for i in self.itemsHeld:
            ItemNames += str(i.name + " ")
        Itemlist += ItemNames
        return ItemNames

class Item(object):
    def __init__(self,name,itemDesc,Use):
        self.name = name;
        self.itemDesc = itemDesc;
        self.Use = Use;
    def __str__(self):
        return ("You picked up "+self.name)
