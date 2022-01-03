from collections import defaultdict
from typing import Dict, List, Optional

from csv import DictReader

from coins import Coin
from pages import Page
from countries import map_to_region_name


def parser(filename: str) -> Optional[Dict[str, List[Coin]]]:
    """Parse a csv and return a dictionary of all current collections."""
    needed_fields = ["Country", "Issuer", "Face value", "Reference", "N# number (with link)", "Title", "Composition", "Weight", "Diameter", "Thickness", "Year", "Collection"]
    with open(filename, "r") as f:
        reader = DictReader(f)
        if not all(x in needed_fields for x in reader.fieldnames):
            return None


def main():
    pass


if __name__ == "__main__":
    main()