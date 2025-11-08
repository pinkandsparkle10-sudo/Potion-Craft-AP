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
    create_region(world, "Chapter 1 Goals", location_dict)
    create_region(world, "Chapter 2 Goals", location_dict)
    create_region(world, "Chapter 3 Goals", location_dict)
    create_region(world, "Chapter 4 Goals", location_dict)
    create_region(world, "Chapter 5 Goals", location_dict)
    create_region(world, "Chapter 6 Goals", location_dict)
    create_region(world, "Chapter 7 Goals", location_dict)
    create_region(world, "Chapter 8 Goals", location_dict)
    create_region(world, "Chapter 9 Goals", location_dict)
    create_region(world, "Chapter 10 Goals", location_dict)

    create_region(world, "Chapter 1", location_dict)
    create_region(world, "Chapter 2", location_dict)
    create_region(world, "Chapter 3", location_dict)
    create_region(world, "Chapter 4", location_dict)
    create_region(world, "Chapter 5", location_dict)
    create_region(world, "Chapter 6", location_dict)
    create_region(world, "Chapter 7", location_dict)
    create_region(world, "Chapter 8", location_dict)
    create_region(world, "Chapter 9", location_dict)
    create_region(world, "Chapter 10", location_dict)


def connect_regions(world, from_name: str, to_name: str, entrance_name: str, entrance_group = 0) -> Entrance:
    entrance_region = world.get_region(from_name)
    exit_region = world.get_region(to_name)
    entrance = entrance_region.connect(exit_region, entrance_name)
    entrance.randomization_group = entrance_group
    return entrance

def connect_potion_craft_regions(world):
    print("Connect the regions!")
    connect_regions(world, "Menu", "Chapter 1 Goals", "Goals")
    connect_regions(world, "Chapter 1 Goals", "Chapter 2 Goals", "Goals 1")
    connect_regions(world, "Chapter 2 Goals", "Chapter 3 Goals", "Goals 2")
    connect_regions(world, "Chapter 3 Goals", "Chapter 4 Goals", "Goals 3")
    connect_regions(world, "Chapter 4 Goals", "Chapter 5 Goals", "Goals 4")
    connect_regions(world, "Chapter 5 Goals", "Chapter 6 Goals", "Goals 5")
    connect_regions(world, "Chapter 6 Goals", "Chapter 7 Goals", "Goals 6")
    connect_regions(world, "Chapter 7 Goals", "Chapter 8 Goals", "Goals 7")
    connect_regions(world, "Chapter 8 Goals", "Chapter 9 Goals", "Goals 8")
    connect_regions(world, "Chapter 9 Goals", "Chapter 10 Goals", "Goals 9")

    connect_regions(world, "Menu", "Chapter 1", "Start")
    connect_regions(world, "Chapter 1", "Chapter 2", "Chapter 1 Complete")
    connect_regions(world, "Chapter 2", "Chapter 3", "Chapter 2 Complete")
    connect_regions(world, "Chapter 3", "Chapter 4", "Chapter 3 Complete")
    connect_regions(world, "Chapter 4", "Chapter 5", "Chapter 4 Complete")
    connect_regions(world, "Chapter 5", "Chapter 6", "Chapter 5 Complete")
    connect_regions(world, "Chapter 6", "Chapter 7", "Chapter 6 Complete")
    connect_regions(world, "Chapter 7", "Chapter 8", "Chapter 7 Complete")
    connect_regions(world, "Chapter 8", "Chapter 9", "Chapter 8 Complete")
    connect_regions(world, "Chapter 9", "Chapter 10", "Chapter 9 Complete")