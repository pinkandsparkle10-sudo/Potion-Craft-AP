from dataclasses import dataclass
from typing import Dict

from BaseClasses import Item, ItemClassification
from typings.schema import Optional


class PotionCraftItem(Item):
    game: str = "Potion Craft"


@dataclass
class ItemData:
    code: int
    classification: ItemClassification
    amount: Optional[int] = 1

ingredients: Dict[str, ItemData] = {
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