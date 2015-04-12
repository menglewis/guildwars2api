=====
Usage
=====

To use Guild Wars 2 API in a project::

    from guildwars2api.v1 import GuildWars2API

    api = GuildWars2API()
    api.items.get()

The v1 resources have been separated out into their own wrapper class different from the v2 resources because both versions of the API have different resources and endpoints. The different API versions can be accessed by importing the different clients from each version::

    from guildwars2api.v2 import GuildWars2API

    api = GuildWars2API()
    api.items.get()


You can customize the User Agent upon instantiating the API Wrapper::

    from guildwars2api.v1 import GuildWars2API

    api = GuildWars2API(user_agent='Awesome Guild Wars 2 Application')

