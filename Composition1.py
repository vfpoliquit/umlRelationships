class Room:

    def __init__(self, name: str):
        self.name = name


class House:

    def __init__(self):
        # House creates and owns Room objects directly
        self.rooms = [Room("Kitchen"), Room("Bedroom")]


# Usage
my_house = House()
for room in my_house.rooms:
    print(f"Room created: {room.name}")