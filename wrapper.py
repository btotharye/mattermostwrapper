import logging
import time
import json
import requests

class MattermostAPI:
    def __init__(self, url):
        self.url = url
        self.token = ""

    def get(self, request):
        """
        Used to make get calls to mattermost api
        :param request:
        :return:
        """
        headers = {"Authorization": "Bearer " + self.token }
        g = requests.get(self.url + request, headers=headers)
        return json.loads(g.text)

    def post(self, request, data=None):
        """
        Used to make post calls to mattermost api
        :param request:
        :param data:
        :return:
        """
        headers = {"Authorization": "Bearer " + self.token }
        logging.debug(json.dumps(data, indent=4))
        p = requests.post(self.url + request, headers=headers, data=json.dumps(data))
        return json.loads(p.text)
    
    def login(self, login, password):
        """Login to the corresponding (self.url) mattermost instance."""
        props = {'login_id': login, 'password': password}
        p = requests.post(self.url + '/users/login', data=json.dumps(props))
        self.token = p.headers["Token"] # Store the token for further requests
        return json.loads(p.text)
    
    def get_teams(self):
        """
        Get team listing back
        :return:
        """
        return self.get('/teams')

    def get_channel_listing(self, display_name):
        """
        This function takes in display_name of your team and gets the channel listing for that team.
        :param display_name:
        :return:
        """
        teams = self.get('/teams')
        for team in teams:
            if team['display_name'].lower() == display_name:
                channel_listing = self.get('/teams/' + team['id'] + '/channels')
                return channel_listing





