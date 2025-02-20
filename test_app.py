import unittest
from app import app

class FlaskTest(unittest.TestCase):

    # Test if the home page loads successfully
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)

    # Test if a video can be served
    def test_video(self):
        tester = app.test_client(self)
        response = tester.get("/videos/sample.mp4")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
