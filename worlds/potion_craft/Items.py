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