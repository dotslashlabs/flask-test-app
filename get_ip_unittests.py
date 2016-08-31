import get_ip
import unittest
import json
import urllib2

class GetIPTestCase(unittest.TestCase):

    def setUp(self):
        self.app = get_ip.app.test_client()

    def tearDown(self):
        pass

    def test_local_ip(self):
        response = self.app.get('/get_my_ip')
        assert response._status_code == 200

if __name__ == '__main__':
    unittest.main()
