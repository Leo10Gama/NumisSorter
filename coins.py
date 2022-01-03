from dataclasses import dataclass
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
    """A class to encompass a coin in the collection."""
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
    reference: str = ""
    type: CoinType = CoinType.STANDARD
    gregorian_year: int = year
    mintmark: str = ""
    grade: Grade = Grade.NO_GRADE
    comment: str = ""
