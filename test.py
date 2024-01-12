import unittest
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_item(self):
        response = self.app.post('/add', data={'item': 'test item'}, follow_redirects=True)
        self.assertIn(b'test item', response.data)

if __name__ == '__main__':
    unittest.main()
