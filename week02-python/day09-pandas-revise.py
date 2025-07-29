## 🚀 Day 9 Exercises: Advanced Pandas Operations

### Exercise 1: Multi-Index DataFrames & Hierarchical Data (10 mins)
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create a multi-level student performance dataset
np.random.seed(42)

# Generate hierarchical data: University > Department > Student
universities = ['MIT', 'Stanford', 'Berkeley']
departments = ['CS', 'Math', 'Physics']
students_per_dept = 5

data = []
for uni in universities:
    for dept in departments:
        for i in range(students_per_dept):
            data.append({
                'university': uni,
                'department': dept,
                'student_id': f"{uni}_{dept}_{i+1:03d}",
                'student_name': f"Student_{uni}_{dept}_{i+1}",
                'semester': np.random.choice(['Fall2024', 'Spring2025']),
                'course': np.random.choice(['Course_A', 'Course_B', 'Course_C']),
                'grade': np.random.randint(70, 100),
                'credits': np.random.choice([3, 4, 5]),
                'gpa': np.round(np.random.uniform(2.5, 4.0), 2)
            })

df = pd.DataFrame(data)

# 1. First, create a multi-index DataFrame with university and department as index
multi_df = df.set_index(['university', 'department'])

# 2. Now, we'll calculate average grade by university and department
avg_grades = multi_df.groupby(level=[0, 1])['grade'].mean()

# 3. Let's Find the best performing department in each university
best_depts = avg_grades.groupby(level=0).idxmax()

# 4. This is a pivot table showing average GPA by university and semester
pivot_gpa = pd.pivot_table(df, values='gpa', index='university', 
                          columns='semester', aggfunc='mean')

print("Multi-Index DataFrame:")
print(multi_df.head())
print(f"\nAverage grades by university and department:")
print(avg_grades)
print(f"\nBest performing departments:")
print(best_depts)
print(f"\nGPA by university and semester:")
print(pivot_gpa)


###Move on to Exercise 2: Time Series Data Analysis


# Create time series dataset - daily student login data
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Generate realistic login patterns
np.random.seed(42)
time_series_data = []

for date in date_range:
    # Simulate fewer logins on weekends
    if date.weekday() >= 5:  # Weekend
        base_logins = np.random.poisson(50)
    else:  # Weekday
        base_logins = np.random.poisson(200)
    
    # Add seasonal effects (lower during summer/winter breaks)
    if date.month in [6, 7, 8, 12, 1]:  # Break months
        base_logins = int(base_logins * 0.3)
    
    time_series_data.append({
        'date': date,
        'daily_logins': base_logins,
        'unique_users': int(base_logins * 0.7),
        'avg_session_duration': np.random.normal(25, 8)  # minutes
    })

ts_df = pd.DataFrame(time_series_data)
ts_df.set_index('date', inplace=True)


# Resample to weekly averages
weekly_avg = ts_df.resample('W').mean()

# 2. Calculate rolling 7-day average for daily logins
ts_df['rolling_7_avg'] = ts_df['daily_logins'].rolling(window=7).mean()

# 3. Find the month with highest average logins
monthly_avg = ts_df.resample('M')['daily_logins'].mean()
peak_month = monthly_avg.idxmax()

# 4. Detect outliers (days with unusually high/low activity)
q1 = ts_df['daily_logins'].quantile(0.25)
q3 = ts_df['daily_logins'].quantile(0.75)
iqr = q3 - q1
outliers = ts_df[(ts_df['daily_logins'] < (q1 - 1.5 * iqr)) | 
                 (ts_df['daily_logins'] > (q3 + 1.5 * iqr))]

print("Time Series Analysis Results:")
print(f"Weekly averages (first 5 weeks):")
print(weekly_avg.head())
print(f"\nPeak month for logins: {peak_month.strftime('%B %Y')}")
print(f"Peak month average: {monthly_avg[peak_month]:.1f} logins/day")
print(f"\nOutlier days detected: {len(outliers)}")
print(f"Outlier dates: {outliers.index.date[:5]}...")  # Show first 5


