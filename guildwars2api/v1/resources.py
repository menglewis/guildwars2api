# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from guildwars2api.base import BaseResource


class Event(BaseResource):
    resource = "events.json"


class EventName(BaseResource):
    resource = "event_names.json"


class MapName(BaseResource):
    resource = "map_names.json"


class WorldName(BaseResource):
    resource = "world_names.json"


class EventDetail(BaseResource):
    resource = "event_details.json"


class GuildDetail(BaseResource):
    resource = "guild_details.json"


class Item(BaseResource):
    resource = "items.json"


class ItemDetail(BaseResource):
    resource = "item_details.json"


class Recipe(BaseResource):
    resource = "recipes.json"


class RecipeDetail(BaseResource):
    resource = "recipe_details.json"


class Skin(BaseResource):
    resource = "skins.json"


class SkinDetail(BaseResource):
    resource = "skin_details.json"

