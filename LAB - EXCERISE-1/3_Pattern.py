ListColour = ["Black", "Red", "Maroon", "Yellow"]
ListHex = ["000000", "FF0000", "800000", "FFFF00"]

result = [{"colour": colour, "hex": hex_code} for colour, hex_code in zip(ListColour, ListHex)]

print(result)