### Exercise 3: Advanced Data Merging & Joins


# Create related datasets for complex joins
np.random.seed(42)

# Student information
students = pd.DataFrame({
    'student_id': [f'STU_{i:04d}' for i in range(1, 101)],
    'name': [f'Student_{i}' for i in range(1, 101)],
    'major': np.random.choice(['CS', 'Math', 'Physics', 'Biology'], 100),
    'enrollment_year': np.random.choice([2021, 2022, 2023, 2024], 100),
    'gpa': np.round(np.random.uniform(2.0, 4.0), 2)
})

# Course enrollments (some students may not be enrolled)
enrollments = pd.DataFrame({
    'student_id': np.random.choice(students['student_id'], 150),  # Some duplicates
    'course_id': [f'CS_{i:03d}' for i in np.random.choice(range(100, 200), 150)],
    'semester': np.random.choice(['Fall2024', 'Spring2025'], 150),
    'grade': np.random.choice(['A', 'B', 'C', 'D', 'F'], 150, p=[0.3, 0.3, 0.25, 0.1, 0.05])
})

# Course information
courses = pd.DataFrame({
    'course_id': [f'CS_{i:03d}' for i in range(100, 200)],
    'course_name': [f'Course_{i}' for i in range(100, 200)],
    'credits': np.random.choice([3, 4, 5], 100),
    'difficulty': np.random.choice(['Easy', 'Medium', 'Hard'], 100, p=[0.3, 0.5, 0.2])
})

# Faculty information (not all courses have assigned faculty)
faculty = pd.DataFrame({
    'course_id': np.random.choice(courses['course_id'], 80),  # Only 80 courses have faculty
    'professor': [f'Prof_{i}' for i in range(1, 81)],
    'department': np.random.choice(['CS', 'Math', 'Physics'], 80),
    'years_experience': np.random.randint(1, 30, 80)
})

# YOUR TASKS:
# 1. Inner join: Students who are actually enrolled in courses
enrolled_students = pd.merge(students, enrollments, on='student_id', how='inner')

# 2. Left join: All students with their enrollment info (including those not enrolled)
all_students_enrollments = pd.merge(students, enrollments, on='student_id', how='left')

# 3. Complex join: Full course information with enrollment and faculty data
course_details = pd.merge(courses, enrollments, on='course_id', how='left')
course_details = pd.merge(course_details, faculty, on='course_id', how='left')

# 4. Multi-condition merge: Students in CS courses taught by CS department faculty
cs_courses_cs_faculty = course_details[
    (course_details['course_id'].str.startswith('CS_')) & 
    (course_details['department'] == 'CS')
]

# 5. Calculate advanced analytics
# Average GPA by major and enrollment status
student_enrollment_status = all_students_enrollments.groupby('student_id').size().reset_index(name='courses_enrolled')
student_analytics = pd.merge(students, student_enrollment_status, on='student_id', how='left')
student_analytics['courses_enrolled'] = student_analytics['courses_enrolled'].fillna(0)

gpa_by_major_enrollment = student_analytics.groupby(['major', pd.cut(student_analytics['courses_enrolled'], 
                                                                   bins=[0, 1, 3, 10], 
                                                                   labels=['None', 'Light', 'Heavy'])])['gpa'].mean()

print("Advanced Join Results:")
print(f"Students with enrollments: {len(enrolled_students)}")
print(f"Total students: {len(students)}")
print(f"Students not enrolled in any course: {len(all_students_enrollments[all_students_enrollments['course_id'].isna()])}")
print(f"\nCS courses with CS faculty: {len(cs_courses_cs_faculty)}")
print(f"\nGPA by major and course load:")
print(gpa_by_major_enrollment)


## 🎯 Mini-Project: ML Data Preprocessing Pipeline

# Build a complete data preprocessing pipeline for machine learning:


