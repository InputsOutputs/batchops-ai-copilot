# --------------------------------
# job_monitor.py
# --------------------------------
# Main monitoring script for batch jobs
from app.services.job_service import get_all_jobs
from app.services.job_analyzer import analyze_job
from app.services.diagnosis_service import generate_diagnosis

def monitor_jobs():
    """
    Runs analysis on all jobs
    """

    jobs = get_all_jobs()

    for job in jobs:

        print("\n====================================")
        print(f"Analyzing Job: {job['job_name']}")
        print("====================================")

        results = analyze_job(job)

        # Determine job status based on whether errors were detected
        if not results:
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
        root_cause, action, owner_info, contributing_error_types = generate_diagnosis(results)

        if root_cause:
            print(f"Root Cause: {root_cause}")
            print(f"Suggested Action: {action}")

            # Print ownership details
            print(f"\nPrimary Owner: {owner_info['primary_owner']}")
            print(f"Secondary Owner: {owner_info['secondary_owner']}")

            # Print contributing issues only if present
            if contributing_error_types:
                print("\nContributing Issues:")
                for issue in contributing_error_types:
                    print(f"- {issue}")


        # If errors exist, print details
        """
        if results:
            print("\nDetected Errors:")

            for error in results:
                print(
                    f"- {error['error_type']} "
                    f"(Severity: {error['severity']})"
                )
                
                print(f"  Message: {error['message']}\n")
        """

if __name__ == "__main__":
    monitor_jobs()