# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from guildwars2api.resources import Item, Recipe, RecipeSearch, Skin


class GuildWars2API(object):

    BASE_URL = "https://api.guildwars2.com/{version}"

    def __init__(self, version='v2', user_agent='Guild Wars 2 Python API Wrapper'):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': user_agent, 'Accept': 'application/json'})
        self.host = self.BASE_URL.format(version=version)

        if version == 'v2':
            self.items = self._register(Item)
            self.recipes = self._register(Recipe)
            self.recipes_search = self._register(RecipeSearch)
            self.skins = self._register(Skin)

    def _register(self, resource):
        return resource(self.host, self.session)
