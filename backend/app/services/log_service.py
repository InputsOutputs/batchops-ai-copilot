#--------------------------------------
# log_service.py
#--------------------------------------
# Day 6 improvements:
# 1. Read log files safely
# 2. Extract error lines using multiple patterns
# 3. Convert raw error lines into structured data
#--------------------------------------

# Keywords that indicate failure-related log lines
ERROR_PATTERNS = [
    "ERROR",
    "FAILED",
    "EXCEPTION",
    "TIMEOUT",
    "PERMISSION_DENIED",
    "DATA_DUPLICATE"
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

def classify_error_line(error_line):
    """
    Converts a raw error line into a structured dictionary.

    Returns:
        {
            "error_type": ...,
            "severity": ...,
            "message": ...
        }
    """
    
    # Normalize the text to uppercase for easier matching
    upper_line = error_line.upper()
    
    # Detect missing file errors
    if "FILE" in upper_line and "NOT FOUND" in upper_line:
        return {
            "error_type": "FILE_NOT_FOUND",
            "severity": "HIGH",
            "message": error_line
        }
        
    # Detect database timeout errors
    elif "DATABASE" in upper_line and "TIMEOUT" in upper_line:
        return {
            "error_type": "DATABASE_TIMEOUT",
            "severity": "HIGH",
            "message": error_line
        }

    # Detect Duplicate Data Issues
    elif "duplicate" in upper_line.lower():
        return {
            "error_type": "DATA_DUPLICATE",
            "severity": "HIGH",
            "message": error_line
        }
    

    # Detect dependency-related failures
    elif "DEPENDENCY" in upper_line:
        return {
            "error_type": "DEPENDENCY_FAILURE",
            "severity": "MEDIUM",
            "message": error_line
        }

    # Detect permission-related issues
    elif "PERMISSION" in upper_line:
        return {
            "error_type": "PERMISSION_DENIED",
            "severity": "HIGH",
            "message": error_line
        }

    # Default fallback when no known rule matches
    else:
        return {
            "error_type": "UNKNOWN_ERROR",
            "severity": "MEDIUM",
            "message": error_line
        }

def structure_detected_errors(error_lines):
    """
    Takes a list of raw error lines and returns
    a list of structured error dictionaries.
    """
    structured_errors = []

    # Convert each raw error line into structured data
    for error_line in error_lines:
        structured_error = classify_error_line(error_line)
        structured_errors.append(structured_error)
    
    return structured_errors
