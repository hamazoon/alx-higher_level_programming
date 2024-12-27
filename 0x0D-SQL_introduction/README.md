# 0x0D. SQL - Introduction

This directory focuses on introducing Structured Query Language (SQL), a standard language for interacting with relational databases. The tasks cover fundamental SQL concepts, including creating tables, inserting data, querying, updating, and deleting records.

---

## Table of Contents

- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Project Structure](#project-structure)
- [Tasks](#tasks)
- [Usage](#usage)
- [Author](#author)

---

## Introduction

SQL (Structured Query Language) is essential for managing and manipulating relational databases. It enables users to perform operations like creating tables, retrieving data, updating records, and managing permissions. This project provides a hands-on approach to learning SQL basics using MySQL.

---

## Learning Objectives

By the end of this project, you will:
- Understand the basics of relational databases.
- Learn how to create and manage tables using SQL.
- Retrieve data using `SELECT` statements with conditions and filters.
- Modify existing data using `UPDATE` and `DELETE`.
- Perform aggregation operations using functions like `COUNT()`, `SUM()`, and `AVG()`.

---

## Project Structure

The directory contains `.sql` script files for each task. Each script performs a specific SQL operation or solves a specific challenge.

### Files
- **`0-list_databases.sql`**: Lists all databases.
- **`1-create_database_if_missing.sql`**: Creates a database if it doesn't already exist.
- **`2-create_table.sql`**: Creates a table with specific columns.
- **`3-insert_data.sql`**: Inserts data into a table.
- **`4-select_data.sql`**: Selects all data from a table.
- **`5-filter_data.sql`**: Selects data based on a condition.
- **`6-update_table.sql`**: Updates data in a table.
- **`7-delete_data.sql`**: Deletes specific records.
- **`8-count_data.sql`**: Counts rows matching a condition.
- **`9-sum_data.sql`**: Calculates the sum of values in a column.
- **`10-avg_data.sql`**: Calculates the average of a column.

---

## Tasks

### Basic Operations
1. **List Databases**  
   Use `SHOW DATABASES;` to list all available databases.

2. **Create a Database**  
   Create a database if it doesn't already exist.

3. **Create a Table**  
   Define a table with specific column types and constraints.

4. **Insert Data**  
   Add rows to the table using `INSERT INTO`.

5. **Retrieve Data**  
   Use `SELECT` to query data from the table.

6. **Filter Data**  
   Apply conditions with `WHERE` to retrieve specific rows.

7. **Update Data**  
   Modify existing data in a table using `UPDATE`.

8. **Delete Data**  
   Remove specific rows from a table using `DELETE`.

### Aggregations
9. **Count Rows**  
   Use `COUNT()` to determine the number of rows that match a condition.

10. **Calculate Totals and Averages**  
    Use `SUM()` and `AVG()` to calculate aggregated values.

---

## Usage

1. **Setup MySQL**  
   Install MySQL on your system and start the server.

2. **Run SQL Scripts**  
   Execute the provided SQL scripts using:
   ```bash
   mysql -u <username> -p < database_name> < script.sql

