
print("=== DAY 5: ERROR HANDLING AND DEBUGGING ===\n")

print("PART 1: Common Error Types You'll Encounter")
print("=" * 50)

def demonstrate_common_errors():
    print("🔍 Common Errors in Data Processing:\n")
    print("1. FileNotFoundError Example:")
    try:
        with open('nonexistent_file.csv', 'r') as file:
            data = file.read()
    except FileNotFoundError as e:
        print(f"   ❌ Caught FileNotFoundError: {e}")
        print("   💡 Solution: Check file path, create file, or handle gracefully\n")
    
    print("2. ValueError Example:")
    try:
        # This often happens with real datasets that have unexpected values
        age = int("twenty-five")  # Can't convert text to integer
    except ValueError as e:
        print(f"   ❌ Caught ValueError: {e}")
        print("   💡 Solution: Validate data before conversion, use default values\n")
    
    print("3. KeyError Example:")
    try:
        student = {"name": "Alice", "age": 20}
        grade = student["grade"]  # Key doesn't exist
    except KeyError as e:
        print(f"   ❌ Caught KeyError: {e}")
        print("   💡 Solution: Use .get() method or check if key exists\n")
    
    print("4. ZeroDivisionError Example:")
    try:
        average = 100 / 0
    except ZeroDivisionError as e:
        print(f"   ❌ Caught ZeroDivisionError: {e}")
        print("   💡 Solution: Check for zero before division\n")
    
    print("5. IndexError Example:")
    try:
        numbers = [1, 2, 3]
        value = numbers[10]  # Index doesn't exist
    except IndexError as e:
        print(f"   ❌ Caught IndexError: {e}")
        print("   💡 Solution: Check list length or use safer access methods\n")

demonstrate_common_errors()

print("PART 2: Professional Error Handling Patterns")
print("=" * 50)

import csv
import json
from typing import Optional, List, Dict, Any

def safe_file_reader(filename: str) -> Optional[str]:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content.strip():  # Check for empty files
                print(f"⚠️  Warning: {filename} is empty")
                return None
            return content
            
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        return None
    except PermissionError:
        print(f"❌ Permission denied: {filename}")
        return None
    except UnicodeDecodeError:
        print(f"❌ File encoding issue: {filename}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error reading {filename}: {e}")
        return None

def safe_csv_reader(filename: str) -> List[Dict[str, str]]:
    try:
        students = []
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            
            # Validate that we have the expected columns
            expected_columns = {'Name', 'Age', 'Major', 'GPA', 'Credits', 'Graduation_Year'}
            actual_columns = set(reader.fieldnames or [])
            
            if not expected_columns.issubset(actual_columns):
                missing = expected_columns - actual_columns
                print(f"⚠️  Warning: CSV missing columns: {missing}")
                print(f"   Available columns: {actual_columns}")
            
            for row_num, row in enumerate(reader, start=2):  # Start at 2 (after header)
                try:
                    # Validate individual row data
                    validated_row = validate_student_data(row, row_num)
                    if validated_row:
                        students.append(validated_row)
                        
                except Exception as e:
                    print(f"⚠️  Skipping row {row_num} due to error: {e}")
                    continue
            
            print(f"✅ Successfully loaded {len(students)} valid student records")
            return students
            
    except FileNotFoundError:
        print(f"❌ CSV file not found: {filename}")
        return []
    except csv.Error as e:
        print(f"❌ CSV parsing error: {e}")
        return []
    except Exception as e:
        print(f"❌ Unexpected error reading CSV: {e}")
        return []

