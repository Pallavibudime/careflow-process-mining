patients = [
    ["P001", "Registration"],
    ["P001", "Doctor"],
    ["P001", "Discharge"],
    ["P002", "Registration"],
    ["P002", "Doctor"],
    ["P002", "Discharge"]
]

print("CareFlow Patient Journey")
print("------------------------")

for patient in patients:
    print("Patient:", patient[0], "| Activity:", patient[1])