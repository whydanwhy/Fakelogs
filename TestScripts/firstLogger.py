from datetime import datetime

def generate_log():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level = "INFO"
    message = "Application started"
    
    log_line = f"{timestamp} [{level}] {message}"
    return log_line

print(generate_log())