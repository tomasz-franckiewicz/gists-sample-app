import base64
import json
import urllib.request


class GitHubClient:
    base_url = ""

    def __init__(self, base_url):
        self.base_url = base_url

    def get_gists(self):
        return json.loads(urllib.request.urlopen(self.base_url + "/gists").read())

    def get_gist(self, gist_id):
        return json.loads(urllib.request.urlopen(self.base_url + "/gists/" + gist_id).read())

    def create_gist(self, api_token, description, file_name, file_content_base_64, public):
        files = {
            file_name: {
                "content": base64.b64decode(file_content_base_64).decode('utf-8')}
        }

        headers = {'Authorization': 'token %s' % api_token}
        payload = {"description": description, "files": files, "public": public}

        request = urllib.request.Request(
            url=self.base_url + "/gists",
            headers=headers,
            data=json.dumps(payload).encode('utf8')
        )

        response = urllib.request.urlopen(request)
        return json.loads(response.read())