def create_ml_preprocessing_pipeline():
    """
    Creating a realistic dataset with common ML preprocessing challenges
    """
    np.random.seed(42)
    
    # Create synthetic dataset with common real-world issues
    n_samples = 1000
    
    data = {
        'user_id': range(1, n_samples + 1),
        'age': np.random.randint(18, 70, n_samples),
        'income': np.random.lognormal(10, 1, n_samples),  # Log-normal distribution
        'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n_samples, p=[0.4, 0.3, 0.2, 0.1]),
        'experience_years': np.random.randint(0, 40, n_samples),
        'city': np.random.choice(['NYC', 'SF', 'LA', 'Chicago', 'Boston'], n_samples),
        'purchased': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]),  # Target variable
        'last_login': pd.date_range('2024-01-01', periods=n_samples, freq='H'),
        'device_type': np.random.choice(['mobile', 'desktop', 'tablet'], n_samples, p=[0.6, 0.3, 0.1])
    }
    
    df = pd.DataFrame(data)
    
    # Introduce realistic data quality issues
    # Missing values
    missing_indices = np.random.choice(df.index, size=50, replace=False)
    df.loc[missing_indices, 'income'] = np.nan
    
    missing_indices = np.random.choice(df.index, size=30, replace=False)
    df.loc[missing_indices, 'education'] = np.nan
    
    # Outliers
    outlier_indices = np.random.choice(df.index, size=10, replace=False)
    df.loc[outlier_indices, 'age'] = np.random.randint(100, 120, 10)  # Unrealistic ages
    
    # Inconsistent formats
    df.loc[df.index[:100], 'city'] = df.loc[df.index[:100], 'city'].str.lower()
    
    return df

print("🚀 STEP 1: Loading and Exploring Dataset")
print("=" * 60)

# Load the dataset
ml_df = create_ml_preprocessing_pipeline()

# Basic exploration using pandas only
print("📊 Dataset Shape:", ml_df.shape)
print("\n📋 Column Information:")
print(ml_df.info())

print("\n📈 Statistical Summary:")
print(ml_df.describe())

print("\n🔍 First 5 rows:")
print(ml_df.head())

print("\n📊 Data Types:")
print(ml_df.dtypes)

# Memory usage
print("\n💾 Memory Usage:")
print(ml_df.memory_usage(deep=True))


print("\n\n🔍 STEP 2: Handling Missing Values")
print("=" * 60)

# Check for missing values using pandas
print("🚨 Missing Values Analysis:")
missing_count = ml_df.isnull().sum()
missing_percentage = (ml_df.isnull().sum() / len(ml_df)) * 100

missing_summary = pd.DataFrame({
    'Missing_Count': missing_count,
    'Missing_Percentage': missing_percentage.round(2),
    'Non_Missing': ml_df.count(),
    'Total_Rows': len(ml_df)
})

# Display only columns with missing values
missing_summary_filtered = missing_summary[missing_summary['Missing_Count'] > 0]
print(missing_summary_filtered)

# Detailed missing value patterns
print("\n🔍 Missing Value Patterns:")
missing_combinations = ml_df.isnull().value_counts()
print("Combinations of missing values:")
print(missing_combinations.head())

# Handle missing values using pandas methods
print("\n💡 Handling Missing Values:")

# Strategy 1: Fill income with median (numerical)
income_median = ml_df['income'].median()
print(f"Income median before filling: {income_median:.2f}")
ml_df['income'] = ml_df['income'].fillna(income_median)
print(f"✅ Filled missing income values with median: {income_median:.2f}")

# Strategy 2: Fill education with mode (categorical)
education_mode = ml_df['education'].mode().iloc[0]  # Use iloc[0] to get the value
print(f"Education mode: {education_mode}")
ml_df['education'] = ml_df['education'].fillna(education_mode)
print(f"✅ Filled missing education values with mode: {education_mode}")

# Verify no missing values remain
print(f"\n🎯 Missing values after handling: {ml_df.isnull().sum().sum()}")


print("\n\n🔍 STEP 3: Detecting and Handling Outliers")
print("=" * 60)

