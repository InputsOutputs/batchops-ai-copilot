# ---------------------------------------
# log_reader_test.py
# ---------------------------------------
# This script test our log service functions
# ----------------------------------------

# Import functions from the log_service module
from app.services.log_service import read_log_file
from app.services.log_service import extract_error_lines

# Path to the log file
log_path = "backend/data/logs/vendor_file_import.log"

# Read the log file
log_text = read_log_file(log_path)

print("Full Log File:")
print(log_text)

print("\nDetected Errors:")

#Extract error lines
errors = extract_error_lines(log_text)

# Print the detected errors
for error in errors:
    print(error)