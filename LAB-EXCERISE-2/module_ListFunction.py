def find_max(lst):
    if not lst:
        return None
    return max(lst)

def find_min(lst):
    if not lst:
        return None
    return min(lst)

def calculate_sum(lst):
    return sum(lst)

def compute_average(lst):
    if not lst:
        return None
    return sum(lst) / len(lst)

def determine_median(lst):
    if not lst:
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]
