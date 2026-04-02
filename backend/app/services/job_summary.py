# Definition to create job summary
def build_job_summary(job, job_status, severity, diagnosis):
    return {
        "job_name": job["job_name"],
        "status": job_status,
        "severity": severity,
        "diagnosis": {
            "root_cause": diagnosis["root_cause"],
            "action": diagnosis["action"],
            "primary_owner": diagnosis["owner_info"]["primary_owner"] if diagnosis["owner_info"] else None,
            "secondary_owner": diagnosis["owner_info"]["secondary_owner"] if diagnosis["owner_info"] else None,
            "contributing_errors": diagnosis["contributing_errors"]
        }
    }