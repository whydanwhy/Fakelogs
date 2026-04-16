from datetime import datetime
import random

def generate_log():
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    levels=["INFO","WARN","ERROR"]
    levelweights=[0.7, 0.2, 0.1]

    level = random.choices(levels, weights=levelweights, k=1)[0]

    message = {
        "INFO": [
            "App started",
            "User Logged in",
            "Scheduled job completed",
            "Connection established"
        ],
        "WARN": [
            "High memory usage deteched",
            "API response delayed",
            "Disk space running low"
        ],
        "ERROR": [
            "Database connection failed",
            "Unhandled exception occurred",
            "Service unavailable"
        ]
    }

    message = random.choice(message[level])

    log_line = f"{timestamp} [{level}] {message}"
    return log_line

for _ in range(20):
    print(generate_log())