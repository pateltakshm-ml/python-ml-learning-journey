# =============================================================================
# PART 1: WHY NUMPY CHANGES EVERYTHING 
# =============================================================================

"""
Welcome to Week 2: Data Science Foundations!

NumPy (Numerical Python) is the foundation of the entire Python data science ecosystem.
Every major library (Pandas, Matplotlib, Scikit-learn) is built on NumPy.

Key Advantages:
- Performance: 50-100x faster than pure Python
- Memory efficiency: Uses less RAM for large datasets
- Vectorized operations: Apply functions to entire arrays instantly
- Broadcasting: Operations between arrays of different shapes
- Mathematical functions: Comprehensive library of math operations

Think of NumPy as upgrading from a bicycle to a rocket ship! 🚀
"""

print("=== DAY 7: NUMPY FUNDAMENTALS ===\n")

# First, let's install and import NumPy
try:
    import numpy as np
    print("✅ NumPy is ready!")
    print(f"📦 NumPy version: {np.__version__}")
except ImportError:
    print("❌ NumPy not installed. Run: pip install numpy")
    print("💡 For this lesson, we'll show examples assuming NumPy is available")

# =============================================================================
# PART 2: ARRAYS VS LISTS - THE GAME CHANGER
# =============================================================================

print("\nPART 1: Arrays vs Lists - Why NumPy is Revolutionary")
print("=" * 55)

def compare_lists_vs_arrays():
    
    print("🐍 Traditional Python Lists:")
    
    # Python lists - the old way
    grades_list = [85, 90, 78, 92, 88, 76, 94, 89]
    print(f"   Original grades: {grades_list}")
    
    # To add 5 points to each grade (pure Python)
    bonus_grades_list = []
    for grade in grades_list:
        bonus_grades_list.append(grade + 5)
    print(f"   After +5 bonus: {bonus_grades_list}")
    
    # To calculate average (pure Python)
    total = sum(grades_list)
    average = total / len(grades_list)
    print(f"   Average: {average:.2f}")
    
    print(f"\n🚀 NumPy Arrays - The Data Science Way:")
    
    try:
        # NumPy arrays - the modern way
        grades_array = np.array([85, 90, 78, 92, 88, 76, 94, 89])
        print(f"   Original grades: {grades_array}")
        
        # Add 5 to ALL grades in ONE operation!
        bonus_grades_array = grades_array + 5
        print(f"   After +5 bonus: {bonus_grades_array}")
        
        # Calculate statistics instantly
        average = np.mean(grades_array)
        std_dev = np.std(grades_array)
        max_grade = np.max(grades_array)
        min_grade = np.min(grades_array)
        
        print(f"   Average: {average:.2f}")
        print(f"   Standard deviation: {std_dev:.2f}")
        print(f"   Highest grade: {max_grade}")
        print(f"   Lowest grade: {min_grade}")
        
        print(f"\n💡 Key Differences:")
        print(f"   Lists: grades_list + 5 → ERROR! Can't add number to list")
        print(f"   Arrays: grades_array + 5 → Works perfectly!")
        print(f"   Lists: Need loops for element-wise operations")
        print(f"   Arrays: Vectorized operations work on entire array")
        
    except NameError:
        print("   (NumPy not available - install with: pip install numpy)")

compare_lists_vs_arrays()

# =============================================================================
# PART 3: CREATING NUMPY ARRAYS
# =============================================================================

print("\n\nPART 2: Creating NumPy Arrays - Your Data Science Toolkit")
print("=" * 60)

