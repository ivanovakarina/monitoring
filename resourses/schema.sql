CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    project_name TEXT NOT NULL,
    project_status_activate BOOLEAN NOT NULL,
    repeat_time INTEGER NOT NULL DEFAULT 1800,
    project_request_status BOOLEAN NOT NULL DEFAULT TRUE,
    last_check_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    url TEXT NOT NULL,
    post_request BOOLEAN DEFAULT FALSE,
    request_body TEXT DEFAULT NULL,
    search_in_answer TEXT DEFAULT NULL,
    request_status_activate BOOLEAN NOT NULL DEFAULT TRUE,
    request_status BOOLEAN NOT NULL DEFAULT TRUE,
    last_request_answer TEXT NOT NULL,
    project_id INTEGER,
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
);
