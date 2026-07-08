students = {
    101: {
        "name": "Alia",
        "marks": {
            "math": 85,
            "science": 90,
            "english": 78
        }
    },
    102: {
        "name": "Sara",
        "marks": {
            "math": 95,
            "science": 88,
            "english": 92
        }
    }
}

feature = int(input("Enter 1 to store student details\nEnter 2 to analyze details\nEnter 3 for total marks and percentage "))

def add_student():
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    math = int(input("Enter math marks: "))
    science = int(input("Enter science marks: "))
    english = int(input("Enter english marks: "))

    students[roll] = {
        "name": name,
        "marks": {
            "math": math,
            "science": science,
            "english": english
        }
    }

    print("Student added:")
    print(students[roll])


if feature == 1:
    add_student()

elif feature == 2:
    roll = int(input("Enter roll number to view details: "))
    print(students[roll])

elif feature == 3:
    roll = int(input("Enter roll number: "))

    def calculate_total(roll):
        marks = students[roll]["marks"]
        total = sum(marks.values())
        return total

    def calculate_percentage(roll):
        total = calculate_total(roll)
        percentage = (total / 300) * 100
        return percentage
    
    total = calculate_total(roll)
    percentage = calculate_percentage(roll)
    def calculate_grade(percentage):
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        else:
            return "Fail"
    grade = calculate_grade(percentage)

    print("Name:", students[roll]["name"])
    print("Total Marks:", total)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade: ",grade)