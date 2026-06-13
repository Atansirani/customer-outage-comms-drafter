from agent import generate_outage_updates

timeline = """
10:05 Database cluster unavailable
10:12 Root cause identified
10:30 Failover initiated
10:45 Recovery in progress
11:00 Service restored
"""

result = generate_outage_updates(
    timeline,
    "Critical",
    "Empathetic"
)

print(result)