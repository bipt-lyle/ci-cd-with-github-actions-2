import unittest
from app import app

class TestAppIntegration(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_item_addition_and_deletion(self):
        add_response = self.app.post('/add', data={'item': 'Test Item'}, follow_redirects=True)
        self.assertIn('Test Item', str(add_response.data))

        delete_response = self.app.get('/delete/0', follow_redirects=True)
        self.assertNotIn('Test Item', str(delete_response.data))

if __name__ == '__main__':
    unittest.main()
