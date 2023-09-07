#!/usr/bin/env python

import os
import datetime

def delete_old_files(directory):
    now = datetime.datetime.now()
    six_months_ago = now - datetime.timedelta(days=6*30)
    # one_week_ago = now - datetime.timedelta(days=7)
    # one_year_ago = now - datetime.timedelta(days=365)

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if modification_time < six_months_ago:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

# Provide the directory path where you want to delete files
directory_path = "/path/to/directory"

delete_old_files(directory_path)

