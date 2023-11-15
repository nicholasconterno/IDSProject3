import unittest
from unittest.mock import patch
from main import run
import dotenv
import os
# Load the environment variables
dotenv.load_dotenv()
class TestMainScript(unittest.TestCase):

    @patch('main.requests.post')
    def test_run_success(self, mock_post):
        # Mock the response object
        mock_response = mock_post.return_value
        mock_response.status_code = 200

        # Call the run function with mock data
        result = run("mock_token", "mock_job_id", "mock_server_host_name")

        # Check if the function returns the expected result
        self.assertEqual(result, 200)

    @patch('main.requests.post')
    def test_run_failure(self, mock_post):
        # Mock the response object
        mock_response = mock_post.return_value
        mock_response.status_code = 400
        mock_response.text = "Error message"

        # Call the run function with mock data
        result = run("mock_token", "mock_job_id", "mock_server_host_name")

        # Check if the function returns the expected result
        self.assertEqual(result, 400)

#test that .env file is loaded
    def test_env_file(self):
        assert (os.getenv("PAT") != None)
        assert (os.getenv("JOB_ID") != None)
        assert (os.getenv("HOST") != None)
if __name__ == '__main__':
    unittest.main()
