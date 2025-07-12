# =============================================================================
# PART 1: WORKING WITH LISTS (10 minutes)
# =============================================================================

# 1. Create different types of lists
print("=== BASIC LISTS ===")
fruits = ["apple", "banana", "orange", "grape"]
numbers = [10, 25, 3, 47, 12]
mixed_list = ["Python", 42, True, 3.14]
empty_list = []

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed list: {mixed_list}")
print(f"Empty list: {empty_list}")

# 2. List operations
print("\n=== LIST OPERATIONS ===")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"First 2 fruits: {fruits[:2]}")
print(f"Length of fruits: {len(fruits)}")

# 3. Modifying lists
fruits.append("mango")  # Add to end
fruits.insert(1, "kiwi")  # Insert at position 1
print(f"After adding: {fruits}")

removed_fruit = fruits.pop()  # Remove last item
print(f"Removed: {removed_fruit}")
print(f"After removing: {fruits}")

# =============================================================================
# PART 2: FOR LOOPS (10 minutes)
# =============================================================================

print("\n=== FOR LOOPS ===")

# 4. Loop through a list
print("All fruits:")
for fruit in fruits:
    print(f"- {fruit}")

# 5. Loop with index
print("\nFruits with index:")
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# 6. Loop through numbers
print("\nNumbers and their squares:")
for num in numbers:
    square = num ** 2
    print(f"{num} squared is {square}")

# 7. Range function
print("\nCounting to 5:")
for i in range(5):
    print(f"Count: {i}")

print("\nCounting 2 to 8:")
for i in range(2, 9):
    print(f"Number: {i}")

# =============================================================================
# PART 3: LIST COMPREHENSIONS (5 minutes)
# =============================================================================

print("\n=== LIST COMPREHENSIONS ===")

# 8. Create new lists using comprehensions
squares = [x ** 2 for x in numbers]
print(f"Original numbers: {numbers}")
print(f"Squares: {squares}")

# Even numbers only
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Uppercase fruits
upper_fruits = [fruit.upper() for fruit in fruits]
print(f"Uppercase fruits: {upper_fruits}")


# =============================================================================
# PART 4: WHILE LOOPS (5 minutes)
# =============================================================================

print("\n=== WHILE LOOPS ===")

# 9. Basic while loop
count = 0
print("Counting with while loop:")
while count < 3:
    print(f"Count is: {count}")
    count += 1

# 10. While loop with list
shopping_list = ["milk", "bread", "eggs"]
print("\nShopping list:")
while shopping_list:
    item = shopping_list.pop(0)
    print(f"Bought: {item}")
    print(f"Remaining: {shopping_list}")


# =============================================================================
# MINI PROJECT: GRADE ANALYZER (Complete this!)
# =============================================================================

print("\n=== GRADE ANALYZER PROJECT ===")

student_grades = [85, 92, 78, 96, 88, 76, 94, 89, 82, 91]


# 1. Total number of students
total_students = len(student_grades) 

# 2. Average grade
average_grade = sum(student_grades) / len(student_grades)

# 3. Highest grade
highest_grade = max(student_grades)

# 4. Lowest grade
lowest_grade = min(student_grades)

# 5. Number of students with A grades (90+)
a_grades = len([i for i in student_grades if i>90])

# 6. Number of students with failing grades (below 60)
failing_grades = len([i for i in student_grades if i<60])

# 7. All grades above average
above_average = [i for i in student_grades if i > sum(student_grades) / len(student_grades)]

print("GRADE ANALYSIS REPORT")
print("=" * 30)
print(f"Total Students: {total_students}")
print(f"Average Grade: {average_grade:.2f}")
print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")
print(f"A Grades (90+): {a_grades}")
print(f"Failing Grades (<60): {failing_grades}")
print(f"Above Average Grades: {above_average}")


# Create a list of even numbers from 1 to 20
even_list = [x for x in range(1,20) if x%2==0]  # Using a loop or list comprehension

# Reverse a list without using reverse() method
original = [1, 2, 3, 4, 5]
reversed_list = original[::-1] 

# Find common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1).intersection(set(list2)))  # Find common elements

print("\n=== BONUS RESULTS ===")
print(f"Even numbers 1-20: {even_list}")
print(f"Reversed {original}: {reversed_list}")
print(f"Common elements: {common}")

print("\n🎉 Day 2 Complete! You've mastered lists and loops!")
print("💡 Next: Day 3 - Dictionaries and Functions")