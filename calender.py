def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31

def day_of_week(year, month, day):
    # Using Zeller's Congruence to find the day of the week
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    f = day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 + 5 * J
    return (f % 7 + 1) % 7  # Adjusting so that 0 = Sunday

def print_calendar(year, month):
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    print(" ".join(days))
    
    # Find the first day of the month
    first_day = day_of_week(year, month, 1)
    
    # Get the number of days in the month
    num_days = days_in_month(month, year)
    
    # Print leading spaces for the first day
    print("     " * first_day, end="")

    # Print the days of the month
    for day in range(1, num_days + 1):
        print(f"{day:2}", end="    ")
        first_day += 1
        if first_day % 7 == 0:
            print()  # New line after Saturday
    print()  # New line after the last row of the month

# Example: Print the calendar for October 2024
print_calendar(2024, 10)
