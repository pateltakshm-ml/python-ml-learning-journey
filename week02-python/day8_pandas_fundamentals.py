# Day 8 Practice: Introduction to Pandas - Data Manipulation Powerhouse
# Learning Goals: Master DataFrames, data loading, filtering, and cleaning
# Recommended: Use Jupyter Lab for interactive exploration, then finalize in VS Code
# Time: 30 minutes

# =============================================================================
# PART 1: DATAFRAMES VS NUMPY - THE GAME CHANGER
# =============================================================================
import pandas as pd
import numpy as np
"""
Welcome to Day 8: Pandas DataFrames!

Pandas is built on NumPy but adds incredible functionality:
- Labeled data (row and column names)
- Automatic alignment of data
- Powerful data manipulation methods
- Built-in file I/O (CSV, Excel, JSON)
- Missing data handling
- Time series analysis

Think of it as upgrading from a calculator to a computer! 🚀
"""

print("=== DAY 8: PANDAS DATAFRAMES ===\n")

# First, let's install and import Pandas
try:
    import pandas as pd
    import numpy as np
    print("✅ Pandas is ready!")
    print(f"📦 Pandas version: {pd.__version__}")
    print(f"📦 NumPy version: {np.__version__}")
except ImportError:
    print("❌ Pandas not installed. Run: pip install pandas")
    print("💡 For this lesson, we'll show examples assuming Pandas is available")

# =============================================================================
# PART 2: YOUR FIRST DATAFRAME - LABELED DATA POWER
# =============================================================================

print("\nPART 1: DataFrames vs NumPy Arrays - The Revolution")
print("=" * 55)

def compare_numpy_vs_pandas():
    """
    Show the incredible difference between NumPy arrays and Pandas DataFrames.
    This demonstrates why every data scientist uses Pandas!
    """
    
    print("🐍 Your NumPy Way (Day 7):")

    try:
        # Student data as NumPy arrays
        student_names = np.array(['Alice', 'Bob', 'Charlie', 'Diana'])
        math_scores = np.array([85, 92, 78, 88])
        science_scores = np.array([90, 88, 82, 95])
        english_scores = np.array([78, 95, 89, 82])
        
        print(f"   Names: {student_names}")
        print(f"   Math:  {math_scores}")
        print(f"   Science: {science_scores}")
        print(f"   English: {english_scores}")
        print(f"   Average for Alice: {(math_scores[0] + science_scores[0] + english_scores[0]) / 3:.1f}")
        
        print(f"\n🚀 Pandas Way - The Data Science Standard:")
        
        # Pandas approach - organized, labeled, powerful!
        df = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
            'Math': [85, 92, 78, 88],
            'Science': [90, 88, 82, 95],
            'English': [78, 95, 89, 82]
        })
        
        print(f"   Complete DataFrame:")
        print(df)
        
        # Show the power of labeled data
        print(f"\n💡 Pandas Superpowers:")
        print(f"   Alice's average: {df[df['Name'] == 'Alice'][['Math', 'Science', 'English']].mean().mean():.1f}")
        print(f"   Class Math average: {df['Math'].mean():.1f}")
        print(f"   Students above 90 in any subject:")
        high_performers = df[(df['Math'] >= 90) | (df['Science'] >= 90) | (df['English'] >= 90)]
        print(high_performers[['Name']])
        
    except NameError:
        print("   (Pandas not available - install with: pip install pandas)")

compare_numpy_vs_pandas()

# =============================================================================
# PART 3: CREATING DATAFRAMES - MULTIPLE METHODS
# =============================================================================

print("\n\nPART 2: Creating DataFrames - Your Data Science Toolkit")
print("=" * 55)

def demonstrate_dataframe_creation():
    """
    Show all the ways to create DataFrames.
    These methods cover 95% of real data science scenarios.
    """
    
    try:
        print("🛠️  DataFrame Creation Methods:\n")
        
        # 1. From dictionary (most common)
        print("1. From Dictionary (Most Common):")
        student_dict = {
            'student_id': [1, 2, 3, 4],
            'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
            'age': [20, 19, 21, 20],
            'gpa': [3.8, 3.6, 3.2, 3.9],
            'major': ['CS', 'Math', 'Physics', 'CS']
        }
        df_dict = pd.DataFrame(student_dict)
        print(df_dict)
        print(f"   Shape: {df_dict.shape} (rows, columns)")
        
        # 2. From lists of lists
        print(f"\n2. From Lists of Lists:")
        student_data = [
            ['Alice', 20, 3.8, 'CS'],
            ['Bob', 19, 3.6, 'Math'],
            ['Charlie', 21, 3.2, 'Physics'],
            ['Diana', 20, 3.9, 'CS']
        ]
        df_lists = pd.DataFrame(student_data, 
                               columns=['name', 'age', 'gpa', 'major'])
        print(df_lists)
        
        # 3. From NumPy array (your skills transfer!)
        print(f"\n3. From NumPy Array (Your Skills Transfer!):")
        np_scores = np.random.randint(70, 100, (5, 3))
        df_numpy = pd.DataFrame(np_scores, 
                               columns=['Test1', 'Test2', 'Test3'],
                               index=['Student1', 'Student2', 'Student3', 'Student4', 'Student5'])
        print(df_numpy)
        
        # 4. From CSV file (real-world most common)
        print(f"\n4. From CSV File (Real-World Standard):")
        print("   # This is how you'll load real datasets:")
        print("   df = pd.read_csv('student_data.csv')")
        print("   # Pandas automatically handles headers, data types, etc.")
        
        # 5. Empty DataFrame for gradual building
        print(f"\n5. Empty DataFrame (For Gradual Building):")
        df_empty = pd.DataFrame(columns=['name', 'score', 'grade'])
        print(f"   Empty DataFrame: {df_empty}")
        print(f"   Shape: {df_empty.shape}")
        
        # 6. From range data (useful for time series)
        print(f"\n6. Date Range DataFrame (Time Series):")
        dates = pd.date_range('2024-01-01', periods=5, freq='D')
        df_dates = pd.DataFrame({
            'date': dates,
            'temperature': [20, 22, 19, 25, 23],
            'humidity': [60, 65, 70, 55, 58]
        })
        print(df_dates)
        
    except NameError:
        print("Pandas not available. Install with: pip install pandas")

