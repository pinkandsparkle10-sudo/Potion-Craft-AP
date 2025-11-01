from BaseClasses import ItemClassification
from worlds.potion_craft.Items import PotionCraftItem


def get_rules(world):
    rules = {
        "locations": {
            "Alchemy Wizard Shop Check1": lambda state: #example Location rule on a location name
                state.has("Alchemy Wizard Summon", world.player) and state.has("Waterbloom", world.player), #THIS IS AN ITEM NAME
        },
        "entrances": {
            "Start": lambda state: #Example entrance rule on an entrance name
            state.has("Waterbloom", world.player),#THIS IS AN ITEM NAME
        }
    }
    return rules

def set_rules(world):

    rules_lookup = get_rules(world)

    for entrance_name, rule in rules_lookup["entrances"].items():
        try:
            world.get_entrance(entrance_name).access_rule = rule
        except KeyError as e:
            print(f"Key error, {e}")
            pass

    for location_name, rule in rules_lookup["locations"].items():
        try:
            world.get_location(location_name).access_rule = rule
        except KeyError as e:
            print(f"Key error, {e}")
            pass

    #Set our goal to be at completing the "Chapter 3" Location
    world.multiworld.get_location(f"Chapter 3", world.player).place_locked_item(
        PotionCraftItem("Victory", ItemClassification.progression, None, world.player))
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)