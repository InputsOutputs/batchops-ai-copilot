#--------------------------------------
# log_service.py
#--------------------------------------
# This module contains functions that work
# with log files.
#
# Today we will:
# 1. Read log files
# 2. Extract error messages
#--------------------------------------


# Function to read the contents of a log file
def read_log_file(file_path):
    """
    Reads a log file and returns its contents as a string.
    """

    # Open the file in read mode ("r")
    with open(file_path, "r") as file:

        # Read the entire file contents
        log_text = file.read()

    # Retrun the log text
    return log_text

# Function to extract error lines form a log
def extract_error_lines(log_text):
    """
    Looks through the log text and returns
    lines that contain ERROR.
    """

    # Split the log into individual lines
    lines = log_text.split("\n")

    error_lines = []

    # Loop through each line
    for line in lines:

        # Check if the word ERROR exists in a line
        if "ERROR" in line:

            # ADD the line to the list
            error_lines.append(line)
    return error_lines
