# 0x0E. SQL - More Queries

This directory continues the exploration of SQL, focusing on advanced query techniques and database management. The tasks include creating users, managing permissions, and working with relationships between tables using `JOIN` statements.

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

This project builds on the foundational SQL knowledge from the previous project and introduces more complex concepts:
- User and permission management.
- Advanced querying using `JOIN` statements.
- Aggregation with grouping.
- Filtering and sorting query results.
- Understanding relationships between tables.

---

## Learning Objectives

By the end of this project, you will:
- Manage users and set permissions in a database.
- Create and manage relationships between tables using foreign keys.
- Write advanced SQL queries to retrieve and manipulate data.
- Use `JOIN` statements to combine data from multiple tables.
- Apply grouping and aggregation functions like `GROUP BY` and `HAVING`.

---

## Project Structure

The directory contains `.sql` script files, each focusing on a specific concept or task:

### Files
- **`0-privileges.sql`**: Lists all privileges of the current database user.
- **`1-create_user.sql`**: Creates a new database user with specific privileges.
- **`2-create_read_user.sql`**: Creates a user with only read permissions on a database.
- **`3-force_name.sql`**: Ensures that a table column has specific constraints.
- **`4-never_empty.sql`**: Adds a `NOT NULL` constraint to a column.
- **`5-unique_id.sql`**: Ensures a column has unique values.
- **`6-states.sql`**: Creates a `states` table.
- **`7-cities.sql`**: Creates a `cities` table and establishes a relationship with the `states` table.
- **`8-cities_of_california.sql`**: Retrieves all cities in California using a `JOIN`.
- **`9-cities_by_state.sql`**: Lists all cities grouped by state.
- **`10-genre_id_by_show.sql`**: Retrieves genre information for TV shows.
- **`11-genre_id_all_shows.sql`**: Retrieves genre information for all shows.
- **`12-no_genre.sql`**: Finds shows without a genre assigned.
- **`13-count_shows_by_genre.sql`**: Counts the number of shows per genre.
- **`14-my_genres.sql`**: Lists genres a specific user likes.
- **`15-comedy_only.sql`**: Filters for shows that are comedies.
- **`16-shows_by_user.sql`**: Lists all shows watched by a specific user.

---

## Tasks

### User and Permission Management
1. **Privileges**  
   View all privileges of the current user.

2. **Create Users**  
   Create new database users and assign permissions.

### Table Creation and Constraints
3. **Enforce Constraints**  
   Add `NOT NULL` and `UNIQUE` constraints to table columns.

4. **Foreign Keys**  
   Establish relationships between tables using foreign keys.

### Advanced Queries
5. **Joins and Relationships**  
   Use `INNER JOIN`, `LEFT JOIN`, and other join types to retrieve related data from multiple tables.

6. **Grouping and Aggregation**  
   Group results and apply aggregate functions like `COUNT()` and `SUM()`.

7. **Filtering Results**  
   Filter and sort query results using `WHERE`, `ORDER BY`, and `HAVING`.

---

## Usage

### Setting Up
1. Install MySQL and start the server.
2. Create a database to test the scripts:
   ```bash
   mysql -u <username> -p
   CREATE DATABASE test_db;

