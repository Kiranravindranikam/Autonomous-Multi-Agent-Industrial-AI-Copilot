import pandas as pd
import random
from datetime import datetime, timedelta

machines = [f"M-{i}" for i in range(100, 151)]

issues = [
    "Bearing Wear",
    "Overheating",
    "High Vibration",
    "Lubrication Failure",
    "Rotor Damage",
    "Motor Failure",
    "Pressure Drop",
    "Sensor Fault",
    "Coolant Leakage",
    "Belt Damage"
]

actions = [
    "Replaced Bearing",
    "Added Lubrication",
    "Changed Coolant",
    "Replaced Sensor",
    "Adjusted Alignment",
    "Tightened Belt",
    "Motor Repair",
    "Rotor Replacement",
    "Pressure Valve Repair",
    "General Maintenance"
]

technicians = [
    "Tech_A",
    "Tech_B",
    "Tech_C",
    "Tech_D",
    "Tech_E"
]

rows = []

start_date = datetime(2023, 1, 1)

for _ in range(1000):

    date = start_date + timedelta(days=random.randint(0, 900))

    machine = random.choice(machines)

    issue = random.choice(issues)

    action = random.choice(actions)

    downtime = round(random.uniform(0.5, 12), 2)

    repair_cost = random.randint(500, 25000)

    technician = random.choice(technicians)

    rows.append([
        date.date(),
        machine,
        issue,
        action,
        downtime,
        repair_cost,
        technician
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "date",
        "machine_id",
        "issue",
        "action_taken",
        "downtime_hours",
        "repair_cost",
        "technician"
    ]
)

df.to_csv(
    "data/raw/maintenance_logs/maintenance_logs.csv",
    index=False
)

print("Dataset Created")
print(df.head())