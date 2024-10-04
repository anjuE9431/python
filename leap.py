def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

start_year = 2024
end_year = int(input("Enter the end year: "))

print("Leap years between", end_year,"are:")
for year in range(start_year, end_year + 1):
    if is_leap_year(year):
        print(year)
