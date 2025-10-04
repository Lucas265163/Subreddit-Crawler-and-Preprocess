import unittest
from src.scraper import Scraper

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = Scraper(subreddit='laptop', start_date='2022-01-01', end_date='2024-12-31')

    def test_fetch_comments(self):
        comments = self.scraper.fetch_comments()
        self.assertIsInstance(comments, list)
        self.assertGreater(len(comments), 0)

    def test_process_comments(self):
        raw_comments = [{'body': 'This is a test comment!', 'created_utc': 1620000000}]
        processed_comments = self.scraper.process_comments(raw_comments)
        self.assertIsInstance(processed_comments, list)
        self.assertEqual(len(processed_comments), 1)
        self.assertIn('cleaned_body', processed_comments[0])

    def test_date_range(self):
        comments = self.scraper.fetch_comments()
        for comment in comments:
            self.assertGreaterEqual(comment['created_utc'], 1640995200)  # 2022-01-01
            self.assertLessEqual(comment['created_utc'], 1704067200)    # 2024-12-31

if __name__ == '__main__':
    unittest.main()