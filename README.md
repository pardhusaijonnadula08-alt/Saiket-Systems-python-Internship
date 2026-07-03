# Python Development Internship - SaiKet Systems

This repository contains the technical tasks and problem-solving scripts developed during my Python Development Internship at SaiKet Systems.

## 📁 Repository Structure

* **Task-1/01_ToDo_List.py**: A command-line To-Do List application. It features complete CRUD operations (Add, Show, Mark Complete, Delete) utilizing Python classes and robust try-except exception handling for user inputs.

  
* ### 🎮 Task 2: Guess the Number Game (`02_Guess The Number Game.py`)
A dynamic command-line mini-game designed to demonstrate control flow manipulation, loop optimization, and random variable evaluation.
* **Core Mechanisms:** Utilizes Python's `random` standard library to generate targets, tracks player attempts via dynamic variables, and implements high/low boundary logic to provide precise contextual feedback.
* **Defensive Design:** Implemented structural error isolation to ensure non-numeric character inputs do not break the operational execution loop.


### 📂 Task 3: Basic File Handling Tool (`03_Basic File Handling.py`)
A backend-focused text-manipulation utility developed to interact safely with external storage systems to search, parse, and overwrite text files dynamically.
* **Context Management:** Built using the standard `with open()` design pattern to guarantee smooth data stream closures and completely prevent file leaks or thread locks.
* **Exception Layering:** Implemented granular fault handling using specific `FileNotFoundError` catch blocks alongside catch-all exceptions to maximize terminal execution stability.
* **Write Optimization:** Integrated checking logic (`if old_word not in content`) to prevent costly disk write operations if the original target pattern is missing.

## 🛠️ Technical Skill Stack Covered
* **Language:** Python 3
* **Concepts:** Object-Oriented Programming (OOP), Data Stream I/O Operations, Encoding Protocols (`utf-8`)
* **Defensive Coding:** Advanced Exception Handling (`try-except` execution loops


