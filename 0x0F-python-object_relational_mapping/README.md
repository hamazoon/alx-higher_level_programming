# 0x0F. Python - Object-Relational Mapping (ORM)

This project introduces the concept of **Object-Relational Mapping (ORM)**, a programming paradigm for interacting with databases using Python objects. The project explores how to connect Python scripts to a MySQL database using `MySQLdb` and `SQLAlchemy`, demonstrating how ORM abstracts direct SQL queries into Pythonic operations.

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

**Object-Relational Mapping (ORM)** allows developers to interact with databases in a high-level, Pythonic way by representing tables as classes and rows as instances. This project focuses on:
- Writing SQL queries directly in Python using `MySQLdb`.
- Leveraging `SQLAlchemy` to simplify database interactions.
- Transitioning between raw SQL queries and ORM methodologies.

---

## Learning Objectives

By the end of this project, you will be able to:
- Connect to a MySQL database using Python.
- Execute raw SQL queries using `MySQLdb`.
- Use `SQLAlchemy` to interact with databases through ORM.
- Create, read, update, and delete records using ORM techniques.
- Understand the advantages and trade-offs of ORM compared to raw SQL.

---

## Project Structure

This directory contains Python scripts for each task. Scripts demonstrate different aspects of ORM and SQL integration.

### Files

- **`0-select_states.py`**: Lists all `states` from a MySQL database.
- **`1-filter_states.py`**: Filters and lists states starting with 'N'.
- **`2-my_filter_states.py`**: Accepts user input to filter states.
- **`3-my_safe_filter_states.py`**: Prevents SQL injection in user input.
- **`4-cities_by_state.py`**: Lists cities by state.
- **`5-filter_cities.py`**: Filters cities by state.
- **`model_state.py`**: Defines a `State` class for use with `SQLAlchemy`.
- **`7-model_state_fetch_all.py`**: Lists all `State` objects using `SQLAlchemy`.
- **`8-model_state_fetch_first.py`**: Fetches the first `State` object using `SQLAlchemy`.
- **`9-model_state_filter_a.py`**: Lists `State` objects containing the letter 'a'.
- **`10-model_state_my_get.py`**: Prints the `State` object with a specified name.
- **`11-model_state_insert.py`**: Adds a new `State` object.
- **`12-model_state_update_id_2.py`**: Updates a `State` object.
- **`13-model_state_delete_a.py`**: Deletes all `State` objects containing the letter 'a'.
- **`model_city.py`**: Defines a `City` class for use with `SQLAlchemy`.
- **`14-model_city_fetch_by_state.py`**: Lists all cities and their states using `SQLAlchemy`.

---

## Tasks

### Connecting with MySQLdb
1. Write scripts to connect to a database and execute basic queries using raw SQL.

### Transitioning to SQLAlchemy
2. Define ORM classes to represent tables.
3. Perform CRUD operations using `SQLAlchemy`.

### Advanced Operations
4. Combine `State` and `City` models to explore relationships between tables.
5. Demonstrate the use of relationships in `SQLAlchemy`.

---

## Usage

1. **Set Up MySQL Database**  
   Ensure you have a MySQL database server running and populated with the required schema. Example database initialization files are provided in the tasks.

2. **Install Dependencies**  
   Install the required Python packages:
   ```bash
   pip install MySQLdb SQLAlchemy

