print("=== DAY 6: WORKING WITH LIBRARIES ===\n")

# =============================================================================
# EXPLORING PYTHON'S STANDARD LIBRARY (8 minutes)
# =============================================================================

print("PART 1: Python's Built-in Powerhouse")
print("=" * 40)

# Standard library modules - already available, no installation needed
import os
import sys
import datetime
import random
import collections
import urllib.request
import pathlib

def explore_standard_library(): 
    print("🔧 System and OS Information:")
    print(f"   Python version: {sys.version}")
    print(f"   Operating system: {os.name}")
    print(f"   Current directory: {os.getcwd()}")
    print(f"   Python executable: {sys.executable}")
    
    print(f"\n📅 Date and Time Operations:")
    now = datetime.datetime.now()
    print(f"   Current time: {now}")
    print(f"   Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   Days until New Year: {(datetime.datetime(2026, 1, 1) - now).days}")
    
    print(f"\n🎲 Random Data Generation:")
    print(f"   Random number (1-100): {random.randint(1, 100)}")
    print(f"   Random choice from list: {random.choice(['Data Science', 'ML', 'AI', 'Analytics'])}")
    sample_data = random.sample(range(1, 51), 5)
    print(f"   Random sample of 5 numbers: {sample_data}")
    
    print(f"\n📊 Advanced Data Structures:")
    # Counter - counts occurrences
    text = "machine learning is amazing for data analysis"
    word_count = collections.Counter(text.split())
    print(f"   Word frequency: {dict(word_count)}")
    
    # defaultdict - provides default values for missing keys
    student_grades = collections.defaultdict(list)
    student_grades['Alice'].extend([85, 90, 88])
    student_grades['Bob'].extend([78, 82, 80])
    print(f"   Student grades: {dict(student_grades)}")
    
    print(f"\n📁 Path Operations:")
    current_path = pathlib.Path.cwd()
    print(f"   Current path object: {current_path}")
    print(f"   Parent directory: {current_path.parent}")
    print(f"   Path exists: {current_path.exists()}")
    
    # Create example paths without actually creating files
    data_path = current_path / "data" / "students.csv"
    print(f"   Example data path: {data_path}")
    print(f"   File extension: {data_path.suffix}")

explore_standard_library()

# =============================================================================
# UNDERSTANDING IMPORTS AND MODULES (7 minutes)
# =============================================================================

print("\n\nPART 2: Mastering Import Systems")
print("=" * 35)

def demonstrate_import_patterns():
    print("🔍 Different Import Patterns:\n")
    
    # 1. Standard import
    print("1. Standard Import:")
    import math
    print(f"   math.pi = {math.pi}")
    print(f"   math.sqrt(16) = {math.sqrt(16)}")
    
    # 2. Import with alias
    import statistics as stats
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"   stats.mean({data}) = {stats.mean(data)}")
    print(f"   stats.median({data}) = {stats.median(data)}")
    
    # 3. Import specific functions
    print(f"\n3. Import Specific Functions:")
    from random import choice, shuffle, randint
    sample_list = [1, 2, 3, 4, 5]
    shuffle(sample_list)  # Note: no 'random.' prefix needed
    print(f"   Shuffled list: {sample_list}")
    print(f"   Random choice: {choice(['NumPy', 'Pandas', 'Matplotlib'])}")
    
    # 4. Import all 
    print(f"\n4. Import All (use carefully):")
    # from math import *  
    # print(f"   pi = {pi}")  # Can use directly without math. prefix
    # print(f"   cos(0) = {cos(0)}")
    
    print(f"\n💡 Best Practices:")
    print(f"   - Use aliases for commonly used libraries (import pandas as pd)")
    print(f"   - Import specific functions when you only need a few")
    print(f"   - Avoid 'import *' in production code")
    print(f"   - Group imports: standard library, third-party, local modules")

demonstrate_import_patterns()

# =============================================================================
# WORKING WITH THIRD-PARTY LIBRARIES
# =============================================================================

