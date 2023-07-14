default = open("./package/default/database.json", "r").read()

with open("./package/db/database.json", "w") as f:
    f.write(default)