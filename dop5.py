import json

text = json.load(open("output.json", encoding="utf-8"))


def json_to_csv(json_data):
    rows = []
    for day, lessons in json_data.items():
        for lesson, details in lessons.items():
            row = {
                "Day": day,
                "Lesson": lesson,
                "Type": details.get("type", ""),
                "Subject": details.get("subject", ""),
                "Start Time": details["time"].get("start", ""),
                "End Time": details["time"].get("end", ""),
                "Teacher": details.get("teacher", ""),
                "Location": details.get("location", "")
            }
            rows.append(row)

    headers = ["Day", "Lesson", "Type", "Subject", "Start Time", "End Time", "Teacher", "Location"]
    csv_content = ",".join(headers) + "\n"
    for row in rows:
        csv_content += ",".join(f'"{row[header]}"' for header in headers) + "\n"

    return csv_content

with open("output5.csv", "w", encoding="utf-8") as output:
    output.write(json_to_csv(text))