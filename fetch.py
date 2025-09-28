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

connection = sqlite3.connect("projects.db")
cursor = connection.cursor()

result = subprocess.run(
    ["gh", "repo", "list", "msh31", "--visibility", "public", "--json", "name,description,languages,updatedAt,url,stargazerCount"],
    capture_output=True,
    text=True
)

found_repos = json.loads(result.stdout)

for repo in found_repos:
    print(repo)

connection.commit()
connection.close()
