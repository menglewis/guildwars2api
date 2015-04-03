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
        self.assertEqual(self.api.items.build_url(ids="1051,1052"), 'https://api.guildwars2.com/v2/items?ids=1051,1052')

    def test_items_url_with_bad_param(self):
        self.assertEqual(self.api.items.build_url(testattr="food"), 'https://api.guildwars2.com/v2/items?testattr=food')
