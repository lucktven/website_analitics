import csv
import os
from typing import Set, List
from collections import defaultdict


class WebsiteAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def validate_file_exists(filepath: str) -> bool:
        if not os.path.exists(filepath):
            print(f"Error: File {filepath} not found.")
            return False
        return True

    def analyze(self, day1_file: str, day2_file: str) -> Set[str]:
        if not self.validate_file_exists(day1_file) or not self.validate_file_exists(day2_file):
            return set()

        print("Starting analysis...")

        day1_users = set()
        print("Step 1: Collecting Day 1 users...")

        with open(day1_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # skip header

            for row in reader:
                if len(row) >= 2:
                    day1_users.add(row[0])

        print(f"Found {len(day1_users)} unique users in Day 1")

        print("Step 2: Building user products map for Day 1...")
        user_products = defaultdict(set)

        with open(day1_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                if len(row) >= 2 and row[0] in day1_users:
                    user_products[row[0]].add(row[1])

        print("Step 3: Analyzing Day 2 data...")
        eligible_users = set()

        with open(day2_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)

            for i, row in enumerate(reader):
                if len(row) >= 2 and row[0] in user_products:
                    if row[1] not in user_products[row[0]]:
                        eligible_users.add(row[0])

                # Прогрес для дуже великих файлів
                if i > 0 and i % 1_000_000 == 0:
                    print(f"  Processed {i:,} rows from Day 2...")

        print(f"Analysis complete. Found {len(eligible_users)} eligible users.")
        return eligible_users