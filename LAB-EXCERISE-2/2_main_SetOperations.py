import module_SetOperations as mso

# Demonstration of the set operations

s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Add element
print("Add element:")
print(mso.add_element(s1, 4))
print(mso.add_element(s1, 4))  # should handle no error if element is already present
print()

# Remove element
print("Remove element:")
print(mso.remove_element(s1, 2))
print(mso.remove_element(s1, 2))  # should handle no error if element is not present
print()

# Union and Intersection
print("Union and Intersection:")
union, intersection = mso.union_intersection(s1, s2)
print("Union:", union)
print("Intersection:", intersection)
print()

# Difference
print("Difference S1 - S2:")
print(mso.difference(s1, s2))
print()

# Is Subset
print("Is Subset:")
print(mso.is_subset({1, 2}, {1, 2, 3}))
print(mso.is_subset({1, 2, 3}, {1, 2}))
print()

# Set Length
print("Set Length:")
print(mso.set_length(s1))
print(mso.set_length(set()))
print()

# Symmetric Difference
print("Symmetric Difference:")
print(mso.symmetric_difference(s1, s2))
print()

# Power Set
print("Power Set:")
print(mso.power_set(s1))
print()

# Unique Subsets
print("Unique Subsets:")
print(mso.unique_subsets(s1))
print()
