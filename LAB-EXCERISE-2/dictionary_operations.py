
def merging_Dict(*args):
    merged_dict = {}
    for dictionary in args:
        merged_dict.update(dictionary)
    return merged_dict

def common_keys(*args):
    if not args:
        return set()
    common_keys_set = set(args[0].keys())
    for dictionary in args[1:]:
        common_keys_set &= set(dictionary.keys())
    return common_keys_set

def invert_dict(d):
    inverted_dict = {}
    for key, value in d.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    return inverted_dict

def common_key_value_pairs(*args):
    if not args:
        return {}
    common_pairs = set(args[0].items())
    for dictionary in args[1:]:
        common_pairs &= set(dictionary.items())
    return dict(common_pairs)
