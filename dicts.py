# travel_types = set(["teleport", "walk", "fly", "ride"])
# alignments = set(["allied", "neutral", "enemy"])

class Room(dict):
    def __init__(self, hidden, pathways):
        self.dict = {
            self.hidden : hidden,
            self.pathways : pathways
        }

class Location(dict):
   def __init__(self, rooms, alignment):
      self.dict = {
          self.alignment : alignment,
          self.rooms : rooms
      }

void_room = Room(True, ["p1"])
village_entrance = Room(False, ["p1"])
forest1 = Room(False, [])
castle_entrance = Room(False, [])
mountains1 = Room(False, [])
cave_entrance = Room(False, [])

void = Location([void_room], "neutral")
village = Location([village_entrance], "good")
forest = Location([forest1], "neutral")
castle = Location([castle_entrance], "")
mountains = Location([mountains1], "")
cave = Location([cave_entrance], "")

world = {
    "void" : void,
    "village" : village,
    "forest" : forest,
    "castle" : castle,
    "mountains" : mountains,
    "cave" : cave

}

def location_data_retrieval(path):
    val = world.get(path)
    return val

print(world)