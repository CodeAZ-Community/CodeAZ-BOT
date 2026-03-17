import json # Just put this script in the data folder or modify the paths for urself

with open("current_xp.json", "r", encoding="utf-8") as file:
    data = json.load(file)

users = []

for user in data:
    if data.get(user) > 5000:
        users.append(user)

with open("users.txt", "a", encoding="utf-8") as file:
    file.write(str(users))