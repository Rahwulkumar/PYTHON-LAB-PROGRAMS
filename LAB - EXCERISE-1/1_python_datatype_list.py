def sum_of_list(lst):
    return sum(lst)

def multiply_list(lst):
    multiplication = 1
    for i in lst:
        multiplication *= i
    return multiplication

def get_largest(lst):
    largest = lst[0]
    for i in lst:
        if i > largest:
            largest = i
    return largest

def get_smallest(lst):
    smallest = lst[0]
    for i in lst:
        if i < smallest:
            smallest = i
    return smallest

def get_user_list():
    user_input = input("Enter a list of numbers separated by spaces: ")
    user_list = [int(item) for item in user_input.split()]
    return user_list

def main():
    mylist = get_user_list()

    print("Sum of list:", sum_of_list(mylist))
    print("Multiplication of list:", multiply_list(mylist))
    print("Largest number in list:", get_largest(mylist))
    print("Smallest number in list:", get_smallest(mylist))

if __name__ == "__main__": #is a bulit in variable that is automatically set by the interpreter
    main()
