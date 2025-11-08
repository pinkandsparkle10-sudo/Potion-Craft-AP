from typing import NamedTuple, Optional, Dict

from BaseClasses import Location
from worlds.potion_craft.Items import potion_effects


class PotionCraftLocation(Location):
    game: str = "Potion Craft"

class LocData(NamedTuple):
    code: Optional[int]
    region: Optional[str]

starting_potion_id = 1000

def get_tier3_potion_locs():
    tier3_dict: Dict[str, LocData] = {}
    index = 0

    for key,value in potion_effects.items():
        tier3_dict[key] = LocData(starting_potion_id + index, f"Chapter {value.chapter} Goals")
        index += 1
    return tier3_dict


def create_potion_craft_locations(world):
    print("Create a Dict[str, LocData] and return it here!")
    return get_all_potion_craft_locations()

def get_all_potion_craft_locations():
    locations = {**Chapter1_dict,**Chapter2_dict,**Chapter3_dict,**Chapter4_dict,
                 **Chapter5_dict,**Chapter6_dict,**Chapter7_dict,**Chapter8_dict,**Chapter9_dict,**Chapter10_dict}
    locations.update(get_tier3_potion_locs())
    return locations

Chapter1_dict: Dict[str, LocData] = {
    "Grab an ingredient from Inventory": LocData(1, "Chapter 1 Goals"),
    "Grind an Ingredient": LocData(None, "Chapter 1 Goals"),
    "Toss Ingredient in Cauldron": LocData(3, "Chapter 1 Goals"),
    "Stir Cauldron": LocData(4, "Chapter 1 Goals"),
    "Heat Cauldron": LocData(5, "Chapter 1 Goals"),
    "Craft a Potion": LocData(6, "Chapter 1 Goals"),
    "Go to Garden": LocData(7, "Chapter 1 Goals"),
    "Gather Ingredients": LocData(8, "Chapter 1 Goals"),
    "Go to Shop": LocData(9, "Chapter 1 Goals"),
    "Sell a Potion": LocData(10, "Chapter 1 Goals"),
    "Buy From Merchant": LocData(11, "Chapter 1 Goals"),
    "Collect Small Experience": LocData(12, "Chapter 1 Goals"),
    "Learn New Talent": LocData(13, "Chapter 1 Goals"),
    "Go to Basement": LocData(14, "Chapter 1 Goals"),
    "Go to Bedroom": LocData(15, "Chapter 1 Goals"),
    "Start a New Day": LocData(16, "Chapter 1 Goals"),
    "Reach Popularity Level 2": LocData(17, "Chapter 1 Goals"),
    "Create Potion of Healing": LocData(18, "Chapter 1 Goals"),
    "Create Potion of Poisoning": LocData(19, "Chapter 1 Goals"),
    "Create Potion of Fire": LocData(20, "Chapter 1 Goals"),
    "Create Potion of Frost": LocData(21, "Chapter 1 Goals"),
}
Chapter2_dict: Dict[str, LocData] = {
    "Use Water": LocData(22, "Chapter 2 Goals"),
    "Create a Tier 2 Or Higher Potion": LocData(23, "Chapter 2 Goals"),
    "Create a Potion with 2 different effects": LocData(24, "Chapter 2 Goals"),
    "Save a New Recipe" : LocData(25, "Chapter 2 Goals"),
    "Brew a Potion From Recipe Book" : LocData(26, "Chapter 2 Goals"),
    "Haggle For a Better Deal" : LocData(27, "Chapter 2 Goals"),
    "Reach a Popularity Level Of 4" : LocData(28, "Chapter 2 Goals"),
    "Collect small experience on the Alchemy Map" : LocData(29, "Chapter 2 Goals"),
    "Create Potion of Explosion" : LocData(30, "Chapter 2 Goals"),
    "Create Potion of Wild Growth" : LocData(31, "Chapter 2 Goals"),
    "Create Potion of Strength" : LocData(32, "Chapter 2 Goals"),
    "Create Potion of Dexterity" : LocData(33, "Chapter 2 Goals"),
    "Create Potion of Swiftness" : LocData(34, "Chapter 2 Goals"),
}
Chapter3_dict: Dict[str, LocData] = {
    "Repair the Alchemy Machine" : LocData(35, "Chapter 3 Goals"),
    "Buy a page for the Recipe Book" : LocData(36, "Chapter 3 Goals"),
    "Create a potion with effect of tier 3" : LocData(37, "Chapter 3 Goals"),
    "Create a potion with 3 different effects" : LocData(38, "Chapter 3 Goals"),
    "Collect medium experience book on the Alchemy Map (3 book icon)": LocData(39, "Chapter 3 Goals"),
    "Reach a popularity level of 5" : LocData(40, "Chapter 3 Goals"),
    "Create a potion with custom appearance or name" : LocData(41, "Chapter 3 Goals"),
    "Create Potion of Lightning" : LocData(42, "Chapter 3 Goals"),
    "Create Potion of Mana" : LocData(43, "Chapter 3 Goals"),
    "Create Potion of Stone Skin" : LocData(44, "Chapter 3 Goals"),
    "Create Potion of Sleep" : LocData(45, "Chapter 3 Goals"),
    "Create Potion of Light" : LocData(46, "Chapter 3 Goals"),

}

