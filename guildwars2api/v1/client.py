# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from guildwars2api.base import BaseClient
from .resources import (
    Event,
    EventName,
    MapName,
    WorldName,
    EventDetail,
    GuildDetail,
    Item,
    ItemDetail,
    Recipe,
    RecipeDetail,
    Skin,
    SkinDetail,
    Continent,
    Map,
    MapFloor,
    WvWMatch,
    WvWMatchDetail,
    WvWObjectiveName,
    Build,
    Color,
    File,
)


class GuildWars2API(BaseClient):

    base_url = "https://api.guildwars2.com/v1"

    def __init__(self, user_agent='Guild Wars 2 Python API Wrapper'):
        super(GuildWars2API, self).__init__(user_agent=user_agent)

        self.events = self._register(Event)
        self.event_names = self._register(EventName)
        self.map_names = self._register(MapName)
        self.world_names = self._register(WorldName)
        self.event_details = self._register(EventDetail)
        self.guild_details = self._register(GuildDetail)
        self.items = self._register(Item)
        self.item_details = self._register(ItemDetail)
        self.recipes = self._register(Recipe)
        self.recipe_details = self._register(RecipeDetail)
        self.skins = self._register(Skin)
        self.skin_detail = self._register(SkinDetail)
        self.continents = self._register(Continent)
        self.maps = self._register(Map)
        self.map_floors = self._register(MapFloor)
        self.matches = self._register(WvWMatch)
        self.match_details = self._register(WvWMatchDetail)
        self.objective_names = self._register(WvWObjectiveName)
        self.build = self._register(Build)
        self.colors = self._register(Color)
        self.file = self._register(File)

    def _register(self, resource):
        return resource(self.host, self.session)
