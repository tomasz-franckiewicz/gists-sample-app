import unittest
from main.git_hub_client import GitHubClient


class MyTestCase(unittest.TestCase):
    git_hub_client = GitHubClient("https://api.github.com")

    def test_get_gists_public(self):
        gists = self.git_hub_client.get_gists()
        print(gists)
        self.assertTrue(self, gists[0]["owner"]["id"] != "8328949")

    def test_get_gists_for_user(self):
        token = "bf42cd72b71c9d6c0bee9ac2b00d5b720aef7489"
        gists = self.git_hub_client.get_gists(token)
        print(gists)
        self.assertTrue(self, gists[0]["owner"]["id"] == "8328949")