def validate_student_data(row: Dict[str, str], row_num: int) -> Optional[Dict[str, Any]]:
    try:
        # Create cleaned data dictionary
        cleaned = {}
        
        # Validate name (required, non-empty string)
        name = row.get('Name', '').strip()
        if not name:
            raise ValueError("Name is required and cannot be empty")
        cleaned['Name'] = name
        
        # Validate age (must be reasonable integer)
        try:
            age = int(row.get('Age', '0'))
            if not (16 <= age <= 100):  # Reasonable age range
                raise ValueError(f"Age {age} is outside reasonable range (16-100)")
            cleaned['Age'] = age
        except ValueError:
            raise ValueError(f"Invalid age value: '{row.get('Age', '')}'")
        
        # Validate GPA (must be valid float in range)
        try:
            gpa = float(row.get('GPA', '0'))
            if not (0.0 <= gpa <= 4.0):  # Standard GPA range
                print(f"⚠️  Row {row_num}: GPA {gpa} outside typical range (0.0-4.0)")
            cleaned['GPA'] = gpa
        except ValueError:
            raise ValueError(f"Invalid GPA value: '{row.get('GPA', '')}'")
        
        # Validate major (required string)
        major = row.get('Major', '').strip()
        if not major:
            raise ValueError("Major is required")
        cleaned['Major'] = major
        
        # Validate credits (non-negative integer)
        try:
            credits = int(row.get('Credits', '0'))
            if credits < 0:
                raise ValueError(f"Credits cannot be negative: {credits}")
            cleaned['Credits'] = credits
        except ValueError:
            raise ValueError(f"Invalid credits value: '{row.get('Credits', '')}'")
        
        # Validate graduation year (reasonable future year)
        try:
            grad_year = int(row.get('Graduation_Year', '0'))
            if not (2020 <= grad_year <= 2030):  # Reasonable range
                print(f"⚠️  Row {row_num}: Graduation year {grad_year} seems unusual")
            cleaned['Graduation_Year'] = grad_year
        except ValueError:
            raise ValueError(f"Invalid graduation year: '{row.get('Graduation_Year', '')}'")
        
        return cleaned
        
    except ValueError as e:
        print(f"⚠️  Row {row_num} validation error: {e}")
        return None
    except Exception as e:
        print(f"⚠️  Row {row_num} unexpected error: {e}")
        return None

def safe_calculation(numbers: List[float], operation: str = "average") -> Optional[float]:
    try:
        if not numbers:
            print("⚠️  Cannot calculate on empty list")
            return None
        
        # Remove any None values or handle non-numeric data
        clean_numbers = []
        for num in numbers:
            try:
                if num is not None:
                    clean_numbers.append(float(num))
            except (ValueError, TypeError):
                print(f"⚠️  Skipping invalid number: {num}")
                continue
        
        if not clean_numbers:
            print("⚠️  No valid numbers found after cleaning")
            return None
        
        # Perform requested operation safely
        if operation == "average":
            return sum(clean_numbers) / len(clean_numbers)
        elif operation == "sum":
            return sum(clean_numbers)
        elif operation == "max":
            return max(clean_numbers)
        elif operation == "min":
            return min(clean_numbers)
        else:
            print(f"❌ Unknown operation: {operation}")
            return None
            
    except Exception as e:
        print(f"❌ Calculation error: {e}")
        return None

# Demonstrate the robust functions
print("\n🛡️  Testing Robust Error Handling:")

# Test file reading
print("\n1. Testing safe file reading:")
content = safe_file_reader("nonexistent.txt")
print(f"   Result: {content}")

# Test CSV reading with validation
print("\n2. Testing CSV reading (will work if student_data.csv exists):")
students = safe_csv_reader("student_data.csv")
print(f"   Loaded {len(students)} students")

# Test safe calculations
print("\n3. Testing safe calculations:")
test_numbers = [3.8, 3.9, 3.2, "invalid", None, 4.0]
avg = safe_calculation(test_numbers, "average")
print(f"   Average of {test_numbers}: {avg}")

# =============================================================================
# PART 4: DEBUGGING TECHNIQUES AND TOOLS
# =============================================================================

print("\n\nPART 3: Systematic Debugging Approaches")
print("=" * 45)

def debug_problematic_function():
    print("🐛 Debugging Example: Finding Issues Systematically\n")
    
    # Sample data with various issues
    messy_data = [
        {"name": "Alice", "scores": [85, 90, 88]},
        {"name": "Bob", "scores": [78, "82", 80]},  # String in numbers
        {"name": "Charlie"},  # Missing scores
        {"name": "", "scores": [92, 95]},  # Empty name
        {"name": "Diana", "scores": []},  # Empty scores
        {"name": "Eve", "scores": [88, 86, 91, "N/A", 94]},  # Mixed data
    ]
    
    print("🔍 Step 1: Examine the data structure")
    print(f"   Data type: {type(messy_data)}")
    print(f"   Number of records: {len(messy_data)}")
    print(f"   Sample record: {messy_data[0]}")
    
    print("\n🔍 Step 2: Process each record with detailed logging")
    for i, record in enumerate(messy_data):
        print(f"\n   Processing record {i}: {record.get('name', 'NO NAME')}")
        
        # Check for required fields
        if 'name' not in record:
            print(f"   Missing 'name' field")
            continue
            
        if not record['name'].strip():
            print(f"      ❌ Empty name field")
            continue
            
        if 'scores' not in record:
            print(f"      ❌ Missing 'scores' field")
            continue
        
        # Process scores with error handling
        scores = record['scores']
        print(f"      📊 Raw scores: {scores}")
        
        valid_scores = []
        for j, score in enumerate(scores):
            try:
                numeric_score = float(score)
                if 0 <= numeric_score <= 100:  # Reasonable score range
                    valid_scores.append(numeric_score)
                    print(f"         ✅ Score {j}: {numeric_score}")
                else:
                    print(f"         ⚠️  Score {j}: {numeric_score} outside range 0-100")
            except (ValueError, TypeError):
                print(f"         ❌ Score {j}: Cannot convert '{score}' to number")
        
        if valid_scores:
            average = sum(valid_scores) / len(valid_scores)
            print(f"      📈 Final average: {average:.2f} from {len(valid_scores)} valid scores")
        else:
            print(f"      ❌ No valid scores found")

