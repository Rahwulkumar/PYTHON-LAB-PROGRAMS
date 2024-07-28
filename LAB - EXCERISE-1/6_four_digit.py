def sum_of_digits(number):
    total = sum(int(digit) for digit in str(number))
    return total

def reverse_number(number):
    reversed_num = int(str(number)[::-1])
    return reversed_num

def main():
    number = int(input("Enter a four-digit number: "))
    
    if 1000 <= number <= 9999:
        sum_digits = sum_of_digits(number)
        reversed_num = reverse_number(number)
        
        print(f"Sum of digits: {sum_digits}")
        print(f"Reversed number: {reversed_num}")
    else:
        print("Please enter a valid four-digit number.")

if __name__ == "__main__":
    main()
