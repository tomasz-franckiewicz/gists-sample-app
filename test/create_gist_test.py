import unittest

from main.git_hub_client import GitHubClient


class MyTestCase(unittest.TestCase):
    git_hub_client = GitHubClient("https://api.github.com")
    token = "bf42cd72b71c9d6c0bee9ac2b00d5b720aef7489"

    def test_create_gist_with_base64_file(self):
        description = "Sample GIST description"
        file_name = "file_from_python_app.txt"
        file_content_base_64 = "U2FtcGxlIEdJU1QgZGVzY3JpcHRpb24="
        public = True

        gist = self.git_hub_client.create_gist(self.token, description, file_name, file_content_base_64, public)
        self.assertTrue(self, gist["description"] == description)
