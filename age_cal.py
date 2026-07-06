current_year = input("Enter the current date (YYYY MM DD): ")
current_month = int(current_year.split(" ")[1])
current_day = int(current_year.split(" ")[2])
birth_year = input("Enter your birth date (YYYY MM DD): ")
birth_month = int(birth_year.split(" ")[1])
birth_day = int(birth_year.split(" ")[2])
if (current_month == birth_month and current_day < birth_day) or (current_month < birth_month):
    age = int(current_year.split(" ")[0]) - int(birth_year.split(" ")[0]) - 1
    print(age)
else:
    age = int(current_year.split(" ")[0]) - int(birth_year.split(" ")[0])   
    print(age)