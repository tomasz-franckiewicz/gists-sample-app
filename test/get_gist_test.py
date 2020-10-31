import unittest
from main.git_hub_client import GitHubClient


class MyTestCase(unittest.TestCase):
    gitHubClient = GitHubClient("https://api.github.com")

    def test_get_gist(self):
        gist_id = "ee9cd5361077e2c0be784554ba7045fc"

        gist = self.gitHubClient.get_gist(gist_id)
        self.assertTrue(self, gist["id"] == gist_id)
