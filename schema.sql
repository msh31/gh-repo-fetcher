CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    repo TEXT NOT NULL,
    languages TEXT NOT NULL,
    school BOOLEAN DEFAULT FALSE,
    stars INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

DELETE FROM projects;

-- Indexes for better performance
CREATE INDEX idx_projects_school ON projects(school);
CREATE INDEX idx_projects_repo ON projects(repo);
CREATE INDEX idx_projects_languages ON projects(languages);
CREATE INDEX idx_projects_updated_at ON projects(updated_at);

-- Views
CREATE VIEW school_projects AS
SELECT * FROM projects WHERE school = true ORDER BY updated_at DESC;

CREATE VIEW personal_projects AS
SELECT * FROM projects WHERE school = false ORDER BY updated_at DESC;

CREATE VIEW project_summary AS
SELECT 
    'School Projects' as category,
    COUNT(*) as count,
    GROUP_CONCAT(DISTINCT languages) as all_languages
FROM projects WHERE school = true
UNION ALL
SELECT 
    'Personal Projects' as category,
    COUNT(*) as count,
    GROUP_CONCAT(DISTINCT languages) as all_languages
FROM projects WHERE school = false;

