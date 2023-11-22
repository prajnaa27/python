from pathlib import Path

# Create a Path object representing a file
file_path = Path("example.txt")

# Check if the file exists
if file_path.exists():
    print(f"{file_path} exists.")

# Create a new directory
new_dir = Path("my_directory")
new_dir.mkdir()

# Create a file inside the new directory
new_file = new_dir / "new_file.txt"
new_file.touch()

# List the contents of the directory
for item in new_dir.iterdir():
    print(item)

# Delete the file and the directory
new_file.unlink()
new_dir.rmdir()
