from datetime import datetime, timedelta
import random

def generate_log(current_time):
    levels = ["INFO","WARN","ERROR"]
    levelweights = [0.7, 0.2, 0.1]

    level = random.choices(levels, weights=levelweights, k=1)[0]

    messages = {
    "INFO": [
        "Application started",
        "User logged in",
        "Scheduled job completed",
        "Connection established"
    ],
    "WARN": [
        "High memory usage detected",
        "API response delayed",
        "Disk space running low"
    ],
    "ERROR": [
        "Database connection failed",
        "Unhandled exception occurred",
        "Service unavailable"
    ]
}

    message = random.choice(messages[level])

    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

    log_line=f"{timestamp} [{level}] {message}"
    return log_line

#Time simulation
start_time = datetime.now()

current_time = start_time

for _ in range(20):
    print(generate_log(current_time))

#time crement ransom by seconds
    increment = random.randint(1, 60)
    current_time += timedelta(seconds=increment)