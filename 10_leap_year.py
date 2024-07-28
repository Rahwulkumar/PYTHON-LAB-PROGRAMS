def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(month, year=None):
    months_with_31_days = ("January", "March", "May", "July", "August", "October", "December")
    months_with_30_days = ("April", "June", "September", "November")
    february = "February"
    
    if month in months_with_31_days:
        return 31
    elif month in months_with_30_days:
        return 30
    elif month == february:
        if year is not None and is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return None

def main():
    month = input("Enter the month name: ").strip().title()
    
    if month == "February":
        year = int(input("Enter the year: "))
        days = get_days_in_month(month, year)
    else:
        days = get_days_in_month(month)
    
    if days:
        print(f"The number of days in {month} is: {days}")
    else:
        print("Invalid month name")

if __name__ == "__main__":
    main()
