import module_ListFunction as mlf

even_numbers = [x for x in range(2, 21, 2)]
odd_numbers = [x for x in range(1, 20, 2)]
squares = [x**2 for x in range(1, 11)]
random_list = [12, 4, 7, 9, 21, 5, 8, 3]

print("Even Numbers List:", even_numbers)
print("Max:", mlf.find_max(even_numbers))
print("Min:", mlf.find_min(even_numbers))
print("Sum:", mlf.calculate_sum(even_numbers))
print("Average:", mlf.compute_average(even_numbers))
print("Median:", mlf.determine_median(even_numbers))
print()

print("Odd Numbers List:", odd_numbers)
print("Max:", mlf.find_max(odd_numbers))
print("Min:", mlf.find_min(odd_numbers))
print("Sum:", mlf.calculate_sum(odd_numbers))
print("Average:", mlf.compute_average(odd_numbers))
print("Median:", mlf.determine_median(odd_numbers))
print()

print("Squares List:", squares)
print("Max:", mlf.find_max(squares))
print("Min:", mlf.find_min(squares))
print("Sum:", mlf.calculate_sum(squares))
print("Average:", mlf.compute_average(squares))
print("Median:", mlf.determine_median(squares))
print()

print("Random List:", random_list)
print("Max:", mlf.find_max(random_list))
print("Min:", mlf.find_min(random_list))
print("Sum:", mlf.calculate_sum(random_list))
print("Average:", mlf.compute_average(random_list))
print("Median:", mlf.determine_median(random_list))
