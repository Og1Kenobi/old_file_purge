#!/usr/bin/env python3

import os
import sys
import datetime

def get_age_threshold(days):
    now = datetime.datetime.now()
    return now - datetime.timedelta(days=days)

def delete_old_files(directory, age_threshold):
    files_to_delete = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                if modification_time < age_threshold:
                    files_to_delete.append(file_path)
            except OSError as e:
                print(f"Error accessing file: {file_path} - {e}")

    if len(files_to_delete) == 0:
        print("No files found to delete.")
        sys.exit(0)

    print("Files to be deleted:")
    for file_path in files_to_delete:
        print(file_path)

    confirmation = input("Are you sure you want to delete the files? (y/n): ")
    if confirmation.lower() != "y":
        print("File deletion aborted.")
        sys.exit(0)

    for file_path in files_to_delete:
        try:
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        except OSError as e:
            print(f"Error deleting file: {file_path} - {e}")

# Validate and retrieve the directory and age threshold from command-line arguments
if len(sys.argv) < 3:
    print("Please provide the directory path and age threshold (in days) as command-line arguments.")
    sys.exit(1)

directory_path = sys.argv[1]

try:
    age_threshold = get_age_threshold(int(sys.argv[2]))
except ValueError:
    print("Invalid age threshold. Please provide a valid integer value.")
    sys.exit(1)

delete_old_files(directory_path, age_threshold)

