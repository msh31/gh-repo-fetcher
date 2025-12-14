import json, sqlite3, subprocess, requests

def check_if_installed(cmd):
    try:
        subprocess.run([cmd, "--version"])
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

if not check_if_installed("sqlite3"):
    print("SQLite3 is not installed or not found in your PATH")
    exit(1)

print("\nFetching repos from Forgejo...")

connection = sqlite3.connect("projects.db")
cursor = connection.cursor()

response = requests.get(
    "https://git.marco007.dev/api/v1/users/marco/repos",
    params={"limit": 200}
)

if response.status_code != 200:
    print(f"Error fetching repos: {response.status_code}")
    exit(1)

found_repos = response.json()
cursor.execute("DELETE FROM projects")  # clear all entries

for repo in found_repos:
    if repo.get("private"):
        continue
    
    lang_response = requests.get(
        f"https://git.marco007.dev/api/v1/repos/marco/{repo['name']}/languages"
    )
    languages = lang_response.json() if lang_response.status_code == 200 else {}
    languages_str = ", ".join(languages.keys())
    
    cursor.execute(
        """INSERT INTO projects (name, description, repo, languages, stars, updated_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
        (
            repo["name"],
            repo.get("description"),
            repo["name"], 
            languages_str,
            repo.get("stars_count", 0),
            repo["updated_at"],
        ),
    )

connection.commit()
connection.close()

print(f"\nDone! Imported {len(found_repos)} repos")
