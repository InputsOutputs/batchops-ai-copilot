ERROR_PRIORITY = {
    "DATA_DUPLICATE": 5,
    "PERMISSION_DENIED": 4,
    "FILE_NOT_FOUND": 3,
    "DATABASE_TIMEOUT": 2,
    "DEPENDENCY_FAILURE": 1,
    "UNKNOWN_ERROR": 0
}

ROOT_CAUSE_MAP = {
    "FILE_NOT_FOUND": "Missing input file from upstream source.",
    "DATABASE_TIMEOUT": "Database running issue or long running query.",
    "PERMISSION_DENIED": "Authentication or authorization failure.",
    "DEPENDENCY_FAILURE": "Upstream job dependency not completed.",
    "DATA_DUPLICATE": "Duplicate records detected in database."
}

ACTION_MAP = {
    "FILE_NOT_FOUND": "Check if the file was delivered to the expected location (SFTP/inbound folder).",
    "DATABASE_TIMEOUT": "Verify database connectivity and check for long running queries.",
    "PERMISSION_DENIED": "Verify credentials, permissions, and access configuration.",
    "DEPENDENCY_FAILURE": "Check upstream job status and rerun dependency if needed.",
    "DATA_DUPLICATE": "Run queries to identify duplicate records and clean up data."
}

OWNER_MAP = {
    "FILE_NOT_FOUND": {
        "primary_owner": "Operations Team",
        "secondary_owner": "Vendor / Upstream Team"
    },
    "DATABASE_TIMEOUT": {
        "primary_owner": "Database Team",
        "secondary_owner": "Application Team"
    },
    "PERMISSION_DENIED": {
        "primary_owner": "Security Team",
        "secondary_owner": "Application Team"
    },
    "DEPENDENCY_FAILURE": {
        "primary_owner": "Operations Team",
        "secondary_owner": "Application Team"
    },
    "DATA_DUPLICATE": {
        "primary_owner": "Application Team",
        "secondary_owner": "Database Team"
    }
}