def demonstrate_array_creation():
    
    try:
        print("🛠️  Array Creation Methods:\n")
        
        # 1. From Python lists (most common)
        print("1. From Python Lists:")
        list_data = [1, 2, 3, 4, 5]
        array_from_list = np.array(list_data)
        print(f"   List: {list_data}")
        print(f"   Array: {array_from_list}")
        print(f"   Type: {type(array_from_list)}")
        
        # 2. Multi-dimensional arrays (like spreadsheets)
        print(f"\n2. Multi-dimensional Arrays (2D - like spreadsheets):")
        student_grades = [
            [85, 90, 88],  # Student 1's grades
            [78, 82, 80],  # Student 2's grades  
            [92, 95, 89]   # Student 3's grades
        ]
        grades_2d = np.array(student_grades)
        print(f"   2D Array:\n{grades_2d}")
        print(f"   Shape: {grades_2d.shape} (3 students, 3 grades each)")
        
        # 3. Arrays of zeros (useful for initialization)
        print(f"\n3. Arrays of Zeros (for initialization):")
        zeros_array = np.zeros(5)
        zeros_2d = np.zeros((3, 4))  # 3 rows, 4 columns
        print(f"   1D zeros: {zeros_array}")
        print(f"   2D zeros:\n{zeros_2d}")
        
        # 4. Arrays of ones
        print(f"\n4. Arrays of Ones:")
        ones_array = np.ones(4)
        print(f"   1D ones: {ones_array}")
        
        # 5. Range arrays (like Python range, but better)
        print(f"\n5. Range Arrays:")
        range_array = np.arange(0, 10, 2)  # Start, stop, step
        print(f"   Range 0-10 step 2: {range_array}")
        
        linspace_array = np.linspace(0, 1, 5)  # 5 evenly spaced numbers between 0 and 1
        print(f"   5 points 0-1: {linspace_array}")
        
        # 6. Random arrays (essential for data science)
        print(f"\n6. Random Arrays (essential for ML):")
        random_array = np.random.random(5)  # 5 random numbers 0-1
        random_integers = np.random.randint(1, 100, 5)  # 5 random integers 1-99
        print(f"   Random floats: {random_array}")
        print(f"   Random integers: {random_integers}")
        
        # 7. Arrays from statistical distributions
        print(f"\n7. Statistical Distributions (advanced):")
        normal_data = np.random.normal(100, 15, 5)  # Mean=100, std=15, 5 samples
        print(f"   Normal distribution: {normal_data}")
        
    except NameError:
        print("NumPy not available. Install with: pip install numpy")

demonstrate_array_creation()

# =============================================================================
# PART 4: ARRAY OPERATIONS - THE MAGIC OF VECTORIZATION
# =============================================================================

print("\n\nPART 3: Array Operations - Where NumPy Shines")
print("=" * 50)

def demonstrate_array_operations():
    
    try:
        print("⚡ Vectorized Operations (The NumPy Superpower):\n")
        
        # Sample data: student test scores
        test_scores = np.array([85, 90, 78, 92, 88, 76, 94, 89, 82, 87])
        print(f"📊 Original test scores: {test_scores}")
        
        # 1. Basic arithmetic (applies to ALL elements)
        print(f"\n1. Basic Arithmetic Operations:")
        curved_scores = test_scores + 5  # Add 5 to everyone
        doubled_scores = test_scores * 2  # Double all scores
        scaled_scores = test_scores / 100  # Convert to 0-1 scale
        
        print(f"   +5 curve: {curved_scores}")
        print(f"   Doubled: {doubled_scores}")
        print(f"   0-1 scale: {scaled_scores}")
        
        # 2. Mathematical functions
        print(f"\n2. Mathematical Functions:")
        sqrt_scores = np.sqrt(test_scores)
        log_scores = np.log(test_scores)
        rounded_scores = np.round(test_scores / 10) * 10  # Round to nearest 10
        
        print(f"   Square root: {sqrt_scores}")
        print(f"   Natural log: {log_scores}")
        print(f"   Rounded to 10s: {rounded_scores}")
        
        # 3. Comparison operations (create boolean arrays)
        print(f"\n3. Comparison Operations (Boolean Arrays):")
        passing_scores = test_scores >= 80
        excellent_scores = test_scores >= 90
        
        print(f"   Passing (≥80): {passing_scores}")
        print(f"   Excellent (≥90): {excellent_scores}")
        print(f"   Number passing: {np.sum(passing_scores)}")
        print(f"   Number excellent: {np.sum(excellent_scores)}")
        
        # 4. Conditional operations
        print(f"\n4. Conditional Operations:")
        # Give everyone below 80 a boost to 80
        boosted_scores = np.where(test_scores < 80, 80, test_scores)
        print(f"   Boosted scores: {boosted_scores}")
        
        # 5. Array-to-array operations
        print(f"\n5. Array-to-Array Operations:")
        quiz_scores = np.array([88, 85, 82, 95, 90, 78, 92, 86, 84, 89])
        total_scores = test_scores + quiz_scores  # Element-wise addition
        average_scores = (test_scores + quiz_scores) / 2
        
        print(f"   Quiz scores: {quiz_scores}")
        print(f"   Total scores: {total_scores}")
        print(f"   Average scores: {average_scores}")
        
        # 6. Statistical operations
        print(f"\n6. Statistical Operations:")
        print(f"   Mean: {np.mean(test_scores):.2f}")
        print(f"   Median: {np.median(test_scores):.2f}")
        print(f"   Standard deviation: {np.std(test_scores):.2f}")
        print(f"   Min: {np.min(test_scores)}, Max: {np.max(test_scores)}")
        print(f"   25th percentile: {np.percentile(test_scores, 25):.2f}")
        print(f"   75th percentile: {np.percentile(test_scores, 75):.2f}")
        
    except NameError:
        print("NumPy not available. Install with: pip install numpy")

