#!/usr/bin/env python3
"""
Website Analytics Tool
Finds users who visited pages on both days and viewed new products on the second day.
"""

import argparse
import sys
import os

# Add the parent directory to Python path to import from src
sys.path.insert(0, os.path.dirname(__file__))

from src.analyzer import WebsiteAnalyzer
from src.file_utils import create_sample_files


def main():
    """Main function to run the website analytics tool."""
    parser = argparse.ArgumentParser(
        description="Website visit analyzer to find users who discovered new products."
    )
    parser.add_argument(
        "day1_file",
        nargs='?',
        help="Path to CSV file with Day 1 data (user_id,product_id,timestamp)"
    )
    parser.add_argument(
        "day2_file",
        nargs='?',
        help="Path to CSV file with Day 2 data (user_id,product_id,timestamp)"
    )
    parser.add_argument(
        "--create-samples",
        action="store_true",
        help="Create sample CSV files for testing"
    )

    args = parser.parse_args()

    # Create sample files if requested
    if args.create_samples:
        create_sample_files()
        return

    # Check if both files are provided
    if not args.day1_file or not args.day2_file:
        parser.print_help()
        print("\nExamples:")
        print("  python main.py --create-samples")
        print("  python main.py day1.csv day2.csv")
        return

    # Analyze the data
    analyzer = WebsiteAnalyzer()
    found_users = analyzer.analyze(args.day1_file, args.day2_file)

    # Display results
    if found_users:
        print("\nUser IDs that match the criteria:")
        for user_id in sorted(found_users):
            print(user_id)
    else:
        print("\nNo users found that match the criteria.")


if __name__ == "__main__":
    main()