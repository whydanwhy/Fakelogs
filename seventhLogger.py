from datetime import datetime, timedelta
import random

def generate_log(current_time, burst_mode):

    # Dyanmic weights
    if burst_mode:
        levelweights = [0.4,0.4,0.3]
    else:
        levelweights = [0.7,0.2,0.1]

    levels = ["INFO","WARN","ERROR"]
    level = random.choices(levels, weights=levelweights,k=1)[0]

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

    # Structured entites
    services = ["auth", "paynets", "orders", "inventory"]
    service = random.choice(services)
    
    user_id = random.randint(1000,1100)

    ip = f"192/168.0.{random.randint(1,255)}"

    message = random.choice(messages[level])
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

    return (
        f"{timestamp} [{level}] "
        f"service={service} user_id={user_id} ip={ip} "
        f"{message}"
    )

# Simulation control
current_time = datetime.now()

burst_mode = False
burst_remaining = 0

log_file = "application.log"

with open(log_file, "w") as file:
    
    for _ in range(500):
        
        log_line = generate_log(current_time,burst_mode)
        file.write(log_line + "\n")

        # Enter Burst Mode
        if not burst_mode and random.random() < 0.1:
            burst_mode = True
            burst_remaining = random.randint(5,15)

        # Behavour
        if burst_mode:
            increment = random.randint(0,1)
            burst_remaining -= 1

            if burst_remaining <= 0:
                burst_mode = False
        
        else:
            increment = random.randint(2, 10)

        current_time += timedelta(seconds=increment)

    