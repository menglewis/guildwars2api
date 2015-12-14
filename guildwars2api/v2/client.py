# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from guildwars2api.base import BaseClient
from .resources import (
    Item,
    Recipe,
    RecipeSearch,
    Skin,
    Continent,
    Floor,
    Map,
    Listing,
    Exchange,
    Transaction,
    Price,
    Build,
    Color,
    File,
    Quaggan,
    World,
    Material,
    Bank,
    BankMaterial,
    Character,
    Inventory,
    Equipment,
    Account,
    TokenInfo,
    Currency,
    AccountWallet,
    AccountDye,
    AccountSkin,
    PvPStat,
    PvPGame,
    Specialization,
    WvWObjective,
    Mini,
    AccountMini,
    Achievement,
    AccountAchievement,
)


class GuildWars2API(BaseClient):

    base_url = "https://api.guildwars2.com/v2"

    def __init__(self, user_agent='Guild Wars 2 Python API Wrapper', api_key=None):
        super(GuildWars2API, self).__init__(user_agent=user_agent, api_key=api_key)

        self.items = self._register(Item)
        self.recipes = self._register(Recipe)
        self.recipes_search = self._register(RecipeSearch)
        self.skins = self._register(Skin)
        self.continents = self._register(Continent)
        self.floors = self._register(Floor)
        self.maps = self._register(Map)
        self.listings = self._register(Listing)
        self.exchange = self._register(Exchange)
        self.transactions = self._register(Transaction)
        self.prices = self._register(Price)
        self.build = self._register(Build)
        self.colors = self._register(Color)
        self.files = self._register(File)
        self.quaggans = self._register(Quaggan)
        self.worlds = self._register(World)
        self.materials = self._register(Material)
        self.bank = self._register(Bank)
        self.bank_materials = self._register(BankMaterial)
        self.characters = self._register(Character)
        self.inventory = self._register(Inventory)
        self.equipment = self._register(Equipment)
        self.account = self._register(Account)
        self.token_info = self._register(TokenInfo)
        self.currencies = self._register(Currency)
        self.account_wallet = self._register(AccountWallet)
        self.account_dyes = self._register(AccountDye)
        self.account_skins = self._register(AccountSkin)
        self.pvp_stats = self._register(PvPStat)
        self.pvp_games = self._register(PvPGame)
        self.specializations = self._register(Specialization)
        self.wvw_objectives = self._register(WvWObjective)
        self.minis = self._register(Mini)
        self.account_minis = self._register(AccountMini)
        self.achievements = self._register(Achievement)
        self.account_achievements = self._register(AccountAchievement)

    def _register(self, resource):
        return resource(self.host, self.session)
