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

        if not results:
            print("No errors detected.")
        else:

            print("Detected Errors:")
            
            for error in results:

                print(
                    f"- {error['error_type']} "
                    f"(Severity: {error['severity']})"
                )
                
                print(f" Message: {error['message']}")

if __name__ == "__main__":
    monitor_jobs()