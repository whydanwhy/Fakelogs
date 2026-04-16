from datetime import datetime, timedelta
import random



outage_rules = {
        "auth": {
            "error": "Service unavailable",
            "blocked_info": ["User logged in"]
        },
        "payments": {
            "error": "Database connection failed",
            "blocked_info": ["Scheduled job completed"]
        }
}

def generate_log(current_time, burst_mode, incident_service, outage_rules):

    services = ["auth", "payments", "orders", "inventory"]

    # --- Service selection ---
    if incident_service and random.random() < 0.7:
        service = incident_service
    else:
        service = random.choice(services)

    # --- Level weights ---
    if burst_mode:
        weights = [0.4, 0.3, 0.3]
    else:
        weights = [0.7, 0.2, 0.1]

    # Incident bias
    if incident_service and service == incident_service:
        weights = [0.2, 0.3, 0.5]

    levels = ["INFO", "WARN", "ERROR"]
    level = random.choices(levels, weights=weights, k=1)[0]

    # --- Messages ---
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
    # outage rules

    # --- Apply outage rules ---
    if incident_service and service == incident_service:

        rule = outage_rules.get(incident_service)

        if rule:
            # Force specific error more often
            if level == "ERROR" and random.random() < 0.7:
                message = rule["error"]
            else:
                message = random.choice(messages[level])

            # Block certain INFO messages
            if level == "INFO":
                allowed = [
                    m for m in messages["INFO"]
                    if m not in rule["blocked_info"]
                ]

                # If everything is blocked, downgrade to WARN
                if not allowed:
                    level = "WARN"
                    message = random.choice(messages["WARN"])
                else:
                    message = random.choice(allowed)
        else:
            message = random.choice(messages[level])
    else:
        message = random.choice(messages[level])

    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    user_id = random.randint(1000, 1100)
    ip = f"192.168.1.{random.randint(1, 255)}"

    return (
        f"{timestamp} [{level}] "
        f"service={service} user_id={user_id} ip={ip} "
        f"{message}"
    )

# --- Simulation control ---
current_time = datetime.now()

burst_mode = False
burst_remaining = 0

incident_service = None
incident_remaining = 0

log_file = "application.log"

with open(log_file, "w") as file:

    for _ in range(100):

        log_line = generate_log(current_time, burst_mode, incident_service, outage_rules)
        file.write(log_line + "\n")

        # --- Trigger incident ---
        if not incident_service and random.random() < 0.05:
            incident_service = random.choice(["auth", "payments"])
            incident_type = outage_rules[incident_service]["error"]
            incident_remaining = random.randint(10, 25)

        # --- Resolve incident ---
        if incident_service:
            print(f"INCIDENT ACTIVE: {incident_service}")
            incident_remaining -= 1
            if incident_remaining <= 0:
                incident_service = None
                incident_type = None

        # --- Burst logic ---
        if not burst_mode and random.random() < 0.1:
            burst_mode = True
            burst_remaining = random.randint(5, 15)

        if burst_mode:
            increment = random.randint(0, 1)
            burst_remaining -= 1

            if burst_remaining <= 0:
                burst_mode = False
        else:
            increment = random.randint(2, 10)

        current_time += timedelta(seconds=increment)