def detect_outliers_iqr(series, column_name):
    """Detect outliers using IQR method with pandas"""
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Find outliers
    outlier_mask = (series < lower_bound) | (series > upper_bound)
    outliers = series[outlier_mask]
    
    return outliers, lower_bound, upper_bound

# Check for outliers in numerical columns
numerical_columns = ['age', 'income', 'experience_years']

outlier_summary = pd.DataFrame()

for col in numerical_columns:
    outliers, lower, upper = detect_outliers_iqr(ml_df[col], col)
    
    outlier_info = pd.DataFrame({
        'Column': [col],
        'Lower_Bound': [round(lower, 2)],
        'Upper_Bound': [round(upper, 2)],
        'Outlier_Count': [len(outliers)],
        'Outlier_Percentage': [round((len(outliers) / len(ml_df)) * 100, 2)]
    })
    
    outlier_summary = pd.concat([outlier_summary, outlier_info], ignore_index=True)
    
    print(f"\n📊 {col.upper()} Outliers:")
    print(f"  Valid range: {lower:.2f} to {upper:.2f}")
    print(f"  Outliers found: {len(outliers)} ({(len(outliers)/len(ml_df)*100):.1f}%)")
    
    if len(outliers) > 0:
        print(f"  Min outlier: {outliers.min():.2f}")
        print(f"  Max outlier: {outliers.max():.2f}")

print("\n📋 Outlier Summary:")
print(outlier_summary)

# Handle age outliers using pandas clip
print(f"\n🔧 Handling Age Outliers:")
age_outliers_before = len(ml_df[ml_df['age'] > 100])
print(f"Ages > 100: {age_outliers_before} records")

# Use pandas clip method
ml_df['age'] = ml_df['age'].clip(upper=80)
age_outliers_after = len(ml_df[ml_df['age'] > 80])
print(f"✅ Capped ages at 80. Records with age > 80: {age_outliers_after}")

# Handle income outliers using pandas quantile and clip
income_99th = ml_df['income'].quantile(0.99)
extreme_income_count = len(ml_df[ml_df['income'] > income_99th])
ml_df['income'] = ml_df['income'].clip(upper=income_99th)
print(f"✅ Capped {extreme_income_count} extreme income values at 99th percentile: ${income_99th:.2f}")



print("\n\n🛠️ STEP 4: Feature Engineering")
print("=" * 60)

# Create age groups using pandas cut
age_bins = [0, 25, 40, 60, 100]
age_labels = ['Young', 'Middle', 'Senior', 'Elder']
ml_df['age_group'] = pd.cut(ml_df['age'], bins=age_bins, labels=age_labels, include_lowest=True)
print("✅ Created age_group feature using pd.cut()")

# Create income levels using pandas qcut (quantile-based)
ml_df['income_level'] = pd.qcut(ml_df['income'], q=3, labels=['Low', 'Medium', 'High'])
print("✅ Created income_level feature using pd.qcut()")

# Create experience to age ratio
ml_df['experience_ratio'] = ml_df['experience_years'] / ml_df['age']
ml_df['experience_ratio'] = ml_df['experience_ratio'].fillna(0)  # Handle any division by zero
print("✅ Created experience_ratio feature")

# Extract date features using pandas datetime methods
ml_df['login_hour'] = ml_df['last_login'].dt.hour
ml_df['login_day_of_week'] = ml_df['last_login'].dt.dayofweek
ml_df['login_is_weekend'] = (ml_df['login_day_of_week'].isin([5, 6])).astype(int)
ml_df['login_month'] = ml_df['last_login'].dt.month
print("✅ Created login time features using pandas datetime methods")

# Create interaction features
ml_df['age_income_interaction'] = ml_df['age'] * ml_df['income'] / 1000
print("✅ Created age-income interaction feature")

# Create bins for experience years
exp_bins = [0, 5, 15, 25, 50]
exp_labels = ['Entry', 'Junior', 'Senior', 'Expert']
ml_df['experience_level'] = pd.cut(ml_df['experience_years'], bins=exp_bins, labels=exp_labels, include_lowest=True)
print("✅ Created experience_level feature using pd.cut()")