def demonstrate_debugging_tools():
    print("\n🛠️  Practical Debugging Techniques:\n")
    
    # 1. Strategic print statements
    print("1. Strategic Print Debugging:")
    def calculate_student_average(student_data):
        print(f"   🔍 Input data: {student_data}")
        
        if 'grades' not in student_data:
            print("   ❌ No grades found in student data")
            return None
        
        grades = student_data['grades']
        print(f"   🔍 Grades list: {grades}")
        print(f"   🔍 Grades type: {type(grades)}")
        print(f"   🔍 Number of grades: {len(grades)}")
        
        total = sum(grades)
        count = len(grades)
        print(f"   🔍 Sum: {total}, Count: {count}")
        
        if count == 0:
            print("   ❌ Cannot calculate average of empty grades")
            return None
        
        average = total / count
        print(f"   ✅ Calculated average: {average}")
        return average
    
    # Test the debugging function
    test_student = {"name": "Test Student", "grades": [85, 90, 78, 92]}
    result = calculate_student_average(test_student)
    
    # 2. Using assertions for validation
    print(f"\n2. Using Assertions for Validation:")
    def safe_divide(a, b):
        print(f"   🔍 Dividing {a} by {b}")
        
        # Assertions help catch invalid inputs early
        assert isinstance(a, (int, float)), f"First argument must be number, got {type(a)}"
        assert isinstance(b, (int, float)), f"Second argument must be number, got {type(b)}"
        assert b != 0, "Cannot divide by zero"
        
        result = a / b
        print(f"   ✅ Result: {result}")
        return result
    
    # Test assertions
    try:
        safe_divide(10, 2)
        safe_divide(10, 0)  # This will trigger assertion
    except AssertionError as e:
        print(f"   ❌ Assertion failed: {e}")
    
    # 3. Logging different types of information
    print(f"\n3. Different Levels of Information:")
    def process_with_logging(data):
        print(f"   ℹ️  INFO: Starting processing of {len(data)} items")
        
        for i, item in enumerate(data):
            if i % 2 == 0:
                print(f"   ✅ SUCCESS: Processed item {i}: {item}")
            else:
                print(f"   ⚠️  WARNING: Item {i} might need attention: {item}")
        
        print(f"   ✅ INFO: Processing complete")
    
    process_with_logging(["item1", "item2", "item3", "item4"])

# Run debugging demonstrations
debug_problematic_function()
demonstrate_debugging_tools()

# =============================================================================
# TODAY'S CHALLENGE: BUILD A ROBUST DATA PROCESSOR
# =============================================================================

import csv
import json
from typing import Dict, Any

def robust_data_loader(csv_file: str, json_file: str = None) -> Dict[str, Any]:
    result= {"csv_data":[], "json_data":None, "errors":[]}

    try:
        with open(csv_file, 'r', newline='') as file:
            print("CSV file opened successfully.")
            reader = csv.DictReader(file)
            result["csv_data"] = list(reader)
            print(f"Loaded {len(result['csv_data'])} rows from CSV")
    except FileNotFoundError:
        print(f"File not found: {csv_file}")
        result["errors"].append(f"CSV file not found: {csv_file}")
    except Exception as e:
        print(f"Error reading CSV: {e}")
        result["errors"].append(f"CSV error: {e}")

    if json_file:
        try:
            with open(json_file, 'r') as file:
                print("file opened successfully")
                reader=json.load(file)
                result["json_data"]= reader
                print("Data loaded successfully")
        except FileNotFoundError:
            print(f"File not found : {json_file}")
            result["errors"].append(f"Json file not found : {json_file}")
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON format: {e}")
            result["errors"].append(f"JSON format error: {e}")
        except Exception as e:
            print(f"Error reading Json : {e}")
            result["errors"].append(f"Json Error:{e}")

    return result


