# ------------------------------------------------
# python_basics.py
# ------------------------------------------------
# Day 3 goal:
# Learn how to organize code using functions
#
# This script:
# 1. returns a list of batch jobs
# 2. prints all jobs
# 3. filters failed jobs
# 4. counts failed jobs
# ------------------------------------------------

# This function returns a list of job records
# Each job is represented as a dictionary.
def get_all_jobs():
    return [
        {"job_id": 1, "job_name": "Inventory_Load", "status": "SUCCESS"},
        {"job_id": 2, "job_name": "Vendor_File_Import", "status": "FAILED"},
        {"job_id": 3, "job_name": "Billing_Export", "status": "FAILED"},
        {"job_id": 4, "job_name": "Daily_GL_Posting", "status": "SUCCESS"}
    ]


# This function prints all jobs passed into it.
# The parameter "jobs" is expected to be a list of dictionaries.
def print_jobs(jobs):
    print("All Jobs:")

    # Loop through each job in the list
    for job in jobs:
        print(f"{job['job_id']} - {job['job_name']} - {job['status']}")

# This function filters the list and returns
# only jobs with a status of FAILED.
def get_failed_jobs(jobs):
    failed_jobs = []

    # Check each job one by one
    for job in jobs:
        if job["status"] == "FAILED":
            failed_jobs.append(job)

    return failed_jobs


# This function counts how many failed jobs exist.
def count_failed_jobs(jobs):
    failed_count = 0

    # Loop through all jobs and increase the counter
    # whenever a failed job is found.
    for job in jobs:
        if job["status"] == "FAILED":
            failed_count += 1

    return failed_count


# This funtion prints failed jobs
def print_failed_jobs(jobs):
    print("Failed Jobs:")

    # Loop through failed jobs and print them
    for job in jobs:
        print(f"{job['job_id']} - {job['job_name']}")


#---------------------------------------------
# Main program execution starts here
#---------------------------------------------

# Get all jobs from the function
jobs = get_all_jobs()

# Print all jobs
print_jobs(jobs)

# Print a blank line for cleaner output
print()

# Get only failed jobs
failed_jobs = get_failed_jobs(jobs)

# Print failed jobs
print_failed_jobs(failed_jobs)

# Count failed jobs and print the result
total_failed = count_failed_jobs(jobs)
print(f"\nTotal failed jobs: {total_failed}")