# =============================================================================
# PART 1: WORKING WITH TEXT FILES (8 minutes)
# =============================================================================

print("PART 1: Basic Text File Operations")
print("=" * 40)

# Writing to a text file
def create_sample_file():
    with open('students.txt', 'w') as file:
        file.write("Alice,20,Computer Science,85\n")
        file.write("Bob,19,Mathematics,92\n")
        file.write("Charlie,21,Physics,78\n")
        file.write("Diana,20,Computer Science,95\n")
    
    print("✅ Created students.txt file")

# Reading from a text file
def read_student_file():
    try:
        with open('students.txt', 'r') as file:
            print("\n📖 Reading student data:")
            for line_number, line in enumerate(file, 1):
                # Remove whitespace and split by comma
                data = line.strip().split(',')
                if len(data) == 4:  # Ensure we have all fields
                    name, age, major, grade = data
                    print(f"  {line_number}. {name} (Age {age}) - {major}: {grade}%")
    
    except FileNotFoundError:
        print("❌ File not found! Create the file first.")

# Create and read the file
create_sample_file()
read_student_file()

# =============================================================================
# PART 2: WORKING WITH CSV FILES (10 minutes)
# =============================================================================

print("\n\nPART 2: CSV Files - The Backbone of Data Science")
print("=" * 50)

import csv

