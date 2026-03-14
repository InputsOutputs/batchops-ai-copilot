# ------------------------------------
# job_service.py
# ------------------------------------
# Service responsible for job data and job analysis
# ------------------------------------


def get_all_jobs():
    """
    Returns a list of batch jobs.
    Each job included the log file location.
    """

    jobs = [
        {
            "job_id": 1,
            "job_name": "Vendor_File_Import",
            "log_file": "backend/data/logs/vendor_file_import.log"
        },
        {
            "job_id": 2,
            "job_name": "Billing_Export",
            "log_file": "backend/data/logs/billing_export.log"
        }
    ]
    return jobs