# ---------------------------------------
# log_reader_test.py
# ---------------------------------------
# Day 6 test script:
# 1. Read a log file
# 2. Extract raw error lines
# 3. Convert them into structured error records
# ----------------------------------------

# Import functions from the log_service module
from app.services.log_service import read_log_file
from app.services.log_service import extract_error_lines
from app.services.log_service import structure_detected_errors

# Path to the log file
log_path = "backend/data/logs/billing_export.log"

# Read the log file
log_text = read_log_file(log_path)

print("Full Log File:")
print(log_text)

print("\nDetected Raw Errors:")

#Extract raw matching lines
error_lines = extract_error_lines(log_text)

for error_line in error_lines:
    print(error_line)

print("\nStructured Errors:")

# Convert raw lines into structured dictionaries
structured_errors = structure_detected_errors(error_lines)
# Print the detected errors
for error in structured_errors:
    print(error)