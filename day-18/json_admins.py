import json
from pathlib import Path

base_dir = Path(__file__).parent
input_file = base_dir / "users.json"

with open(input_file, "r", encoding="utf-8") as file:
    users = json.load(file)

admins = []

for user in users:
    if not isinstance(user, dict):
        print("Skipping invalid record:", user)
        continue

    name = user.get("name")

    if not isinstance(name, str) or not name.strip():
        print("Skipping record with invalid name:", user)
        continue

    if user.get("role") == "admin":
        admins.append(user)

print("Admin users:", admins)

output_file = base_dir / "admin_users.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(admins, file, indent=4)

print("Admin users saved successfully.")