Chapter4_dict: Dict[str, LocData] = {
    "Create Nigredo": LocData(47, "Chapter 4 Goals"),
    "Create a Potion with 4 different Effects": LocData(48, "Chapter 4 Goals"),
    "Reach Popularity 6": LocData(49, "Chapter 4 Goals"),
    "Collect Big Experience": LocData(50, "Chapter 4 Goals"),
    "Create Potion of Charm": LocData(51, "Chapter 4 Goals"),
    "Create Potion of Slowness": LocData(52, "Chapter 4 Goals"),
    "Create Potion of Rage": LocData(53, "Chapter 4 Goals"),
    "Create Potion of Magical Vision": LocData(54, "Chapter 4 Goals"),

}
Chapter5_dict: Dict[str, LocData] = {
    "Buy Basic Alchemy Machine Upgrade": LocData(55, "Chapter 5 Goals"),
    "Buy Void Salt Recipe": LocData(56, "Chapter 5 Goals"),
    "Create Void Salt": LocData(57, "Chapter 5 Goals"),
    "Create a potion with 5 different effects": LocData(58, "Chapter 5 Goals"),
    "Collect Very Big Experience": LocData(59, "Chapter 5 Goals"),
    "Reach Popularity 7": LocData(60, "Chapter 5 Goals"),
    "Create Potion of Acid": LocData(61, "Chapter 5 Goals"),
    "Create Potion of Libido": LocData(62, "Chapter 5 Goals"),
    "Create Potion of Invisibility": LocData(63, "Chapter 5 Goals"),
    "Create Potion of Levitation": LocData(64, "Chapter 5 Goals"),
    "Create Potion of Necromancy": LocData(65, "Chapter 5 Goals"),
}
Chapter6_dict: Dict[str, LocData] = {
    "Buy Potion Base: Oil": LocData(66, "Chapter 6 Goals"),
    "Create Albedo": LocData(67, "Chapter 6 Goals"),
    "Reach a popularity level of 8": LocData(68, "Chapter 6 Goals"),
    "Create Potion of Poison Protection": LocData(69, "Chapter 6 Goals"),
    "Create Potion of Lightning Protection": LocData(70, "Chapter 6 Goals"),
    "Create Potion of Fire Protection": LocData(71, "Chapter 6 Goals"),
    "Create Potion of Frost Protection": LocData(72, "Chapter 6 Goals"),
    "Create Potion of Gluing": LocData(73, "Chapter 6 Goals"),
    "Create Potion of Slipperiness": LocData(74, "Chapter 6 Goals"),
    "Create Potion of Stench": LocData(75, "Chapter 6 Goals"),
}
Chapter7_dict: Dict[str, LocData] = {
    "Buy Advanced Alchemy Machine": LocData(76, "Chapter 7 Goals"),
    "Buy the Moon Salt Recipe": LocData(77, "Chapter 7 Goals"),
    "Create Moon Salt": LocData(78, "Chapter 7 Goals"),
    "Reach a popularity level of 9": LocData(79, "Chapter 7 Goals"),
    "Create Potion of Acid Protection": LocData(80, "Chapter 7 Goals"),
    "Create Potion of Anti-Magic": LocData(81, "Chapter 7 Goals"),
    "Create Potion of Shrinking": LocData(82, "Chapter 7 Goals"),
    "Create Potion of Enlargement": LocData(83, "Chapter 7 Goals"),
    "Create Potion of Rejuvenation": LocData(84, "Chapter 7 Goals"),
}
Chapter8_dict: Dict[str, LocData] = {
    "Create Citrinitas": LocData(85, "Chapter 8 Goals"),
    "Reach Popularity level 10": LocData(86, "Chapter 8 Goals"),
    "Create Potion of Inspiration": LocData(87, "Chapter 8 Goals"),
    "Create Potion of Fragrance": LocData(88, "Chapter 8 Goals"),
    "Create Potion of Fear": LocData(89, "Chapter 8 Goals"),
}
Chapter9_dict: Dict[str, LocData] = {
    "Buy the Sun Salt recipe": LocData(90, "Chapter 9 Goals"),
    "Create Sun Salt": LocData(91, "Chapter 9 Goals"),
    "Create Rubedo": LocData(92, "Chapter 9 Goals"),
    "Reach a popularity level of 12": LocData(93, "Chapter 9 Goals"),
    "Create Potion of Hallucinations": LocData(94, "Chapter 9 Goals"),
    "Create Potion of Luck": LocData(95, "Chapter 9 Goals"),
    "Create Potion of Curse": LocData(96, "Chapter 9 Goals"),
}
Chapter10_dict: Dict[str, LocData] = {
    "Create Philosopher's Stone": LocData(97, "Chapter 10 Goals"),
    "Buy the Life Salt recipe" : LocData(98, "Chapter 10 Goals"),
    "Create Life Salt": LocData(99, "Chapter 10 Goals"),
    "Buy the Philosopher's Salt recipe": LocData(100, "Chapter 10 Goals"),
    "Create Philosopher's Salt": LocData(101, "Chapter 10 Goals"),
    "Reach a popularity level of 15": LocData(102, "Chapter 10 Goals"),
}