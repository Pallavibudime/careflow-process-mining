import csv
from datetime import datetime

patients = {}

with open("patients.csv", "r") as file:
    data = csv.DictReader(file)

    for row in data:
        patient = row["patient_id"]

        if patient not in patients:
            patients[patient] = []

        patients[patient].append(
            (row["activity"], row["event_time"])
        )

print("CareFlow Transition Time Analysis")
print("----------------------------------")

for patient, events in patients.items():

    for i in range(len(events) - 1):

        activity1, time1 = events[i]
        activity2, time2 = events[i + 1]

        t1 = datetime.strptime(time1, "%H:%M")
        t2 = datetime.strptime(time2, "%H:%M")

        minutes = (t2 - t1).seconds // 60

        print(
            patient,
            "|",
            activity1,
            "→",
            activity2,
            "|",
            minutes,
            "minutes"
        )