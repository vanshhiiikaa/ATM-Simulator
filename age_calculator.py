current_year = int(input("Please enter the current year: "))
current_month = int(input("Please enter the current month: "))
current_day = int(input("Please enter the current day: "))
birth_year = int(input("Please enter your birth year: "))
birth_date = input("Please enter the date (YYYY-MM-DD): ")
birth_month = int(birth_date.split("-")[1])
birth_day = int(birth_date.split("-")[2])
age = current_year - birth_year
if (current_month == birth_month and current_day < birth_day) or (current_month < birth_month):
    age -= 1
    print(age)
else:
    print(age)
