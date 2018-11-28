class Room(object):
    def __init__(self,items,position,exits,description):
        self.items = items;
        self.position = position;
        self.exits = exits;
        self.description = description;

    def __str__(self):
        RoomEnterDescription = ("You are "+ self.description)
        return str(RoomEnterDescription)

    def RoomDescription(self):
        Description = self.description
        return str(Description)

class Character(object):
    def __init__(self, itemsHeld,position):
        self.itemsHeld = itemsHeld;
        self.position = position;
    def __str__(self):
        return str("Check you pockets to find : ",itemsHeld)
