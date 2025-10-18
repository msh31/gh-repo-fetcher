# GitHub Repo Fetcher
This is a simple script to fetch public repositories from a GitHub username and put their details into an SQLite database. It's used for my personal website where I just run this script on my server through a cron job.

## Usage
> Note: You need [SQLite](https://sqlite.org/) installed!

```py
sqlite3 projects.db < schema.sql
```
