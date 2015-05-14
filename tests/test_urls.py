# -*- coding: utf-8 -*-
import unittest
from guildwars2api.v2 import GuildWars2API


class URLBuildTestCase(unittest.TestCase):

    def setUp(self):
        self.api = GuildWars2API()

    def test_all_items_url(self):
        self.assertEqual(self.api.items.build_url(), 'https://api.guildwars2.com/v2/items')

    def test_specific_item_url(self):
        self.assertEqual(self.api.items.build_url(id=1051), 'https://api.guildwars2.com/v2/items?id=1051')

    def test_multiple_items_url(self):
        self.assertEqual(self.api.items.build_url(ids="1051,1052"), 'https://api.guildwars2.com/v2/items?ids=1051%2C1052')

    def test_list_items_url(self):
        self.assertEqual(self.api.items.build_url(ids=[1051,1052]), 'https://api.guildwars2.com/v2/items?ids=1051%2C1052')

    def test_items_url_with_bad_param(self):
        self.assertEqual(self.api.items.build_url(testattr="food"), 'https://api.guildwars2.com/v2/items?testattr=food')

    def test_transactions(self):
        self.assertEqual(self.api.transactions.build_url(), 'https://api.guildwars2.com/v2/commerce/transactions')

    def test_transactions_current(self):
        self.assertEqual(self.api.transactions.build_url('current'), 'https://api.guildwars2.com/v2/commerce/transactions/current')

    def test_transactions_history(self):
        self.assertEqual(self.api.transactions.build_url('history'), 'https://api.guildwars2.com/v2/commerce/transactions/history')

    def test_transactions_current_buys(self):
        self.assertEqual(self.api.transactions.build_url('current', 'buys'), 'https://api.guildwars2.com/v2/commerce/transactions/current/buys')

    def test_transactions_current_sells(self):
        self.assertEqual(self.api.transactions.build_url('current', 'sells'), 'https://api.guildwars2.com/v2/commerce/transactions/current/sells')

    def test_transactions_history_buys(self):
        self.assertEqual(self.api.transactions.build_url('history', 'buys'), 'https://api.guildwars2.com/v2/commerce/transactions/history/buys')

    def test_transactions_history_sells(self):
        self.assertEqual(self.api.transactions.build_url('history', 'sells'), 'https://api.guildwars2.com/v2/commerce/transactions/history/sells')
