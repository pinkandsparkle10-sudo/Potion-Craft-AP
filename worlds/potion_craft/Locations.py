from typing import NamedTuple, Optional, Dict

from BaseClasses import Location


class PotionCraftLocation(Location):
    game: str = "Potion Craft"

class LocData(NamedTuple):
    code: Optional[int]
    region: Optional[str]
    id: Optional[int] = -1



race_dict: Dict[str, LocData] = {
    "Refinery Run": LocData(0x6d000007, "SR - Refinery Run", 7),
}