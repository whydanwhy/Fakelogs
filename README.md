Fake but realistic log generator.

A Python based log simulation tool that generated realistic, randomised, but structured logs with:

Probabilitistic log levels - INFO WARN ERROR
Time Progression from the current time onwards.
Burst behaviour - simulate outages and spikes.
Service level incidents
Supressional of events on condition
Structured JSON output NSJSON
Request tracing via request_id

Example output - 

{"timestamp": "2026-04-16 12:00:10", "level": "ERROR", "service": "auth", "request_id": "req-a1b2c3d4", "incident": true, "message": "Service unavailable"}

How to use:
python fake_logs.py

Logs will be written to:

application.log


Designed for me to learn:
Python
AI prompting for design and execution
and for me to build observability tools.

