-- NOTE Running this file will DELETE ALL CONTENT in your database
-- This file will clear out and set up the courses table in a database
-- To use this file run your Shell, then type the commands below
-- sqlite3
-- .read courses.sql

--set up
.mode column
.headers on
.open courses.db

DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS departments;

PRAGMA foreign_keys = ON;

CREATE TABLE departments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  chair TEXT
);


CREATE TABLE courses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  teacher TEXT,
  room TEXT,
  department INTEGER,
  FOREIGN KEY (department)
    REFERENCES departments (id)
);