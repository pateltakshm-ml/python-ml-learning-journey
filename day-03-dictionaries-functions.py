# =============================================================================
# PART 1: WORKING WITH DICTIONARIES 
# =============================================================================

print("=== BASIC DICTIONARIES ===")

# 1. Create dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "grade": 85,
    "major": "Computer Science"
}

# Empty dictionary
scores = {}

# Dictionary with mixed data types
course_info = {
    "course_name": "Python Programming",
    "credits": 3,
    "students": ["Alice", "Bob", "Charlie"],
    "is_online": True
}

print(f"Student info: {student}")
print(f"Course info: {course_info}")

# 2. Accessing dictionary values
print(f"\nStudent name: {student['name']}")
print(f"Student grade: {student['grade']}")
print(f"Course credits: {course_info['credits']}")

# Safe way to access (won't crash if key doesn't exist)
print(f"Student email: {student.get('email', 'Not provided')}")

# 3. Modifying dictionaries
student["email"] = "alice@university.edu"
student["grade"] = 90  # Update existing value
print(f"Updated student: {student}")

# 4. Dictionary methods
print(f"\nAll keys: {list(student.keys())}")
print(f"All values: {list(student.values())}")

# Loop through dictionary
print("\nStudent details:")
for key, value in student.items():
    print(f"  {key}: {value}")

# =============================================================================
# PART 2: BASIC FUNCTIONS 
# =============================================================================

print("\n=== BASIC FUNCTIONS ===")

# 5. Simple function
def greet():
    return "Hello, World!"

print(greet())

# 6. Function with parameters
def greet_person(name):
    return f"Hello, {name}!"

print(greet_person("Alice"))
print(greet_person("Bob"))

# 7. Function with multiple parameters
def calculate_grade(homework, quiz, exam):
    total = (homework * 0.3) + (quiz * 0.3) + (exam * 0.4)
    return total

final_grade = calculate_grade(85, 90, 88)
print(f"Final grade: {final_grade}")

# 8. Function with default parameters
def introduce(name, age=18):
    return f"Hi, I'm {name} and I'm {age} years old."

print(introduce("Charlie"))
print(introduce("Diana", 22))

# 9. Function that returns multiple values
def get_student_stats(grades):
    avg = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    return avg, highest, lowest

grades = [85, 92, 78, 96, 88]
average, high, low = get_student_stats(grades)
print(f"Average: {average}, Highest: {high}, Lowest: {low}")

# =============================================================================
# PART 3: COMBINING DICTIONARIES AND FUNCTIONS (10 minutes)
# =============================================================================

print("\n=== DICTIONARIES + FUNCTIONS ===")

# 10. Function that works with dictionaries
def display_student(student_dict):
    name = student_dict["name"]
    grade = student_dict["grade"]
    return f"Student: {name}, Grade: {grade}"

student1 = {"name": "Emma", "grade": 94}
student2 = {"name": "James", "grade": 87}

print(display_student(student1))
print(display_student(student2))

# 11. Function that creates dictionaries
def create_student(name, age, grade, major):
    return {
        "name": name,
        "age": age,
        "grade": grade,
        "major": major
    }

new_student = create_student("Sarah", 19, 92, "Mathematics")
print(f"New student: {new_student}")

# =============================================================================
# MAIN PROJECT: STUDENT MANAGEMENT SYSTEM (Complete this!)
# =============================================================================

print("\n=== STUDENT MANAGEMENT SYSTEM ===")

# Student database (list of dictionaries)
students_db = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 88], "major": "CS"},
    {"name": "Bob", "age": 19, "grades": [78, 82, 80], "major": "Math"},
    {"name": "Charlie", "age": 21, "grades": [92, 95, 89], "major": "Physics"},
    {"name": "Diana", "age": 20, "grades": [88, 86, 91], "major": "CS"}
]

# TODO: Write these functions yourself!

def calculate_average(grades_list):
    avg_grades = sum(grades_list) / len(grades_list)
    return avg_grades  

def get_letter_grade(average):
    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"
    
    return letter

def find_student_by_name(database, student_name):
    for student in database:
        if student["name"] == student_name:
            return student
    return None

def get_students_by_major(database, major):
    students_with_major = []
    for student in database:
        if student["major"] == major:
            students_with_major.append(student)
    return students_with_major

def get_top_student(database):
    top_student = None
    highest_average = 0  

    for student in database:
        student_average = calculate_average(student["grades"])
        if student_average > highest_average:
            highest_average = student_average
            top_student = student
    return top_student

print("TESTING YOUR FUNCTIONS:")
print("=" * 40)

# Calculate Alice's average
alice = students_db[0]
alice_avg = calculate_average(alice["grades"])
print(f"Alice's average: {alice_avg}")

# Get Alice's letter grade
alice_letter = get_letter_grade(alice_avg)
print(f"Alice's letter grade: {alice_letter}")

# Find Bob
bob = find_student_by_name(students_db, "Bob")
print(f"Found Bob: {bob}")

# Get all CS students
cs_students = get_students_by_major(students_db, "CS")
print(f"CS students: {cs_students}")

# Get top student
top_student = get_top_student(students_db)
print(f"Top student: {top_student}")


print("\nDay 3 Practice Complete!")