def data_validator_and_cleaner(raw_data: List[Dict]) -> Dict[str, Any]:
    result = {
        "clean_data": [],
        "error_report": {"valid": 0, "invalid": 0, "total": len(raw_data)},
        "warnings": []
    }
    
    for i, student in enumerate(raw_data):
        try:
            # Name validation
            name = student.get('Name', '').strip()
            if not name:
                result["warnings"].append(f"Row {i+1}: Empty name found")
                result["error_report"]["invalid"] += 1
                continue
            
            # Age validation
            try:
                age = int(student.get('Age', '0'))
                if not (16 <= age <= 80):
                    result["warnings"].append(f"Row {i+1}: Age {age} outside valid range (16-80)")
                    result["error_report"]["invalid"] += 1
                    continue
            except ValueError:
                result["warnings"].append(f"Row {i+1}: Age '{student.get('Age', '')}' is not a valid number")
                result["error_report"]["invalid"] += 1
                continue
            
            # GPA validation
            try:
                gpa = float(student.get('GPA', '0.0'))
                if not (0.0 <= gpa <= 4.0):
                    result["warnings"].append(f"Row {i+1}: GPA {gpa} outside valid range (0.0-4.0)")
                    result["error_report"]["invalid"] += 1
                    continue
            except ValueError:
                result["warnings"].append(f"Row {i+1}: GPA '{student.get('GPA', '')}' is not a valid number")
                result["error_report"]["invalid"] += 1
                continue
            
            # Major validation
            major = student.get('Major', '').strip()
            if not major:
                result["warnings"].append(f"Row {i+1}: Major cannot be empty")
                result["error_report"]["invalid"] += 1
                continue
            
            # Credits validation (your code!)
            try:
                credits = int(student.get('Credits', '0'))
                if credits < 0:  
                    result["warnings"].append(f"Row {i+1}: Credits cannot be negative")
                    result["error_report"]["invalid"] += 1
                    continue
            except ValueError:
                result["warnings"].append(f"Row {i+1}: Credits '{student.get('Credits', '')}' is not a valid number")
                result["error_report"]["invalid"] += 1
                continue
            
            # If we get here, all validations passed!
            cleaned_student = {
                "Name": name,        # String
                "Age": age,          # Integer
                "GPA": gpa,          # Float
                "Major": major,      # String
                "Credits": credits,  # Integer
            }
            
            result["clean_data"].append(cleaned_student)
            result["error_report"]["valid"] += 1
            
        except Exception as e:
            result["warnings"].append(f"Row {i+1}: Unexpected error - {e}")
            result["error_report"]["invalid"] += 1
    
    return result


