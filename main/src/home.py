# patients = [
#     ["P001", "Registration", "09:00"],
#     ["P001", "Doctor", "09:30"],
#     ["P001", "Discharge", "11:00"],
#     ["P002", "Registration", "09:15"],
#     ["P002", "Doctor", "10:00"],
#     ["P002", "Discharge", "11:30"]
# ]

# print("CareFlow Patient Journey")
# print("------------------------")

# for patient in patients:
#     print(
#         "Patient:", patient[0],
#         "| Activity:", patient[1],
#         "| Time:", patient[2]
#     )

import csv

with open("patients.csv", "r") as file:
    data = csv.DictReader(file)

    for row in data:
        print(
            row["patient_id"],
            "|",
            row["activity"],
            "|",
            row["event_time"]
        )