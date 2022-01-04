from dataclasses import dataclass, field
from enum import Enum


class CoinType(Enum):
    """An enum to encompass types of coins that may be found in a collection."""

    STANDARD = "Standard circulation coin"
    COMMEMORATIVE = "Circulating commemorative coin"
    NONCIRCULATING = "Non-circulating coin"
    PATTERN = "Pattern"
    TOKEN = "Token"


class Grade(Enum):
    """An enum to encompass the ways a coin can be graded."""

    GOOD = "G"
    VERY_GOOD = "VG"
    FINE = "F"
    VERY_FINE = "VF"
    EXTREMELY_FINE = "XF"
    ALMOST_UNCIRCULATED = "AU"
    UNCIRCULATED = "UNC"
    NO_GRADE = ""


@dataclass(frozen=True)
class Coin:
    """A class to encompass a coin in the collection.
    
    Attributes
    ----------
    country : str
        The country where the coin is used.
    issuer : str
        The region that issued the coin.
    face_value : float
        The decimal value on the face of the coin.
    numista_id : int
        The unique ID of the coin on numista.com.
    title: str
        The name of the coin.
    composition : str
        A description of the metallic content of the coin.
    weight : float
        The weight of the coin, in grams.
    diameter : float
        The diameter of the coin, in millimeters.
    thickness : float
        The thickness of the coin, in millimeters.
    year : int
        The year written on the coin, indicating when it was minted.
    gregorian_year : int
        The gregorian year that the coin was minted, which may differ from 
        `year` based on the calendar system of the region (e.g. Japan, Thailand)
    reference : str = ""
        A reference to a catalogue for which the coin's specifications can be
        found.
    type: CoinType = CoinType.STANDARD
        The type of the coin. (i.e. Standard, Commemorative, Non-circulating, 
        Pattern, or Token)
    mintmark : str = ""
        The mark given to the coin to indicate which facility it was minted in.
    grade : Grade = Grade.NO_GRADE
        The grade of the coin, which ranges from Good, Very Good, Fine, 
        Very Fine, Extremely Fine, Almost Uncirculated, and Uncirculated. An
        option of No Grade is also available.
    comment : str = ""
        The public comment put on the coin.
    """

    country: str
    issuer: str
    face_value: float
    numista_id: int
    title: str
    composition: str
    weight: float
    diameter: float
    thickness: float
    year: int
    gregorian_year: int
    reference: str = ""
    type: CoinType = CoinType.STANDARD
    mintmark: str = ""
    grade: Grade = Grade.NO_GRADE
    comment: str = ""
