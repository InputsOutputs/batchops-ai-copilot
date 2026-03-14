# ------------------------------------
# job_analyzer.py
# ------------------------------------
# Combines job data with log analysis
# ------------------------------------

from app.services.log_service import read_log_file
from app.services.log_service import extract_error_lines
from app.services.log_service import structure_detected_errors


def analyze_job(job):
    """
    Runs log analysis for a given job.
    Returns structured error results.
    """

    log_file = job["log_file"]

    # Read the log file
    log_text = read_log_file(log_file)

    # Extract raw error lines
    error_lines = extract_error_lines(log_text)

    # Convert them into structured errors
    structured_errors = structure_detected_errors(error_lines)

    return structured_errors