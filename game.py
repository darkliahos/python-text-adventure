class Location:
    def __init__(self, description):
        self.description = description
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.items = []
        self.monsters = []

    def addPickup(self, item):
        self.items.append(item)

    def addMonsters(self, monster):
        self.monsters.append(monster)

    def checkForMonsters(self):
        if(len(self.monsters) > 0):
            return "You have encountered " + self.monsters[0].name + " "
        else:
            return ""

    def pickUpItem(self, item):
        self.items.remove(item)
        return item

class Monster: 
    def __init__(self, name):
        self.health = 20
        self.name = name

class Player:
    def __init__(self):
        self.health = 400
        self.attack = 50

    def kick(self, monster):
        if self.attack > monster.health:
            return monster.name + " died"

class Backpack: 
    def __init__(self, totalStorage):
        self.storage = totalStorage
        self.items = []
    def addToBackPack(self, item):
        if(item == "cheese"):
            self.storage = self.storage - 10

        self.items.append(item)

doras_backpack = Backpack(300)
dining_room = Location('An old decrepit dining room. ')
dining_room.addMonsters(Monster("Osama Bin Laden"))
kitchen = Location(
    'A mouldy kitchen with cheese on the counter and drugs littered on the floor. ')
kitchen.addPickup('cheese')
kitchen.addPickup('drugs')

kitchen.south = dining_room

bathroom = Location('A room full of defecation. ')
bedroom = Location('A kinky sex dungeon. ')
bedroom.west = dining_room

porch = Location('A dark place in Detroit. ')


dining_room.north = kitchen
dining_room.east = bedroom
dining_room.west = bathroom
dining_room.south = porch

print("Welcome to your worst nightmare, press enter to continue")

current_location = dining_room

response = ''
while response != 'quit':
    response = input('You see ' + current_location.description + "\n" + current_location.checkForMonsters())
    if response == "north":
        current_location = current_location.north
    elif response == 'south':
        current_location = current_location.south
    elif response == "west":
        current_location = current_location.west
    elif response == 'east':
        current_location = current_location.east
    elif response == 'check bag':
        print("Backpack has " + str(doras_backpack.storage) + " left")
    elif response .startswith('take '):
        success = False
        for item in current_location.items:
            if response.endswith(item):
                current_location.pickUpItem(item)
                success = True
                break

        if success == True:
            doras_backpack.addToBackPack(item)
            print("Picked up " + item)
        else:
            print("Items does not exist")

print("The End...")
