# Website Analytics Tool

A Python tool for analyzing website visit data to find users who visited pages on both days and discovered new products on the second day.

## Problem Description

Find all users who:
- Visited product pages on both days
- On the second day visited at least one page that they hadn't visited on the first day

## Installation

Clone the repository:
```
git clone https://github.com/lucktven/website_analytics.git
cd website_analytics
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
- `user_id`: Unique identifier for the user
- `product_id`: Unique identifier for the product/page  
- `timestamp`: Visit timestamp (not used in analysis)

Example:
```
user_id,product_id,timestamp
A,1,1678886400
A,2,1678886401
B,1,1678886402
```

### Output

The tool outputs to console all user IDs that match the criteria, sorted alphabetically.

Example output:
```
Found 2 eligible users:
  - A
  - C
```

## Algorithm Efficiency

### Time Complexity
- **O(N + M)** where N is the number of records in Day 1 and M is the number of records in Day 2
- Three passes over the data: two for Day 1, one for Day 2
- Set operations: O(1) average case for lookups and additions

### Space Complexity
- **O(U × P)** where U is the number of unique users in Day 1 and P is the average number of products per user
- Stores user-to-products mapping only for users present in Day 1

### Optimization Strategies
1. **Efficient Data Structures**: Uses Python sets and defaultdict for optimal performance
2. **Early Filtering**: Processes only users present in both days
3. **Single Pass Processing**: Each file is processed sequentially without random access
4. **Memory-Efficient Design**: Handles large datasets without loading entire files into memory

## Project Structure

```
website_analytics/
├── src/
│   ├── __init__.py
│   ├── analyzer.py          # Main analysis logic
│   └── file_utils.py        # File handling utilities
├── tests/
│   ├── __init__.py
│   └── test_analyzer.py     # Unit tests
├── main.py                  # CLI entry point
└── README.md               # This file
```

## Running Tests

```
python -m unittest tests/test_analyzer.py
```

The test suite includes:
- Basic functionality tests
- Edge cases (no new products, users in one day only)
- Large number of products per user
- File validation tests

## Example Analysis

Given:
- **Day 1**: User A viewed products [1, 2, 3]; User B viewed products [1]
- **Day 2**: User A viewed products [2, 4, 5]; User B viewed products [1]; User C viewed products [6]

**Result**: User A is included because they viewed products 4 and 5 which are new. User C is not included because they didn't visit on Day 1. User B is not included because they only viewed existing products.

Output:
```
Found 1 eligible users:
  - A
```