demonstrate_array_operations()

# =============================================================================
# PART 5: INDEXING AND SLICING - DATA EXTRACTION MASTERY
# =============================================================================

print("\n\nPART 4: Array Indexing and Slicing")
print("=" * 40)

def demonstrate_indexing_slicing():
    
    try:
        print("🔍 Indexing and Slicing (Data Extraction):\n")
        
        # 1D array indexing
        data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        print(f"📊 Sample data: {data}")
        
        print(f"\n1. Basic Indexing:")
        print(f"   First element: {data[0]}")
        print(f"   Last element: {data[-1]}")
        print(f"   Third element: {data[2]}")
        
        print(f"\n2. Slicing:")
        print(f"   First 3: {data[:3]}")
        print(f"   Last 3: {data[-3:]}")
        print(f"   Middle elements: {data[2:8]}")
        print(f"   Every other element: {data[::2]}")
        
        # 2D array indexing (like spreadsheet cells)
        print(f"\n3. 2D Array Indexing (Spreadsheet-like):")
        grades_2d = np.array([
            [85, 90, 88],  # Student 0
            [78, 82, 80],  # Student 1
            [92, 95, 89]   # Student 2
        ])
        print(f"   Grades matrix:\n{grades_2d}")
        print(f"   Student 0, Test 1: {grades_2d[0, 1]}")
        print(f"   All of Student 1's grades: {grades_2d[1, :]}")
        print(f"   Test 2 for all students: {grades_2d[:, 2]}")
        
        # Boolean indexing (advanced filtering)
        print(f"\n4. Boolean Indexing (Advanced Filtering):")
        data = np.array([85, 90, 78, 92, 88, 76, 94, 89])
        high_scores = data[data >= 90]  # Only scores 90 or above
        medium_scores = data[(data >= 80) & (data < 90)]  # Between 80-89
        
        print(f"   All scores: {data}")
        print(f"   High scores (≥90): {high_scores}")
        print(f"   Medium scores (80-89): {medium_scores}")
        
    except NameError:
        print("NumPy not available. Install with: pip install numpy")

demonstrate_indexing_slicing()

# =============================================================================
# STUDENT PERFORMANCE ANALYZER 
# =============================================================================

print("\n\n🎯 COMPLETE STUDENT PERFORMANCE ANALYZER")
print("=" * 50)

def create_sample_data():
    
    try:
        import numpy as np
        
        # Number of students
        num_students = 8
        student_ids = np.arange(1, num_students + 1)
        
        # Generate realistic score data
        np.random.seed(47)  # For consistent results
        
        # Test scores (2 tests per student)
        test_scores = np.random.randint(50, 100, (num_students, 2))
        
        # Assignment scores (3 assignments per student)  
        assignment_scores = np.random.randint(60, 90, (num_students, 3))
        
        # Calculate averages
        avg_test_score = np.mean(test_scores, axis=1)
        avg_assign_scores = np.mean(assignment_scores, axis=1)
        final_score = (avg_test_score + avg_assign_scores) / 2
        
        return {
            "student_ids": student_ids,
            "test_scores": test_scores,
            "assignment_scores": assignment_scores,
            "avg_test_score": avg_test_score,
            "avg_assign_scores": avg_assign_scores,
            "final_score": final_score
        }
        
    except NameError:
        print("NumPy not available for data generation")
        return None

