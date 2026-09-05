import csv
from datetime import datetime

INPUT_FILE = "event_log.csv"
TRANSITION_OUTPUT = "transition_analysis.csv"
PATIENT_OUTPUT = "patient_performance.csv"

# -------------------------------------------------
# 1. Read event log
# -------------------------------------------------

patients = {}

with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        case_id = row["Case_ID"]
        activity = row["Activity"]
        timestamp = datetime.strptime(
            row["Timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )

        if case_id not in patients:
            patients[case_id] = []

        patients[case_id].append((activity, timestamp))


# -------------------------------------------------
# 2. Calculate transition times
# -------------------------------------------------

transition_rows = []
patient_rows = []

for case_id, events in patients.items():

    # Sort events by timestamp
    events.sort(key=lambda x: x[1])

    registration_to_doctor = None
    doctor_to_discharge = None

    for i in range(len(events) - 1):

        activity1, time1 = events[i]
        activity2, time2 = events[i + 1]

        minutes = int((time2 - time1).total_seconds() / 60)

        transition_rows.append({
            "Case_ID": case_id,
            "From_Activity": activity1,
            "To_Activity": activity2,
            "Transition_Minutes": minutes
        })

        if activity1 == "Registration" and activity2 == "Doctor":
            registration_to_doctor = minutes

        if activity1 == "Doctor" and activity2 == "Discharge":
            doctor_to_discharge = minutes

    # Total process time
    if len(events) >= 2:
        total_minutes = int(
            (events[-1][1] - events[0][1]).total_seconds() / 60
        )
    else:
        total_minutes = 0

    patient_rows.append({
        "Case_ID": case_id,
        "Registration_to_Doctor_Minutes": registration_to_doctor,
        "Doctor_to_Discharge_Minutes": doctor_to_discharge,
        "Total_Process_Minutes": total_minutes
    })


# -------------------------------------------------
# 3. Save transition analysis
# -------------------------------------------------

with open(
    TRANSITION_OUTPUT,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "Case_ID",
        "From_Activity",
        "To_Activity",
        "Transition_Minutes"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(transition_rows)


# -------------------------------------------------
# 4. Save patient performance
# -------------------------------------------------

with open(
    PATIENT_OUTPUT,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "Case_ID",
        "Registration_to_Doctor_Minutes",
        "Doctor_to_Discharge_Minutes",
        "Total_Process_Minutes"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(patient_rows)


# -------------------------------------------------
# 5. Display results
# -------------------------------------------------

print()
print("==============================================")
print("CareFlow Transition Time Analysis")
print("==============================================")

for row in transition_rows:
    print(
        row["Case_ID"],
        "|",
        row["From_Activity"],
        "->",
        row["To_Activity"],
        "|",
        row["Transition_Minutes"],
        "minutes"
    )

print()
print("Files created successfully!")
print("1. transition_analysis.csv")
print("2. patient_performance.csv")