def create_csv_data():
    # Sample student data with more details
    students = [
        ['Name', 'Age', 'Major', 'GPA', 'Credits', 'Graduation_Year'],
        ['Alice Johnson', 20, 'Computer Science', 3.8, 60, 2025],
        ['Bob Smith', 19, 'Mathematics', 3.9, 45, 2026],
        ['Charlie Brown', 21, 'Physics', 3.2, 90, 2024],
        ['Diana Ross', 20, 'Computer Science', 4.0, 75, 2025],
        ['Eve Wilson', 22, 'Chemistry', 3.7, 95, 2024]
    ]
    
    # Write CSV file with proper formatting
    with open('student_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in students:
            writer.writerow(row)
    
    print("✅ Created student_data.csv with structured data")

def read_and_analyze_csv():
    try:
        with open('student_data.csv', 'r') as file:
            reader = csv.DictReader(file)  # DictReader gives us column names
            
            print("\n📊 CSV Data Analysis:")
            
            # Collect data for analysis
            students = []
            for row in reader:
                students.append(row)
            
            print(f"  📈 Total students: {len(students)}")
            
            # Calculate average GPA
            total_gpa = sum(float(student['GPA']) for student in students)
            avg_gpa = total_gpa / len(students)
            print(f"  📈 Average GPA: {avg_gpa:.2f}")
            
            # Find students by major
            cs_students = [s for s in students if s['Major'] == 'Computer Science']
            print(f"  💻 Computer Science students: {len(cs_students)}")
            
            # Display each student nicely
            print("\n  👥 Student Details:")
            for student in students:
                print(f"    • {student['Name']}: {student['Major']}, GPA {student['GPA']}")
    
    except FileNotFoundError:
        print("❌ CSV file not found!")

# Create and analyze CSV data
create_csv_data()
read_and_analyze_csv()

# =============================================================================
# PART 3: WORKING WITH JSON FILES (7 minutes)  
# =============================================================================

print("\n\nPART 3: JSON Files - Structured Data Storage")
print("=" * 45)

import json  # Built-in library for JSON handling

def create_json_data():
    # Complex student data with nested information
    school_data = {
        "school_name": "Tech University",
        "semester": "Fall 2024",
        "courses": {
            "CS101": {
                "course_name": "Introduction to Programming",
                "instructor": "Dr. Smith",
                "students": ["Alice Johnson", "Diana Ross"],
                "credits": 3
            },
            "MATH201": {
                "course_name": "Calculus II", 
                "instructor": "Prof. Wilson",
                "students": ["Bob Smith"],
                "credits": 4
            },
            "PHYS301": {
                "course_name": "Quantum Physics",
                "instructor": "Dr. Brown",
                "students": ["Charlie Brown"],
                "credits": 3
            }
        },
        "statistics": {
            "total_students": 4,
            "total_courses": 3,
            "average_class_size": 1.3
        }
    }
    
    # Write JSON with proper formatting (indent makes it readable)
    with open('school_data.json', 'w') as file:
        json.dump(school_data, file, indent=2)
    
    print("✅ Created school_data.json with nested structure")

def read_and_explore_json():
    """
    Read JSON data and explore its hierarchical structure.
    This shows how to navigate complex, nested data.
    """
    try:
        with open('school_data.json', 'r') as file:
            data = json.load(file)
        
        print(f"\n🏫 School: {data['school_name']}")
        print(f"📅 Semester: {data['semester']}")
        
        print(f"\n📚 Course Catalog:")
        for course_code, course_info in data['courses'].items():
            print(f"  {course_code}: {course_info['course_name']}")
            print(f"    👨‍🏫 Instructor: {course_info['instructor']}")
            print(f"    👥 Students: {', '.join(course_info['students'])}")
            print(f"    📖 Credits: {course_info['credits']}")
            print()
        
        print(f"📊 School Statistics:")
        stats = data['statistics']
        for key, value in stats.items():
            print(f"  {key.replace('_', ' ').title()}: {value}")
    
    except FileNotFoundError:
        print("❌ JSON file not found!")

# Create and explore JSON data
create_json_data()
read_and_explore_json()

# =============================================================================
# TODAY'S CHALLENGE: BUILD A STUDENT MANAGEMENT SYSTEM (Complete this!)
# =============================================================================

print("\n\n🎯 TODAY'S CHALLENGE: Student Data Manager")
print("=" * 50)

"""
YOUR TASK: Create functions that can:
1. Add new students to the CSV file
2. Search for students by name or major
3. Update student information
4. Export data in different formats

This combines everything you've learned about files with your function skills!
"""

def add_student_to_csv(name, age, major, gpa, credits, grad_year):
    try:
        with open('student_data.csv', 'a', newline='') as file:  # Empty string for newline
            writer = csv.writer(file)
            writer.writerow([name, age, major, gpa, credits, grad_year])
        print(f"✅ Successfully added {name} to the database")
        
    except FileNotFoundError:
        print("❌ Student database file not found. Create it first!")
    except Exception as e:
        print(f"❌ Error adding student: {e}")  # Fixed typo in "Error"

def search_students_by_major(major):
    try:  # Added error handling for file operations
        with open('student_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            matching_students = []
            
            for student in reader:
                if student["Major"].lower() == major.lower():
                    matching_students.append(student)

            if matching_students:
                print(f"\n📚 Found {len(matching_students)} student(s) studying {major}:")  # Fixed variable name
                for student in matching_students:
                    print(f"  • {student['Name']}: GPA {student['GPA']}, "
                          f"Credits: {student['Credits']}, Graduates: {student['Graduation_Year']}")
            else:
                print(f"❌ No students found studying {major}")  # Fixed variable name
                
            return matching_students
            
    except FileNotFoundError:
        print("❌ Student database file not found!")
        return []
    except Exception as e:
        print(f"❌ Error searching database: {e}")
        return []


def export_students_to_json():
    try:
        # Step 1: Read all the CSV data into Python structures
        students_list = []
        with open('student_data.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for student in reader:
                students_list.append(student)
        
        # Step 2: Organize the data in a more structured way
        organized_data = {
            "school_database": {
                "total_students": len(students_list),
                "students": students_list,
                "export_date": "2024-07-12",  # You could use datetime for current date
                "statistics": {
                    "total_students": len(students_list)
                }
            }
        }
        
        # Step 3: Write the organized data to a JSON file
        with open('students_export.json', 'w') as json_file:
            json.dump(organized_data, json_file, indent=2)
        
        print("✅ Successfully exported student data to JSON format")
        print(f"📄 Exported {len(students_list)} students to students_export.json")
        
    except FileNotFoundError:
        print("CSV file not found! Make sure student_data.csv exists.")
    except Exception as e:
        print(f"Error during export: {e}")




def calculate_class_statistics():
    try:
        # Read all student data
        students = []
        with open('student_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for student in reader:
                students.append(student)
        
        if not students:
            print("❌ No students found in database")
            return
        
        # Group students by major for analysis
        majors = {}
        graduation_years = {}
        
        for student in students:
            major = student['Major']
            grad_year = student['Graduation_Year']
            
            # Group by major
            if major not in majors:
                majors[major] = []
            majors[major].append(float(student['GPA']))  # Convert to float for math
            
            # Group by graduation year
            if grad_year not in graduation_years:
                graduation_years[grad_year] = 0
            graduation_years[grad_year] += 1
        
        # Calculate and display statistics
        print("\n📊 Class Statistics:")
        print("=" * 30)
        
        print("\n📚 Average GPA by Major:")
        for major, gpas in majors.items():
            avg_gpa = sum(gpas) / len(gpas)
            print(f"  {major}: {avg_gpa:.2f} (based on {len(gpas)} students)")
        
        print("\n🎓 Students by Graduation Year:")
        for year in sorted(graduation_years.keys()):
            print(f"  {year}: {graduation_years[year]} students")
        
        # Overall statistics
        all_gpas = [float(s['GPA']) for s in students]
        overall_avg = sum(all_gpas) / len(all_gpas)
        print(f"\n🎯 Overall Statistics:")
        print(f"  Total students: {len(students)}")
        print(f"  Overall average GPA: {overall_avg:.2f}")
        print(f"  Highest GPA: {max(all_gpas):.2f}")
        print(f"  Lowest GPA: {min(all_gpas):.2f}")
        
    except FileNotFoundError:
        print("❌ Student database not found!")
    except Exception as e:
        print(f"❌ Error calculating statistics: {e}")

# Test your functions here:
print("\n🧪 Testing Your Functions:")
print("(Implement the functions above, then test them here)")


add_student_to_csv("John Doe", 21, "Engineering", 3.5, 80, 2025)

add_student_to_csv("Alice Johnson", 20, "Computer Science", 3.8, 60, 2025)

print("\nStudents in Computer Science:")
search_students_by_major("Computer Science")

export_students_to_json()

calculate_class_statistics()




