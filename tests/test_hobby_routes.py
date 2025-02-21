import unittest
from app import create_app

class HobbyRoutesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_get_hobbies(self):
        response = self.client.get('/hobbies')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Reading', response.data)
        self.assertIn(b'Swimming', response.data)

if __name__ == '__main__':
    unittest.main()