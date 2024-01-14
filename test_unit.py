import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()


    def test_add_item_route(self):
        response = self.app.post('/add', data={'item': 'Test Item'})
        self.assertEqual(response.status_code, 302)  
    def test_delete_item(self):

        self.app.post('/add', data={'item': 'Test Item'}, follow_redirects=True)
        delete_response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(delete_response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