demonstrate_dataframe_creation()

# =============================================================================
# PART 4: DATA EXPLORATION - YOUR DETECTIVE TOOLKIT
# =============================================================================

print("\n\nPART 3: Data Exploration - Detective Work")
print("=" * 45)

def demonstrate_data_exploration():
    """
    Master the essential DataFrame exploration methods.
    These are the first commands every data scientist runs!
    """
    
    try:
        print("🔍 Essential Data Exploration Methods:\n")
        
        # Create sample student dataset
        np.random.seed(42)
        n_students = 20
        
        sample_data = {
            'student_id': range(1, n_students + 1),
            'name': [f'Student_{i}' for i in range(1, n_students + 1)],
            'age': np.random.randint(18, 25, n_students),
            'gpa': np.round(np.random.uniform(2.0, 4.0, n_students), 2),
            'credits': np.random.randint(15, 150, n_students),
            'major': np.random.choice(['CS', 'Math', 'Physics', 'Biology', 'Chemistry'], n_students),
            'graduation_year': np.random.choice([2024, 2025, 2026, 2027], n_students)
        }
        
        df = pd.DataFrame(sample_data)
        
        # 1. First look at data
        print("1. First Look at Your Data:")
        print(f"   df.head() - First 5 rows:")
        print(df.head())
        
        print(f"\n   df.tail() - Last 5 rows:")
        print(df.tail())
        
        # 2. Data structure information
        print(f"\n2. Data Structure Information:")
        print(f"   df.shape: {df.shape} (rows, columns)")
        print(f"   df.columns: {list(df.columns)}")
        print(f"   df.dtypes:")
        print(df.dtypes)
        
        # 3. Statistical summary
        print(f"\n3. Statistical Summary:")
        print(f"   df.describe() - Numerical columns:")
        print(df.describe())
        
        # 4. Information about DataFrame
        print(f"\n4. DataFrame Information:")
        print(f"   df.info() shows data types and missing values:")
        print("   (In Jupyter, run df.info() to see full output)")
        
        # 5. Unique values and counts
        print(f"\n5. Unique Values and Counts:")
        print(f"   Major distribution:")
        print(df['major'].value_counts())
        
        print(f"\n   Unique majors: {df['major'].nunique()}")
        print(f"   All unique majors: {df['major'].unique()}")
        
        # 6. Basic statistics for specific columns
        print(f"\n6. Column-Specific Statistics:")
        print(f"   Average GPA: {df['gpa'].mean():.2f}")
        print(f"   GPA range: {df['gpa'].min():.2f} to {df['gpa'].max():.2f}")
        print(f"   Students above 3.5 GPA: {(df['gpa'] >= 3.5).sum()}")
        
    except NameError:
        print("Pandas not available. Install with: pip install pandas")

demonstrate_data_exploration()

# =============================================================================
# PART 5: FILTERING AND SELECTION - YOUR NUMPY SKILLS SUPERCHARGED
# =============================================================================

print("\n\nPART 4: Data Filtering and Selection")
print("=" * 40)

def demonstrate_filtering_selection():
    """
    Use your NumPy boolean indexing skills with the power of labeled data!
    This is where Pandas becomes incredibly powerful.
    """
    
    try:
        print("🎯 Filtering and Selection (Your NumPy Skills Enhanced!):\n")
        
        # Create sample data
        df = pd.DataFrame({
            'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
            'age': [20, 19, 21, 20, 22, 19],
            'gpa': [3.8, 3.2, 2.9, 3.9, 3.5, 2.8],
            'major': ['CS', 'Math', 'CS', 'Physics', 'CS', 'Biology'],
            'credits': [90, 75, 60, 110, 95, 45]
        })
        
        print("📊 Sample Dataset:")
        print(df)
        
        # 1. Column selection
        print(f"\n1. Column Selection:")
        print(f"   Single column: df['name']")
        print(df['name'])
        
        print(f"\n   Multiple columns: df[['name', 'gpa']]")
        print(df[['name', 'gpa']])
        
        # 2. Row selection by index
        print(f"\n2. Row Selection:")
        print(f"   First row: df.iloc[0]")
        print(df.iloc[0])
        
        print(f"\n   First 3 rows: df.iloc[:3]")
        print(df.iloc[:3])
        
        # 3. Boolean filtering (your NumPy skills!)
        print(f"\n3. Boolean Filtering (Your NumPy Skills Enhanced!):")
        
        # High GPA students
        high_gpa = df[df['gpa'] >= 3.5]
        print(f"   Students with GPA >= 3.5:")
        print(high_gpa[['name', 'gpa']])
        
        # CS majors
        cs_students = df[df['major'] == 'CS']
        print(f"\n   CS majors:")
        print(cs_students[['name', 'major', 'gpa']])
        
        # Complex conditions (multiple criteria)
        print(f"\n4. Complex Filtering (Multiple Conditions):")
        
        # CS majors with high GPA
        cs_high_gpa = df[(df['major'] == 'CS') & (df['gpa'] >= 3.5)]
        print(f"   CS majors with GPA >= 3.5:")
        print(cs_high_gpa[['name', 'major', 'gpa']])
        
        # Students ready to graduate (high credits) OR high GPA
        graduation_ready = df[(df['credits'] >= 90) | (df['gpa'] >= 3.8)]
        print(f"\n   Students ready to graduate (90+ credits OR 3.8+ GPA):")
        print(graduation_ready[['name', 'credits', 'gpa']])
        
        # 5. String operations
        print(f"\n5. String Operations:")
        
        # Names starting with specific letter
        names_with_c = df[df['name'].str.startswith('C')]
        print(f"   Names starting with 'C':")
        print(names_with_c['name'])
        
        # 6. Sorting
        print(f"\n6. Sorting Data:")
        
        # Sort by GPA (highest first)
        sorted_by_gpa = df.sort_values('gpa', ascending=False)
        print(f"   Students sorted by GPA (highest first):")
        print(sorted_by_gpa[['name', 'gpa']])
        
        # 7. Aggregation by groups
        print(f"\n7. Group Analysis:")
        
        # Average GPA by major
        major_stats = df.groupby('major')['gpa'].mean().sort_values(ascending=False)
        print(f"   Average GPA by major:")
        print(major_stats)
        
    except NameError:
        print("Pandas not available. Install with: pip install pandas")

