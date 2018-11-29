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
        return str("Check you pockets to find : ",itemsHeld)
