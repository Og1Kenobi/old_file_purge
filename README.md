# old_file_purge
This is a Python script that deletes files from a specified directory that are older than a certain number of days.

The script takes two command-line arguments: the directory path and the age threshold (in days). It then calls the delete_old_files() function with the directory path and age threshold as arguments.

The delete_old_files() function walks through the directory recursively using os.walk(). For each file, it checks the modification time using os.path.getmtime() and compares it with the age threshold. If the modification time is older than the age threshold, the file path is added to a list of files to be deleted.

After traversing the entire directory, the function checks if any files were found to be deleted. If no files are found, it prints a message and exits. Otherwise, it displays the list of files to be deleted and prompts the user for confirmation. If the user confirms, it deletes each file using os.remove().

If there are any errors accessing or deleting files, it prints an error message.