demonstrate_filtering_selection()

# =============================================================================
# TODAY'S PROJECT: STUDENT GRADE MANAGEMENT SYSTEM
# =============================================================================

print("\n\n🎯 TODAY'S PROJECT: Pandas Student Grade Management System")
print("=" * 65)

"""
BUILD A COMPREHENSIVE STUDENT MANAGEMENT SYSTEM

Your task: Create a powerful grade management tool using Pandas that:
1. Loads student data from multiple sources
2. Performs advanced filtering and analysis
3. Handles missing data and data cleaning
4. Generates detailed reports and insights
5. Exports results in multiple formats

This project demonstrates real-world Pandas usage!
"""

def load_student_data():
    np.random.seed(42)

    student_data = {
        'student_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010,
                      1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020],
        
        'name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince', 'Eve Davis',
                'Frank Miller', 'Grace Chen', 'Henry Wilson', 'Ivy Martinez', 'Jack Taylor',
                'Kate Anderson', 'Leo Garcia', 'Maya Patel', 'Noah Kim', 'Olivia White',
                'Paul Rodriguez', 'Quinn Thompson', 'Ruby Lee', 'Sam Jackson', 'Tina Clark'],
        
        'age': [19, 20, 21, 19, 22, 20, 18, 21, 19, 20,
               23, 19, 20, 21, 19, 22, 20, 18, 21, 20],
        
        'major': ['Computer Science', 'Mathematics', 'Physics', 'Computer Science', 'Biology',
                 'Mathematics', 'Chemistry', 'Physics', 'Computer Science', 'Biology',
                 'Engineering', 'Computer Science', 'Mathematics', 'Chemistry', 'Physics',
                 'Biology', 'Engineering', 'Computer Science', 'Mathematics', 'Chemistry'],
        
        'gpa': [3.8, 3.2, 2.9, 3.9, 3.5, 2.8, 3.7, 3.1, 3.6, 3.4,
               3.0, 3.8, 3.3, 2.7, 3.5, 3.2, 3.9, 3.1, 2.9, 3.6],
        
        'credits_completed': [90, 75, 60, 110, 95, 45, 85, 70, 80, 65,
                            55, 100, 88, 50, 92, 78, 105, 72, 58, 96],
        
        'graduation_year': [2024, 2025, 2026, 2024, 2024, 2027, 2025, 2026, 2025, 2026,
                          2027, 2024, 2025, 2027, 2024, 2025, 2024, 2026, 2027, 2024],
        
        # Test scores (3 tests)
        'test1_score': [85, 78, 72, 92, 88, 65, 89, 75, 82, 77,
                       68, 90, 81, 63, 87, 79, 94, 74, 70, 86],
        
        'test2_score': [88, 82, None, 89, 91, 70, 85, 78, 85, 80,
                       72, 88, 84, None, 90, 82, 92, 77, 73, 89],  # Some missing values
        
        'test3_score': [92, 79, 75, 95, 89, 68, 91, 80, 87, 82,
                       70, 92, 86, 65, 88, 84, 96, 79, 75, 91],
        
        # Assignment scores (5 assignments, out of 100)
        'assignment1': [95, 85, 80, 98, 92, 75, 94, 82, 88, 85,
                       78, 96, 89, 72, 91, 86, 97, 83, 79, 93],
        
        'assignment2': [90, 88, None, 94, 89, 78, 91, 85, 90, 87,
                       80, 92, 91, None, 93, 89, 95, 86, 81, 92],  # Some missing values
        
        'assignment3': [88, 82, 85, 91, 87, 72, 89, 80, 85, 83,
                       75, 90, 87, 70, 89, 84, 92, 81, 77, 88],
        
        'assignment4': [92, 86, 78, 96, 90, 74, 93, 83, 89, 86,
                       79, 94, 90, 73, 92, 87, 98, 84, 80, 91],
        
        'assignment5': [89, 84, None, 93, 88, 76, 90, 81, 87, 84,
                       77, 91, 88, 71, 90, 85, 95, 82, 78, 89],  # Some missing values
        
        # Additional information
        'scholarship': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No',
                       'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes'],
        
        'hometown_state': ['CA', 'TX', 'NY', 'CA', 'FL', 'TX', 'WA', 'NY', 'CA', 'FL',
                          'TX', 'CA', 'WA', 'NY', 'FL', 'TX', 'CA', 'WA', 'NY', 'FL'],
        
        'part_time_job': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes',
                         'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No'],
        
        # Email addresses
        'email': [f"{name.lower().replace(' ', '.')}@university.edu" 
                 for name in ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince', 'Eve Davis',
                            'Frank Miller', 'Grace Chen', 'Henry Wilson', 'Ivy Martinez', 'Jack Taylor',
                            'Kate Anderson', 'Leo Garcia', 'Maya Patel', 'Noah Kim', 'Olivia White',
                            'Paul Rodriguez', 'Quinn Thompson', 'Ruby Lee', 'Sam Jackson', 'Tina Clark']]
    }

    df = pd.DataFrame(student_data)

    # Create DataFrame
    df = pd.DataFrame(student_data)
    
    # IMP : Add intentional data quality issues for cleaning practice
    
    # 1. Invalid GPA values (should be 0.0-4.0)
    df.loc[5, 'gpa'] = 4.5  # Too high
    df.loc[12, 'gpa'] = -0.1  # Negative
    
    # 2. Inconsistent major names
    df.loc[8, 'major'] = 'Comp Sci'  # Should be "Computer Science"
    df.loc[15, 'major'] = 'Bio'      # Should be "Biology"
    
    # 3. Missing scholarship information
    df.loc[3, 'scholarship'] = None
    df.loc[10, 'scholarship'] = None
    
    # 4. Unusual age values
    df.loc[7, 'age'] = 16  # Too young for typical college
    df.loc[14, 'age'] = 35  # Older student (valid but unusual)
    
    # 5. Invalid email format
    df.loc[9, 'email'] = 'invalid-email'  # Missing @university.edu
    
    # Display summary information
    print("📊 STUDENT DATASET LOADED SUCCESSFULLY!")
    print("=" * 45)
    print(f"📈 Dataset Shape: {df.shape} (rows, columns)")
    print(f"👥 Number of Students: {len(df)}")
    print(f"📋 Number of Columns: {len(df.columns)}")
    
    print(f"\n🔍 COLUMN OVERVIEW:")
    print(f"  Basic Info: student_id, name, age, email")
    print(f"  Academic: major, gpa, credits_completed, graduation_year")
    print(f"  Assessments: 3 tests + 5 assignments")
    print(f"  Demographics: scholarship, hometown_state, part_time_job")
    
    print(f"\n  DATA QUALITY ISSUES INCLUDED (for cleaning practice):")
    print(f"  Missing values in test2_score, assignment2, assignment5")
    print(f"  Invalid GPA values (4.5, -0.1)")
    print(f"  Inconsistent major names ('Comp Sci', 'Bio')")
    print(f"  Missing scholarship information")
    print(f"  Unusual age values (16, 35)")
    print(f"  Invalid email format")
    
    print(f"\n📊 FIRST 5 ROWS:")
    print(df.head())
    
    print(f"\n✅ Ready for data cleaning and analysis!")
    
    return df


