import json

with open("data.json", "r", encoding="utf-8") as f:
    student = json.load(f)

print(student)

print(student["jméno"])

student["prospěch"].append(1)
print(student["prospěch"])

student["status"] = "absolvent"


with open("data.json", "w", encoding="utf-8") as f:
    json.dump(student, f, ensure_ascii=False, indent=4)