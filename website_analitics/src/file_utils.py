import os
import csv


def create_sample_files() -> None:
    """
    Create sample CSV files for demonstration purposes.
    """
    if not os.path.exists('day1.csv'):
        print("Creating day1.csv for demonstration...")
        with open('day1.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['user_id', 'product_id', 'timestamp'])
            writer.writerow(['A', '1', '1678886400'])
            writer.writerow(['A', '2', '1678886401'])
            writer.writerow(['B', '1', '1678886402'])
            writer.writerow(['C', '3', '1678886403'])
            writer.writerow(['A', '3', '1678886404'])  # duplicate, will be ignored by set

    if not os.path.exists('day2.csv'):
        print("Creating day2.csv for demonstration...")
        with open('day2.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['user_id', 'product_id', 'timestamp'])
            writer.writerow(['A', '2', '1678972800'])
            writer.writerow(['A', '4', '1678972801'])  # new product for A
            writer.writerow(['A', '5', '1678972802'])  # new product for A
            writer.writerow(['B', '1', '1678972803'])  # not new for B
            writer.writerow(['D', '6', '1678972804'])  # D not active on Day 1
            writer.writerow(['C', '3', '1678972805'])  # not new for C

    print("Sample files created: day1.csv, day2.csv")