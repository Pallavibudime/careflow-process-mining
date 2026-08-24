import csv

with open("patients.csv", "r") as input_file, open("event_log.csv", "w", newline="") as output_file:

    reader = csv.DictReader(input_file)

    fieldnames = ["Case_ID", "Activity", "Timestamp"]

    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        writer.writerow({
            "Case_ID": row["patient_id"],
            "Activity": row["activity"],
            "Timestamp": "2026-08-20 " + row["event_time"] + ":00"
        })

print("Event Log Created Successfully!")