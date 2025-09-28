import json, sqlite3, subprocess

def check_if_installed(cmd):
    try:
        subprocess.run([cmd, "--version"])
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

if not check_if_installed("gh"):
    print("GitHub CLI is not installed or not found in your PATH")

if not check_if_installed("sqlite3"):
    print("SQLite3 is not installed or not found in your PATH")

print("\ngoodjob! all requirements are fulfilled. Let's continue")
# print(output)
#
# connection = sqlite3.connect("projects.db")
# cursor = connection.cursor()
#
# for row in cursor.execute("SELECT * FROM projects"):
#     print(row)
#
# connection.close()
