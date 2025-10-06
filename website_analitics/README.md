# Website Analytics Tool

A Python tool for analyzing website visit data to find users who visited pages on both days and discovered new products on the second day.

## Problem Description

Find all users who:
1. Visited product pages on both days
2. On the second day visited at least one page that they hadn't visited on the first day

## Installation

1. Clone the repository:
```
git clone https://github.com/lucktven/website_analitics.git
```
## Usage

### Basic Usage
```
python main.py day1.csv day2.csv
```
### Create Sample Files
```
python main.py --create-samples
```
### Example
```
# Create sample files first
python main.py --create-samples

# Then analyze them
python main.py day1.csv day2.csv
```
### Input Format
CSV files with the following columns:

* `user_id`: Unique identifier for the user

* `product_id`: Unique identifier for the product/page

* `timestamp`: Visit timestamp (not used in analysis)

Example:
```
csv
user_id,product_id,timestamp
A,1,1678886400
A,2,1678886401
B,1,1678886402
```
### Output
The tool outputs to console all user IDs that match the criteria, sorted alphabetically.

## Algorithm Efficiency
### Time Complexity
* O(N + M) where N is the number of records in Day 1 and M is the number of records in Day 2

* Reading both files: O(N + M)

* Set operations: O(1) average case for lookups and additions

### Space Complexity
* O(K + L) where K is the number of unique users in Day 1 and L is the number of unique users present in both days

* Stores only unique product sets for relevant users

### Optimization Strategies
1. Streaming processing: Day 2 data is processed in a single pass

2. Early filtering: Only users present in Day 1 are considered for Day 2 analysis

3. Set operations: Efficient difference operations using Python's built-in sets

4. Minimal storage: Only stores necessary data (user→products mapping)

## Project Structure
```
website_analytics/
├── src/
│   ├── analyzer.py          # Main analysis logic
│   └── file_utils.py        # File handling utilities
├── tests/
│   └── test_analyzer.py     # Unit tests
├── main.py                  # CLI entry point
├── requirements.txt         # Dependencies (none required)
└── README.md               # This file
```
## Running Tests
```
python -m unittest tests/test_analyzer.py
```
## Example Analysis
Given:

* Day 1: User A viewed products [1, 2, 3]

* Day 2: User A viewed products [2, 4, 5]

Result: User A is included because they viewed products 4 and 5 which are new.
