# freeCodeCamp Python Certification 🎓🐍

Welcome to my repository documenting my coursework, workshop exercises, core topic notes, and completed certification projects for the **freeCodeCamp Python Certification** (Scientific Computing with Python).

This repository contains:
- 🛠️ **Hands-on Workshops (W1–W7)** building fundamental to intermediate Python applications.
- 📚 **Comprehensive Topic Modules** covering Data Structures, Algorithms, Object-Oriented Programming, Recursion, and Dynamic Programming.
- 📖 **Complete Python Reviewer Guide** (`reviewer.md`) detailing Python theory, syntax, and time/space complexity analysis.
- 🏆 **All 5 Required Certification Projects** meeting all specification criteria and unit tests.

---

## 📑 Table of Contents

- [Repository Overview](#repository-overview)
- [Workshops (W1 – W7)](#workshops-w1--w7)
- [Core Topic Modules](#core-topic-modules)
- [Certification Projects](#certification-projects)
  - [1. User Configuration](#1-user-configuration)
  - [2. Budget App](#2-budget-app)
  - [3. Polygon Area Calculator](#3-polygon-area-calculator)
  - [4. Tower of Hanoi Algorithm](#4-tower-of-hanoi-algorithm)
  - [5. Hash Table Implementation](#5-hash-table-implementation)
- [Directory Structure](#directory-structure)
- [Getting Started & How to Run](#getting-started--how-to-run)
- [Technologies & Concepts Mastered](#technologies--concepts-mastered)

---

## 📌 Repository Overview

This repository acts as an end-to-end learning archive and reference manual for Python programming and computer science foundations. The structure is separated into hands-on workshops, topic-based learning modules, detailed study notes, and the mandatory certification capstone projects.

---

## 🛠️ Workshops (W1 – W7)

Located in [`TOPICS/PYTHON_BASICS/`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/TOPICS/PYTHON_BASICS/), each workshop represents a practical code challenge focusing on core language concepts:

| Workshop | File | Focus Areas & Concepts |
| :--- | :--- | :--- |
| **W1** | [`report_card_printerW1.py`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/TOPICS/PYTHON_BASICS/report_card_printerW1.py) | **Variables & Data Types**: Dynamic typing, declaring variables, primitive types (`int`, `float`, `str`, `bool`), type inspection with `type()`, and type checking with `isinstance()`. |
| **W2** | [`employee_profile_generatorW2.py`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/TOPICS/PYTHON_BASICS/employee_profile_generatorW2.py) | **String Formatting & Slicing**: String concatenation, augmented assignment (`+=`), string interpolation with f-strings, and index slicing (`[start:stop:step]`, negative indexing). |
| **W3** | [`employee_profile_validatorW3.py`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/TOPICS/PYTHON_BASICS/employee_profile_validatorW3.py) | **String Methods & Parsing**: Cleaning inputs with `.strip()`, `.title()`, `.lower()`, `.upper()`, locating substrings with `.find()`, substring replacement with `.replace()`, `.split()` and `.join()`, prefix/suffix validation with `.startswith()` / `.endswith()`, and occurrence counting with `.count()`. |
| **W4** | [`bill_splitterW4.py`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/TOPICS/PYTHON_BASICS/bill_splitterW4.py) | **Numeric Operations & Precision**: Arithmetic operators, tip computation, running balances with augmented assignments, division, and rounding currency amounts with `round()`. |
| **W5** | [`ticket_booking_calculatorW5.py`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/TOPICS/PYTHON_BASICS/ticket_booking_calculatorW5.py) | **Control Flow & Boolean Logic**: Conditional statements (`if`, `elif`, `else`), logical operators (`and`, `or`), operator precedence, boolean short-circuit evaluation, tiered discount rules, and dynamic service charges. |
| **W6** | [`kitchen_inventory_trackerW6.py`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/TOPICS/PYTHON_BASICS/kitchen_inventory_trackerW6.py) | **Collections & Inventory State**: Managing collections of inventory items, list operations, element tracking, and mutable data structure updates. |
| **W7** | [`caesar_cipherW7.py`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/TOPICS/PYTHON_BASICS/caesar_cipherW7.py) | **Functions & Cryptographic Transformations**: Reusable functions, parameter validation (`isinstance`), rotational string shifting, ASCII mapping using `str.maketrans()`, and cipher substitution via `.translate()`. |

---

## 📚 Core Topic Modules

The [`TOPICS/`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/TOPICS/) directory organizes deep-dive study areas:

- **`PYTHON_BASICS`**: Fundamentals of the language, REPL, variable declarations, built-in functions, primitive data types, and scoping rules (local vs. global).
- **`LOOPS_AND_SEQUENCES`**: Iteration constructs (`for`, `while`), loop control (`break`, `continue`, loop `else`), `range()`, `enumerate()`, `zip()`, list comprehensions, functional built-ins (`filter()`, `map()`, `sum()`), and `lambda` expressions.
- **`DICTIONARIES_AND_SETS`**: Key-value data mapping, view objects (`keys()`, `values()`, `items()`), default retrievals with `.get()`, set theory and operations (union `|`, intersection `&`, difference `-`, symmetric difference `^`, subset/superset validations).
- **`ERROR_HANDLINGS`**: Robust exception management using `try...except...else...finally`, exception objects, manual exceptions with `raise`, custom exception classes, and chained exceptions using `from`.
- **`CLASSES_AND_OBJECTS`**: Object-oriented programming building blocks, class declarations, instance vs. class attributes, instance methods, and Python dunder (magic) methods (`__init__`, `__len__`, `__str__`, `__eq__`, `__getitem__`, `__iter__`).
- **`OOP`**: The 4 pillars of OOP — **Encapsulation** (private attributes, name mangling), **Getters & Setters** via `@property` and `@<attr>.setter`, **Inheritance** (single and multiple inheritance, `super()`), **Polymorphism**, and **Abstraction** via `abc.ABC` and `@abstractmethod`.
- **`LINEAR_DATA_STRUCTURE`**: Memory layout, dynamic arrays (Python lists), Stacks (LIFO behavior), Queues (FIFO behavior using `collections.deque`), Singly Linked Lists, and Doubly Linked Lists.
- **`ALGORITHMS`**: Big O notation (time and space complexity), searching algorithms (Linear Search $O(n)$, Binary Search $O(\log n)$), and divide-and-conquer sorting (Merge Sort $O(n \log n)$).
- **`RECURSIONS`**: Base cases, recursive cases, call stack mechanics, and divide-and-conquer problem-solving patterns.
- **`DYNAMIC_PROGRAMMING`**: Overlapping subproblems, optimal substructure, Top-Down Memoization, Bottom-Up Tabulation, and optimization problems.
- **`GRAPH_AND_TREES`**: Graph representations (Adjacency List, Adjacency Matrix), graph traversals (Breadth-First Search [BFS], Depth-First Search [DFS]), Trees, Binary Trees, Binary Search Trees (BST), Prefix Trees (Tries), and Min/Max Heaps / Priority Queues using the Python `heapq` module.
- **`PYTHON_REVIEWER`**: Holds [`reviewer.md`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/TOPICS/PYTHON_REVIEWER/reviewer.md), an exhaustive 2,100+ line reference covering the entire certification curriculum.

---

## 🏆 Certification Projects

All 5 certification projects required to earn the **freeCodeCamp Python Certification** are located in [`CERTIFICATION_PROJECT/`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/CERTIFICATION_PROJECT/). Each project is implemented to satisfy all required criteria and edge cases.

### 1. User Configuration
📁 [`CERTIFICATION_PROJECT/UserConfiguration/main.py`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/CERTIFICATION_PROJECT/UserConfiguration/main.py)

A configuration management utility to manage key-value settings for application users with case-insensitive handling:
- **`add_setting(settings, setting)`**: Adds a new configuration setting `(key, value)` tuple. Validates that duplicate keys are rejected with a descriptive message.
- **`update_setting(settings, setting)`**: Updates existing configuration settings. Rejects updates to non-existent keys.
- **`delete_setting(settings, key)`**: Removes specified keys from the dictionary safely.
- **`view_settings(settings)`**: Formats and prints all currently configured settings with capitalized keys, or returns `"No settings available."` if empty.

---

### 2. Budget App
📁 [`CERTIFICATION_PROJECT/BudgetApp/main.py`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/CERTIFICATION_PROJECT/BudgetApp/main.py)

An object-oriented ledger and financial budgeting application:
- **`Category` Class**:
  - `deposit(amount, description)`: Records an incoming transaction to the ledger.
  - `withdraw(amount, description)`: Deducts funds if sufficient balance is available.
  - `get_balance()`: Computes net balance from transactions.
  - `transfer(amount, category)`: Transfers funds between distinct `Category` objects.
  - `check_funds(amount)`: Safeguards against overdrawing funds.
  - `__str__()`: Formats an ASCII receipt showing a 30-character centered title (`*` filled), truncated descriptions (up to 23 chars), 2-decimal amounts, and the total balance.
- **`create_spend_chart(categories)`**:
  - Calculates percentage spent per category relative to total withdrawals (rounded down to nearest 10%).
  - Renders a vertical ASCII bar chart from 100% to 0% with `o` markers and vertically aligned category names underneath.

---

### 3. Polygon Area Calculator
📁 [`CERTIFICATION_PROJECT/PolygonAreaCalculator/main.py`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/CERTIFICATION_PROJECT/PolygonAreaCalculator/main.py)

An Object-Oriented geometry calculation suite demonstrating inheritance:
- **`Rectangle` Class**:
  - `set_width(width)` & `set_height(height)`: Mutators for dimensions.
  - `get_area()`: Calculates $width \times height$.
  - `get_perimeter()`: Computes $2 \times width + 2 \times height$.
  - `get_diagonal()`: Calculates Euclidean diagonal: $\sqrt{width^2 + height^2}$.
  - `get_picture()`: Draws the shape using lines of `*`. Returns `"Too big for picture."` if dimensions exceed 50 units.
  - `get_amount_inside(shape)`: Determines how many smaller shape instances can fit inside without rotation.
  - `__str__()`: Formats as `Rectangle(width=w, height=h)`.
- **`Square` Subclass (inherits from `Rectangle`)**:
  - Instantiated with a single `side` dimension.
  - Overrides `set_side()`, `set_width()`, and `set_height()` to keep both dimensions equal.
  - Formats as `Square(side=s)`.

---

### 4. Tower of Hanoi Algorithm
📁 [`CERTIFICATION_PROJECT/TowerofHanoiAlgorithm/main.py`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/CERTIFICATION_PROJECT/TowerofHanoiAlgorithm/main.py)

A recursive mathematical puzzle solver for the classical Tower of Hanoi problem:
- **`hanoi_solver(n)`**:
  - Solves transferring $n$ disks from the source peg (`rod1`) to the destination peg (`rod3`) using an auxiliary peg (`rod2`).
  - Follows recursive divide-and-conquer rules:
    1. Move $n-1$ disks from source to auxiliary.
    2. Move the remaining largest disk to target.
    3. Move $n-1$ disks from auxiliary to target.
  - Records the exact state of all three rods (`rod1 rod2 rod3`) before the first move and after every single disk transfer.
  - Returns the complete history of states as a newline-delimited string.

---

### 5. Hash Table Implementation
📁 [`CERTIFICATION_PROJECT/HashTable/main.py`](file:///C:/Users/Acer/Desktop/freeCodeCampCertification/CERTIFICATION_PROJECT/HashTable/main.py)

A custom implementation of the Hash Table data structure from scratch:
- **`HashTable` Class**:
  - `hash(string)`: Custom hash function computing the sum of ASCII values of all characters in the key string.
  - `add(key, value)`: Computes hash bucket index and inserts or updates key-value pairs (handling collisions via dictionary bucketing).
  - `lookup(key)`: Retrieves the value associated with a key in average $O(1)$ time, or returns `None` if absent.
  - `remove(key)`: Deletes the key-value pair and cleans up empty buckets to preserve memory.

---

## 📂 Directory Structure

```text
freeCodeCampCertification/
├── .gitignore
├── Readme.md
├── CERTIFICATION_PROJECT/
│   ├── BudgetApp/
│   │   └── main.py
│   ├── HashTable/
│   │   └── main.py
│   ├── PolygonAreaCalculator/
│   │   └── main.py
│   ├── TowerofHanoiAlgorithm/
│   │   └── main.py
│   └── UserConfiguration/
│       └── main.py
└── TOPICS/
    ├── ALGORITHMS/
    ├── CLASSES_AND_OBJECTS/
    ├── DICTIONARIES_AND_SETS/
    ├── DYNAMIC_PROGRAMMING/
    ├── ERROR_HANDLINGS/
    ├── GRAPH_AND_TREES/
    ├── LINEAR_DATA_STRUCTURE/
    ├── LOOPS_AND_SEQUENCES/
    ├── OOP/
    ├── PYTHON_BASICS/
    │   ├── bill_splitterW4.py
    │   ├── caesar_cipherW7.py
    │   ├── employee_profile_generatorW2.py
    │   ├── employee_profile_validatorW3.py
    │   ├── kitchen_inventory_trackerW6.py
    │   ├── report_card_printerW1.py
    │   └── ticket_booking_calculatorW5.py
    ├── PYTHON_REVIEWER/
    │   └── reviewer.md
    └── RECURSIONS/
```

---

## 🚀 Getting Started & How to Run

### Prerequisites
- Python 3.8 or later installed on your system.
- Check your installation:
  ```bash
  python --version
  ```

### Running Workshops
Navigate to the repository and run any workshop script directly using Python:
```bash
# Example: Run Workshop 7 (Caesar Cipher)
python TOPICS/PYTHON_BASICS/caesar_cipherW7.py

# Example: Run Workshop 4 (Bill Splitter)
python TOPICS/PYTHON_BASICS/bill_splitterW4.py
```

### Running Certification Projects
Each certification project has a standalone `main.py` ready for execution and verification:
```bash
# 1. User Configuration
python CERTIFICATION_PROJECT/UserConfiguration/main.py

# 2. Budget App
python CERTIFICATION_PROJECT/BudgetApp/main.py

# 3. Polygon Area Calculator
python CERTIFICATION_PROJECT/PolygonAreaCalculator/main.py

# 4. Tower of Hanoi Algorithm
python CERTIFICATION_PROJECT/TowerofHanoiAlgorithm/main.py

# 5. Hash Table
python CERTIFICATION_PROJECT/HashTable/main.py
```

---

## 🧠 Technologies & Concepts Mastered

- **Language Core**: Python 3, dynamic typing, scopes, memory references, immutable vs. mutable types.
- **Control Flow**: Conditional expressions, nested branching, boolean logic, `for` and `while` loops, iterators, generators.
- **Data Structures**: Lists, Tuples, Dictionaries, Sets, Stacks, Queues (`deque`), Singly/Doubly Linked Lists, Hash Tables, Trees, Binary Search Trees, Tries, Heaps (`heapq`), Priority Queues.
- **Algorithms**: Big O Complexity (Time & Space), Linear Search, Binary Search, Merge Sort, Recursion, Breadth-First Search (BFS), Depth-First Search (DFS).
- **Optimization**: Dynamic Programming (Top-Down Memoization, Bottom-Up Tabulation), Divide-and-Conquer.
- **Software Design**: Object-Oriented Programming (OOP), Encapsulation, Inheritance, Polymorphism, Abstraction, Dunder methods, Custom Exceptions.
