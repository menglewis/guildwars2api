# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib


class GuildWars2APIError(Exception):
    pass


class Resource(object):
    """
    Base Class for a Guild Wars 2 Resource
    """

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

    def build_url(self, resource, *args, **kwargs):
        """
        Builds the URL using the base API host and the resource
        :param resource:
        :return:
        """
        url = "%s/%s" % (self.api_host, resource)
        params = ""
        if len(kwargs) > 0:
            params = "?{0}".format(urllib.urlencode(kwargs))
        return "{url}{params}".format(url=url, params=params)


class Item(Resource):

    resource = "items"

    def build_url(self, *args, **kwargs):
        return super(Item, self).build_url(self.resource, *args, **kwargs)


class Recipe(Resource):

    resource = "recipes"

    def build_url(self, *args, **kwargs):
        return super(Recipe, self).build_url(self.resource, *args, **kwargs)


class RecipeSearch(Resource):

    resource = "recipes/search"

    def build_url(self, *args, **kwargs):
        return super(RecipeSearch, self).build_url(self.resource, *args, **kwargs)


class Skin(Resource):

    resource = "skins"

    def build_url(self, *args, **kwargs):
        return super(Skin, self).build_url(self.resource, *args, **kwargs)
