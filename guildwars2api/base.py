# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
try:
    from urllib import parse as urllib
except ImportError:
    import urllib


class GuildWars2APIError(Exception):
    pass


class BaseClient(object):
    base_url = ''

    def __init__(self, base_url=None, user_agent='Guild Wars 2 Python API Wrapper'):
        self.session = requests.Session()
        self.session.headers.update(
            {'User-Agent': user_agent, 'Accept': 'application/json'})
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

    def get_all_lazy(self, *args, **kwargs):
        """
        Gets all results for the resource as a Python object, using paging
        (more info at https://wiki.guildwars2.com/wiki/API:2)
        Doesn't fetch all results into a single object, but rather gets them
        one batch at a time, suitable for use in a for-loop.
        :param args:
        :param kwargs:
        :return:
        """
        defaults = {
            'page': 0,
            'page_size': 200,
        }
        defaults.update(kwargs)
        kwargs = defaults

        page_total = kwargs['page'] + 1

        while kwargs['page'] < page_total:
            r = self.response(*args, **kwargs)
            if r.status_code == 200:
                for i in r.json():
                    yield i

                kwargs['page'] += 1
                page_total = int(r.headers.get('X-Page-Total', 1))
            else:
                raise(GuildWars2APIError(r.reason))

    def get_all(self, *args, **kwargs):
        """
        Gets all results for the resource as a Python object, using paging
        (more info at https://wiki.guildwars2.com/wiki/API:2)
        :param args:
        :param kwargs:
        :return:
        """
        res = []
        for r in self.get_all_lazy(*args, **kwargs):
            res += r
        return res

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
        print url
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
            for arg in kwargs:
                if hasattr(kwargs[arg], '__iter__'):
                    kwargs[arg] = ','.join(str(x) for x in kwargs[arg])
            params = "?{0}".format(urllib.urlencode(kwargs))
        return "{url}{params}".format(url=url, params=params)
