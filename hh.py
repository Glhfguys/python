class Item:
  """
  Represents an item in the game with a name and description.
  """
  def __init__(self, name, description):
    self.name = name
    self.description = description

class Room:
  """
  Represents a room in the game with a description, exits (directions), and items.
  """
  def __init__(self, description):
    self.description = description
    self.exits = {"north": None, "south": None, "east": None, "west": None}
    self.items = []

  def connect_rooms(self, north, south, east, west):
    """
    Connects the room to other rooms in the specified directions.
    """
    self.exits["north"] = north
    self.exits["south"] = south
    self.exits["east"] = east
    self.exits["west"] = west

  def add_item(self, item):
    """
    Adds an item to the room.
    """
    self.items.append(item)

  def describe(self):
    """
    Provides a description of the room and its contents.
    """
    print(self.description)
    if self.items:
      print("Items:", ", ".join(item.name for item in self.items))

class Player:
  """
  Represents the player in the game with current location and inventory.
  """
  def __init__(self):
    self.current_room = None
    self.inventory = []

  def move(self, direction):
    """
    Attempts to move the player to the specified direction (if possible).
    """
    if direction in self.current_room.exits and self.current_room.exits[direction]:
      self.current_room = self.current_room.exits[direction]
      self.current_room.describe()
    else:
      print("You cannot go that way.")

  def take_item(self, item_name):
    """
    Attempts to take an item from the current room and add it to the player's inventory.
    """
    item = [item for item in self.current_room.items if item.name.lower() == item_name.lower()]
    if item:
      self.current_room.items.remove(item[0])
      self.inventory.append(item[0])
      print(f"You take the {item[0].name}.")
    else:
      print("There is no such item here.")

def main():
  """
  Sets up the game world, items, rooms, and starts the game loop.
  """

  # Create items
  key = Item("key", "A rusty old key.")
  coin = Item("coin", "A gold coin worth a small fortune.")

  # Create rooms
  kitchen = Room("You are in the kitchen. A faint smell of something delicious lingers in the air.")
  bedroom = Room("You are in the bedroom. Sunlight streams through the window.")
  hallway = Room("You are in the hallway. Doors lead north and south.")

  # Connect rooms
  kitchen.connect_rooms(None, hallway, None, bedroom)
  bedroom.connect_rooms(kitchen, None, None, None)
  hallway.connect_rooms(kitchen, None, None, None)

  # Add items to rooms
  kitchen.add_item(key)
  hallway.add_item(coin)

  # Create player and set starting location
  player = Player()
  player.current_room = kitchen

  # Game loop
  while True:
    print("\nWhat do you do?")
    action = input("> ").lower().split()

    if len(action) >= 2 and action[0] == "go":
      player.move(action[1])
    elif len(action) >= 2 and action[0] == "take":
      player.take_item(action[1])
    elif action[0] == "look":
      player.current_room.describe()
    elif action[0] == "inventory":
      if player.inventory:
        print("You are carrying:", ", ".join(item.name for item in player.inventory))
      