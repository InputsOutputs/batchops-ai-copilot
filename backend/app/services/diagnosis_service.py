# ----------------------------------------------
# diagnosis_service.py
# ----------------------------------------------
# Convers structured errors into human-readable diagnosis
# ----------------------------------------------

# Priority ranking (higher = more important)
ERROR_PRIORITY = {
    "PERMISSION_DENIED": 4,
    "FILE_NOT_FOUND": 3,
    "DATABASE_TIMEOUT": 2,
    "DEPENDENCY_FAILURE": 1,
    "UNKNOWN_ERROR": 0
}

def get_root_cause(error_type):
    """
    Maps error types to root cause explanations.
    """

    if error_type == "FILE_NOT_FOUND":
        return "Missing input file from upstream source."

    elif error_type == "DATABASE_TIMEOUT":
        return "Database running issue or long running query."

    elif error_type == "PERMISSION_DENIED":
        return "Authentication or authorization failure."
        
    elif error_type == "DEPENDENCY_FAILURE":
        return "Upstream job dependency not completed."

    elif error_type == "DATA_DUPLICATE":
        return "Duplicate records detected in database."

    else:
        return "Unknow issue. Further investigation required."

def get_suggested_action(error_type):
    """
    Maps error type to root cause explanations.
    """

    if error_type == "FILE_NOT_FOUND":
        return "Check if the file was delivered to the expected location (SFTP/inbound folder)."

    elif error_type == "DATABASE_TIMEOUT":
        return "Verify database connectivity and check for long running queries."

    elif error_type == "PERMISSION_DENIED":
        return "Verify credentials, permissions, and access configuration."

    elif error_type == "DEPENDENCY_FAILURE":
        return "Check upstream job status and rerun dependency if needed."

    elif error_type == "DATA_DUPLICATE":
        return "Run queries to identify duplicate records and clean up data."

    else:
        return "Review logs and escalate to application team if needed."

def generate_diagnosis(errors):
    """
    Generates a primary root case and suggested action
    based on detected errors.
    """

    if not errors:
        return None, None

    # Pick the first error as primary (simple logic for now)
    primary_error = max(
        errors,
        key=lambda e: ERROR_PRIORITY.get(e["error_type"], 0)
    )

    sorted_errors = sorted(
        errors,
        key=lambda e: ERROR_PRIORITY.get(e["error_type"], 0),
        reverse=True
    )

    error_type = primary_error["error_type"]
    
    primary_error = sorted_errors[0]
    secondary_errors = sorted_errors[1:]

    root_cause = get_root_cause(error_type)
    action = get_suggested_action(error_type)

    return root_cause, action