from datetime import datetime, timedelta
import random

def generate_log(current_time, burst_mode):
    if burst_mode:
        levels = ["INFO", "WARN","ERROR"]
        levelweights = [0.4,0.3,0.3]
    else:
        levels = ["INFO", "WARN","ERROR"]
        levelweights = [0.7,0.2,0.1]

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

    return f"{timestamp} [{level}] {message}"

# Simulation control
current_time = datetime.now()

burst_mode = False
burst_remaining = 0

log_file = "application.log"

with open(log_file, "a") as file:

  for _ in range (500):
    
      log_line=generate_log(current_time, burst_mode)
      file.write(log_line + "\n")

      # decide if burst occurs
      if not burst_mode and random.random() < 0.1:
           burst_mode = True
           burst_remaining = random.randint(5,15)

      # Behavour depending on the state
      if burst_mode:
           increment = random.randint(0,1) # very fast logs
           burst_remaining -= 1

           if burst_remaining <=0:
                burst_mode = False
      
      else:
          increment = random.randint(2,20) # slower logs

      current_time += timedelta(seconds=increment)
