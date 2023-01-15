#  A Python program that ask a month and day  from user and prints the season for that month and day.


def determine_season(month, day):
    if month < 3 or (month == 3 and day <= 15):
        return "Winter"
    elif month < 6 or (month == 6 and day <= 15):
        return "Spring"
    elif month < 9 or (month == 9 and day <= 15):
        return "Summer"
    else:
        return "Autumn"

month = int(input("Enter a month (1-12): "))
day = int(input("Enter a day (1-31): "))

season = determine_season(month, day)
print(f"The current season is {season}")
