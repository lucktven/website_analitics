import unittest
import os
import csv
import tempfile
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.analyzer import WebsiteAnalyzer


class TestWebsiteAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = WebsiteAnalyzer()
        self.temp_dir = tempfile.mkdtemp()

    def create_test_csv(self, filename, rows):
        filepath = os.path.join(self.temp_dir, filename)
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['user_id', 'product_id', 'timestamp'])
            for row in rows:
                writer.writerow(row)
        return filepath

    def test_basic_functionality(self):
        day1_file = self.create_test_csv('day1.csv', [
            ['A', '1', '1678886400'],
            ['A', '2', '1678886401'],
            ['A', '3', '1678886402'],
            ['B', '1', '1678886403'],
        ])

        day2_file = self.create_test_csv('day2.csv', [
            ['A', '2', '1678972800'],
            ['A', '4', '1678972801'],
            ['A', '5', '1678972802'],
            ['B', '1', '1678972803'],
        ])

        result = self.analyzer.analyze(day1_file, day2_file)
        self.assertEqual(result, {'A'})

    def test_large_number_of_products(self):
        """Test"""
        day1_rows = [['A', str(i), f'167888640{i}'] for i in range(1000)]
        day2_rows = [
            ['A', '999', '1678972800'],  # old product
            ['A', '1001', '1678972801'],  # new product
            ['B', '1', '1678972802'],  # another customer
        ]

        day1_file = self.create_test_csv('day1.csv', day1_rows)
        day2_file = self.create_test_csv('day2.csv', day2_rows)

        result = self.analyzer.analyze(day1_file, day2_file)
        self.assertEqual(result, {'A'})  # have to find customer A

    def test_no_new_products(self):
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
        day1_file = self.create_test_csv('day1.csv', [
            ['A', '1', '1678886400'],
        ])

        day2_file = self.create_test_csv('day2.csv', [
            ['B', '1', '1678972800'],
            ['A', '2', '1678972801'],
        ])

        result = self.analyzer.analyze(day1_file, day2_file)
        self.assertEqual(result, {'A'})

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)


if __name__ == '__main__':
    unittest.main()