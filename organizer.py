
from config import FILE_CATEGORIES
from pathlib import Path
import shutil

def get_category(file_extension):

    for category, extensions in FILE_CATEGORIES.items():

        if file_extension.lower() in extensions:
            return category

    return "Others"


def organize_files(source_folder):

    source = Path(source_folder)

    # Check whether the source folder exists
    if not source.exists() or not source.is_dir():
        print("Invalid source folder!")
        return 0

    moved_count = 0

    # Read all items inside the source folder
    for file in source.iterdir():

        # Skip folders
        if not file.is_file():
            continue

        # Identify file category
        category = get_category(file.suffix)

        # Create destination folder
        destination_folder = source / category
        destination_folder.mkdir(exist_ok=True)

        # Define destination file path
        destination_file = destination_folder / file.name

        # Handle duplicate filenames
        counter = 1

        while destination_file.exists():

            destination_file = (
                destination_folder /
                f"{file.stem}_{counter}{file.suffix}"
            )

            counter += 1

        try:
            # Move file
            shutil.move(str(file), str(destination_file))

            moved_count += 1

            print(f"Moved: {file.name} -> {category}")

        except OSError as error:
            print(f"Error moving {file.name}: {error}")

    return moved_count

