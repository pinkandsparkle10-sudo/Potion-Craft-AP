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

keyitems: Dict[str, ItemData] = {
    "progressive alchemy machine" : ItemData(0x0, ItemClassification.useful),
    "progressive garden" : ItemData(0x0, ItemClassification.useful),
    "Talent Points" : ItemData(0x0, ItemClassification.useful),
}

filleritems: Dict[str, ItemData] = {
    "Recipe Pages" : ItemData(0x0, ItemClassification.useful),
    "Bulk Ingredient" : ItemData(0x0, ItemClassification.useful),
}