def analyze_class_performance(data):
   
    if data is None:
        print("No data available for analysis")
        return
    
    try:
        final_score = data["final_score"]
        test_scores = data["test_scores"]
        assignment_scores = data["assignment_scores"]
        
        print("📊 CLASS PERFORMANCE ANALYSIS")
        print("=" * 40)
        
        # Basic statistics
        mean_scores = np.mean(final_score)
        median_score = np.median(final_score)
        std_score = np.std(final_score)
        
        print(f"🎯 Final Scores Statistics:")
        print(f"   Mean: {mean_scores:.2f}")
        print(f"   Median: {median_score:.2f}")
        print(f"   Standard Deviation: {std_score:.2f}")
        print(f"   Min: {np.min(final_score):.2f}, Max: {np.max(final_score):.2f}")
        print(f"   25th percentile: {np.percentile(final_score, 25):.2f}")
        print(f"   75th percentile: {np.percentile(final_score, 75):.2f}")
        
        # Grade classification using our boolean indexing skills
        print(f"\n🏆 Grade Classification:")
        excellent_90_scores = final_score >= 90
        good_scores = (final_score >= 80) & (final_score < 90)
        satisfactory_scores = (final_score >= 70) & (final_score < 80)
        needs_improvement_scores = final_score < 70
        
        print(f"   Students with Excellent Score (≥90): {np.sum(excellent_90_scores)}")
        print(f"   Students with Good Score (80-89): {np.sum(good_scores)}")
        print(f"   Students with Satisfactory Scores (70-79): {np.sum(satisfactory_scores)}")
        print(f"   Students need improvement (<70): {np.sum(needs_improvement_scores)}")
        
        # Performance comparison
        print(f"\n📝 Test vs Assignment Performance:")
        avg_test_performance = np.mean(data["avg_test_score"])
        avg_assignment_performance = np.mean(data["avg_assign_scores"])
        
        print(f"   Average test performance: {avg_test_performance:.2f}")
        print(f"   Average assignment performance: {avg_assignment_performance:.2f}")
        
        if avg_test_performance > avg_assignment_performance:
            print(f"   📈 Students perform better on tests")
        else:
            print(f"   📋 Students perform better on assignments")
        
        # Individual student analysis
        print(f"\n👥 Individual Student Analysis:")
        best_student_idx = np.argmax(final_score)
        worst_student_idx = np.argmin(final_score)
        
        print(f"   🏆 Top performer: Student {data['student_ids'][best_student_idx]} ({final_score[best_student_idx]:.2f})")
        print(f"   📈 Needs support: Student {data['student_ids'][worst_student_idx]} ({final_score[worst_student_idx]:.2f})")
        
        # Students close to next grade level
        close_to_passing = (final_score >= 65) & (final_score < 70)
        close_to_good = (final_score >= 75) & (final_score < 80)
        
        if np.sum(close_to_passing) > 0:
            print(f"   🎯 Students close to passing: {np.sum(close_to_passing)}")
        if np.sum(close_to_good) > 0:
            print(f"   🎯 Students close to good grade: {np.sum(close_to_good)}")
        
    except Exception as e:
        print(f"Error in analysis: {e}")

def demonstrate_numpy_speed():
    
    try:
        import time
        
        print(f"\n⚡ Speed Comparison: Python Lists vs NumPy Arrays")
        print("=" * 55)
        
        # Create large datasets
        size = 100000
        python_list = list(range(size))
        numpy_array = np.arange(size)
        
        print(f"🧪 Testing with {size:,} numbers...")
        
        # Time Python list operation
        start_time = time.time()
        python_result = [x * 2 + 1 for x in python_list]
        python_time = time.time() - start_time
        
        # Time NumPy operation  
        start_time = time.time()
        numpy_result = numpy_array * 2 + 1
        numpy_time = time.time() - start_time
        
        print(f"\n📊 Results:")
        print(f"   Python list time: {python_time:.4f} seconds")
        print(f"   NumPy array time: {numpy_time:.4f} seconds")
        print(f"   🚀 NumPy is {python_time/numpy_time:.1f}x faster!")
        
        # Memory comparison
        import sys
        python_memory = sys.getsizeof(python_list)
        numpy_memory = numpy_array.nbytes
        
        print(f"\n💾 Memory Usage:")
        print(f"   Python list: {python_memory:,} bytes")
        print(f"   NumPy array: {numpy_memory:,} bytes")
        print(f"   💡 NumPy uses {python_memory/numpy_memory:.1f}x less memory!")
        
    except NameError:
        print("Install NumPy to see the speed demonstration!")

# =============================================================================
# RUN THE COMPLETE ANALYSIS
# =============================================================================

def run_complete_numpy_demo():
    
    print(f"\n🚀 RUNNING COMPLETE NUMPY DEMONSTRATION")
    print("=" * 45)
    
    # Generate and analyze student data
    print("\n1. Generating student performance data...")
    student_data = create_sample_data()
    
    if student_data:
        print("✅ Data generated successfully!")
        
        print(f"\n2. Analyzing performance...")
        analyze_class_performance(student_data)
        
        print(f"\n3. Demonstrating NumPy speed advantages...")
        demonstrate_numpy_speed()
    
    print(f"\n🎉 NumPy demonstration complete!")
    print("💡 You now have the mathematical foundation for data science!")

# Run the complete demonstration
run_complete_numpy_demo()

print(f"\n🎉 Day 7 Complete!")
