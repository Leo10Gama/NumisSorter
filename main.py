from collections import defaultdict
from typing import Dict, List, Optional

from csv import DictReader

from coins import Coin, CoinType, Grade
from pages import Page, create_book
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
                    face_value=float(row['Face value']),
                    numista_id=int(row['N# number (with link)'].split("N# ", 1)[1]),
                    title=row['Title'],
                    composition=row['Composition'],
                    weight=float(row['Weight']),
                    diameter=float(row['Diameter']),
                    thickness=float(row['Thickness']) if row['Thickness'] else None,
                    year=int(row['Year']) if row['Year'] else -1,
                    reference=row['Reference'],
                    type=CoinType(row['Type']),
                    gregorian_year=int(row['Gregorian year']),
                    mintmark=row['Mintmark'],
                    grade=Grade(row['Grade']),
                    comment=row['Public comment']
                ))
        return my_coins


def main():
    dont_includes = {
        "Grade": ["UNC"], 
        "Composition": ["Gold (.900)"],
        "Collection": [
            "Uncirculated / Sealed", 
            "Specialized Folder (for circulating coins)", 
            "Quarter Commemorative Book", 
            "Toonie Commemorative Book",
            "Euro Booklet"
        ]
    }
    my_coins = parser("Collections/YaBoiLennyG_coins.csv", dont_includes)

    # Group coins based on how I want my books
    groups: Dict[str, List[str]] = {
        "Asia / Africa": ["Asia", "Africa"],
        "North America / Oceania": ["North America", "Oceania"],
        "Latin America / Eastern Europe": ["Central America", "Caribbean", "South America", "Eastern Europe"],
        "Western Europe": ["Western Europe"]
    }

    # Put all the region coins in a list per book (my_collections)
    my_collections: Dict[str, List[Coin]] = defaultdict(list)
    for group_name, group in groups.items():
        [my_collections[group_name].extend(my_coins[g]) for g in group]

    group_nums = {
        0: "Asia / Africa",
        1: "North America / Oceania",
        2: "Latin America / Eastern Europe",
        3: "Western Europe"
    }

    # The actual algorithm to put the coins into pages
    books: Dict[str, List[Page]] = defaultdict(list)
    for book, coins in my_collections.items():
        print(book)
        books[book] = create_book(coins)
        print(f"Total pages: {len(books[book])}\n{[len(p) for p in books[book]]}\n")

    option = ""
    while option != "q":
        print("Select book:\n")
        for i, book in enumerate(books):
            print(f"({i}) {book}")
        print()
        print(f"(p) Total Pages")
        print(f"(q) Quit\n")
        option = input().strip().lower()
        if option.isnumeric() and int(option) < len(books):
            option = int(option)
            cursor = 0
            while cursor != -1:
                print()
                my_page = books[group_nums[option]][cursor]
                print(f"PAGE: {my_page.name}\n")
                for coin in my_page.get_coins():
                    print(f"({coin.year:4}, {coin.issuer})\t{coin.title}")
                print("\n(n) Next\n(p) Previous\n(q) Quit\n")
                selection = input().strip().lower()
                if selection == "n" and cursor + 1 < len(books[group_nums[option]]):
                    cursor += 1
                elif selection == "p" and cursor > 0:
                    cursor -= 1
                elif selection == "q":
                    cursor = -1
        elif option == "q":
            exit()
        elif option == "p":
            my_pages = defaultdict(int)
            for book in books.values():
                for page in book:
                    my_pages[page.name] += 1
            print("\nTotals for each page:")
            [print(f"{n}:\t{total:2}") for n, total in my_pages.items()]
            print()
        else:
            print(f"\nInvalid input '{option}'\n")


if __name__ == "__main__":
    main()