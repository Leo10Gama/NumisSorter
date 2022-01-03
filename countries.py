from enum import Enum
from typing import Dict


class Region(Enum):
    """A class to encompass different regions of the world."""

    ASIA = "Asia"
    AFRICA = "Africa"
    NORTH_AMERICA = "North America"
    CENTRAL_AMERICA = "Central America"
    CARRIBEAN = "Caribbean"
    SOUTH_AMERICA = "South America"
    WESTERN_EUROPE = "Western Europe"
    EASTERN_EUROPE = "Eastern Europe"
    OCEANIA = "Oceania"


COUNTRIES: Dict[str, Region] = {
    "Afghanistan": Region.ASIA,
    "Albania": Region.EASTERN_EUROPE,
    "Algeria": Region.AFRICA,
    "Andorra": Region.WESTERN_EUROPE,
    "Angola": Region.AFRICA,
    "Anguilla": Region.CARRIBEAN,
    "Antigua and Barbuda": Region.CARRIBEAN,
    "Argentina": Region.SOUTH_AMERICA,
    "Armenia": Region.ASIA,
    "Aruba": Region.CARRIBEAN,
    "Australia": Region.OCEANIA,
    "Austria": Region.WESTERN_EUROPE,
    "Azerbaijan": Region.ASIA,
    "Bahamas, The": Region.CARRIBEAN,
    "Bahrain": Region.ASIA,
    "Bangladesh": Region.ASIA,
    "Barbados": Region.CARRIBEAN,
    "Belarus": Region.EASTERN_EUROPE,
    "Belgium": Region.WESTERN_EUROPE,
    "Belize": Region.CENTRAL_AMERICA,
    "Benin": Region.AFRICA,
    "Bermuda": Region.CARRIBEAN,
    "Bhutan": Region.ASIA,
    "Bohemia": Region.EASTERN_EUROPE,
    "Bolivia": Region.SOUTH_AMERICA,
    "Bosnia and Herzegovina": Region.EASTERN_EUROPE,
    "Botswana": Region.AFRICA,
    "Brazil": Region.SOUTH_AMERICA,
    "British Virgin Islands": Region.CARRIBEAN,
    "British West Africa": Region.AFRICA,
    "British West Indies": Region.ASIA,
    "Brunei": Region.ASIA,
    "Bulgaria": Region.EASTERN_EUROPE,
    "Burkina Faso": Region.AFRICA,
    "Burundi": Region.AFRICA,
    "Cambodia": Region.ASIA,
    "Cameroon": Region.AFRICA,
    "Canada": Region.NORTH_AMERICA,
    "Cape Verde": Region.AFRICA,
    "Cayman Islands": Region.CARRIBEAN,
    "Central African Republic": Region.AFRICA,
    "Central African States": Region.AFRICA,
    "Central American Republic": Region.CENTRAL_AMERICA,
    "Central Asia and Caucasia": Region.ASIA,
    "Chad": Region.AFRICA,
    "Chile": Region.SOUTH_AMERICA,
    "China": Region.ASIA,
    "Colombia": Region.SOUTH_AMERICA,
    "Comoro Islands": Region.AFRICA,
    "Congo, Democratic Republic of the": Region.AFRICA,
    "Congo, Republic of the": Region.AFRICA,
    "Cook Islands": Region.OCEANIA,
    "Costa Rica": Region.CENTRAL_AMERICA,
    "Croatia": Region.EASTERN_EUROPE,
    "Cuba": Region.CARRIBEAN,
    "Cyprus": Region.EASTERN_EUROPE,
    "Czech Republic": Region.EASTERN_EUROPE,
    "Czechoslovakia": Region.EASTERN_EUROPE,
    "Denmark": Region.WESTERN_EUROPE,
    "Djibouti": Region.AFRICA,
    "Dominica": Region.CARRIBEAN,
    "Dominican Republic": Region.CARRIBEAN,
    "East Africa": Region.AFRICA,
    "Eastern Caribbean States": Region.CARRIBEAN,
    "Ecuador": Region.SOUTH_AMERICA,
    "Egypt": Region.AFRICA,
    "El Salvador": Region.CENTRAL_AMERICA,
    "Equatorial African States": Region.AFRICA,
    "Equatorial Guinea": Region.AFRICA,
    "Eritrea": Region.AFRICA,
    "Estonia": Region.EASTERN_EUROPE,
    "Eswatini": Region.AFRICA,
    "Ethiopia": Region.AFRICA,
    "Falkland Islands": Region.SOUTH_AMERICA,
    "Fiji": Region.OCEANIA,
    "Finland": Region.WESTERN_EUROPE,
    "France": Region.WESTERN_EUROPE,
    "French Equatorial Africa": Region.AFRICA,
    "French Polynesia": Region.OCEANIA,
    "French West Africa": Region.AFRICA,
    "Gabon": Region.AFRICA,
    "Gambia, The": Region.AFRICA,
    "Georgia": Region.ASIA,
    "German East Africa": Region.AFRICA,
    "Germany": Region.WESTERN_EUROPE,
    "Ghana": Region.AFRICA,
    "Gibraltar": Region.WESTERN_EUROPE,
    "Greece": Region.EASTERN_EUROPE,
    "Grenada": Region.CARRIBEAN,
    "Guatemala": Region.CENTRAL_AMERICA,
    "Guernsey": Region.WESTERN_EUROPE,
    "Guinea": Region.AFRICA,
    "Guinea-Bissau": Region.AFRICA,
    "Guyana": Region.SOUTH_AMERICA, 
    "Haiti": Region.CARRIBEAN,
    "Honduras": Region.CENTRAL_AMERICA,
    "Hungary": Region.EASTERN_EUROPE,
    "Iceland": Region.WESTERN_EUROPE,
    "India": Region.ASIA,
    "Indonesia": Region.ASIA,
    "Iran": Region.ASIA,
    "Iraq": Region.ASIA,
    "Ireland": Region.WESTERN_EUROPE,
    "Isle of Man": Region.WESTERN_EUROPE,
    "Israel": Region.ASIA,
    "Italy": Region.WESTERN_EUROPE,
    "Ivory Coast": Region.AFRICA,
    "Jamaica": Region.CARRIBEAN,
    "Japan": Region.ASIA,
    "Jersey": Region.WESTERN_EUROPE,
    "Jordan": Region.ASIA,
    "Kazakhstan": Region.ASIA,
    "Kenya": Region.AFRICA,
    "Kievan Rus": Region.EASTERN_EUROPE,
    "Kiribati": Region.OCEANIA, 
    "Korea": Region.ASIA,
    "Kuwait": Region.ASIA,
    "Kyrgyzstan": Region.ASIA,
    "Laos": Region.ASIA,
    "Latvia": Region.EASTERN_EUROPE,
    "Lebanon": Region.ASIA,
    "Lesotho": Region.AFRICA,
    "Liberia": Region.AFRICA,
    "Libya": Region.AFRICA,
    "Liechtenstein": Region.WESTERN_EUROPE,
    "Lithuania": Region.EASTERN_EUROPE, 
    "Luxembourg": Region.WESTERN_EUROPE,
    "Madagascar": Region.AFRICA,
    "Malawi": Region.AFRICA,
    "Malaysia": Region.ASIA,
    "Maldives": Region.ASIA,
    "Mali": Region.AFRICA,
    "Malta": Region.WESTERN_EUROPE,
    "Malta, Order of": Region.WESTERN_EUROPE,
    "Marshall Islands": Region.OCEANIA,
    "Mauritania": Region.AFRICA, 
    "Mauritius": Region.AFRICA,
    "Mexico": Region.NORTH_AMERICA,
    "Moldova": Region.EASTERN_EUROPE,
    "Monaco": Region.WESTERN_EUROPE,
    "Mongol States": Region.ASIA,
    "Mongolia": Region.ASIA,
    "Montenegro": Region.EASTERN_EUROPE,
    "Montserrat": Region.CARRIBEAN,
    "Morocco": Region.AFRICA,
    "Mozambique": Region.AFRICA, 
    "Myanmar": Region.ASIA,
    "Namibia": Region.AFRICA,
    "Nauru": Region.OCEANIA,
    "Nepal": Region.ASIA,
    "Netherlands": Region.WESTERN_EUROPE,
    "Netherlands Antilles": Region.CARRIBEAN,
    "New Caledonia": Region.OCEANIA,
    "New Zealand": Region.OCEANIA,
    "Nicaragua": Region.CENTRAL_AMERICA,
    "Niger": Region.AFRICA,
    "Nigeria": Region.AFRICA, 
    "Niue": Region.OCEANIA,
    "North Korea": Region.ASIA,
    "North Macedonia": Region.EASTERN_EUROPE,
    "Norway": Region.WESTERN_EUROPE,
    "Oman": Region.ASIA,
    "Ottoman Empire": Region.EASTERN_EUROPE,
    "Pakistan": Region.ASIA,
    "Palau": Region.OCEANIA,
    "Panama": Region.CENTRAL_AMERICA,
    "Papua New Guinea": Region.OCEANIA,
    "Paraguay": Region.SOUTH_AMERICA,
    "Peru": Region.SOUTH_AMERICA,
    "Philippines": Region.ASIA,
    "Pitcairn Islands": Region.OCEANIA,
    "Poland": Region.EASTERN_EUROPE,
    "Portugal": Region.WESTERN_EUROPE,
    "Puerto Rico": Region.CARRIBEAN,
    "Qatar": Region.ASIA,
    "Rhodesia and Nyasaland": Region.AFRICA,
    "Romania": Region.EASTERN_EUROPE,
    "Russia": Region.EASTERN_EUROPE,
    "Rwanda": Region.AFRICA, 
    "Rwanda-Burundi": Region.AFRICA,
    "Saint Barthelemy": Region.CARRIBEAN,
    "Saint Helena, Ascension and Tristan da Cunha": Region.AFRICA,
    "Saint Kitts and Nevis": Region.CARRIBEAN,
    "Saint Lucia": Region.CARRIBEAN,
    "Saint Vincent": Region.CARRIBEAN,
    "Samoa": Region.OCEANIA,
    "San Marino": Region.WESTERN_EUROPE,
    "São Tomé and Príncipe": Region.AFRICA,
    "Saudi Arabia": Region.ASIA,
    "Senegal": Region.AFRICA, 
    "Serbia": Region.EASTERN_EUROPE,
    "Seychelles": Region.AFRICA,
    "Sierra Leone": Region.AFRICA,
    "Singapore": Region.ASIA,
    "Sint Maarten": Region.CARRIBEAN,
    "Slovakia": Region.EASTERN_EUROPE,
    "Slovenia": Region.EASTERN_EUROPE,
    "Solomon Islands": Region.OCEANIA,
    "Somalia": Region.AFRICA,
    "South Africa": Region.AFRICA,
    "South Georgia and the South Sandwich Islands": Region.SOUTH_AMERICA, 
    "South Korea": Region.ASIA,
    "South Sudan": Region.AFRICA,
    "Spain": Region.WESTERN_EUROPE,
    "Sri Lanka": Region.ASIA,
    "Sudan": Region.AFRICA,
    "Suriname": Region.CARRIBEAN,
    "Sweden": Region.WESTERN_EUROPE,
    "Switzerland": Region.WESTERN_EUROPE,
    "Syria": Region.ASIA,
    "Tajikistan": Region.ASIA,
    "Tanzania": Region.AFRICA, 
    "Thailand": Region.ASIA, 
    "Timor-Leste": Region.OCEANIA, 
    "Togo": Region.AFRICA, 
    "Tokelau": Region.OCEANIA, 
    "Tonga": Region.OCEANIA, 
    "Trinidad and Tobago": Region.CARRIBEAN, 
    "Tunisia": Region.AFRICA, 
    "Turkey": Region.EASTERN_EUROPE, 
    "Turkmenistan": Region.ASIA, 
    "Turks and Caicos Islands": Region.CARRIBEAN, 
    "Tuvalu": Region.OCEANIA, 
    "Uganda": Region.AFRICA, 
    "Ukraine": Region.EASTERN_EUROPE, 
    "United Arab Emirates": Region.ASIA, 
    "United Kingdom": Region.WESTERN_EUROPE, 
    "United States": Region.NORTH_AMERICA, 
    "Uruguay": Region.SOUTH_AMERICA, 
    "Uzbekistan": Region.ASIA, 
    "Vanuatu": Region.OCEANIA, 
    "Vatican City": Region.WESTERN_EUROPE,
    "Venezuela": Region.SOUTH_AMERICA, 
    "Vietnam": Region.ASIA, 
    "Western African States": Region.AFRICA, 
    "Windward Islands": Region.CARRIBEAN, 
    "Yemen": Region.ASIA, 
    "Yugoslavia": Region.EASTERN_EUROPE, 
    "Zambia": Region.AFRICA, 
    "Zimbabwe": Region.AFRICA,
    "Abkhazia": Region.ASIA,
    "Artsakh": Region.ASIA,
    "Somaliland": Region.AFRICA,
    "South Ossetia": Region.ASIA,
    "Taiwan": Region.ASIA,
    "Transnistria": Region.ASIA,
    "Western Sahara": Region.AFRICA,
}


def map_to_region_name(country: str) -> str:
    """Return a region that a country belongs to."""
    if country in COUNTRIES:
        return COUNTRIES[country].value
    return ""