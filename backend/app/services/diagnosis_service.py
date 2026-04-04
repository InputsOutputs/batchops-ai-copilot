# ----------------------------------------------
# diagnosis_service.py
# ----------------------------------------------
# Converts structured errors into human-readable diagnosis
# ----------------------------------------------

from app.config.constants import ERROR_PRIORITY, ROOT_CAUSE_MAP, ACTION_MAP, OWNER_MAP
# Priority ranking (higher = more important)

def get_root_cause(error_type):
    return ROOT_CAUSE_MAP.get(error_type, "Unknown Issue. Further Investigation Required.")

def get_suggested_action(error_type):
    """
    Maps error type to root cause explanations.
    """
    return ACTION_MAP.get(error_type, "Review logs and escalate to application team if needed.")

# This function gets the team owners
def get_team_owner(error_type):
    """
    Determines which team should handle the issue
    based on the error type.

    Returns:
    dictionary: primary and secondary team owners
    """
    return OWNER_MAP.get(error_type, {
        "primary_team": "Run My Jobs Team",
        "secondary_team": "Application Team"
    })

def generate_diagnosis(errors):
    """
    Generates diagnosis including:
    - Root Cause
    - Suggested Action
    - Ownership
    """
    # If no errors, return empty values
    if not errors:
        return {
            "root_cause": None,
            "action": None,
            "owner_info": None,
            "contributing_errors": []
        }

    # Import priority mapping (adding in day 10)
    from app.services.diagnosis_service import ERROR_PRIORITY

    # Sort errors by priority (highest first)
    sorted_errors = sorted(
        errors,
        key=lambda e: ERROR_PRIORITY.get(e["error_type"], 0),
        reverse=True
    )

    # Pick highest priority error as root cause
    primary_error = sorted_errors[0]

    # Contributing errors
    contributing_errors = sorted_errors[1:]

    contributing_error_types = [e["error_type"] for e in contributing_errors]
    
    error_type = primary_error["error_type"]

    # Get root cause explanation
    root_cause = get_root_cause(error_type)

    # Get suggested action
    action = get_suggested_action(error_type)

    # Get ownership mapping
    owner_info = get_team_owner(error_type)

    return {
        "root_cause": root_cause,
        "action": action,
        "owner_info": owner_info,
        "contributing_errors": contributing_error_types
    }