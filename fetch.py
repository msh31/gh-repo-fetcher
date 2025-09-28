import json, sqlite3, subprocess

output = subprocess.check_output(["gh", "version"])

if len(output) == 0:
    print("the github cli is required for this script to work!")
else:
    print("goodjob! github cli is installed")
# print(output)
#
# connection = sqlite3.connect("projects.db")
# cursor = connection.cursor()
#
# for row in cursor.execute("SELECT * FROM projects"):
#     print(row)
#
# connection.close()
