from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from coins import Coin


@dataclass
class Slot:
    """A class to represent a slot in a page."""
    capacity: int
    max_diameter: float
    coins: List[Coin] = field(default_factory=list)
    
    def __post_init__(self):
        self.coins = list([None for _ in range(self.capacity)])


@dataclass
class Page:
    """A class to represent a page in a book."""
    name: str
    slots: List[Slot]


def get_page(name: str) -> Optional[Page]:
    """Retrieve a potential page based on its name."""
    if name == "NUMIS 44":
        return Page(name, [Slot(4, 44) for _ in range(3)])
    if name == "NUMIS 34":
        return Page(name, [Slot(10, 34) for _ in range(2)])
    if name == "NUMIS 25":
        return Page(name, [Slot(12, 25), Slot(6, 25), Slot(12, 25)])
    if name == "NUMIS 17":
        return Page(name, [Slot(16, 17) for _ in range(3)])
    if name == "NUMIS MIX":
        return Page(name, [Slot(5, 34), Slot(12, 25), Slot(16, 17)])
    return None
