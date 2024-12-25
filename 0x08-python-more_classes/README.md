# 0x08. Python - More Classes and Objects

This directory continues exploring Object-Oriented Programming (OOP) in Python, building upon the foundational concepts covered previously. The tasks introduce advanced features of classes, focusing on practical applications and optimization of OOP principles.

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

Classes and objects are at the heart of OOP, allowing developers to model real-world entities and relationships. This project explores advanced concepts, including:
- Class methods and static methods.
- Special methods for customized behaviors (`__str__`, `__repr__`, etc.).
- Advanced attribute manipulation.
- Application of class-level and instance-level attributes.

---

## Learning Objectives

By completing these tasks, you will:
- Understand and implement class and static methods.
- Leverage special methods for custom string representation.
- Compare objects using comparison operators.
- Understand mutability and immutability of class-level attributes.
- Write reusable, modular, and well-structured code.

---

## Project Structure

This directory includes the following files:

- **`0-rectangle.py`**: Defines an empty `Rectangle` class.
- **`1-rectangle.py`**: Adds width and height attributes with validation.
- **`2-rectangle.py`**: Implements methods to calculate area and perimeter.
- **`3-rectangle.py`**: Adds `__str__` for a string representation of the rectangle.
- **`4-rectangle.py`**: Adds `__repr__` to recreate a rectangle object.
- **`5-rectangle.py`**: Implements a destructor method `__del__` with a custom message.
- **`6-rectangle.py`**: Tracks the number of instances of the `Rectangle` class.
- **`7-rectangle.py`**: Adds a public class attribute for symbol representation.
- **`8-rectangle.py`**: Implements a static method to compare rectangles based on area.
- **`9-rectangle.py`**: Adds a class method to create a square instance.

---

## Tasks

1. **Simple Rectangle**  
   Define an empty class `Rectangle`.

2. **Rectangle with attributes**  
   Add attributes `width` and `height`, with validation.

3. **Area and Perimeter**  
   Implement methods to calculate the area and perimeter.

4. **String Representation**  
   Override the `__str__` method for a visual representation of the rectangle.

5. **Object Representation**  
   Use `__repr__` to recreate the object from its string representation.

6. **Object Destruction**  
   Add a custom message when an instance of the class is deleted.

7. **Instance Counter**  
   Track the number of active instances of the class.

8. **Custom Symbol**  
   Use a class attribute to customize the symbol used for rectangle representation.

9. **Static Method**  
   Compare two rectangles based on their area.

10. **Class Method for Squares**  
    Create a square instance using a class method.

---

## Usage

Run Python scripts using:
```bash
python3 <script_name>.py