def safe_statistics_calculator(clean_data: List[Dict]) -> Dict[str, Any]:
    result = {
        "gpa_by_major": {},           # Average GPA for each major
        "student_count_by_major": {}, # How many students per major
        "age_statistics": {},         # Age-related stats
        "credit_statistics": {},      # Credit-related stats
        "overall_stats": {},          # General statistics
        "errors": []                  # Any calculation errors
    }
    
    if not clean_data:
        result["errors"].append("No data provided for statistics calculation")
        return result
    
    print(f"📊 Calculating statistics for {len(clean_data)} students...")
    
    # Calculate GPA statistics by major
    try:
        # Step 1: Group students by major and collect their GPAs
        majors_data = {}  # Will store: {"Computer Science": [3.8, 3.2], "Mathematics": [3.9]}
        
        for student in clean_data:
            major = student.get("Major", "Unknown")
            gpa = student.get("GPA", 0.0)
            
            # Create list for this major if it doesn't exist
            if major not in majors_data:
                majors_data[major] = []
            
            # Add this student's GPA to their major's list
            majors_data[major].append(gpa)
        
        print(f"🎓 Found students in {len(majors_data)} different majors")
        
        # Step 2: Calculate statistics for each major
        for major, gpa_list in majors_data.items():
            if gpa_list:  # Make sure list isn't empty
                average_gpa = sum(gpa_list) / len(gpa_list)
                result["gpa_by_major"][major] = {
                    "average_gpa": round(average_gpa, 2),
                    "student_count": len(gpa_list),
                    "highest_gpa": max(gpa_list),
                    "lowest_gpa": min(gpa_list)
                }
                print(f"   📚 {major}: {average_gpa:.2f} average ({len(gpa_list)} students)")
        
        # Step 3: Count students by major
        for major, gpa_list in majors_data.items():
            result["student_count_by_major"][major] = len(gpa_list)
        
    except Exception as e:
        result["errors"].append(f"Error calculating GPA by major: {e}")
    
    # Calculate age statistics
    try:
        # Extract all ages and filter out invalid ones
        ages = [student.get("Age", 0) for student in clean_data]
        ages = [age for age in ages if age > 0]  # Remove invalid ages
        
        if ages:
            result["age_statistics"] = {
                "average_age": round(sum(ages) / len(ages), 1),
                "youngest": min(ages),
                "oldest": max(ages),
                "total_students": len(ages),
                "age_range": max(ages) - min(ages)
            }
            print(f"👥 Age range: {min(ages)} to {max(ages)}, average: {result['age_statistics']['average_age']}")
        
    except Exception as e:
        result["errors"].append(f"Error calculating age statistics: {e}")
    
    # Calculate credit statistics
    try:
        credits = [student.get("Credits", 0) for student in clean_data]
        credits = [c for c in credits if c >= 0]  # Remove invalid credits
        
        if credits:
            result["credit_statistics"] = {
                "average_credits": round(sum(credits) / len(credits), 1),
                "min_credits": min(credits),
                "max_credits": max(credits),
                "total_credits": sum(credits),
                "students_near_graduation": len([c for c in credits if c >= 100])  # Assuming 120 is graduation
            }
            print(f"📚 Credits: {min(credits)} to {max(credits)}, average: {result['credit_statistics']['average_credits']}")
            print(f"🎓 {result['credit_statistics']['students_near_graduation']} students near graduation (100+ credits)")
        
    except Exception as e:
        result["errors"].append(f"Error calculating credit statistics: {e}")
    
    # Calculate overall statistics
    try:
        # Extract all GPAs for overall analysis
        all_gpas = [student.get("GPA", 0.0) for student in clean_data]
        all_gpas = [gpa for gpa in all_gpas if gpa > 0]  # Remove invalid GPAs
        
        if all_gpas:
            result["overall_stats"] = {
                "total_students": len(clean_data),
                "overall_average_gpa": round(sum(all_gpas) / len(all_gpas), 2),
                "highest_gpa": max(all_gpas),
                "lowest_gpa": min(all_gpas),
                "gpa_range": round(max(all_gpas) - min(all_gpas), 2),
                "students_with_high_gpa": len([gpa for gpa in all_gpas if gpa >= 3.5]),  # A- or better
                "students_with_honors": len([gpa for gpa in all_gpas if gpa >= 3.7]),    # Dean's list
                "students_on_probation": len([gpa for gpa in all_gpas if gpa < 2.0]),   # Academic probation
                "median_gpa": round(sorted(all_gpas)[len(all_gpas)//2], 2)              # Middle value
            }
            
            print(f"🎯 Overall: {result['overall_stats']['overall_average_gpa']} average GPA")
            print(f"🌟 {result['overall_stats']['students_with_high_gpa']} students with high GPA (3.5+)")
            print(f"🏆 {result['overall_stats']['students_with_honors']} students with honors (3.7+)")
            
            if result['overall_stats']['students_on_probation'] > 0:
                print(f"⚠️  {result['overall_stats']['students_on_probation']} students on academic probation (<2.0)")
        
    except Exception as e:
        result["errors"].append(f"Error calculating overall statistics: {e}")
    
    # Summary report
    try:
        print(f"\n📋 STATISTICS SUMMARY:")
        print(f"   Total students analyzed: {len(clean_data)}")
        print(f"   Majors represented: {len(result.get('gpa_by_major', {}))}")
        print(f"   Calculation errors: {len(result['errors'])}")
        
        if result['errors']:
            print(f"⚠️  Errors encountered: {result['errors']}")
        else:
            print("✅ All calculations completed successfully!")
            
    except Exception as e:
        result["errors"].append(f"Error generating summary: {e}")
    
    return result


print("\n🧪 Testing Framework:")
print("Implement the functions above, then run:")
print("comprehensive_data_pipeline('student_data.csv')")


print("\n🎉 Day 5 Complete! You've mastered professional error handling!")
print("💡 Tomorrow: Working with libraries - expanding Python's capabilities!")