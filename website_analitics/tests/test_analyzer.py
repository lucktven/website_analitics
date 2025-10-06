import unittest
import os
import csv
import tempfile
import sys

# Add the parent directory to Python path to import from src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.analyzer import WebsiteAnalyzer


class TestWebsiteAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = WebsiteAnalyzer()
        self.temp_dir = tempfile.mkdtemp()

    def create_test_csv(self, filename, rows):
        """Helper method to create test CSV files."""
        filepath = os.path.join(self.temp_dir, filename)
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['user_id', 'product_id', 'timestamp'])
            for row in rows:
                writer.writerow(row)
        return filepath

    def test_basic_functionality(self):
        """Test basic functionality with sample data."""
        # Day 1: User A viewed products 1, 2, 3
        day1_file = self.create_test_csv('day1.csv', [
            ['A', '1', '1678886400'],
            ['A', '2', '1678886401'],
            ['A', '3', '1678886402'],
            ['B', '1', '1678886403'],
        ])

        # Day 2: User A viewed products 2 (old), 4 (new), 5 (new)
        day2_file = self.create_test_csv('day2.csv', [
            ['A', '2', '1678972800'],
            ['A', '4', '1678972801'],
            ['A', '5', '1678972802'],
            ['B', '1', '1678972803'],  # B only viewed old products
        ])

        result = self.analyzer.analyze(day1_file, day2_file)

        # Only user A should be in results (viewed new products)
        self.assertEqual(result, {'A'})

    def test_no_new_products(self):
        """Test when no users view new products."""
        day1_file = self.create_test_csv('day1.csv', [
            ['A', '1', '1678886400'],
            ['A', '2', '1678886401'],
        ])

        day2_file = self.create_test_csv('day2.csv', [
            ['A', '1', '1678972800'],
            ['A', '2', '1678972801'],
        ])

        result = self.analyzer.analyze(day1_file, day2_file)
        self.assertEqual(result, set())

    def test_user_not_in_both_days(self):
        """Test when users are only active in one day."""
        day1_file = self.create_test_csv('day1.csv', [
            ['A', '1', '1678886400'],
        ])

        day2_file = self.create_test_csv('day2.csv', [
            ['B', '1', '1678972800'],  # B not in Day 1
            ['A', '2', '1678972801'],  # A views new product
        ])

        result = self.analyzer.analyze(day1_file, day2_file)
        self.assertEqual(result, {'A'})  # Only A should be in results

    def tearDown(self):
        """Clean up temporary files."""
        import shutil
        shutil.rmtree(self.temp_dir)


if __name__ == '__main__':
    unittest.main()