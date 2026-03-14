# --------------------------------
# job_monitor.py
# --------------------------------
# Main monitoring script for batch jobs
from app.services.job_service import get_all_jobs
from app.services.job_analyzer import analyze_job

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

        # If errors exist, print details
        if results:
            print("\nDetected Errors:")

            for error in results:
                print(
                    f"- {error['error_type']} "
                    f"(Severity: {error['severity']})"
                )
                
                print(f"  Message: {error['message']}\n")

if __name__ == "__main__":
    monitor_jobs()