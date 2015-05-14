# -*- coding: utf-8 -*-
import unittest
from guildwars2api.v2 import GuildWars2API


class ClientTestCase(unittest.TestCase):

    def setUp(self):
        self.api = GuildWars2API()

    def test_no_api_key(self):
        self.assertTrue(self.api.api_key is None)

    def test_api_key_setter(self):
        self.api.api_key = "testkey"
        self.assertEqual(self.api.api_key, "testkey")

    def test_api_key_removal(self):
        self.api.api_key = "testkey"
        self.api.api_key = None
        self.assertTrue(self.api.api_key is None)

    def test_api_key_headers(self):
        self.api.api_key = "testkey"
        self.assertTrue("Authorization" in self.api.session.headers)
        self.assertEqual(self.api.session.headers['Authorization'], "Bearer testkey")
