# Smart File Organizer

A simple Python project I built to make file management easier.

I often end up with a Downloads folder full of images, documents, videos and other files. Instead of sorting everything manually, I wanted to create a small Python tool that could handle this automatically.

## What does it do?

The program scans a selected folder, identifies files based on their extensions and moves them into separate category folders.

### Features

- Automatically detects file extensions.
- Organizes files into categories.
- Creates folders when needed.
- Handles duplicate filenames by renaming them.
- Skips directories while scanning files.
- Displays the number of files organized.

## Technologies Used

- Python
- pathlib
- os
- shutil

## Project Structure

```text
smart-file-organizer/
├── main.py
├── organizer.py
├── config.py
├── Raw_files/
├── logs/
└── README.md
```

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/Anishmote/Smart-File-Organizer.git
```

2. Open the project folder:

```bash
cd smart-file-organizer
```

3. Add some sample files inside `Raw_files/`.

4. Run the application:

```bash
python main.py
```

The program will automatically organize the files into their respective folders.

## What I Learned

While building this project, I got practical experience with Python file handling, working with directories, dictionaries, loops, functions and exception handling.

I also learned how to structure a Python project into multiple files instead of writing everything in one script.

## Future Improvements

- Add a graphical user interface.
- Support recursive folder scanning.
- Add detailed activity logs.
- Allow users to choose custom file categories.

---

**Built as a hands-on Python automation project.**

By Anish Mote