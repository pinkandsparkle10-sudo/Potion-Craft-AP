from dataclasses import dataclass

from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionGroup, PerGameCommonOptions

class Goal(Choice):
    """
    Determines the goal of the seed

    Boss Cass Bust-Up: Boss Cass must be beaten-up
    """
    display_name = "Goal"
    option_nigredo: 0
    option_void_salt: 1
    option_albedo: 2
    option_citrinitas: 3
    option_rubedo: 4
    option_philosophers_stone: 5
    default = 0

class IngredientItems(Choice):
    option_vanilla: 0
    option_seed_items : 1
    option_infinite_items: 2
    default = 1


@dataclass
class potion_craft_option_groups(PerGameCommonOptions):
    OptionGroup("Goal Options", [
        Goal,

    ]),
    OptionGroup("Death Link", [
        DeathLink
    ])

@dataclass
class PotionCraftOptions(PerGameCommonOptions):
    goal: Goal


    death_link: DeathLink