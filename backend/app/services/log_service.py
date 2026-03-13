#--------------------------------------
# log_service.py
#--------------------------------------
# Improved log parsing service
#
# Improvments added in Day 5:
# 1. Multiple error keyword detection
# 2. Error handling for missing files
# 3. Cleaner and scalable detection logic
#--------------------------------------

# List of patterns that indicate a failure
ERROR_PATTERNS = [
    "ERROR",
    "FAILED",
    "EXCEPTION",
    "TIMEOUT"
]
# Function to read the contents of a log file
def read_log_file(file_path):
    """
    Reads a log file and returns its contents as a string.
    """

    try:
        # Open file safely
        with open(file_path, "r") as file:
            log_text = file.read()

        return log_text
    
    except FileNotFoundError:
        print(f"Log file not found: {file_path}")
        return ""

    except Exception as e:
        print(f"Unexpected error while reading log file: {e}")
        return ""

# Function to extract error lines form a log
def extract_error_lines(log_text):
    """
    Looks through the log text and returns
    lines that contain ERROR.
    """

    # Split the log into individual lines
    lines = log_text.split("\n")

    detected_errors = []

    # Loop through each line
    for line in lines:

        # Check each error pattern
        for pattern in ERROR_PATTERNS:

            if pattern in line:
                detected_errors.append(line)

                # Once matched, stop checking other patterns
                break
    return detected_errors
