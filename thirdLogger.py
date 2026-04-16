from datetime import datetime
import random

def gereate_log():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    levels = ["INFO", "WARN", "ERROR"]
    levelweights = [0.7,0.2,0.1] # probabilities

    level = random.choices(levels, weights=levelweights, k=1)[0]

    message = "Application event occurred"

    log_line=f"{timestamp} {level} {message}"
    return log_line

for _ in range(100):
  print(gereate_log())