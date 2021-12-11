from enum import Enum


class Colors(Enum):
    Black = 'Color-Black'
    Blue = 'Color-Blue'
    Brown = 'Color-Brown'
    Green = 'Color-Green'
    Grey = 'Color-Grey'
    Orange = 'Color-Orange'
    Pink = 'Color-Pink'
    Purple = 'Color-Purple'
    Red = 'Color-Red'
    White = 'Color-White'
    Yellow = 'Color-Yellow'
    Mixture = 'Color-Mixture'
    Other = 'Color-Other'


class AttributeName(Enum):
    Gender_Female = 'Gender-Female'

    UpperBody_Length_Short = 'UpperBody-Length-Short'

    UpperBody_Color_Black = 'UpperBody-Color-Black'
    UpperBody_Color_Blue = 'UpperBody-Color-Blue'
    UpperBody_Color_Brown = 'UpperBody-Color-Brown'
    UpperBody_Color_Green = 'UpperBody-Color-Green'
    UpperBody_Color_Grey = 'UpperBody-Color-Grey'
    UpperBody_Color_Orange = 'UpperBody-Color-Orange'
    UpperBody_Color_Pink = 'UpperBody-Color-Pink'
    UpperBody_Color_Purple = 'UpperBody-Color-Purple'
    UpperBody_Color_Red = 'UpperBody-Color-Red'
    UpperBody_Color_White = 'UpperBody-Color-White'
    UpperBody_Color_Yellow = 'UpperBody-Color-Yellow'
    UpperBody_Color_Mixture = 'UpperBody-Color-Mixture'
    UpperBody_Color_Other = 'UpperBody-Color-Other'

    LowerBody_Length_Short = 'LowerBody-Length-Short'

    LowerBody_Color_Black = 'LowerBody-Color-Black'
    LowerBody_Color_Blue = 'LowerBody-Color-Blue'
    LowerBody_Color_Brown = 'LowerBody-Color-Brown'
    LowerBody_Color_Green = 'LowerBody-Color-Green'
    LowerBody_Color_Grey = 'LowerBody-Color-Grey'
    LowerBody_Color_Orange = 'LowerBody-Color-Orange'
    LowerBody_Color_Pink = 'LowerBody-Color-Pink'
    LowerBody_Color_Purple = 'LowerBody-Color-Purple'
    LowerBody_Color_Red = 'LowerBody-Color-Red'
    LowerBody_Color_White = 'LowerBody-Color-White'
    LowerBody_Color_Yellow = 'LowerBody-Color-Yellow'
    LowerBody_Color_Mixture = 'LowerBody-Color-Mixture'
    LowerBody_Color_Other = 'LowerBody-Color-Other'

    Accessory_Backpack = 'Accessory-Backpack'


upper_body_part_to_color = {
    AttributeName.UpperBody_Color_Black: Colors.Black,
    AttributeName.UpperBody_Color_Blue: Colors.Blue,
    AttributeName.UpperBody_Color_Brown: Colors.Brown,
    AttributeName.UpperBody_Color_Green: Colors.Green,
    AttributeName.UpperBody_Color_Grey: Colors.Grey,
    AttributeName.UpperBody_Color_Orange: Colors.Orange,
    AttributeName.UpperBody_Color_Pink: Colors.Pink,
    AttributeName.UpperBody_Color_Purple: Colors.Purple,
    AttributeName.UpperBody_Color_Red: Colors.Red,
    AttributeName.UpperBody_Color_White: Colors.White,
    AttributeName.UpperBody_Color_Yellow: Colors.Yellow,
    AttributeName.UpperBody_Color_Mixture: Colors.Mixture,
    AttributeName.UpperBody_Color_Other: Colors.Other,
}
lower_body_part_to_color = {
    AttributeName.LowerBody_Color_Black: Colors.Black,
    AttributeName.LowerBody_Color_Blue: Colors.Blue,
    AttributeName.LowerBody_Color_Brown: Colors.Brown,
    AttributeName.LowerBody_Color_Green: Colors.Green,
    AttributeName.LowerBody_Color_Grey: Colors.Grey,
    AttributeName.LowerBody_Color_Orange: Colors.Orange,
    AttributeName.LowerBody_Color_Pink: Colors.Pink,
    AttributeName.LowerBody_Color_Purple: Colors.Purple,
    AttributeName.LowerBody_Color_Red: Colors.Red,
    AttributeName.LowerBody_Color_White: Colors.White,
    AttributeName.LowerBody_Color_Yellow: Colors.Yellow,
    AttributeName.LowerBody_Color_Mixture: Colors.Mixture,
    AttributeName.LowerBody_Color_Other: Colors.Other,
}


class Part(Enum):
    UpperBody = "Part_UpperBody"
    LowerBody = "Part_LowerBody"
    Backpack = "Part_Backpack"


attribute_keyword_lookup = {
    "Gender_Female": ["she", "her", "women", "girl", "lady", "female", "dame", "bimbo", "chick", "baroness", "contessa", "mother", "mistress"],
    "Gender_Male": ["he", "him", "male", 'man', "guy", "boy", "dude", "fellow", "gentleman", "lad"],
    Part.UpperBody.value: ['suit', "shirt", "t-shirt", "top", "blouse", "jacket", "hoodie", "blazer", "sweater", "jumper", "vest", "coat", "raincoat", "sweatshirt", "swimsuit", "pullover", "dress"],
    Part.LowerBody.value: ['jeans', 'pant', 'pants', 'trousers', 'shorts', "skirt", "sweatpants", "slacks", "pantyhose", "leggings"],
    Part.Backpack.value: ['backpack', 'bag', "pack", "pounch", "haversack", "rucksack", "briefcase", "baggage", "handbag", "packsack"],
    "Length_Short": ['short', 'shorts', "shirt", "t-shirt", 'sleeveless', "skirt", "top", "blouse", "vest"],
    "Length_Long": ['long', 'sleeves', 'trousers', "jeans", "pant", "pants", "sweatpants", "pantyhose", "blazer", "leggings", "jacket", "hoodie", "raincoat", "sweatshirt", "pullover"],
    Colors.Black.value: ["black", "dark"],
    Colors.Blue.value: ["blue"],
    Colors.Brown.value: ["brown"],
    Colors.Green.value: ["green"],
    Colors.Grey.value: ["grey", "gray"],
    Colors.Orange.value: ["orange"],
    Colors.Pink.value: ["pink"],
    Colors.Purple.value: ["purple"],
    Colors.Red.value: ["red"],
    Colors.White.value: ["white", "light"],
    Colors.Yellow.value: ["yellow"],
    Colors.Mixture.value: ["mixture", "colorfull", "colored", "rainbow"],
    Colors.Other.value: ["other"],
}
