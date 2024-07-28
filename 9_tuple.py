def extract_rear_elements(tuple_of_strings):
    return [string[-1] for string in tuple_of_strings]

user_input = input("Enter the elements of the tuple separated by commas: ")

input_tuple = tuple(user_input.split(","))

output_list = extract_rear_elements(input_tuple)

print(output_list)
