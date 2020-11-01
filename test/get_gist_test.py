import unittest
from main.git_hub_client import GitHubClient


class MyTestCase(unittest.TestCase):
    git_hub_client = GitHubClient("https://api.github.com")

    def test_get_gist_public(self):
        public_gist_id = "996e240ced19b1c42e13f265e7d88082"

        gist = self.git_hub_client.get_gist(public_gist_id)
        self.assertTrue(self, gist["id"] == public_gist_id)

    def test_get_gist_secret(self):
        secret_gist_id = "414dafa9880931941b027f48b2455484"

        gist = self.git_hub_client.get_gist(secret_gist_id)
        self.assertTrue(self, gist["id"] == secret_gist_id)
