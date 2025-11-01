from BaseClasses import Location, Region, Entrance


def create_location(world, region, name: str, code: int):
    location = Location(world.player, name, code, region)
    region.locations.append(location)

def create_locations(world, region, loc_dict):
    for (key, data) in loc_dict.items():
        if data.region != region.name:
            continue
        create_location(world, region, key, data.code)




def create_region(world, name: str, location_dict):
    region = Region(name, world.player, world.multiworld)
    create_locations(world, region, location_dict)
    world.multiworld.regions.append(region)
    return region

def create_potion_craft_regions(world, location_dict):
    print("create regions!")
    create_region(world, "Menu", location_dict)
    create_region(world, "Chapter 1", location_dict)


def connect_regions(world, from_name: str, to_name: str, entrance_name: str, entrance_group = 0) -> Entrance:
    entrance_region = world.get_region(from_name)
    exit_region = world.get_region(to_name)
    entrance = entrance_region.connect(exit_region, entrance_name)
    entrance.randomization_group = entrance_group
    return entrance

def connect_potion_craft_regions(world):
    print("Connect the regions!")
    connect_regions(world, "Menu", "Chapter 1", "Start")