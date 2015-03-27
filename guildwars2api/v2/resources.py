# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from guildwars2api.base import BaseResource


class Item(BaseResource):
    """
    BaseResource class for an Item. See https://wiki.guildwars2.com/wiki/API:2/items
    Parameters for a request
    id: a single ID
    ids: a comma-delimited string of IDs
    lang: "en", "es", "fr", "de"
    """
    resource = "items"


class Recipe(BaseResource):
    resource = "recipes"


class RecipeSearch(BaseResource):
    resource = "recipes/search"


class Skin(BaseResource):
    resource = "skins"


class Continent(BaseResource):
    resource = "continents"


class Floor(BaseResource):
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


class Map(BaseResource):
    resource = "maps"


class Listing(BaseResource):
    resource = "commerce/listings"


class Exchange(BaseResource):
    resource = "commerce/exchange"

    def build_url(self, currency="coins", **kwargs):
        url_pieces = super(Exchange, self).build_url(self.resource, **kwargs).split("?")
        if len(url_pieces) > 1:
            base_url, query_string = url_pieces
        else:
            base_url = url_pieces[0]
            query_string = ""

        return "{base_url}/{currency}?{query_string}".format(base_url=base_url, currency=currency, query_string=query_string)


class Price(BaseResource):
    resource = "commerce/prices"


class Build(BaseResource):
    resource = "build"


class Color(BaseResource):
    resource = "colors"


class File(BaseResource):
    resource = "files"


class Quaggan(BaseResource):
    resource = "quaggans"


class World(BaseResource):
    resource = "worlds"

