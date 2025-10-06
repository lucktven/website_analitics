import csv
from typing import Set, Dict
import os


class WebsiteAnalyzer:

    def __init__(self):
        self.user_products_day1: Dict[str, Set[str]] = {}
        self.eligible_users: Set[str] = set()

    def validate_file_exists(self, filepath: str) -> bool:

        if not os.path.exists(filepath):
            print(f"Error: File {filepath} not found.")
            return False
        return True

    def load_day1_data(self, filepath: str) -> bool:

        print(f"Loading Day 1 data from {filepath}...")

        if not self.validate_file_exists(filepath):
            return False

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader, None)

                for i, row in enumerate(reader):
                    if len(row) < 2:
                        print(f"Warning: Skipped row {i + 2} in {filepath} - insufficient columns: {row}")
                        continue

                    user_id, product_id = row[0], row[1]
                    if user_id not in self.user_products_day1:
                        self.user_products_day1[user_id] = set()
                    self.user_products_day1[user_id].add(product_id)

            print(f"Loaded Day 1 data for {len(self.user_products_day1)} unique users.")
            return True

        except Exception as e:
            print(f"Error reading file {filepath}: {e}")
            return False

    def analyze_day2_data(self, filepath: str) -> bool:

        print(f"Loading Day 2 data from {filepath} and analyzing...")

        if not self.validate_file_exists(filepath):
            return False

        try:
            user_products_day2_temp: Dict[str, Set[str]] = {}

            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader, None)

                for i, row in enumerate(reader):
                    if len(row) < 2:
                        print(f"Warning: Skipped row {i + 2} in {filepath} - insufficient columns: {row}")
                        continue

                    user_id, product_id = row[0], row[1]

                    # Only process users who were active on Day 1
                    if user_id in self.user_products_day1:
                        if user_id not in user_products_day2_temp:
                            user_products_day2_temp[user_id] = set()
                        user_products_day2_temp[user_id].add(product_id)

            print(f"Filtered Day 2 data for {len(user_products_day2_temp)} potentially eligible users.")

            # Check criteria for each user
            for user_id, products_day2 in user_products_day2_temp.items():
                products_day1 = self.user_products_day1[user_id]
                new_products_on_day2 = products_day2 - products_day1

                if new_products_on_day2:
                    self.eligible_users.add(user_id)

            print(f"Found {len(self.eligible_users)} eligible users.")
            return True

        except Exception as e:
            print(f"Error reading file {filepath}: {e}")
            return False

    def get_eligible_users(self) -> Set[str]:

        return self.eligible_users

    def analyze(self, day1_file: str, day2_file: str) -> Set[str]:

        self.user_products_day1.clear()
        self.eligible_users.clear()

        if not self.load_day1_data(day1_file):
            return set()

        if not self.analyze_day2_data(day2_file):
            return set()

        return self.eligible_users