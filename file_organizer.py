import os
import shutil
import time

# Source folder in iCloud Drive's Documents folder
source_folder = '/Users/zem/Documents'

# Target folders in Documents folder
target_folders = {
    'images': '/Users/zem/Documents/Images',
    'documents': '/Users/zem/Documents/Documents',
    'videos': '/Users/zem/Documents/Videos',
    'music': '/Users/zem/Documents/Music',
}

# File extensions mapping to categories
file_types = {
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'videos': ['.mp4', '.avi', '.mov'],
    'music': ['.mp3', '.wav'],
}


def move_files():
    # Iterate through all files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            # Get the file extension
            file_ext = os.path.splitext(filename)[1].lower()

            # Determine the target folder based on the file extension
            moved = False
            for category, extensions in file_types.items():
                if file_ext in extensions:
                    target_path = target_folders[category]

                    # Ensure the target folder exists
                    if not os.path.exists(target_path):
                        os.makedirs(target_path)

                    # Move the file
                    try:
                        shutil.move(file_path, target_path)
                        print(f"Moved {filename} to {target_path}")
                    except Exception as e:
                        print(f"Error moving {filename}: {e}")
                    moved = True
                    break

            # If the file type is not recognized
            if not moved:
                print(f"Skipped {filename}: unknown file type")


def main():
    while True:  # Infinite loop to keep the script running
        move_files()  # Call the move_files function
        time.sleep(60)  # Wait for 60 seconds before checking again


if __name__ == "__main__":
    main()


