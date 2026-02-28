import csv
import json

# -----------------------
# Safe Conversion Functions
# -----------------------

def safe_int(value):
    try:
        return int(value)
    except:
        return None

def safe_float(value):
    try:
        return float(value)
    except:
        return None


# -----------------------
# Initialize Lists
# -----------------------

clean_records = []
error_records = []

total_rows = 0


# -----------------------
# Read CSV & Process
# -----------------------

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row_number, row in enumerate(reader, start=1):
        total_rows += 1
        errors = []

        name = row["name"].strip()
        age = safe_int(row["age"])
        income = safe_float(row["income"])

        # Validation Rules
        if not name:
            errors.append("Missing name")

        if age is None:
            errors.append("Invalid age")
        elif age < 18 or age > 60:
            errors.append("Age out of range")

        if income is None:
            errors.append("Invalid income")
        elif income < 0:
            errors.append("Negative income")

        # If errors → store in error list
        if errors:
            error_records.append({
                "row": row_number,
                "errors": errors
            })
        else:
            clean_records.append({
                "name": name,
                "age": age,
                "income": income
            })


# -----------------------
# Write clean.jsonl
# -----------------------

with open("clean.jsonl", "w") as f:
    for record in clean_records:
        f.write(json.dumps(record) + "\n")


# -----------------------
# Write errors.jsonl
# -----------------------

with open("errors.jsonl", "w") as f:
    for record in error_records:
        f.write(json.dumps(record) + "\n")


# -----------------------
# Generate Report
# -----------------------

valid_count = len(clean_records)
invalid_count = len(error_records)
error_rate = (invalid_count / total_rows) * 100 if total_rows > 0 else 0

report = {
    "total_rows": total_rows,
    "valid_rows": valid_count,
    "invalid_rows": invalid_count,
    "error_rate_percent": round(error_rate, 2)
}

with open("report.json", "w") as f:
    json.dump(report, f, indent=4)


# -----------------------
# Logging
# -----------------------

print("Total rows read:", total_rows)
print("Valid rows:", valid_count)
print("Invalid rows:", invalid_count)
print("Clean data saved to clean.jsonl")
print("Errors saved to errors.jsonl")
print("Report saved to report.json")


# -----------------------
# Preview First 5 Clean Records
# -----------------------

print("\nPreview (First 5 Clean Records):")
for record in clean_records[:5]:
    print(record)