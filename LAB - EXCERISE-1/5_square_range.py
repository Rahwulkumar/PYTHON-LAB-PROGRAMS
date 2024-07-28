def even_range(start, end):
    for i in range(start, end):
        if i % 2 == 0:
            square = i **2
            print(f"Even Number: {i}, Square:{square}")

even_range(1,50)
print("\n")
even_range(1,100)