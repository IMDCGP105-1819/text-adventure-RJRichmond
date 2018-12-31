class Room(object):
    def __init__(self,items,positionx,positiony,exits,description,locked,lockUse):
        self.items = items;
        self.positionx = positionx;
        self.positiony = positiony;
        self.exits = exits;
        self.description = description;
        self.locked = locked;
        self.lockUse = lockUse

    def __str__(self):
        RoomEnterDescription = ("You are"+ self.description)
        return str(RoomEnterDescription)

    def RoomDescription(self):
        Description = self.description
        return str(Description)

    def ItemsInRoom(self):
        Itemlist = []
        ItemNames = ""
        for i in self.items:
            ItemNames = ""
            ItemNames += str(i.name)
            print(ItemNames)
            Itemlist.append(ItemNames)
        return Itemlist


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
            ItemNames = ""
            ItemNames += str(i.name)
            print(ItemNames)
            Itemlist.append(ItemNames)
        return Itemlist

class Item(object):
    def __init__(self,name,itemDesc,Use):
        self.name = name;
        self.itemDesc = itemDesc;
        self.Use = Use;
    def __str__(self):
        return ("You picked up "+self.name)
