CREATE TABLE employees (
    login TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    second_name TEXT NOT NULL,
    email TEXT,
    manager_login TEXT
);

CREATE TABLE sprints (
    sprint_id SERIAL,
    name TEXT NOT NULL UNIQUE,
    start_datetime TIMESTAMP NOT NULL,
    finish_datetime TIMESTAMP NOT NULL
);

CREATE TABLE issues (
    issue_id SERIAL UNIQUE,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    sprint_id INT,
    owner_login TEXT,
    employee_login TEXT,
    change_time TIMESTAMP,
    status TEXT
);

CREATE TABLE records (
    record_id SERIAL UNIQUE,
    content TEXT NOT NULL,
    sprint_name DATE NOT NULL
);