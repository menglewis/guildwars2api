# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
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

    def _register(self, resource):
        return resource(self.host, self.session)
