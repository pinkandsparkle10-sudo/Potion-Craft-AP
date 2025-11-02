from dataclasses import dataclass
from enum import Enum
from typing import Dict

from BaseClasses import Item, ItemClassification
from typings.schema import Optional


class PotionCraftItem(Item):
    game: str = "Potion Craft"
class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

@dataclass
class ItemData:
    code: int
    classification: ItemClassification
    chapter: int = 0
    direction: list[Direction] | None = None
    amount: Optional[int] = 1

def get_junk_item_names(rand, k: int) -> str:
    junk = rand.choices(
        list(junk_weights.keys()),
        weights=list(junk_weights.values()),
        k=k)
    return junk

def create_item(world, name: str, classification: ItemClassification, amount: Optional[int] = 1):
    for i in range(amount):
        world.itempool.append(Item(name, classification, world.item_name_to_id[name], world.player))


def create_potion_craft_items(world):
    total_location_count = len(world.multiworld.get_unfilled_locations(world.player)) #adds items to world.item pool

    print(len(world.itempool))

    remaining_locations: int = total_location_count - len(world.itempool)
    junk_count: int = remaining_locations - 1  # Minus 1 because we placed victory at the goal check in Rules.py
    junk = get_junk_item_names(world.random, junk_count)
    for name in junk:
        create_item(world, name, ItemClassification.filler)
    world.multiworld.itempool += world.itempool

