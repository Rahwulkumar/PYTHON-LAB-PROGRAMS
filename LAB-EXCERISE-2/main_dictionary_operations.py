# main_dictionary_operations.py

import dictionary_operations as do

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
dict3 = {'c': 3, 'd': 5, 'e': 6}

# Merging dictionaries
print("Merging Dictionaries:")
merged_dict = do.merging_Dict(dict1, dict2, dict3)
print(merged_dict)
print()

# Finding common keys
print("Common Keys:")
common_keys = do.common_keys(dict1, dict2, dict3)
print(common_keys)
print()

# Inverting a dictionary
print("Inverting Dictionary (dict1):")
inverted_dict = do.invert_dict(dict1)
print(inverted_dict)
print()

# Finding common key-value pairs
print("Common Key-Value Pairs:")
common_pairs = do.common_key_value_pairs(dict1, dict2, dict3)
print(common_pairs)
print()