print("\n\nPART 3: Third-Party Library Ecosystem")
print("=" * 40)

def demonstrate_requests_library(): #You might need to install request 1st using "pip install requests"
    print("🌐 Working with External Libraries - Requests Example:\n")
    
    try:
        import requests
        print("✅ Requests library is available!")
        
        # Example: Get information about Python packages
        print("\n📦 Fetching Package Information from PyPI:")
        
        # PyPI API example - get info about pandas
        try:
            response = requests.get("https://pypi.org/pypi/pandas/json", timeout=5)
            if response.status_code == 200:
                data = response.json()
                info = data['info']
                print(f"   Package: {info['name']}")
                print(f"   Version: {info['version']}")
                print(f"   Description: {info['summary'][:100]}...")
                print(f"   Author: {info['author']}")
            else:
                print(f"   API request failed with status: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"   ⚠️  Network request failed: {e}")
            print("   (This is normal if you're offline)")
        
    except ImportError:
        print("❌ Requests library not installed")
        print("\n🔧 To install requests, run in terminal:")
        print("   pip install requests")
        print("\n💡 Then restart this script to see it in action!")

# Try to demonstrate requests (may fail if not installed)
demonstrate_requests_library()

def explore_data_science_libraries():
    # Dictionary of important libraries and their purposes
    libraries = {
        "NumPy": {
            "purpose": "Numerical computing with arrays",
            "typical_import": "import numpy as np",
            "key_features": ["Multi-dimensional arrays", "Mathematical functions", "Linear algebra"],
            "example": "np.array([1, 2, 3]) * 2  # Element-wise operations"
        },
        "Pandas": {
            "purpose": "Data manipulation and analysis",
            "typical_import": "import pandas as pd",
            "key_features": ["DataFrames", "CSV/Excel reading", "Data cleaning"],
            "example": "pd.read_csv('data.csv')  # Load data easily"
        },
        "Matplotlib": {
            "purpose": "Data visualization and plotting",
            "typical_import": "import matplotlib.pyplot as plt",
            "key_features": ["Line plots", "Bar charts", "Histograms"],
            "example": "plt.plot([1, 2, 3], [1, 4, 9])  # Simple plotting"
        },
        "Scikit-learn": {
            "purpose": "Machine learning algorithms",
            "typical_import": "from sklearn import ...",
            "key_features": ["Classification", "Regression", "Clustering"],
            "example": "from sklearn.linear_model import LinearRegression"
        },
        "Requests": {
            "purpose": "HTTP requests and web APIs",
            "typical_import": "import requests",
            "key_features": ["GET/POST requests", "JSON handling", "Authentication"],
            "example": "requests.get('https://api.example.com/data')"
        }
    }
    
    for lib_name, details in libraries.items():
        print(f"📚 {lib_name}:")
        print(f"   Purpose: {details['purpose']}")
        print(f"   Import: {details['typical_import']}")
        print(f"   Features: {', '.join(details['key_features'])}")
        print(f"   Example: {details['example']}")
        
        # Try to import and show status
        try:
            module_name = details['typical_import'].split()[-1]
            if 'as' in details['typical_import']:
                module_name = details['typical_import'].split()[1]
            
            __import__(module_name.split()[0])
            print(f"   Status: ✅ Installed")
        except ImportError:
            print(f"   Status: ❌ Not installed")
        
        print()

# explore_data_science_libraries()

# =============================================================================
# TODAY'S PROJECT: LIBRARY EXPLORATION TOOL (Complete this!)
# =============================================================================

print("🎯 TODAY'S PROJECT: Library Information Tool")
print("=" * 50)

def check_library_availability(library_list):
    """Check which libraries are available for import"""
    result = {}
    
    print(f"🔍 Checking {len(library_list)} libraries...")
    
    for library_num, library in enumerate(library_list, 1):
        print(f"Checking {library_num}/{len(library_list)}: {library}")
        
        try:
            __import__(library)
            result[library] = {"status": "Available", "importable": True}
        except ImportError:
            result[library] = {"status": "Not installed", "importable": False}
        except Exception as e:
            result[library] = {"status": f"Error: {e}", "importable": False}
    
    available = sum(1 for lib in result.values() if lib["importable"])
    total = len(library_list)
    print(f"\n✅ Check complete: {available}/{total} libraries available")
    
    return result

# check_library_availability(libraries)



def get_library_info(library_name):
    """Get detailed information about a library"""
    result = {}
    
    try:
        # Import and store the library
        lib = __import__(library_name)
    
        try:
            version = lib.__version__
        except AttributeError:
            try:
                version = lib.VERSION  # Some libraries use this instead
            except AttributeError:
                version = "Version not available"
        
        # Get library documentation
        doc = lib.__doc__ if lib.__doc__ else "No documentation available"
        doc_preview = doc[:100] + "..." if len(doc) > 100 else doc
        
        # Get available functions and classes (first 10 to avoid overwhelming output)
        all_items = dir(lib)
        public_items = [item for item in all_items if not item.startswith('_')][:10]
        
        # Get library file location
        try:
            location = lib.__file__
        except AttributeError:
            location = "Built-in module"
        
        # Try to get package info
        try:
            package_name = lib.__name__
        except AttributeError:
            package_name = library_name
        
        # Build comprehensive result
        result = {
            "library_name": library_name,
            "package_name": package_name,
            "status": "Available",
            "importable": True,
            "version": version,
            "documentation_preview": doc_preview,
            "location": location,
            "public_functions": public_items,
            "total_attributes": len(all_items),
            "has_version": hasattr(lib, '__version__'),
            "is_package": hasattr(lib, '__path__')
        }
        
        print(f"✅ {library_name}: {version}")
        
    except ImportError:
        result = {
            "library_name": library_name,
            "status": "Not installed", 
            "importable": False,
            "error": "Library not found or not importable"
        }
        print(f"❌ {library_name}: Not installed")
        
    except Exception as e:
        result = {
            "library_name": library_name,
            "status": "Error", 
            "importable": False,
            "error": str(e)
        }
        print(f"⚠️ {library_name}: Error - {e}")
    
    return result



def demonstrate_library_usage(library_name):
    try:
        lib = __import__(library_name)
        print(f"✅ {library_name} is available. Here's how to use it:")
        print(f" Go to https://docs.python.org/3/library/{library_name}.html")
        print("Please scroll through the link for specific library for example")
        
        if library_name == "datetime":
            print("📅 Datetime Examples:")
            import datetime
            now = datetime.datetime.now()
            print(f"   Current time: {now}")
            print(f"   Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            
        elif library_name == "random":
            print("🎲 Random Examples:")
            import random
            print(f"   Random number 1-100: {random.randint(1, 100)}")
            print(f"   Random choice: {random.choice(['apple', 'banana', 'orange'])}")
            
        elif library_name == "os":
            print("💻 OS Examples:")
            import os
            print(f"   Current directory: {os.getcwd()}")
            print(f"   Operating system: {os.name}")
            
        elif library_name == "json":
            print("📄 JSON Examples:")
            import json
            data = {"name": "Alice", "age": 25}
            json_string = json.dumps(data)
            print(f"   Dictionary to JSON: {json_string}")

        elif library_name == "sys":
            print("🖥️ Sys Examples:")
            import sys
            print(f"   Python version: {sys.version_info.major}.{sys.version_info.minor}")
            print(f"   Platform: {sys.platform}")
            print(f"   Python executable: {sys.executable}")
            
        elif library_name == "pathlib":
            print("📁 Pathlib Examples:")
            from pathlib import Path
            current = Path.cwd()
            print(f"   Current directory: {current}")
            print(f"   Parent directory: {current.parent}")
            print(f"   Directory exists: {current.exists()}")

        else:
            # For libraries we don't have examples for
            print(f"🔗 For detailed examples, visit:")
            print(f"   https://docs.python.org/3/library/{library_name}.html")
            print(f"   Or try: help({library_name})")

        

        return {"Status": "Available", "Demonstrated": True}
        
    except ImportError:
        print(f"❌ {library_name} is not installed")
        print(f"   Install using: pip install {library_name}")
        return {"Status": "Unavailable", "Demonstrated": False}
    



def create_environment_report():
    
    result = {
        "Total modules checked": 0,
        "Available": 0,
        "Missing": 0
    }

    print("🐍 PYTHON ENVIRONMENT REPORT")
    print("="*50)

    import sys
    from pathlib import Path
    import os

    print(f"Python Version: {sys.version.split()[0]}")
    print(f"Python Path: {sys.executable}")
    print(f"Operating System: {os.name}")
    print(f"Platform: {sys.platform}")

    print("\n📦 INSTALLED LIBRARIES:")
    
    # List of libraries to check
    libraries_to_check = [
        'os', 'sys', 'json', 'datetime', 'random',
        'numpy', 'pandas', 'matplotlib', 'requests'
    ]

    # Check each library - MUCH SIMPLER!
    for library_name in libraries_to_check:
        try:
            lib = __import__(library_name)
            version = getattr(lib, '__version__', 'Built-in')
            print(f"   ✅ {library_name}: {version}")
            result["Available"] += 1
        except ImportError:
            print(f"   ❌ {library_name}: Not installed")
            result["Missing"] += 1
        
        # Count every library we check (success or failure)
        result["Total modules checked"] += 1

    # Print summary
    print(f"\n📊 SUMMARY:")
    print(f"   Total modules checked: {result['Total modules checked']}")
    print(f"   Available: {result['Available']}")
    print(f"   Missing: {result['Missing']}")
    
    return result




def interactive_library_explorer():
    """
    Create an interactive tool for exploring Python libraries.
    This function ties together all the previous functions into a user-friendly interface.
    """
    
    print("🔍 WELCOME TO PYTHON LIBRARY EXPLORER")
    print("=" * 40)
    print("Your one-stop tool for exploring Python libraries!")
    print()
    
    while True:
        # Display main menu
        print("\n🎯 What would you like to do?")
        print("=" * 30)
        print("1. 📋 Check multiple libraries")
        print("2. 🔍 Get detailed library info") 
        print("3. 🎮 See library demonstration")
        print("4. 📊 Generate environment report")
        print("5. 🚪 Exit")
        print()
        
        # Get user choice
        try:
            choice = input("Enter your choice (1-5): ").strip()
            print()  # Add blank line for readability
            
            if choice == "1":
                handle_multiple_library_check()
                
            elif choice == "2":
                handle_single_library_info()
                
            elif choice == "3":
                handle_library_demonstration()
                
            elif choice == "4":
                handle_environment_report()
                
            elif choice == "5":
                print("👋 Thanks for using Library Explorer!")
                print("Happy coding! 🚀")
                break
                
            else:
                print("❌ Invalid choice. Please enter 1-5.")
                continue
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for using Library Explorer!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            continue
        
        # Ask if they want to continue
        print("\n" + "-" * 40)
        continue_choice = input("Press Enter to continue or 'q' to quit: ").strip().lower()
        if continue_choice == 'q':
            print("👋 Thanks for using Library Explorer!")
            break


def handle_multiple_library_check():
    """Handle checking multiple libraries"""
    print("📋 LIBRARY AVAILABILITY CHECKER")
    print("=" * 35)
    
    # Get libraries from user
    user_input = input("Enter library names (separated by commas): ").strip()
    
    if not user_input:
        print("❌ No libraries entered.")
        return
    
    # Parse input
    library_list = [lib.strip() for lib in user_input.split(',')]
    print(f"\n🔍 Checking {len(library_list)} libraries...\n")
    
    # Use our existing function
    results = check_library_availability(library_list)
    
    # Display summary
    available = sum(1 for lib in results.values() if lib.get("importable", False))
    total = len(library_list)
    print(f"\n📊 Summary: {available}/{total} libraries are available")


def handle_single_library_info():
    """Handle getting detailed info about a single library"""
    print("🔍 DETAILED LIBRARY INFORMATION")
    print("=" * 35)
    
    library_name = input("Enter library name: ").strip()
    
    if not library_name:
        print("❌ No library name entered.")
        return
    
    print(f"\n📚 Getting information about '{library_name}'...\n")
    
    # Use our existing function
    info = get_library_info(library_name)
    
    # Display detailed info
    print(f"📖 DETAILED REPORT FOR '{library_name.upper()}':")
    print("-" * 30)
    
    for key, value in info.items():
        if key == "public_functions" and isinstance(value, list):
            print(f"🔧 Public Functions (first 5): {', '.join(value[:5])}")
        elif key == "documentation_preview":
            print(f"📄 Documentation: {value}")
        else:
            print(f"   {key.replace('_', ' ').title()}: {value}")


def handle_library_demonstration():
    """Handle demonstrating library usage"""
    print("🎮 LIBRARY USAGE DEMONSTRATION")
    print("=" * 35)
    
    library_name = input("Enter library name to see examples: ").strip()
    
    if not library_name:
        print("❌ No library name entered.")
        return
    
    print(f"\n🎯 Demonstrating '{library_name}'...\n")
    
    # Use our existing function
    demonstrate_library_usage(library_name)


def handle_environment_report():
    """Handle generating environment report"""
    print("📊 GENERATING ENVIRONMENT REPORT")
    print("=" * 35)
    print("This may take a moment...\n")
    
    # Use our existing function
    create_environment_report()


def quick_library_suggestions():
    """Provide some quick suggestions for libraries to explore"""
    print("\n💡 SUGGESTED LIBRARIES TO EXPLORE:")
    print("=" * 35)
    
    suggestions = {
        "📅 Date & Time": ["datetime", "time"],
        "🎲 Random & Math": ["random", "math", "statistics"],
        "💻 System & OS": ["os", "sys", "pathlib"],
        "🌐 Web & APIs": ["requests", "urllib", "json"],
        "📊 Data Science": ["numpy", "pandas", "matplotlib"],
        "🔧 Utilities": ["collections", "itertools", "functools"]
    }
    
    for category, libs in suggestions.items():
        print(f"{category}: {', '.join(libs)}")


# Enhanced version with suggestions
def interactive_library_explorer_enhanced():
    """
    Enhanced version of the library explorer with additional features
    """
    
    print("🔍 PYTHON LIBRARY EXPLORER v2.0")
    print("=" * 40)
    print("Your comprehensive Python library exploration tool!")
    
    # Show suggestions on startup
    quick_library_suggestions()
    
    while True:
        print("\n🎯 Main Menu:")
        print("=" * 15)
        print("1. 📋 Check multiple libraries")
        print("2. 🔍 Get detailed library info") 
        print("3. 🎮 See library demonstration")
        print("4. 📊 Generate environment report")
        print("5. 💡 Show library suggestions")
        print("6. 🚪 Exit")
        print()
        
        try:
            choice = input("Enter your choice (1-6): ").strip()
            print()
            
            if choice == "1":
                handle_multiple_library_check()
            elif choice == "2":
                handle_single_library_info()
            elif choice == "3":
                handle_library_demonstration()
            elif choice == "4":
                handle_environment_report()
            elif choice == "5":
                quick_library_suggestions()
            elif choice == "6":
                print("👋 Thanks for exploring Python libraries!")
                print("Keep coding and keep exploring! 🚀")
                break
            else:
                print("❌ Invalid choice. Please enter 1-6.")
                continue
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Happy coding! 🚀")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            continue
        
        # Continue prompt
        print("\n" + "-" * 40)
        continue_choice = input("Press Enter to continue or 'q' to quit: ").strip().lower()
        if continue_choice == 'q':
            print("👋 Thanks for using Library Explorer!")
            break


# Main function to run everything
def run_library_explorer():
    """
    Main function to run the complete library exploration tool.
    This combines all the functions you've built into one comprehensive tool.
    """
    
    print("🐍 PYTHON LIBRARY EXPLORATION TOOLKIT")
    print("=" * 45)
    print("Built with love during your Day 6 Python journey! 💪")
    print()
    
    choice = input("Run basic (b) or enhanced (e) version? [b/e]: ").strip().lower()
    
    if choice == 'e':
        interactive_library_explorer_enhanced()
    else:
        interactive_library_explorer()


# To run the complete tool:
if __name__ == "__main__":
    run_library_explorer()


# Test your functions here
print("\n🧪 Testing Your Library Explorer:")

# Example usage (implement these functions above):
# standard_libs = ['os', 'sys', 'datetime', 'random', 'json', 'csv']
# data_science_libs = ['numpy', 'pandas', 'matplotlib', 'requests', 'sklearn']

# availability = check_library_availability(standard_libs + data_science_libs)
# print(f"Library availability: {availability}")

# create_environment_report()

# =============================================================================
# BONUS: VIRTUAL ENVIRONMENTS AND BEST PRACTICES
# =============================================================================

print("\n💡 Professional Development Practices:")
print("=" * 45)

def explain_virtual_environments():
    """
    Explain virtual environments and why they're important.
    """
    
    print("🏠 Virtual Environments - Why They Matter:\n")
    
    print("❌ Without Virtual Environments:")
    print("   - All packages installed globally")
    print("   - Version conflicts between projects")
    print("   - Difficult to share exact dependencies")
    print("   - Risk of breaking system Python")
    
    print(f"\n✅ With Virtual Environments:")
    print("   - Isolated package installations per project")
    print("   - No version conflicts")
    print("   - Easy to recreate exact environment")
    print("   - Clean, professional development")
    
    print(f"\n🔧 Common Virtual Environment Commands:")
    print("   Create: python -m venv myproject_env")
    print("   Activate (Windows): myproject_env\\Scripts\\activate")
    print("   Activate (Mac/Linux): source myproject_env/bin/activate")
    print("   Install packages: pip install numpy pandas matplotlib")
    print("   Save requirements: pip freeze > requirements.txt")
    print("   Install from requirements: pip install -r requirements.txt")
    print("   Deactivate: deactivate")
    
    print(f"\n📋 Professional Project Structure:")
    print("   myproject/")
    print("   ├── myproject_env/          # Virtual environment")
    print("   ├── src/                    # Source code")
    print("   ├── data/                   # Data files")
    print("   ├── notebooks/              # Jupyter notebooks")
    print("   ├── requirements.txt        # Package dependencies")
    print("   ├── README.md              # Project documentation")
    print("   └── .gitignore             # Git ignore file")

explain_virtual_environments()

def package_management_best_practices():
    print(f"\n📦 Package Management Best Practices:\n")
    
    practices = [
        ("Use requirements.txt", "Track exact package versions for reproducibility"),
        ("Pin critical versions", "Use specific versions for important dependencies"),
        ("Regular updates", "Keep packages updated but test thoroughly"),
        ("Virtual environments", "Isolate projects from each other"),
        ("Documentation", "Document why specific packages are needed"),
        ("Security awareness", "Be cautious with packages from unknown sources"),
        ("Development vs Production", "Separate dev tools from production requirements")
    ]
    
    for practice, explanation in practices:
        print(f"   • {practice}: {explanation}")
    
    print(f"\n🔍 Useful pip Commands:")
    commands = [
        ("pip list", "Show all installed packages"),
        ("pip show package_name", "Show detailed package information"),
        ("pip install --upgrade package_name", "Update a specific package"),
        ("pip uninstall package_name", "Remove a package"),
        ("pip freeze", "List all packages with exact versions"),
        ("pip check", "Check for package conflicts")
    ]
    
    for command, description in commands:
        print(f"   {command:<35} # {description}")

package_management_best_practices()

print(f"\n🎉 Day 6 Complete! You've entered the Python ecosystem!")
print("💡 You now understand how to leverage the power of libraries!")
print("🚀 Tomorrow: NumPy - the mathematical foundation of data science!")