# 0x07. Python - Test-Driven Development

This directory focuses on the principles of Test-Driven Development (TDD) in Python, emphasizing the importance of writing tests before implementing code. By using the `doctest` and `unittest` modules, these projects help you create more reliable, maintainable, and predictable Python programs.

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

Test-Driven Development (TDD) is a software development approach where tests are written before the code is implemented. The process ensures that:
- Code functionality meets specifications.
- Bugs are caught early during development.
- Refactoring becomes safer and more efficient.

This project explores:
- Writing and running test cases using `doctest` and `unittest`.
- Structuring Python programs to integrate testing.
- Documenting code for clarity and maintainability.

---

## Learning Objectives

By completing these tasks, you will:
- Understand the principles and workflow of TDD.
- Write `doctest` cases embedded in docstrings.
- Use the `unittest` module for comprehensive test cases.
- Test edge cases and handle errors gracefully in your code.
- Gain confidence in the correctness of your implementations.

---

## Project Structure

This directory includes the following files:

- **`0-add_integer.py`**: Adds two integers, with test cases in `0-add_integer.txt`.
- **`2-matrix_divided.py`**: Divides all elements of a matrix, with test cases in `2-matrix_divided.txt`.
- **`3-say_my_name.py`**: Prints a formatted string, with test cases in `3-say_my_name.txt`.
- **`4-print_square.py`**: Prints a square with the `#` character, with test cases in `4-print_square.txt`.
- **`5-text_indentation.py`**: Adds new lines after specific punctuation marks, with test cases in `5-text_indentation.txt`.
- **`tests/`**: Contains unit test files for each module.

---

## Tasks

1. **Integer addition**  
   Write a function that adds two integers. Ensure the inputs are validated and write corresponding test cases using `doctest`.

2. **Matrix division**  
   Implement a function that divides all elements of a matrix by a given number. Validate the inputs and write test cases.

3. **Say my name**  
   Create a function that prints a formatted name. Write tests to handle different input scenarios.

4. **Print a square**  
   Write a function that prints a square using the `#` character, and validate edge cases with test cases.

5. **Text indentation**  
   Implement a function that formats a string by adding new lines after `.`, `?`, and `:`. Write tests to cover different scenarios.

6. **Advanced tasks** (optional)  
   Solve additional challenges to deepen your understanding of TDD.

---

## Usage

### Running Scripts
Execute Python scripts using:
```bash
python3 <script_name>.py

