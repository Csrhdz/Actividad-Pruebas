import unittest
import requests

class TestUserAPI(unittest.TestCase):
    base_url = 'http://localhost:3000'  # Reemplaza esto con la URL de tu servidor de desarrollo

    def test_get_users(self):
        response = requests.get(f'{self.base_url}/users')
        self.assertEqual(response.status_code, 200)
        users = response.json()
        self.assertGreater(len(users), 0)

    def test_get_user_by_id_existing(self):
        response = requests.get(f'{self.base_url}/users/1')
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_id_non_existing(self):
        response = requests.get(f'{self.base_url}/users/999')
        self.assertEqual(response.status_code, 404)

    def test_create_user(self):
        user_data = {'name': 'Test User', 'email': 'test@example.com'}
        response = requests.post(f'{self.base_url}/users', json=user_data)
        self.assertEqual(response.status_code, 201)
        user_id = response.json().get('id')
        self.assertGreater(user_id, 0)

    def test_create_user_invalid_data(self):
        user_data = {'name': '', 'email': 'invalid_email'}  # Invalid name and email
        response = requests.post(f'{self.base_url}/users', json=user_data)
        self.assertEqual(response.status_code, 400)

    def test_delete_user_existing(self):
        response = requests.delete(f'{self.base_url}/users/1')
        self.assertIn(response.status_code, [200, 404])  # It could be 200 if user exists or 404 if not
        # Add additional checks for count of users after deletion if needed

    def test_update_user_existing(self):
        user_data = {'name': 'Updated Name', 'email': 'updated@example.com'}
        response = requests.put(f'{self.base_url}/users/1', json=user_data)
        self.assertEqual(response.status_code, 200)
        # Add additional checks for verifying the update in the database


if __name__ == '__main__':
    unittest.main()
