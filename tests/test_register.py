import json

from test.BaseCase import BaseCase


class TestAuthRegister(BaseCase):
    def test_successful_register(self):
        payload = json.dumps({
            'name': 'Lucas Santos',
            'email': 'lucassantoos56@gmail.com'
        })

        response = self.app.post('/auth/register', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['access_token']))
        self.assertEqual(201, response.status_code)
    
    def test_already_exists_user(self):
        payload = json.dumps({
            'name': 'Admin',
            'email': 'admin@admin.com'
        })

        response = self.app.post('/auth/register', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('User already exists', response.json['msg'])
        self.assertEqual(409, response.status_code)

    def test_payload_empty(self):
        payload = json.dumps({})

        response = self.app.post('/auth/register', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('Registration data was not informed.', response.json['msg'])
        self.assertEqual(400, response.status_code)