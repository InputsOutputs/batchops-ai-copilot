# --------------------------------
# job_monitor.py
# --------------------------------
# Main monitoring script for batch jobs
from app.services.job_service import get_all_jobs
from app.services.job_analyzer import analyze_job
from app.services.diagnosis_service import generate_diagnosis
import json


def monitor_jobs():
    """
    Runs analysis on all jobs
    """

    jobs = get_all_jobs()
    total_jobs = 0
    failed_jobs = 0
    unknown_jobs = 0
    success_jobs = 0

    all_jobs_summary = []

    for job in jobs:

        total_jobs += 1

        print("\n====================================")
        print(f"Analyzing Job: {job['job_name']}")
        print("====================================")

        results, log_text = analyze_job(job)

        # Determine job status based on whether errors were detected
        if log_text is None:
            job_status = "UNKNOWN"
            overall_severity = "MEDIUM"
        elif not results:
            print("No errors detected.")
            job_status = "SUCCESS"
            overall_severity = "NONE"
        else:
            job_status = "FAILED"

            for error in results:

                # Determine the highest severity among detected errors
                severities = [error["severity"] for error in results]
                if "HIGH" in severities:
                    overall_severity = "HIGH"
                elif "MEDIUM" in severities:
                    overall_severity = "MEDIUM"
                else:
                    overall_severity = "LOW"
            
        print(f"Job Status: {job_status}")
        print(f"Overall Severity: {overall_severity}")

        # Generate diagnosis
        diagnosis = generate_diagnosis(results)

        print_diagnosis(diagnosis)

        if job_status == "FAILED":
            failed_jobs += 1
        elif job_status == "SUCCESS":
            success_jobs += 1
        elif job_status == "UNKNOWN":
            unknown_jobs += 1

        # Create job summary for this job for structured output
        job_summary = {
            "job_name": job["job_name"],
            "status": job_status,
            "severity": overall_severity,
            "diagnosis": {
                "root_cause": diagnosis["root_cause"],
                "action": diagnosis["action"],
                "primary_owner": diagnosis["owner_info"]["primary_owner"] if diagnosis["owner_info"] else None,
                "secondary_owner": diagnosis["owner_info"]["secondary_owner"] if diagnosis["owner_info"] else None,
                "contributing_errors": diagnosis["contributing_errors"]
            }
        }
        # Appends summary of each job to overall summary list
        all_jobs_summary.append(job_summary)

    print("\nAll Jobs Summary:")
    print(all_jobs_summary)

    print("\n====================================")
    print("Monitoring Summary")
    print("====================================")

    print(f"Total Jobs: {total_jobs}")
    print(f"Failed Jobs: {failed_jobs}")
    print(f"Unknown Jobs: {unknown_jobs}")
    print(f"Successful Jobs: {success_jobs}")

# Function for printing logic
def print_diagnosis(diagnosis):
    """
    Print diagnosis output in structured format.
    """
    if diagnosis["root_cause"]:
        print(f"Root Cause: {diagnosis['root_cause']}")
        print(f"Suggested Action: {diagnosis['action']}")

        # Print ownership details
        print(f"\nPrimary Owner: {diagnosis['owner_info']['primary_owner']}")
        print(f"Secondary Owner: {diagnosis['owner_info']['secondary_owner']}")

        # Print contributing issues only if present
        if diagnosis["contributing_errors"]:
            print(f"\nContributing Issues ({len(diagnosis['contributing_errors'])}):")
            for issue in diagnosis["contributing_errors"]:
                print(f"- {issue}")


if __name__ == "__main__":
    monitor_jobs()