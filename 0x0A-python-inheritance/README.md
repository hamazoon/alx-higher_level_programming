# 0x0A. Python - Inheritance

This directory focuses on inheritance in Python, a key feature of object-oriented programming (OOP). The tasks explore how classes can inherit attributes and methods from other classes, enabling code reuse and extensibility.

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

Inheritance is a mechanism in OOP that allows one class (child class) to inherit attributes and methods from another class (parent class). It promotes code reuse and supports the creation of hierarchical relationships between classes.

Key topics covered in this project include:
- Creating child classes from parent classes.
- Overriding methods in a child class.
- Using the `super()` function to access methods and attributes of a parent class.
- Identifying the class hierarchy using built-in functions like `isinstance()` and `issubclass()`.

---

## Learning Objectives

By the end of this project, you will:
- Understand the principles of inheritance and its benefits in OOP.
- Know how to create child classes and extend the functionality of parent classes.
- Be able to override parent methods and use `super()` to reference the parent class.
- Recognize when and how to use type-checking functions in Python.

---

## Project Structure

This directory includes the following files:

- **`0-lookup.py`**: Returns the list of available attributes and methods of an object.
- **`1-my_list.py`**: A class that inherits from `list` and includes a method to print the list in sorted order.
- **`2-is_same_class.py`**: Checks if an object is an instance of a specific class.
- **`3-is_kind_of_class.py`**: Checks if an object is an instance of, or inherited from, a specific class.
- **`4-inherits_from.py`**: Checks if an object is an instance of a class that inherited directly or indirectly from a specified class.
- **`5-base_geometry.py`**: An empty class called `BaseGeometry`.
- **`6-base_geometry.py`**: Extends `BaseGeometry` by adding a method for area calculation.
- **`7-base_geometry.py`**: Adds input validation to `BaseGeometry`.
- **`8-rectangle.py`**: Defines a `Rectangle` class that inherits from `BaseGeometry`.
- **`9-rectangle.py`**: Adds an implementation for the `area()` method in the `Rectangle` class.
- **`10-square.py`**: Defines a `Square` class that inherits from `Rectangle`.
- **`11-square.py`**: Adds a string representation for the `Square` class.

---

## Tasks

1. **Lookup**  
   Implement a function to return the list of attributes and methods of an object.

2. **My List**  
   Create a class that inherits from `list` and includes a method to print the list in sorted order.

3. **Same class**  
   Write a function to check if an object is exactly an instance of a specified class.

4. **Kind of class**  
   Write a function to check if an object is an instance of, or inherits from, a specified class.

5. **Only sub class of**  
   Check if an object is an instance of a class that inherits directly or indirectly from a specified class.

6. **Geometry module**  
   Create an empty `BaseGeometry` class.

7. **Improve Geometry**  
   Add a method for area calculation and input validation to `BaseGeometry`.

8. **Rectangle module**  
   Define a `Rectangle` class that inherits from `BaseGeometry` and implements area calculation.

9. **Full rectangle**  
   Extend the `Rectangle` class with additional functionality and representation.

10. **Square module**  
    Define a `Square` class that inherits from `Rectangle` and implements size validation.

11. **String representation**  
    Add a custom string representation for the `Square` class.

---

## Usage

Run Python scripts using:
```bash
python3 <script_name>.py