# Test the function
if __name__ == "__main__":
    # Load the data
    student_df = load_student_data()
    
    # Quick data exploration
    print(f"\n📈 QUICK DATA EXPLORATION:")
    print(f"   Data types:\n{student_df.dtypes}")
    
    print(f"\n   Missing values per column:")
    missing_values = student_df.isnull().sum()
    print(missing_values[missing_values > 0])
    
    print(f"\n   GPA statistics:")
    print(student_df['gpa'].describe())
    
    print(f"\n   Major distribution:")
    print(student_df['major'].value_counts())





def clean_student_data_complete(df):
    """
    Complete data cleaning function for messy student data.
    Handles all common data quality issues step by step.
    """
    
    print("🧹 COMPLETE DATA CLEANING PROCESS")
    print("=" * 40)
    
    # Work on a copy to preserve original data
    df_clean = df.copy()
    
    print(f"Starting with {len(df_clean)} students and {len(df_clean.columns)} columns")
    print(f"Initial missing values:\n{df_clean.isnull().sum()}")
    
    # =========================================================================
    # STEP 1: HANDLE MISSING VALUES
    # =========================================================================
    
    print(f"\n1️⃣  HANDLING MISSING VALUES")
    print("-" * 30)
    
    # Fix missing names
    print("Fixing missing names...")
    df_clean['name'] = df_clean['name'].replace('', 'Unknown Student')
    df_clean['name'] = df_clean['name'].fillna('Unknown Student')
    
    # Fix missing ages - use median of valid ages
    print("Fixing missing ages...")
    valid_ages = df_clean['age'][(df_clean['age'] >= 16) & (df_clean['age'] <= 30)]
    median_age = valid_ages.median()
    df_clean['age'] = df_clean['age'].fillna(median_age)
    print(f"   Filled missing ages with median: {median_age}")
    
    # Fix missing GPAs - use mean of valid GPAs
    print("Fixing missing GPAs...")
    valid_gpas = df_clean['gpa'][(df_clean['gpa'] >= 0.0) & (df_clean['gpa'] <= 4.0)]
    mean_gpa = valid_gpas.mean()
    df_clean['gpa'] = df_clean['gpa'].fillna(mean_gpa)
    print(f"   Filled missing GPAs with mean: {mean_gpa:.2f}")
    
    # Fix missing test scores
    print("Fixing missing test scores...")
    mean_test = df_clean['test_score'].mean()
    df_clean['test_score'] = df_clean['test_score'].fillna(mean_test)
    print(f"   Filled missing test scores with mean: {mean_test:.1f}")
    
    # Fix missing emails and scholarship info
    print("Fixing missing emails and scholarship...")
    df_clean['email'] = df_clean['email'].replace('', 'no-email@university.edu')
    df_clean['email'] = df_clean['email'].fillna('no-email@university.edu')
    df_clean['scholarship'] = df_clean['scholarship'].replace('', 'No')
    df_clean['scholarship'] = df_clean['scholarship'].fillna('No')
    
    # =========================================================================
    # STEP 2: FIX INVALID VALUES
    # =========================================================================
    
    print(f"\n2️⃣  FIXING INVALID VALUES")
    print("-" * 25)
    
    # Fix invalid ages
    print("Fixing invalid ages...")
    before_age_fix = len(df_clean[(df_clean['age'] < 16) | (df_clean['age'] > 30)])
    df_clean.loc[df_clean['age'] < 16, 'age'] = median_age
    df_clean.loc[df_clean['age'] > 30, 'age'] = median_age
    print(f"   Fixed {before_age_fix} invalid ages")
    
    # Fix invalid GPAs
    print("Fixing invalid GPAs...")
    # Cap GPAs above 4.0
    high_gpa_count = len(df_clean[df_clean['gpa'] > 4.0])
    df_clean.loc[df_clean['gpa'] > 4.0, 'gpa'] = 4.0
    
    # Fix negative GPAs
    negative_gpa_count = len(df_clean[df_clean['gpa'] < 0.0])
    df_clean.loc[df_clean['gpa'] < 0.0, 'gpa'] = 0.0
    
    print(f"   Fixed {high_gpa_count} GPAs above 4.0")
    print(f"   Fixed {negative_gpa_count} negative GPAs")
    
    # Fix invalid credits
    print("Fixing invalid credits...")
    # Fix negative credits
    df_clean.loc[df_clean['credits'] < 0, 'credits'] = 0
    
    # Fix impossibly high credits (assume max 200)
    df_clean.loc[df_clean['credits'] > 200, 'credits'] = 120  # Typical for seniors
    
    invalid_credits = len(df_clean[(df_clean['credits'] < 0) | (df_clean['credits'] > 200)])
    print(f"   Fixed invalid credit values")
    
    # =========================================================================
    # STEP 3: STANDARDIZE FORMATS
    # =========================================================================
    
    print(f"\n3️⃣  STANDARDIZING FORMATS")
    print("-" * 25)
    
    # Standardize major names
    print("Standardizing major names...")
    major_mapping = {
        'CS': 'Computer Science',
        'comp sci': 'Computer Science',
        'COMPUTER SCIENCE': 'Computer Science',
        'Math': 'Mathematics',
        'Bio': 'Biology'
    }
    df_clean['major'] = df_clean['major'].replace(major_mapping)
    print(f"   Standardized major names")
    print(f"   Unique majors now: {df_clean['major'].unique()}")
    
    # Standardize scholarship values
    print("Standardizing scholarship values...")
    scholarship_mapping = {
        'YES': 'Yes',
        'yes': 'Yes',
        'NO': 'No',
        'no': 'No'
    }
    df_clean['scholarship'] = df_clean['scholarship'].replace(scholarship_mapping)
    print(f"   Scholarship values now: {df_clean['scholarship'].unique()}")
    
    # Fix email formats
    print("Fixing email formats...")
    # Replace invalid email formats
    invalid_email_mask = ~df_clean['email'].str.contains('@university.edu', na=False)
    df_clean.loc[invalid_email_mask, 'email'] = 'corrected@university.edu'
    print(f"   Fixed invalid email formats")
    
    # =========================================================================
    # STEP 4: DATA TYPE CONVERSIONS
    # =========================================================================
    
    print(f"\n4️⃣  CONVERTING DATA TYPES")
    print("-" * 25)
    
    # Ensure numeric columns are properly typed
    df_clean['age'] = pd.to_numeric(df_clean['age'], errors='coerce')
    df_clean['gpa'] = pd.to_numeric(df_clean['gpa'], errors='coerce')
    df_clean['test_score'] = pd.to_numeric(df_clean['test_score'], errors='coerce')
    df_clean['credits'] = pd.to_numeric(df_clean['credits'], errors='coerce')
    
    # Ensure string columns are properly typed
    df_clean['name'] = df_clean['name'].astype(str)
    df_clean['major'] = df_clean['major'].astype(str)
    df_clean['email'] = df_clean['email'].astype(str)
    df_clean['scholarship'] = df_clean['scholarship'].astype(str)
    
    print("   Converted all columns to appropriate data types")
    
    # =========================================================================
    # STEP 5: FINAL VALIDATION
    # =========================================================================
    
    print(f"\n5️⃣  FINAL VALIDATION")
    print("-" * 20)
    
    # Check for remaining issues
    print("Final data quality check:")
    print(f"   Missing values: {df_clean.isnull().sum().sum()}")
    print(f"   Invalid ages: {len(df_clean[(df_clean['age'] < 16) | (df_clean['age'] > 30)])}")
    print(f"   Invalid GPAs: {len(df_clean[(df_clean['gpa'] < 0) | (df_clean['gpa'] > 4.0)])}")
    print(f"   Invalid credits: {len(df_clean[(df_clean['credits'] < 0) | (df_clean['credits'] > 200)])}")
    
    # Summary statistics
    print(f"\n📊 CLEANED DATA SUMMARY:")
    print(f"   Shape: {df_clean.shape}")
    print(f"   Age range: {df_clean['age'].min():.0f} - {df_clean['age'].max():.0f}")
    print(f"   GPA range: {df_clean['gpa'].min():.2f} - {df_clean['gpa'].max():.2f}")
    print(f"   Test score range: {df_clean['test_score'].min():.0f} - {df_clean['test_score'].max():.0f}")
    
    print(f"\n✅ DATA CLEANING COMPLETE!")
    print("=" * 40)
    
    return df_clean


