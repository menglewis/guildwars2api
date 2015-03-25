# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib


class GuildWars2APIError(Exception):
    pass


class Resource(object):
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


class Item(Resource):
    """
    Resource class for an Item. See https://wiki.guildwars2.com/wiki/API:2/items
    Parameters for a request
    id: a single ID
    ids: a comma-delimited string of IDs
    lang: "en", "es", "fr", "de"
    """
    resource = "items"


class Recipe(Resource):
    resource = "recipes"


class RecipeSearch(Resource):
    resource = "recipes/search"


class Skin(Resource):
    resource = "skins"


class Continent(Resource):
    resource = "continents"


class Floor(Resource):
    resource = "floors"

    def build_url(self, continent_id=None, floor_id=None, **kwargs):
        url_pieces = super(Floor, self).build_url(self.resource, **kwargs).split("?")
        if len(url_pieces) > 1:
            base_url, query_string = url_pieces
        else:
            base_url = url_pieces[0]
            query_string = ""
        url = base_url
        if continent_id:
            url = "{base_url}/{continent}".format(base_url=base_url, continent=continent_id)
            if floor_id:
                url = "{url}/{floor}".format(url=url, floor=floor_id)
            if query_string != "":
                url = "{url}?{query_string}".format(url=url, query_string=query_string)
        return url


class Map(Resource):
    resource = "maps"


class Listing(Resource):
    resource = "commerce/listings"


class Exchange(Resource):
    resource = "commerce/exchange"

    def build_url(self, currency="coins", **kwargs):
        url_pieces = super(Exchange, self).build_url(self.resource, **kwargs).split("?")
        if len(url_pieces) > 1:
            base_url, query_string = url_pieces
        else:
            base_url = url_pieces[0]
            query_string = ""

        return "{base_url}/{currency}?{query_string}".format(base_url=base_url, currency=currency, query_string=query_string)


class Price(Resource):
    resource = "commerce/prices"


class Build(Resource):
    resource = "build"


class Color(Resource):
    resource = "colors"


class File(Resource):
    resource = "files"


class Quaggan(Resource):
    resource = "quaggans"


class World(Resource):
    resource = "worlds"

