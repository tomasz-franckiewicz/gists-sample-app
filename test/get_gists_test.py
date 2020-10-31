import unittest
from main.git_hub_client import GitHubClient


class MyTestCase(unittest.TestCase):
    git_hub_client = GitHubClient("https://api.github.com")

    def test_get_gists(self):
        gists = self.git_hub_client.get_gists()
        self.assertTrue(self, gists[0]["id"])
