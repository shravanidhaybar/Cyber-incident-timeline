# Cyber Incident Timeline Generator
# Beginner-friendly Python code

def read_logs(file_name):
    events = []
    with open(file_name, "r") as file:
        for line in file:
            time, description = line.strip().split(" ", 1)
            events.append((time, description))
    return events

def generate_timeline(events):
    events.sort()
    print("\nCyber Incident Timeline:\n")
    for time, desc in events:
        print(f"{time} → {desc}")

def assess_risk(events):
    risk = "Low"
    for _, desc in events:
        if "Privilege" in desc or "Data" in desc:
            risk = "High"
            break
        elif "Suspicious" in desc or "failed" in desc:
            risk = "Medium"
    return risk

logs = read_logs("sample_logs.txt")
generate_timeline(logs)

print("\nIncident Risk Level:", assess_risk(logs))
