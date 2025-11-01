from typing import ClassVar, Dict

from BaseClasses import Tutorial, ItemClassification
from worlds.AutoWorld import WebWorld, World
from worlds.potion_craft.Items import PotionCraftItem, create_potion_craft_items, full_item_dict
from worlds.potion_craft.Locations import create_potion_craft_locations
from worlds.potion_craft.Options import potion_craft_option_groups, PotionCraftOptions
from worlds.potion_craft.Regions import create_potion_craft_regions, connect_potion_craft_regions
from worlds.potion_craft.Rules import set_rules


class PotionCraftWeb(WebWorld):
    theme = "grass"

    setup_en = Tutorial(
        tutorial_name="Multiworld Setup Guide",
        description="A guide to setting up the Potion Craft randomizer connected to an Archipelago Multiworld.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["Pink,FyreDay"]
    )

    tutorials = [setup_en]

class PotionCraftWorld(World):
    """
    Potion Craft is a game that...
    """
    game = "Potion Craft"
    web = PotionCraftWeb()
    options_dataclass = PotionCraftOptions
    options: PotionCraftOptions
    option_groups = potion_craft_option_groups
    item_name_to_id: ClassVar[Dict[str, int]] = {item_name: item_data.code for item_name, item_data in full_item_dict.items()} #needs list of all possible items
    location_name_to_id: ClassVar[Dict[str, int]] = {loc_name: loc_data.code for loc_name, loc_data in full_location_dict.items()} #needs list of all possible locations

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        self.itempool = []
        self.locations = {}

    def generate_early(self) -> None:
        self.locations = create_potion_craft_locations(self)

    def create_regions(self):
        create_potion_craft_regions(self, self.locations)
        connect_potion_craft_regions(self)

    def create_item(self, item: str) -> PotionCraftItem:
        return PotionCraftItem(item, ItemClassification.useful, self.item_name_to_id[item], self.player)

    def create_items(self):
        create_potion_craft_items(self)

    def set_rules(self):
        set_rules(self)

    def fill_slot_data(self) -> id:
        return {
            "ModVersion": "0.6.0"
        }
