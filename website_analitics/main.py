#!/usr/bin/env python3
import argparse
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.analyzer import WebsiteAnalyzer
from src.file_utils import create_sample_files


def main():
    parser = argparse.ArgumentParser(description="Optimized website visit analyzer")
    parser.add_argument("day1_file", nargs='?', help="Path to Day 1 CSV file")
    parser.add_argument("day2_file", nargs='?', help="Path to Day 2 CSV file")
    parser.add_argument("--create-samples", action="store_true", help="Create sample CSV files")
    args = parser.parse_args()

    if args.create_samples:
        create_sample_files()
        return

    if not args.day1_file or not args.day2_file:
        parser.print_help()
        print("\nExamples:")
        print("  python main.py --create-samples")
        print("  python main.py day1.csv day2.csv")
        return

    analyzer = WebsiteAnalyzer()
    users = analyzer.analyze(args.day1_file, args.day2_file)

    if users:
        print(f"\n👥 Found {len(users)} eligible users:")
        for uid in sorted(users):
            print(f"  - {uid}")
    else:
        print("\nNo eligible users found.")


if __name__ == "__main__":
    main()