def compare_before_after(original_df, cleaned_df):
    """
    Compare original and cleaned data to see the improvements.
    """
    
    print("🔍 BEFORE vs AFTER COMPARISON")
    print("=" * 35)
    
    print("BEFORE CLEANING:")
    print(f"Missing values:\n{original_df.isnull().sum()}")
    print(f"\nUnique majors: {original_df['major'].unique()}")
    print(f"Scholarship values: {original_df['scholarship'].unique()}")
    print(f"Age range: {original_df['age'].min()} - {original_df['age'].max()}")
    print(f"GPA range: {original_df['gpa'].min()} - {original_df['gpa'].max()}")
    
    print(f"\nAFTER CLEANING:")
    print(f"Missing values:\n{cleaned_df.isnull().sum()}")
    print(f"\nUnique majors: {cleaned_df['major'].unique()}")
    print(f"Scholarship values: {cleaned_df['scholarship'].unique()}")
    print(f"Age range: {cleaned_df['age'].min():.0f} - {cleaned_df['age'].max():.0f}")
    print(f"GPA range: {cleaned_df['gpa'].min():.2f} - {cleaned_df['gpa'].max():.2f}")
    






def analyze_performance_by_demographics(df):
    """
    Analyze student performance across different demographic groups.
    """
    print("📊 DEMOGRAPHIC PERFORMANCE ANALYSIS")
    print("=" * 40)
    
    # 1. Performance by Major
    print("1️⃣  PERFORMANCE BY MAJOR")
    print("-" * 25)
    
    major_stats = df.groupby('major').agg({
        'overall_average': ['mean', 'median', 'std', 'count'],
        'gpa': ['mean', 'median'],
        'avg_test_score': 'mean',
        'avg_assignment_score': 'mean'
    }).round(2)
    
    print("Overall average by major:")
    print(major_stats['overall_average'].sort_values('mean', ascending=False))
    
    # Find best and worst performing majors
    best_major = major_stats['overall_average']['mean'].idxmax()
    worst_major = major_stats['overall_average']['mean'].idxmin()
    
    print(f"\n🏆 Best performing major: {best_major}")
    print(f"📉 Needs improvement: {worst_major}")
    
    # 2. Performance by Age Group
    print(f"\n2️⃣  PERFORMANCE BY AGE GROUP")
    print("-" * 30)
    
    # Create age groups
    df['age_group'] = pd.cut(df['age'], bins=[17, 19, 21, 23, 25], 
                            labels=['18-19', '20-21', '22-23', '24-25'])
    
    age_stats = df.groupby('age_group').agg({
        'overall_average': ['mean', 'count'],
        'gpa': 'mean',
        'credits_completed': 'mean'
    }).round(2)
    
    print("Performance by age group:")
    print(age_stats)
    
    # 3. Scholarship vs Non-Scholarship Students
    print(f"\n3️⃣  SCHOLARSHIP ANALYSIS")
    print("-" * 25)
    
    scholarship_stats = df.groupby('scholarship').agg({
        'overall_average': ['mean', 'median', 'std'],
        'gpa': ['mean', 'median'],
        'credits_completed': 'mean'
    }).round(2)
    
    print("Scholarship vs Non-scholarship performance:")
    print(scholarship_stats)
    
    # Statistical test for significance
    scholarship_yes = df[df['scholarship'] == 'Yes']['overall_average']
    scholarship_no = df[df['scholarship'] == 'No']['overall_average']
    
    print(f"\nScholarship students average: {scholarship_yes.mean():.2f}")
    print(f"Non-scholarship students average: {scholarship_no.mean():.2f}")
    print(f"Difference: {scholarship_yes.mean() - scholarship_no.mean():.2f} points")
    
    # 4. Part-time Job Impact
    print(f"\n4️⃣  PART-TIME JOB IMPACT")
    print("-" * 25)
    
    job_stats = df.groupby('part_time_job').agg({
        'overall_average': ['mean', 'std'],
        'gpa': 'mean',
        'avg_test_score': 'mean',
        'avg_assignment_score': 'mean'
    }).round(2)
    
    print("Part-time job impact on performance:")
    print(job_stats)
    
    # 5. State-wise Analysis
    print(f"\n5️⃣  GEOGRAPHIC ANALYSIS")
    print("-" * 25)
    
    state_stats = df.groupby('hometown_state').agg({
        'overall_average': ['mean', 'count'],
        'scholarship': lambda x: (x == 'Yes').sum()
    }).round(2)
    
    # Only show states with more than 1 student
    state_stats_filtered = state_stats[state_stats['overall_average']['count'] > 1]
    print("Performance by state (states with >1 student):")
    print(state_stats_filtered.sort_values(('overall_average', 'mean'), ascending=False))
    
    # 6. Gender Analysis
    print(f"\n6️⃣  GENDER ANALYSIS")
    print("-" * 20)
    
    gender_stats = df.groupby('gender').agg({
        'overall_average': ['mean', 'median', 'count'],
        'gpa': 'mean',
        'major': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'N/A'
    }).round(2)
    
    print("Performance by gender:")
    print(gender_stats)
    
    return {
        'major_stats': major_stats,
        'age_stats': age_stats,
        'scholarship_stats': scholarship_stats,
        'job_stats': job_stats,
        'state_stats': state_stats,
        'gender_stats': gender_stats
    }


