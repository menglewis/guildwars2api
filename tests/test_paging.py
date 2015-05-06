# -*- coding: utf-8 -*-
import unittest
from guildwars2api.v2 import GuildWars2API


class PagingTestCase(unittest.TestCase):

    def setUp(self):
        self.api = GuildWars2API()

    def test_get_all_worlds(self):
        worlds = self.api.worlds.get_all(page_size=20)
        count = 0
        for w in worlds:
            count += 1
        self.assertTrue(count > 20)
