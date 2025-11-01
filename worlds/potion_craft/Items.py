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
    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))

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
    "Featherbloom" : ItemData(13, ItemClassification.progression, 3),
    "Druid's Rosemary" : ItemData(14, ItemClassification.progression, 3),
    "Dream Beet" : ItemData(15, ItemClassification.progression, 3),
    "Bloodthorn" : ItemData(16, ItemClassification.progression, 3),
    "Whirlweed" : ItemData(17, ItemClassification.progression, 4),
    "Thornstick" : ItemData(18, ItemClassification.progression, 4),
    "Grasping Root" : ItemData(19, ItemClassification.progression, 4),
    "Flameweed" : ItemData(20, ItemClassification.progression, 4),
    "Coldleaf" : ItemData(21, ItemClassification.progression, 4),
    "Spellbloom" : ItemData(22, ItemClassification.progression, 5),
    "Healer's Heather" : ItemData(23, ItemClassification.progression, 5),
    "Fluffbloom" : ItemData(24, ItemClassification.progression, 5),
    "Dragon Pepper" : ItemData(25, ItemClassification.progression, 5),
    "Boombloom" : ItemData(26, ItemClassification.progression, 5),
    "Terror Bud" : ItemData(27, ItemClassification.progression, 6),
    "Mageberry" : ItemData(28, ItemClassification.progression, 6),
    "Evergreen Fern" : ItemData(29, ItemClassification.progression, 6), #Herb End
    "Dryad's Saddle" : ItemData(30, ItemClassification.progression, 1), #Mushroom Start
    "Mad Mushroom" : ItemData(31, ItemClassification.progression, 1),
    "Marshroom" : ItemData(32, ItemClassification.progression, 1),
    "Mudshroom" : ItemData(33, ItemClassification.progression, 1),
    "Stink Mushroom" : ItemData(34, ItemClassification.progression, 1),
    "Sulphur Shelf" : ItemData(35, ItemClassification.progression, 1),
    "Witch Mushroom" : ItemData(36, ItemClassification.progression, 1),
    "Shadow Chanterelle" : ItemData(37, ItemClassification.progression, 2),
    "Weirdshroom" : ItemData(38, ItemClassification.progression, 2),
    "Foggy Parasol" : ItemData(39, ItemClassification.progression, 3),
    "Goblin Shroom" : ItemData(40, ItemClassification.progression, 3),
    "Moss Shroom" : ItemData(41, ItemClassification.progression, 3),
    "Phantom Skirt" : ItemData(42, ItemClassification.progression, 4),
    "Poopshroom" : ItemData(43, ItemClassification.progression, 4),
    ""
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

full_item_dict: Dict[str, ItemData] = {**ingredients, **skills, **keyitems, **junk_items}