# Task 1: Implementation README

## Implementation Notes

### 1. Python Dict-Like Hashmap
I have implemented a Python dictionary-like hashmap for Task 1.

### 2. Customizable Capacity
You can choose the capacity of the hashmap; however, it will automatically increase if it's filled up to 70% of its capacity. This behavior is similar to Python's defaultdict.

### 3. Memory Optimization
To optimize memory usage, I initialize the hashmap with a list of None values. This approach consumes less memory initially compared to a fully populated list. However, this can impact speed because we need to check if an element is filled or not, which doubles the time required to put elements.

### 4. Efficiency
Python lists have O(1) time complexity for most operations, making our hashmap efficient.

## Usage

To use this implementation, follow these steps:

1. Make sure you have Python 3.10 installed on your system.

2. Create a virtual environment (venv) for this project:
   ```bash
   python3.10 -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the tests for Task 1 located in the "task1" folder:
   ```bash
   python task1/test_task1.py
   ```

# Task 2: Implementation README

## Implementation Notes

### 1. Testing with Unittest
For Task 2, I have chosen to use the `unittest` library for testing.

### 2. In-Memory Database
I've opted for an in-memory database for testing purposes, as it's faster and more suitable for testing scenarios.

## Usage

To use this implementation, follow these steps:

1. Make sure you have Python 3.10 installed on your system.

2. Create a virtual environment (venv) for this project:
   ```bash
   python3.10 -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the tests for Task 2 located in the "task2" folder:
   ```bash
   python task2/test_task2.py
   ```

These steps will help you set up and test the implementations for both Task 1 and Task 2.