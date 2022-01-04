from dataclasses import dataclass, field
from typing import List, Optional

from coins import Coin


class SlotFullException(Exception):
    """Raised when trying to add a Coin to a full Slot."""
    pass


class SlotEmptyException(Exception):
    """Raised when trying to remove a Coin from an empty Slot."""
    pass


@dataclass
class Slot:
    """A class to represent a slot in a page.
    
    Attributes
    ----------
    capacity : int
        The number of pockets in the Slot.
    max_diameter : float
        The maximum diameter able to be contained by the pocket,
        in millimeters.
    coins : List[Coin] = field(default_factory=list)
        The list of Coins being held in the Slot. Initialized to a list of 
        size `capacity`, filled with `None` objects.
    """

    capacity: int
    max_diameter: float
    coins: List[Coin] = field(default_factory=list)
    
    def __post_init__(self):
        self.coins = list([None for _ in range(self.capacity)])

    def is_full(self) -> bool:
        """Return whether or not all spaces of the Slot are filled."""

        return len([x for x in self.coins if x is not None]) == self.capacity


    def is_empty(self) -> bool:
        """Return whether or not none of the Slot's spaces are filled."""

        return len([x for x in self.coins if x is not None]) == 0


    def push_coin(self, c: Coin) -> None:
        """Insert a coin into the first available pocket of the Slot."""

        if self.is_full():
            raise SlotFullException(f"Cannot add Coin '{c.title}' to a full Slot.")
        if c.diameter > self.max_diameter:
            raise ValueError(f"Cannot insert a Coin larger than {self.max_diameter}mm to this Slot (passed Coin is {c.diameter}mm)")

        for i in range(self.capacity):
            if self.coins[i] is None:
                self.coins[i] = c
                return
        else:
            raise RuntimeError(f"Coin '{c.title}' could not be inserted.")


    def pop_coin(self, index: int=-1) -> Coin:
        """Remove the last coin from the Slot."""

        if self.is_empty():
            raise SlotEmptyException(f"Cannot remove a Coin from an empty Slot.")
        if index >= self.capacity:
            raise IndexError(f"Index {index} out of range for Slot of size {self.capacity}.")

        if index == -1:
            for i in reversed(range(self.capacity)):
                if self.coins[i] is not None:
                    c = self.coins[i]
                    self.coins[i] = None
                    return c
        else:
            if self.coins[index] is not None:
                c = self.coins[index]
                self.coins[index] = None
                return c
        raise RuntimeError(f"Coin could not be removed.")


@dataclass
class Page:
    """A class to represent a page in a book.
    
    Attributes
    ----------
    name : str
        The name of the page, as provided by Lighthouse Canada's NUMIS coin 
        pages. Currently varies of values NUMIS 44, NUMIS 34, NUMIS 25, 
        NUMIS 17, and NUMIS MIX (which are the ones I currently own).
    slots : List[Slot]
        The Slots in the Page, which varies depending on the page.
    """

    name: str
    slots: List[Slot]


    def is_full(self) -> bool:
        """Return whether or not all the Page's Slots are filled."""

        return all([s.is_full() for s in self.slots])

    
    def is_empty(self) -> bool:
        """Return whether none of the Page's Slots have coins."""

        return all([s.is_empty() for s in self.slots])


    def push_coin(self, c: Coin) -> None:
        """Insert a Coin into the first available slot on the page."""

        if self.is_full():
            raise SlotFullException(f"Cannot add Coin '{c.title}' to a full Page.")

        for slot in self.slots:
            if slot.is_full():
                continue
            try:
                slot.push_coin(c)
                return
            except ValueError:  # The coin was too large
                pass
        else:
            raise RuntimeError(f"Coin '{c.title}' could not be inserted.")

            
    def pop_coin(self, slot_index: int=-1, coin_index: int=-1) -> Coin:
        """Remove and return the last Coin.
        
        `slot_index` relates to which slot to select a coin from, while 
        `coin_index` indicates the position of the coin in that Slot.
        """

        if self.is_empty():
            raise SlotEmptyException(f"Cannot remove a Coin from an empty Page.")
        if slot_index >= len(self.slots):
            raise IndexError(f"Index {slot_index} out of range for Page with {len(self.slots)} Slots.")
        if slot_index > -1 and coin_index >= self.slots[slot_index].capacity:
            raise IndexError(f"Index {coin_index} out of range for Slot {slot_index} of size {self.slots[slot_index].capacity}.")

        if slot_index == -1:        # Remove from first available Slot
            if coin_index == -1:    # Remove first available Coin
                for slot in reversed(self.slots):
                    if slot.is_empty():
                        continue
                    try:
                        c = slot.pop_coin()
                        return c
                    except IndexError:
                        pass
        else:                       # Remove specific coin
            return self.slots[slot_index].pop_coin(coin_index)


    def get_coin(self, index: int) -> Coin:
        """Return a coin at a given position."""

        counter = 0
        for slot in self.slots:
            if index < slot.capacity:
                return slot.coins[index - counter]
            else:
                counter = slot.capacity
        else:
            raise IndexError(f"Index {index} out of range for Page of size {sum([len(x) for x in self.slots])}.")


    def get_coins(self) -> List[Coin]:
        """Return a list of all Coins on a given page."""

        coins = []
        for slot in self.slots:
            coins.extend(slot.coins)
        return coins


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
