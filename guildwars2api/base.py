# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib
import requests


class GuildWars2APIError(Exception):
    pass


class BaseClient(object):
    base_url = ''

    def __init__(self, base_url=None, user_agent='Guild Wars 2 Python API Wrapper'):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': user_agent, 'Accept': 'application/json'})
        if base_url:
            self.host = base_url
        else:
            self.host = self.base_url

    def _register(self, resource):
        return resource(self.host, self.session)


class BaseResource(object):
    """
    Base Class for a Guild Wars 2 Resource
    """
    resource = ""

    def __init__(self, api_host, session):
        self.api_host = api_host
        self.session = session

    def get(self, *args, **kwargs):
        """
        Makes a request to the URL and returns the response as a Python object
        :param args:
        :param kwargs:
        :return:
        """
        r = self.response(*args, **kwargs)
        if r.status_code == 200:
            return r.json()

        raise(GuildWars2APIError(r.reason))

    def response(self, *args, **kwargs):
        """
        Returns the full Requests response for the Resource
        :param args:
        :param kwargs:
        :return:
        """
        url = self.build_url(*args, **kwargs)
        return self.session.get(url)

    def build_url(self, resource=None, *args, **kwargs):
        """
        Builds the URL using the base API host and the resource
        :param resource:
        :return:
        """
        if resource is None:
            resource = self.resource
        url = "%s/%s" % (self.api_host, resource)
        params = ""
        if len(kwargs) > 0:
            params = "?{0}".format(urllib.urlencode(kwargs))
        return "{url}{params}".format(url=url, params=params)
