import unittest
from main.git_hub_client import GitHubClient


class MyTestCase(unittest.TestCase):
    git_hub_client = GitHubClient("https://api.github.com")

    def test_get_gists_public(self):
        gists = self.git_hub_client.get_gists()
        print(gists)
        self.assertTrue(self, gists[0]["owner"]["id"] != "8328949")

    def test_get_gists_for_user(self):
        token = "022a03d67f7dc7836a1bc54fbc7e97806cde3883"
        gists = self.git_hub_client.get_gists(token)
        print(gists)
        self.assertTrue(self, gists[0]["owner"]["id"] == "8328949")