def generate_student_reports(df):
    """
    Generate individual student progress reports.
    """
    print("📋 INDIVIDUAL STUDENT REPORTS")
    print("=" * 35)
    
    # Add performance categories
    df['performance_category'] = pd.cut(df['overall_average'], 
                                       bins=[0, 70, 80, 90, 100], 
                                       labels=['Needs Improvement', 'Satisfactory', 'Good', 'Excellent'])
    
    # Add grade letter
    def assign_letter_grade(score):
        if score >= 97: return 'A+'
        elif score >= 93: return 'A'
        elif score >= 90: return 'A-'
        elif score >= 87: return 'B+'
        elif score >= 83: return 'B'
        elif score >= 80: return 'B-'
        elif score >= 77: return 'C+'
        elif score >= 73: return 'C'
        elif score >= 70: return 'C-'
        elif score >= 67: return 'D+'
        elif score >= 65: return 'D'
        else: return 'F'
    
    df['letter_grade'] = df['overall_average'].apply(assign_letter_grade)
    
    # Generate reports for top 5 and bottom 5 students
    df_sorted = df.sort_values('overall_average', ascending=False)
    
    print("🏆 TOP 5 PERFORMERS:")
    print("-" * 20)
    
    for i, (idx, student) in enumerate(df_sorted.head().iterrows(), 1):
        print(f"\n{i}. {student['name']} (ID: {student['student_id']})")
        print(f"   Overall Average: {student['overall_average']:.1f} ({student['letter_grade']})")
        print(f"   Major: {student['major']}, GPA: {student['gpa']}")
        print(f"   Test Average: {student['avg_test_score']:.1f}")
        print(f"   Assignment Average: {student['avg_assignment_score']:.1f}")
        print(f"   Scholarship: {student['scholarship']}")
        print(f"   Performance: {student['performance_category']}")
    
    print(f"\n📉 STUDENTS NEEDING SUPPORT:")
    print("-" * 30)
    
    struggling_students = df[df['overall_average'] < 75].sort_values('overall_average')
    
    for idx, student in struggling_students.iterrows():
        print(f"\n• {student['name']} (ID: {student['student_id']})")
        print(f"   Overall Average: {student['overall_average']:.1f} ({student['letter_grade']})")
        print(f"   Weakest Area: {'Tests' if student['avg_test_score'] < student['avg_assignment_score'] else 'Assignments'}")
        print(f"   Test Avg: {student['avg_test_score']:.1f}, Assignment Avg: {student['avg_assignment_score']:.1f}")
        
        # Recommendations
        if student['avg_test_score'] < 70:
            print("   📝 Recommendation: Focus on test preparation and study strategies")
        if student['avg_assignment_score'] < 70:
            print("   📚 Recommendation: Improve assignment submission quality and timeliness")
        if student['part_time_job'] == 'Yes' and student['overall_average'] < 70:
            print("   ⚖️  Recommendation: Consider reducing work hours to focus on studies")
    
    # Generate class summary
    print(f"\n📊 CLASS SUMMARY REPORT:")
    print("-" * 25)
    
    total_students = len(df)
    excellent = len(df[df['performance_category'] == 'Excellent'])
    good = len(df[df['performance_category'] == 'Good'])
    satisfactory = len(df[df['performance_category'] == 'Satisfactory'])
    needs_improvement = len(df[df['performance_category'] == 'Needs Improvement'])
    
    print(f"Total Students: {total_students}")
    print(f"Excellent (90-100): {excellent} ({excellent/total_students*100:.1f}%)")
    print(f"Good (80-89): {good} ({good/total_students*100:.1f}%)")
    print(f"Satisfactory (70-79): {satisfactory} ({satisfactory/total_students*100:.1f}%)")
    print(f"Needs Improvement (<70): {needs_improvement} ({needs_improvement/total_students*100:.1f}%)")
    
    print(f"\nClass Average: {df['overall_average'].mean():.1f}")
    print(f"Class Median: {df['overall_average'].median():.1f}")
    print(f"Standard Deviation: {df['overall_average'].std():.1f}")
    
    return df


