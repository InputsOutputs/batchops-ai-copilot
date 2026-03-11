# ------------------------------------------------
# python_basics.py
# ------------------------------------------------
# This is our first Python script for the project.
# The purpose is to simulate batch jobs and
# identify which ones failed.
# ------------------------------------------------

# A list that contains multiple job records
# Each record is stored as a dictionary
jobs = [
    {"job_id": 1, "job_name": "Inventory_Load", "status": "SUCCESS"},
    {"job_id": 2, "job_name": "Vendor_File_Import", "status": "FAILED"},
    {"job_id": 3, "job_name": "Billing_Export", "status": "FAILED"},
    {"job_id": 4, "job_name": "Daily_GL_Posting", "status": "SUCCESS"}
]

#print a header to make the output easier to read
print("All jobs:")

# Function to print all jobs
def print_jobs(jobs):
    pass

# Function to get all failed jobs
def get_failed_jobs(jobs):
    pass

# Funtion to count all failed jobs
def count_failed_jobs(jobs):
    pass

# Add a variable to count the number of failed jobs
failed_count = 0
# Loop through every job in the jobs list
for job in jobs:

    # Print job details using an f-string
    # job['job_id'] get the job_id value from the dictionary
    # job['job_name'] get the job value
    # job['status'] gets the job status
    print(f"{job['job_id']} - {job['job_name']} - {job['status']}")

# Print a blank line and a new header
print("\nFailed Jobs:")

# Loop through the jobs again
for job in jobs:

    # Check if the status is FAILED
    if job["status"] == "FAILED":

        # If it is failed, print the job ID and name
        print(f"{job['job_id']} - {job['job_name']}")
        failed_count += 1

# Print the total number of jobs failed
print("\nTotal failed jobs: ", failed_count)