# Fix inconsistent city formats using pandas string methods
print(f"City formats before standardization:")
print(ml_df['city'].value_counts())

ml_df['city'] = ml_df['city'].str.title()  # Convert all to title case
print(f"\nCity formats after standardization:")
print(ml_df['city'].value_counts())
print("✅ Standardized city name formats")

print(f"\n📊 New dataset shape: {ml_df.shape}")

# Show new features summary
new_features = ['age_group', 'income_level', 'experience_ratio', 'login_hour', 
                'login_day_of_week', 'login_is_weekend', 'login_month', 
                'age_income_interaction', 'experience_level']

print("\n🆕 New features created:")
for feature in new_features:
    if feature in ml_df.columns:
        print(f"  • {feature}: {ml_df[feature].dtype}")



print("\n\n🏷️ STEP 5: Encoding Categorical Variables")
print("=" * 60)

# Identify categorical columns
categorical_columns = ml_df.select_dtypes(include=['object', 'category']).columns.tolist()
print(f"📋 Categorical columns: {categorical_columns}")

# Remove columns we don't want to encode
columns_to_exclude = ['last_login']
categorical_columns = [col for col in categorical_columns if col not in columns_to_exclude]

print(f"📋 Categorical columns to encode: {categorical_columns}")

# Create a copy for encoding
ml_df_encoded = ml_df.copy()

# One-hot encoding using pandas get_dummies
print("\n🔄 Applying One-Hot Encoding using pd.get_dummies():")

for col in categorical_columns:
    if col in ml_df_encoded.columns:
        # Check unique values before encoding
        unique_vals = ml_df_encoded[col].nunique()
        print(f"  📊 {col}: {unique_vals} unique values")
        
        # Get dummies and add to dataframe
        dummies = pd.get_dummies(ml_df_encoded[col], prefix=col, drop_first=True, dtype=int)
        ml_df_encoded = pd.concat([ml_df_encoded, dummies], axis=1)
        ml_df_encoded = ml_df_encoded.drop(col, axis=1)
        print(f"  ✅ Encoded {col} -> {len(dummies.columns)} new columns")

print(f"\n📊 Dataset shape after encoding: {ml_df_encoded.shape}")

# Show the columns added
encoded_cols = [col for col in ml_df_encoded.columns if any(cat in col for cat in categorical_columns)]
print(f"\n🆕 Encoded columns added ({len(encoded_cols)}):")
for col in sorted(encoded_cols):
    print(f"  • {col}")



print("\n\n📏 STEP 6: Scaling Numerical Features")
print("=" * 60)

# Identify numerical columns to scale
numerical_columns_to_scale = ['age', 'income', 'experience_years', 'experience_ratio', 
                             'login_hour', 'age_income_interaction']

# Remove columns that don't exist
numerical_columns_to_scale = [col for col in numerical_columns_to_scale if col in ml_df_encoded.columns]

print(f"📊 Columns to scale: {numerical_columns_to_scale}")

# Create a copy for scaling
ml_df_scaled = ml_df_encoded.copy()

print("\n📈 Before scaling statistics:")
scaling_stats_before = ml_df_scaled[numerical_columns_to_scale].describe()
print(scaling_stats_before.round(3))

# Apply StandardScaler equivalent using pandas operations
# StandardScaler formula: (x - mean) / std
print("\n🔄 Applying Standard Scaling using pandas operations:")

scaling_params = {}
for col in numerical_columns_to_scale:
    mean_val = ml_df_scaled[col].mean()
    std_val = ml_df_scaled[col].std()
    
    # Store parameters for potential inverse transform
    scaling_params[col] = {'mean': mean_val, 'std': std_val}
    
    # Apply standardization
    ml_df_scaled[col] = (ml_df_scaled[col] - mean_val) / std_val
    
    print(f"  ✅ Scaled {col}: mean={mean_val:.3f}, std={std_val:.3f}")

print("\n📈 After scaling statistics:")
scaling_stats_after = ml_df_scaled[numerical_columns_to_scale].describe()
print(scaling_stats_after.round(3))

