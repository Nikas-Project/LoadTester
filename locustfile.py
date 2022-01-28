from locust import HttpUser, task
from json import JSONDecodeError


class QuickstartUser(HttpUser):

    @task
    def hello_world(self):
        with self.client.post("/new?uri=/", json={
            "author": "Arash Hatami",
            "email": "info@arash-hatami.ir",
            "website": "https://arash-hatami.ir",
            "text": "Comment's Body",
            "parent": None,
            "title": None,
            "notification": 0
        }, catch_response=True) as response:
            try:
                if response.json()["mode"] != 1:
                    response.failure("Did not get expected value in greeting")
            except JSONDecodeError:
                response.failure("Response could not be decoded as JSON")
            except KeyError:
                response.failure(
                    "Response did not contain expected key 'mode'")
