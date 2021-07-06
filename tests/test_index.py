import unittest

import unittest
from ripper.app import create_app


class TestIndex(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_redirect00(self):
        ''' Minimal test if the index page is available. '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_redirect01(self):
        ''' Minimal test if the index page is available. '''
        response = self.client.get('/static')
        self.assertEqual(response.status_code, 302)

    def test_index(self):
        ''' Minimal test if the index page is available. '''
        response = self.client.get('/static/index.html')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