# Verify scaling worked (means should be ~0, stds should be ~1)
print("\n✅ Scaling Verification:")
for col in numerical_columns_to_scale:
    mean_after = ml_df_scaled[col].mean()
    std_after = ml_df_scaled[col].std()
    print(f"  {col}: mean={mean_after:.6f}, std={std_after:.6f}")




print("\n\n🔄 STEP 7: Splitting into Train and Test Sets")
print("=" * 60)

# Prepare features and target using pandas
# Remove non-feature columns
columns_to_remove = ['user_id', 'last_login']
columns_to_remove = [col for col in columns_to_remove if col in ml_df_scaled.columns]

feature_columns = [col for col in ml_df_scaled.columns if col not in columns_to_remove + ['purchased']]

X = ml_df_scaled[feature_columns].copy()
y = ml_df_scaled['purchased'].copy()

print(f"📊 Feature matrix shape: {X.shape}")
print(f"🎯 Target vector shape: {y.shape}")
print(f"📋 Number of features: {len(feature_columns)}")

# Check target distribution
target_dist = y.value_counts().sort_index()
print(f"\n🎯 Target Distribution:")
print(target_dist)
print(f"Class 0 (Not Purchased): {target_dist[0]} ({target_dist[0]/len(y):.1%})")
print(f"Class 1 (Purchased): {target_dist[1]} ({target_dist[1]/len(y):.1%})")

# Manual train-test split using pandas (80/20 split with stratification)
# First, combine X and y for easier stratified splitting
combined_data = pd.concat([X, y], axis=1)

# Separate by class to maintain distribution
class_0_data = combined_data[combined_data['purchased'] == 0]
class_1_data = combined_data[combined_data['purchased'] == 1]

# Calculate split sizes
test_size = 0.2
class_0_test_size = int(len(class_0_data) * test_size)
class_1_test_size = int(len(class_1_data) * test_size)

print(f"\n📊 Split Planning:")
print(f"  Class 0: {len(class_0_data)} total, {class_0_test_size} for test")
print(f"  Class 1: {len(class_1_data)} total, {class_1_test_size} for test")

# Random sampling for test sets using pandas sample
np.random.seed(42)  # For reproducibility
class_0_test = class_0_data.sample(n=class_0_test_size, random_state=42)
class_0_train = class_0_data.drop(class_0_test.index)

class_1_test = class_1_data.sample(n=class_1_test_size, random_state=42)
class_1_train = class_1_data.drop(class_1_test.index)

# Combine train and test sets
train_data = pd.concat([class_0_train, class_1_train], axis=0).sample(frac=1, random_state=42)  # Shuffle
test_data = pd.concat([class_0_test, class_1_test], axis=0).sample(frac=1, random_state=42)    # Shuffle

# Split features and target
X_train = train_data[feature_columns]
y_train = train_data['purchased']
X_test = test_data[feature_columns]
y_test = test_data['purchased']

print(f"\n✅ Data Split Complete:")
print(f"  📚 Training set: {X_train.shape[0]} samples")
print(f"  🧪 Test set: {X_test.shape[0]} samples")

# Verify stratification worked
y_train_dist = y_train.value_counts().sort_index()
y_test_dist = y_test.value_counts().sort_index()

print(f"\n📊 Training set target distribution:")
print(f"    Class 0: {y_train_dist[0]} ({y_train_dist[0]/len(y_train):.1%})")
print(f"    Class 1: {y_train_dist[1]} ({y_train_dist[1]/len(y_train):.1%})")

print(f"\n📊 Test set target distribution:")
print(f"    Class 0: {y_test_dist[0]} ({y_test_dist[0]/len(y_test):.1%})")
print(f"    Class 1: {y_test_dist[1]} ({y_test_dist[1]/len(y_test):.1%})")


print("ML Preprocessing Challenge Dataset:")
print(f"Shape: {ml_df.shape}")
print(f"Missing values:\n{ml_df.isnull().sum()}")
print(f"Data types:\n{ml_df.dtypes}")

