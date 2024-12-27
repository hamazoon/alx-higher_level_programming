# 0x0C. Python - Almost a Circle

This directory is part of the ALX Software Engineering curriculum, focusing on building a larger Python project while reinforcing fundamental concepts like object-oriented programming, file handling, testing, and serialization. The project emulates a basic geometry-based management system with classes such as `Rectangle`, `Square`, and `Base`.

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

The **"Almost a Circle"** project consolidates concepts covered in previous Python projects:
- Object-Oriented Programming (OOP).
- Unit testing with the `unittest` module.
- Serialization and deserialization using JSON.
- File I/O for saving and loading data.
- Error handling and validation.

This project provides a foundational structure for more complex projects, including projects where classes represent real-world entities.

---

## Learning Objectives

By completing this project, you will:
- Master the design and implementation of OOP in Python.
- Understand and implement class hierarchies and inheritance.
- Use JSON for serialization and deserialization.
- Perform robust unit testing with Python's `unittest`.
- Gain experience handling files for saving and loading data.

---

## Project Structure

The directory contains the following components:

### Main Classes
- **`base.py`**  
  A base class to manage `id` attributes and shared functionality for all derived classes.
- **`rectangle.py`**  
  Defines a `Rectangle` class that inherits from `Base`. Includes attributes like width, height, x, and y.
- **`square.py`**  
  Defines a `Square` class that inherits from `Rectangle`. Focuses on a square's unique properties.

### Unit Tests
Located in the `tests/` directory:
- **`test_base.py`**: Tests for the `Base` class.
- **`test_rectangle.py`**: Tests for the `Rectangle` class.
- **`test_square.py`**: Tests for the `Square` class.

---

## Tasks

### Key Tasks

1. **The Base Class**  
   Implement the `Base` class to handle unique IDs and serve as the base for other classes.

2. **The Rectangle Class**  
   Extend `Base` to create a `Rectangle` class, managing attributes like `width`, `height`, `x`, and `y`.

3. **The Square Class**  
   Extend `Rectangle` to create a `Square` class, focusing on a square's single dimension.

4. **JSON Serialization**  
   Implement methods to serialize objects into JSON strings and deserialize them back.

5. **File Storage**  
   Add functionality to save and load objects to/from JSON files.

6. **Unit Testing**  
   Write robust unit tests for all classes to ensure correctness and edge case handling.

### Advanced Features
- Create objects using class methods.
- Implement dictionary-based representations of objects for easier serialization.
- Handle input validation with informative error messages.

---

## Usage

### Running the Program
Run Python scripts using:
```bash
python3 <script_name>.py

