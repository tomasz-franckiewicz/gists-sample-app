import base64
import json
import urllib.request


class GitHubClient:
    gist_base_url = ""

    def __init__(self, base_url):
        self.gist_base_url = base_url + "/gists"

    def get_gists(self, api_token=None):
        request = urllib.request.Request(self.gist_base_url)

        if api_token:
            request.headers = {'Authorization': 'token %s' % api_token}

        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    def get_gist(self, gist_id):
        return json.loads(urllib.request.urlopen(self.gist_base_url + "/" + gist_id).read())

    def create_gist(self, api_token, description, file_name, file_content_base_64, public):
        files = {
            file_name: {
                "content": base64.b64decode(file_content_base_64).decode('utf-8')}
        }

        headers = {'Authorization': 'token %s' % api_token}
        payload = {"description": description, "files": files, "public": public}

        request = urllib.request.Request(
            url=self.gist_base_url,
            headers=headers,
            data=json.dumps(payload).encode('utf8')
        )

        response = urllib.request.urlopen(request)
        return json.loads(response.read())
