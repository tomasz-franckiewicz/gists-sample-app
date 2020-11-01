import unittest

from main.git_hub_client import GitHubClient


class MyTestCase(unittest.TestCase):
    git_hub_client = GitHubClient("https://api.github.com")
    token = "022a03d67f7dc7836a1bc54fbc7e97806cde3883"

    def test_create_gist_from_base64(self):
        description = "Sample GIST description from base64"
        file_name = "file_from_python_app.txt"
        file_content_base_64 = "U2FtcGxlIEdJU1QgY29udGVudA=="
        public = True

        gist = self.git_hub_client.create_gist_from_base64(self.token, description, file_name, file_content_base_64, public)
        self.assertTrue(self, gist["description"] == description)

    def test_create_gist_from_file(self):
        description = "Sample GIST description from data.txt file"
        file_name = "data.txt"
        file_path = "data.txt"
        public = True

        gist = self.git_hub_client.create_gist_from_file(self.token, description, file_name, file_path, public)
        self.assertTrue(self, gist["description"] == description)
