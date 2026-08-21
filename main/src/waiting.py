import csv
from datetime import datetime

patients = {}

with open("patients.csv", "r") as file:
    data = csv.DictReader(file)

    for row in data:
        patient_id = row["patient_id"]
        activity = row["activity"]
        event_time = row["event_time"]

        if patient_id not in patients:
            patients[patient_id] = {}

        patients[patient_id][activity] = event_time


print("CareFlow Waiting Time Analysis")
print("--------------------------------")

for patient_id, activities in patients.items():

    registration = datetime.strptime(
        activities["Registration"], "%H:%M"
    )

    doctor = datetime.strptime(
        activities["Doctor"], "%H:%M"
    )

    waiting_time = doctor - registration

    minutes = waiting_time.seconds // 60

    print(patient_id, "| Waiting Time:", minutes, "minutes")