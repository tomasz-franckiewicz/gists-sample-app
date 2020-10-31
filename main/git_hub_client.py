import urllib.request
import json


class GitHubClient:
    base_url = ""

    def __init__(self, base_url):
        self.base_url = base_url

    def get_gists(self):
        return json.loads(urllib.request.urlopen(self.base_url + "/gists").read())

    def get_gist(self, gist_id):
        return json.loads(urllib.request.urlopen(self.base_url + "/gists/" + gist_id).read())
