import unittest
from web import app

class CheckResponse(unittest.TestCase):
    def __init__(self):
        self.app = app.test_client()
    """def tearDown(self):
        pass"""
    def test_page(self):
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    """def test_num_docs(self):
        pass"""

if __name__ == '__main__':
    unittest.main()