def export_results(df, filename_base="student_analysis"):
    """
    Export processed data and analysis results to multiple formats.
    """
    print("💾 EXPORTING RESULTS")
    print("=" * 20)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 1. Export main dataset to CSV
    csv_filename = f"{filename_base}_{timestamp}.csv"
    df.to_csv(csv_filename, index=False)
    print(f"✅ Exported main data to: {csv_filename}")
    
    # 2. Export to Excel with multiple sheets
    excel_filename = f"{filename_base}_{timestamp}.xlsx"
    
    with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
        # Main data
        df.to_excel(writer, sheet_name='Student_Data', index=False)
        
        # Summary statistics
        summary_stats = df.describe()
        summary_stats.to_excel(writer, sheet_name='Summary_Statistics')
        
        # Performance by major
        major_summary = df.groupby('major').agg({
            'overall_average': ['mean', 'median', 'std', 'count'],
            'gpa': 'mean'
        }).round(2)
        major_summary.to_excel(writer, sheet_name='Performance_by_Major')
        
        # Scholarship analysis
        scholarship_summary = df.groupby('scholarship').agg({
            'overall_average': ['mean', 'median', 'count'],
            'gpa': 'mean'
        }).round(2)
        scholarship_summary.to_excel(writer, sheet_name='Scholarship_Analysis')
        
        # Top performers
        top_performers = df.nlargest(10, 'overall_average')[['name', 'major', 'overall_average', 'gpa', 'letter_grade']]
        top_performers.to_excel(writer, sheet_name='Top_Performers', index=False)
        
        # Students needing support
        needs_support = df[df['overall_average'] < 75][['name', 'major', 'overall_average', 'avg_test_score', 'avg_assignment_score']]
        needs_support.to_excel(writer, sheet_name='Needs_Support', index=False)
    
    print(f"✅ Exported detailed analysis to: {excel_filename}")
    
    # 3. Export grade distribution
    grade_dist_filename = f"grade_distribution_{timestamp}.csv"
    grade_distribution = df['letter_grade'].value_counts().sort_index()
    grade_distribution.to_csv(grade_dist_filename, header=['Count'])
    print(f"✅ Exported grade distribution to: {grade_dist_filename}")
    
    # 4. Export summary report
    report_filename = f"summary_report_{timestamp}.txt"
    
    with open(report_filename, 'w') as f:
        f.write("STUDENT PERFORMANCE SUMMARY REPORT\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Students: {len(df)}\n\n")
        
        f.write("OVERALL STATISTICS:\n")
        f.write(f"Class Average: {df['overall_average'].mean():.2f}\n")
        f.write(f"Class Median: {df['overall_average'].median():.2f}\n")
        f.write(f"Standard Deviation: {df['overall_average'].std():.2f}\n")
        f.write(f"Highest Score: {df['overall_average'].max():.2f}\n")
        f.write(f"Lowest Score: {df['overall_average'].min():.2f}\n\n")
        
        f.write("PERFORMANCE DISTRIBUTION:\n")
        performance_dist = df['performance_category'].value_counts()
        for category, count in performance_dist.items():
            percentage = count / len(df) * 100
            f.write(f"{category}: {count} students ({percentage:.1f}%)\n")
        
        f.write(f"\nTOP MAJOR BY PERFORMANCE:\n")
        top_major = df.groupby('major')['overall_average'].mean().idxmax()
        top_major_avg = df.groupby('major')['overall_average'].mean().max()
        f.write(f"{top_major}: {top_major_avg:.2f} average\n")
    
    print(f"✅ Exported summary report to: {report_filename}")
    
    return {
        'csv_file': csv_filename,
        'excel_file': excel_filename,
        'grade_dist_file': grade_dist_filename,
        'report_file': report_filename
    }


