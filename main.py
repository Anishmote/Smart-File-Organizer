
from pathlib import Path
from organizer import organize_files

# Get project directory
BASE_DIR = Path(__file__).parent

# Define source folder
SOURCE_FOLDER = BASE_DIR / "Raw_files"

# Start file organization
print("Starting File Organizer...")

total_files = organize_files(SOURCE_FOLDER)

# Display summary
print("\nOrganization Completed!")
print(f"Total files organized: {total_files}")
