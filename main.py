from collections import defaultdict
from typing import Dict, List, Optional

from csv import DictReader

from coins import Coin, CoinType, Grade
from pages import Page
from countries import map_to_region_name


def parser(filename: str, exclusions: Dict[str, list]=None) -> Optional[Dict[str, List[Coin]]]:
    """Parse a csv and return a dictionary of all current collections.
    
    Exclusions acts as a filter, where coins whose fields (keys) are of a
    given value (value) are not included in the returned dictionary.
    """

    needed_fields = ["Country", "Issuer", "Face value", "Reference", "N# number (with link)", "Title", "Type", "Composition", "Weight", "Diameter", "Thickness", "Year", "Gregorian year", "Mintmark", "Grade", "Collection", "Public comment"]
    with open(filename, "r") as f:
        reader = DictReader(f)
        # csv is not formatted right
        if [x for x in reader.fieldnames if x in needed_fields] != needed_fields:
            return None
        # parse each line
        my_coins = defaultdict(list)
        for row in reader:
            include = True
            for ex_field in exclusions.keys():
                for ex_value in exclusions[ex_field]:
                    if row[ex_field] == ex_value:
                        include = False
                        break
                if not include:
                    break
            else:
                my_coins[map_to_region_name(row['Country'])].append(Coin(
                    country=row['Country'],
                    issuer=row['Issuer'],
                    face_value=row['Face value'],
                    numista_id=row['N# number (with link)'].split("N# ", 1)[1],
                    title=row['Title'],
                    composition=row['Composition'],
                    weight=row['Weight'],
                    diameter=row['Diameter'],
                    thickness=row['Thickness'],
                    year=row['Year'],
                    reference=row['Reference'],
                    type=CoinType(row['Type']),
                    gregorian_year=row['Gregorian year'],
                    mintmark=row['Mintmark'],
                    grade=Grade(row['Grade']),
                    comment=row['Public comment']
                ))
        return my_coins


def main():
    dont_includes = {
        "Grade": ["UNC"], 
        "Collection": [
            "Uncirculated / Sealed", 
            "Specialized Folder (for circulating coins)", 
            "Quarter Commemorative Book", 
            "Toonie Commemorative Book",
            "Euro Booklet"
        ]
    }
    my_coins = parser("Collections/YaBoiLennyG_coins.csv", dont_includes)

    groups: Dict[str, List[str]] = {
        "Asia / Africa": ["Asia", "Africa"],
        "North America / Oceania": ["North America", "Oceania"],
        "Latin America / East Europe": ["Central America", "Caribbean", "South America", "Eastern Europe"],
        "West Europe": ["Western Europe"]
    }

    my_collections: Dict[str, List[Coin]] = defaultdict(list)
    for group_name, group in groups.items():
        [my_collections[group_name].extend(my_coins[g]) for g in group]

    [print(c.title) for c in my_collections['North America / Oceania']]

    # for region, coin_list in my_coins.items():
    #     print(f"{len(coin_list)}\tCOINS IN {region}")
    # print()
    # print(f"Coins in Europe:\t{len(my_coins['Western Europe']):3}")
    # print(f"Coins in Latin America:\t{len(my_coins['South America']) + len(my_coins['Central America']) + len(my_coins['Caribbean']) + len(my_coins['Eastern Europe']):3}")
    # print(f"Coins in other world:\t{len(my_coins['Africa']) + len(my_coins['Asia']):3}")
    # print(f"Coins in NA + Oceania:\t{len(my_coins['North America']) + len(my_coins['Oceania']):3}")


if __name__ == "__main__":
    main()