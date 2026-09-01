import csv
from datetime import datetime

transitions = {}

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


for patient, events in patients.items():

    for i in range(len(events) - 1):

        activity1, time1 = events[i]
        activity2, time2 = events[i + 1]

        t1 = datetime.strptime(time1, "%H:%M")
        t2 = datetime.strptime(time2, "%H:%M")

        minutes = (t2 - t1).seconds // 60

        transition = activity1 + " → " + activity2

        if transition not in transitions:
            transitions[transition] = []

        transitions[transition].append(minutes)


print("Average Transition Time")
print("------------------------")

for transition, times in transitions.items():

    average = sum(times) / len(times)

    print(
        transition,
        "| Average:",
        round(average, 2),
        "minutes"
    )