def run_complete_analysis():
    """
    Run the complete student grade management system analysis.
    """
    print("🎯 COMPLETE STUDENT GRADE MANAGEMENT SYSTEM")
    print("=" * 50)
    
    # Step 1: Load data
    print("\n1️⃣  LOADING DATA...")
    df = load_student_data()
    print(f"Loaded {len(df)} students with {len(df.columns)} columns")
    
    # Step 2: Clean data
    print(f"\n2️⃣  CLEANING DATA...")
    df_clean = clean_student_data(df)
    
    # Step 3: Demographic analysis
    print(f"\n3️⃣  DEMOGRAPHIC ANALYSIS...")
    demo_results = analyze_performance_by_demographics(df_clean)
    
    # Step 4: Generate reports
    print(f"\n4️⃣  GENERATING STUDENT REPORTS...")
    df_with_reports = generate_student_reports(df_clean)
    
    # Step 5: Export results
    print(f"\n5️⃣  EXPORTING RESULTS...")
    export_files = export_results(df_with_reports)
    
    print(f"\n🎉 ANALYSIS COMPLETE!")
    print("=" * 25)
    print("Files generated:")
    for file_type, filename in export_files.items():
        print(f"  • {filename}")
    
    return df_with_reports, demo_results, export_files


# BONUS: Advanced Pandas Techniques for Practice
def advanced_pandas_techniques(df):
    """
    Demonstrate advanced Pandas techniques for further practice.
    """
    print("🚀 ADVANCED PANDAS TECHNIQUES")
    print("=" * 35)
    
    # 1. Pivot Tables
    print("1️⃣  PIVOT TABLES")
    print("-" * 15)
    
    pivot_table = pd.pivot_table(df, 
                                values='overall_average', 
                                index='major', 
                                columns='scholarship',
                                aggfunc=['mean', 'count'],
                                fill_value=0)
    print("Performance by Major and Scholarship Status:")
    print(pivot_table)
    
    # 2. Cross-tabulation
    print(f"\n2️⃣  CROSS-TABULATION")
    print("-" * 20)
    
    crosstab = pd.crosstab(df['major'], df['performance_category'], margins=True)
    print("Major vs Performance Category:")
    print(crosstab)
    
    # 3. Window functions
    print(f"\n3️⃣  WINDOW FUNCTIONS")
    print("-" * 20)
    
    # Rank students within their major
    df['rank_in_major'] = df.groupby('major')['overall_average'].rank(ascending=False)
    
    # Calculate rolling average (useful for time series)
    df_sorted = df.sort_values('student_id')
    df_sorted['rolling_avg'] = df_sorted['overall_average'].rolling(window=3).mean()
    
    print("Top student in each major:")
    top_in_major = df[df['rank_in_major'] == 1][['name', 'major', 'overall_average']]
    print(top_in_major)
    
    # 4. String operations
    print(f"\n4️⃣  STRING OPERATIONS")
    print("-" * 20)
    
    # Extract information from names
    df['name_length'] = df['name'].str.len()
    df['first_name'] = df['name'].str.split('_').str[0]
    
    # Filter using string methods
    students_with_long_names = df[df['name'].str.len() > 10]
    print(f"Students with names longer than 10 characters: {len(students_with_long_names)}")
    
    # 5. Date operations (bonus)
    print(f"\n5️⃣  DATE OPERATIONS")
    print("-" * 18)
    
    # Create graduation dates
    df['graduation_date'] = pd.to_datetime(df['graduation_year'].astype(str) + '-05-15')
    df['days_to_graduation'] = (df['graduation_date'] - pd.Timestamp.now()).dt.days
    
    print("Students graduating soonest:")
    soon_graduates = df.nsmallest(5, 'days_to_graduation')[['name', 'graduation_date', 'days_to_graduation']]
    print(soon_graduates)
    
    return df



# Test your functions here
print("\n🧪 Testing Your Pandas Management System:")
print("Complete the functions above, then run:")
print("df = load_student_data()")
print("clean_df = clean_student_data(df)")
print("analyze_performance_by_demographics(clean_df)")

def demonstrate_pandas_numpy_integration():
    """
    Show how Pandas builds on NumPy and when to use each.
    """
    
    try:
        print(f"\n⚡ Pandas + NumPy Integration")
        print("=" * 35)
        
        # Create DataFrame
        df = pd.DataFrame({
            'scores': [85, 90, 78, 92, 88, 76, 94, 89],
            'weights': [0.3, 0.3, 0.4, 0.3, 0.3, 0.4, 0.3, 0.4]
        })
        
        print("📊 DataFrame:")
        print(df)
        
        # Access underlying NumPy arrays
        print(f"\n🔗 Underlying NumPy Arrays:")
        print(f"   df['scores'].values: {df['scores'].values}")
        print(f"   Type: {type(df['scores'].values)}")
        
        # NumPy operations on Pandas data
        print(f"\n🧮 NumPy Operations on Pandas:")
        weighted_scores = np.average(df['scores'].values, weights=df['weights'].values)
        print(f"   Weighted average: {weighted_scores:.2f}")
        
        # Pandas operations (easier and more readable)
        print(f"\n🐼 Pandas Operations:")
        df['weighted_score'] = df['scores'] * df['weights']
        print(f"   Weighted scores column:")
        print(df[['scores', 'weights', 'weighted_score']])
        
        print(f"\n💡 When to Use What:")
        print(f"   NumPy: Mathematical computations, large arrays, performance-critical")
        print(f"   Pandas: Data manipulation, labeled data, real-world datasets")
        print(f"   Together: Best of both worlds! 🚀")
        
    except NameError:
        print("Install Pandas and NumPy to see the integration!")

demonstrate_pandas_numpy_integration()

print(f"\n🎉 Day 8 Complete! ")