ingredients: Dict[str, ItemData] = {
    "Windbloom" : ItemData(1, ItemClassification.progression, 1,[Direction.NORTH]), #Herb start
    "Waterbloom" : ItemData(2, ItemClassification.progression, 1, [Direction.EAST]),
    "Terraria" : ItemData(3, ItemClassification.progression, 1, [Direction.SOUTH]),
    "Tangleweed" : ItemData(4, ItemClassification.progression, 1, [Direction.EAST]),
    "Lifeleaf" : ItemData(5, ItemClassification.progression, 1, [Direction.EAST, Direction.SOUTH]),
    "Firebell" : ItemData(6, ItemClassification.progression, 1, [Direction.WEST]),
    "Thunder Thistle" : ItemData(7, ItemClassification.progression, 2, [Direction.WEST, Direction.SOUTH]),
    "Icefruit" : ItemData(8, ItemClassification.progression, 2, [Direction.NORTH, Direction.SOUTH, Direction.EAST]),
    "Hairy Banana" : ItemData(9, ItemClassification.progression, 2, [Direction.SOUTH, Direction.WEST]),
    "Goodberry" : ItemData(10, ItemClassification.progression, 2, [Direction.EAST, Direction.SOUTH]),
    "Goldthorn" : ItemData(11, ItemClassification.progression, 2, [Direction.SOUTH, Direction.EAST]),
    "Lava Root" : ItemData(12, ItemClassification.progression, 3, [Direction.WEST]),
    "Featherbloom" : ItemData(13, ItemClassification.progression, 3, [Direction.NORTH]),
    "Druid's Rosemary" : ItemData(14, ItemClassification.progression, 3, [Direction.SOUTH, Direction.EAST]),
    "Dream Beet" : ItemData(15, ItemClassification.progression, 3, [Direction.EAST, Direction.NORTH]),
    "Bloodthorn" : ItemData(16, ItemClassification.progression, 3, [Direction.NORTH, Direction.WEST]),
    "Whirlweed" : ItemData(17, ItemClassification.progression, 4, [Direction.NORTH]),
    "Thornstick" : ItemData(18, ItemClassification.progression, 4, [Direction.SOUTH, Direction.WEST]),
    "Grasping Root" : ItemData(19, ItemClassification.progression, 4, [Direction.NORTH, Direction.WEST]),
    "Flameweed" : ItemData(20, ItemClassification.progression, 4, [Direction.WEST]),
    "Coldleaf" : ItemData(21, ItemClassification.progression, 4, [Direction.EAST]),
    "Spellbloom" : ItemData(22, ItemClassification.progression, 5, [Direction.NORTH, Direction.EAST]),
    "Healer's Heather" : ItemData(23, ItemClassification.progression, 5, [Direction.SOUTH, Direction.EAST]),
    "Fluffbloom" : ItemData(24, ItemClassification.progression, 5, [Direction.NORTH, Direction.EAST]),
    "Dragon Pepper" : ItemData(25, ItemClassification.progression, 5, [Direction.SOUTH, Direction.WEST, Direction.NORTH]),
    "Boombloom" : ItemData(26, ItemClassification.progression, 5, [Direction.NORTH, Direction.WEST]),
    "Terror Bud" : ItemData(27, ItemClassification.progression, 6, [Direction.SOUTH, Direction.WEST, Direction.NORTH]),
    "Mageberry" : ItemData(28, ItemClassification.progression, 6, [Direction.EAST, Direction.NORTH]),
    "Evergreen Fern" : ItemData(29, ItemClassification.progression, 6, [Direction.EAST, Direction.SOUTH]), #Herb End
    "Dryad's Saddle" : ItemData(30, ItemClassification.progression, 1, [Direction.SOUTH]), #Mushroom Start
    "Mad Mushroom" : ItemData(31, ItemClassification.progression, 1, [Direction.NORTH, Direction.WEST]),
    "Marshroom" : ItemData(32, ItemClassification.progression, 1, [Direction.SOUTH, Direction.EAST]),
    "Mudshroom" : ItemData(33, ItemClassification.progression, 1, [Direction.SOUTH]),
    "Stink Mushroom" : ItemData(34, ItemClassification.progression, 1, [Direction.NORTH, Direction.EAST]),
    "Sulphur Shelf" : ItemData(35, ItemClassification.progression, 1, [Direction.WEST]),
    "Witch Mushroom" : ItemData(36, ItemClassification.progression, 1, [Direction.SOUTH, Direction.WEST]),
    "Shadow Chanterelle" : ItemData(37, ItemClassification.progression, 2, [Direction.NORTH, Direction.EAST]),
    "Weirdshroom" : ItemData(38, ItemClassification.progression, 2, [Direction.SOUTH, Direction.EAST]),
    "Foggy Parasol" : ItemData(39, ItemClassification.progression, 3, [Direction.NORTH]),
    "Goblin Shroom" : ItemData(40, ItemClassification.progression, 3, [Direction.SOUTH, Direction.WEST]),
    "Moss Shroom" : ItemData(41, ItemClassification.progression, 3, [Direction.SOUTH, Direction.EAST]),
    "Phantom Skirt" : ItemData(42, ItemClassification.progression, 4, [Direction.NORTH, Direction.EAST, Direction.WEST]), #TODO might edit later
    "Poopshroom" : ItemData(43, ItemClassification.progression, 4, [Direction.SOUTH]),
    "Watercap" : ItemData(44, ItemClassification.progression, 4, [Direction.EAST]),
    "Kraken Mushroom" : ItemData(45, ItemClassification.progression, 5, [Direction.EAST]),
    "Lust Mushroom" : ItemData(46, ItemClassification.progression, 5, [Direction.SOUTH]),
    "Magma Morel" : ItemData(47, ItemClassification.progression, 5, [Direction.EAST]),
    "Grave Truffle" : ItemData(48, ItemClassification.progression, 6, [Direction.SOUTH, Direction.WEST]), #TODO might edit later
    "Rainbow Cap" : ItemData(49, ItemClassification.progression, 6, [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]),  #Mushroom END #TODO might remove west
    "Cloud Crystal" : ItemData(50, ItemClassification.progression, 2, [Direction.NORTH]), #Mineral Start
    "Earth Pyrite" : ItemData(51, ItemClassification.progression, 2, [Direction.SOUTH]),
    "Frost Sapphire" : ItemData(52, ItemClassification.progression, 2, [Direction.EAST]),
    "Fire Citrine" : ItemData(53, ItemClassification.progression, 2, [Direction.WEST]),
    "Blood Ruby" : ItemData(54, ItemClassification.progression, 3, [Direction.NORTH, Direction.WEST]),
    "Arcane Crystal" : ItemData(55, ItemClassification.progression, 4, [Direction.NORTH, Direction.EAST]),
    "Life Crystal" : ItemData(56, ItemClassification.progression, 5, [Direction.SOUTH, Direction.EAST]),
    "Plague Stibnite" : ItemData(57, ItemClassification.progression, 6, [Direction.SOUTH, Direction.WEST]),
    "Fable Bismuth" : ItemData(58, ItemClassification.progression, 7, [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]), #Mineral END
    #TODO maybe add salts?

}

skills: Dict[str, ItemData] = {
}

keyitems: Dict[str, ItemData] = {
    "progressive alchemy machine" : ItemData(0x0, ItemClassification.useful),
    "progressive garden" : ItemData(0x0, ItemClassification.useful),
    "Talent Points" : ItemData(0x0, ItemClassification.filler),
"Recipe Pages" : ItemData(0x0, ItemClassification.useful),

}


junk_items: Dict[str, ItemData] = {
    "Xp": ItemData(0, ItemClassification.filler),
    "Money": ItemData(0, ItemClassification.filler),
    "Bulk North Ingredient Bundle" : ItemData(0x0, ItemClassification.filler),
}

junk_weights = {
    "Xp": 50,
    "Money": 50,
    "Bulk North Ingredient Bundle": 20
}

full_item_dict: Dict[str, ItemData] = {**ingredients, **skills, **keyitems, **junk_items} #full item dictionary