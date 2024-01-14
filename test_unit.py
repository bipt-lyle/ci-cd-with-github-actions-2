import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_item_route(self):
        response = self.app.post('/add', data={'item': 'Test Item'})
        self.assertEqual(response.status_code, 302)  # Assuming redirection

if __name__ == '__main__':
    unittest.main()
