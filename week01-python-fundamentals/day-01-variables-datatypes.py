# STUDENT INFORMATION 
student_name = "Taksh"
student_id = "S12345"  
course_name = "Python with ML"
semester = "Semester 1" 

# GRADE COMPONENTS
homework_score = 78
quiz_score = 78
midterm_score = 65
final_exam_score = 88
participation_score = 81

# Grade Weights
homework_weight = 0.20     
quiz_weight = 0.15         
midterm_weight = 0.25      
final_weight = 0.30        
participation_weight = 0.10

# Calculate weighted final grade
final_grade = (homework_score * homework_weight) + (quiz_score * quiz_weight) + (midterm_score * midterm_weight) + (final_exam_score * final_weight) + (participation_score * participation_weight)

# Function to determine letter grade
def get_letter_grade(grade):
    if grade >= 90:
        return "A"  
    elif grade >= 80:  
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"  

# Call the function to get the letter grade
letter_grade = get_letter_grade(final_grade)

#Determine pass/fail status
if final_grade >= 60:
    passed = True
    status = "PASSED"  # More descriptive
else:
    passed = False  # Fixed typo: was "Flase"
    status = "FAILED"

#Print formatted report card
print("=====================================")
print("        GRADE REPORT CARD")
print("=====================================")
print(f"Student: {student_name} (ID: {student_id})")  # Added "Student:" label
print(f"Course: {course_name}")  # Added "Course:" label
print(f"Semester: {semester}")  # Added "Semester:" label
print("=====================================")
print("COMPONENT SCORES:")
print(f"  Homework (20%):      {homework_score}/100")
print(f"  Quizzes (15%):       {quiz_score}/100")
print(f"  Midterm (25%):       {midterm_score}/100")
print(f"  Final Exam (30%):    {final_exam_score}/100")  # Fixed: was showing midterm_score
print(f"  Participation (10%): {participation_score}/100")
print("=====================================")
print(f"FINAL GRADE: {final_grade:.2f} ({letter_grade})")  # Added :.2f for 2 decimal places
print(f"STATUS: {status}")
print("=====================================")

# Additional useful information
print(f"\nClass Performance Analysis:")
print(f"• Your final grade: {final_grade:.2f}%")
print(f"• Letter grade: {letter_grade}")

# Calculate points needed for next letter grade
if letter_grade == "F":
    points_needed = 60 - final_grade
    print(f"• Points needed to pass: {points_needed:.2f}")
elif letter_grade == "D":
    points_needed = 70 - final_grade
    print(f"• Points needed for C: {points_needed:.2f}")
elif letter_grade == "C":
    points_needed = 80 - final_grade
    print(f"• Points needed for B: {points_needed:.2f}")
elif letter_grade == "B":
    points_needed = 90 - final_grade
    print(f"• Points needed for A: {points_needed:.2f}")
else:
    print("• Excellent work! You have an A!")

print("\n🎉 Grade calculation complete!")