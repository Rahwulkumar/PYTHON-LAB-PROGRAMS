def print_alphabet_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print(chr(65 + j), end="")
        print()

def print_asterisk_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()

# Number of rows for the patterns
rows = 5

print("Alphabet Pyramid:")
print_alphabet_pyramid(rows)
print("\nAsterisk Triangle:")
print_asterisk_triangle(rows)
