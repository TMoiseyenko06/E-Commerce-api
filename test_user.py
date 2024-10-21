import unittest
from unittest.mock import MagicMock, patch
from app import app


class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.mock_db = MagicMock()
        self.mock_db.return_value = True
        patch('services.userServices.check_roles',return_value = True).start()
        patch('utils.util.verify_token',return_value = None)
        patch('app.db',self.mock_db).start()
    
    def tearDown(self):
        patch.stopall()

    def test_add(self):
        payload = {
            "name":"tim",
            "username":"tim06",
            "password":"password",
            "roles":['1']
        }
        response = self.app.post('/user',json=payload)
        print(response.data)
        self.assertEqual(response.status_code,200)

    def test_edit(self):
        payload = {
            "id":"3",
            "name":"tim",
            "username":"tim06",
            "password":"password",
            "roles":['1']
        }
        response = self.app.put('/user',json=payload)
        print(response.data)
        self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    unittest.main()