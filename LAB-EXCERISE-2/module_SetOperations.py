def add_element(s, element):
    s.add(element)
    return s

def remove_element(s, element):
    s.discard(element)
    return s

def union_intersection(s1, s2):
    union = s1 | s2
    intersection = s1 & s2
    return union, intersection

def difference(s1, s2):
    return s1 - s2

def is_subset(s1, s2):
    return s1 <= s2

def set_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(s1, s2):
    return s1 ^ s2

def power_set(s):
    from itertools import chain, combinations
    s = list(s)
    return set(frozenset(x) for x in chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def unique_subsets(s):
    from itertools import combinations
    s = list(s)
    subsets = set()
    for r in range(len(s) + 1):
        for subset in combinations(s, r):
            subsets.add(frozenset(subset))
    return subsets
