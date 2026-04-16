from datetime import datetime
import random

def generate_log():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    levels = ["INFO","WARN","ERROR"]
    level = random.choice(levels)

    message = "Application event occurred"
    
  

    log_line = f"{timestamp} [{level}] {message}"
    return log_line

print(generate_log())