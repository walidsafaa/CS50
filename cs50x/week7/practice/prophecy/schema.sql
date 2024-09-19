CREATE TABLE students (
    id INTEGER,
    student_name TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE students_houses (
    student_id INTEGER,
    house_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id)
    FOREIGN KEY(house_id) REFERENCES houses(id)
);

CREATE TABLE houses (
    id INTEGER,
    house TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE houses_heads (
    head_id INTEGER,
    house_id INTEGER,
    FOREIGN KEY(head_id) REFERENCES heads(id)
    FOREIGN KEY(house_id) REFERENCES houses(id)
);

CREATE TABLE heads (
    id INTEGER,
    head TEXT,
    PRIMARY KEY(id)
);